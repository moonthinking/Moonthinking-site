import os
import datetime
import functools

from flask import (
    Flask, render_template, request, redirect, url_for, flash,
    session, jsonify, abort, send_from_directory
)
from werkzeug.utils import secure_filename

import db
import notifications
from config import UPLOAD_DIR, WHATSAPP_NUMBER, WHATSAPP_TEXT

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "SApvlCmoNY_s4vHbFX30ZpGQL5PsoUDaNgj17nsadzE")
app.config["MAX_CONTENT_LENGTH"] = 8 * 1024 * 1024  # 8MB uploads cap

with app.app_context():
    db.init_db()


@app.context_processor
def inject_globals():
    import urllib.parse
    return {
        "whatsapp_number": WHATSAPP_NUMBER,
        "whatsapp_text": urllib.parse.quote(WHATSAPP_TEXT),
    }


def human_date(iso_date):
    """Turn an ISO date (YYYY-MM-DD) into 'Hace N días' style label."""
    try:
        d = datetime.date.fromisoformat(iso_date[:10])
    except (ValueError, TypeError):
        return iso_date or ""
    delta = (datetime.date.today() - d).days
    if delta <= 0:
        return "Hoy"
    if delta == 1:
        return "Hace 1 día"
    if delta < 14:
        return f"Hace {delta} días"
    weeks = delta // 7
    if weeks < 5:
        return f"Hace {weeks} semana{'s' if weeks != 1 else ''}"
    months = delta // 30
    return f"Hace {months} mes{'es' if months != 1 else ''}"


def vacancy_to_view(row):
    d = dict(row)
    d["published_label"] = human_date(d.get("published_at"))
    return d


# ---------------------------------------------------------------
#  PUBLIC PAGES
# ---------------------------------------------------------------

def _salary_value(salary_display):
    """Best-effort numeric value pulled out of a free-text salary string
    (e.g. '$65,000 MXN' -> 65000, '$80,000 - $90,000 MXN' -> 90000), used
    only to rank vacancies by pay. Picks the highest individual number
    found, instead of concatenating every digit in the string — that old
    approach turned a range like '$80,000 - $90,000' into 8000090000,
    which wrongly outranked a real, higher single salary like $120,000."""
    import re
    if not salary_display:
        return 0
    numbers = re.findall(r"\d[\d,]*", salary_display)
    values = [int(n.replace(",", "")) for n in numbers if n.replace(",", "")]
    return max(values) if values else 0


@app.route("/")
def inicio():
    conn = db.get_db()
    rows = conn.execute(
        "SELECT * FROM vacancies WHERE status = 'active' ORDER BY published_at DESC"
    ).fetchall()
    post_rows = conn.execute(
        "SELECT * FROM blog_posts WHERE status='published' ORDER BY published_at DESC LIMIT 3"
    ).fetchall()
    conn.close()
    active_vacancies = [vacancy_to_view(r) for r in rows]
    # "Vacantes destacadas": siempre las 3 vacantes activas mejor pagadas.
    featured_vacancies = sorted(
        active_vacancies, key=lambda v: _salary_value(v.get("salary_display")), reverse=True
    )[:3]
    # "Blog": siempre los 3 artículos publicados más recientes.
    latest_posts = post_rows
    return render_template(
        "inicio.html", featured_vacancies=featured_vacancies, latest_posts=latest_posts
    )


@app.route("/soluciones")
def soluciones():
    return render_template("soluciones.html")


@app.route("/empresas", methods=["GET", "POST"])
def empresas():
    if request.method == "POST":
        conn = db.get_db()
        fields = [
            "company_name", "contact_name", "contact_phone", "contact_email",
            "position_title", "position_objective", "position_activities",
            "work_days", "work_hours", "modality", "work_location",
            "has_reports", "reports_to", "department_makeup",
            "min_education", "required_experience", "required_knowledge",
            "required_skills", "tools_equipment", "languages",
            "salary", "pay_period", "benefits", "other_pay",
            "needs_vehicle", "payment_method",
            "candidate_personality", "vacancy_type", "has_procedures_manual",
            "additional_comments",
        ]
        values = {f: request.form.get(f, "").strip() for f in fields}

        attachment_filename = None
        f = request.files.get("attachment")
        if f and f.filename:
            attachment_filename = secure_filename(f"lead-{int(datetime.datetime.utcnow().timestamp())}-{f.filename}")
            f.save(os.path.join(UPLOAD_DIR, attachment_filename))

        cols = list(values.keys()) + ["attachment_filename", "created_at"]
        placeholders = ",".join(["?"] * len(cols))
        vals = list(values.values()) + [attachment_filename, db.now()]
        conn.execute(f"INSERT INTO leads ({','.join(cols)}) VALUES ({placeholders})", vals)
        conn.commit()
        conn.close()

        email_lead = dict(values)
        email_lead["attachment_filename"] = attachment_filename
        notifications.send_lead_email(email_lead)

        return render_template("empresas.html", sent=True)
    return render_template("empresas.html", sent=False)


@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")


# ---------------------------------------------------------------
#  VACANTES
# ---------------------------------------------------------------

@app.route("/vacantes")
def vacantes():
    conn = db.get_db()
    q = request.args.get("q", "").strip()
    location = request.args.get("location", "").strip()
    modality = request.args.get("modality", "").strip()
    sort = request.args.get("sort", "recent")

    query = "SELECT * FROM vacancies WHERE status = 'active'"
    params = []
    if q:
        query += " AND title LIKE ?"
        params.append(f"%{q}%")
    if location:
        query += " AND location = ?"
        params.append(location)
    if modality:
        query += " AND modality = ?"
        params.append(modality)
    if sort == "salary":
        query += " ORDER BY salary_display DESC"
    else:
        query += " ORDER BY published_at DESC"

    rows = conn.execute(query, params).fetchall()
    locations = [r["location"] for r in conn.execute(
        "SELECT DISTINCT location FROM vacancies WHERE status='active' ORDER BY location"
    ).fetchall()]
    conn.close()

    vacancies_list = [vacancy_to_view(r) for r in rows]
    return render_template(
        "vacantes_list.html", vacancies=vacancies_list,
        q=q, location=location, modality=modality, sort=sort, locations=locations,
    )


@app.route("/vacantes/<slug>")
def vacante_detail(slug):
    conn = db.get_db()
    row = conn.execute("SELECT * FROM vacancies WHERE slug = ?", (slug,)).fetchone()
    conn.close()
    if not row:
        abort(404)
    return render_template("vacante_detail.html", v=vacancy_to_view(row))


@app.route("/vacantes/<slug>/postularme", methods=["GET", "POST"])
def vacante_apply(slug):
    conn = db.get_db()
    row = conn.execute("SELECT * FROM vacancies WHERE slug = ?", (slug,)).fetchone()
    if not row:
        conn.close()
        abort(404)
    v = vacancy_to_view(row)

    if request.method == "POST":
        resume_filename = None
        f = request.files.get("resume")
        if f and f.filename:
            resume_filename = secure_filename(f"app-{int(datetime.datetime.utcnow().timestamp())}-{f.filename}")
            f.save(os.path.join(UPLOAD_DIR, resume_filename))

        full_name = request.form.get("full_name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        message = request.form.get("message", "").strip()

        conn.execute(
            "INSERT INTO applications (vacancy_id, vacancy_title, full_name, email, phone, message, resume_filename, created_at) "
            "VALUES (?,?,?,?,?,?,?,?)",
            (row["id"], row["title"], full_name, email, phone, message, resume_filename, db.now()),
        )
        conn.commit()
        conn.close()

        notifications.send_application_email({
            "vacancy_title": row["title"],
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "message": message,
            "resume_filename": resume_filename,
        })

        return render_template("vacante_apply.html", v=v, sent=True)

    conn.close()
    return render_template("vacante_apply.html", v=v, sent=False)


# ---------------------------------------------------------------
#  BLOG
# ---------------------------------------------------------------

@app.route("/blog")
def blog():
    conn = db.get_db()
    rows = conn.execute(
        "SELECT * FROM blog_posts WHERE status='published' ORDER BY published_at DESC"
    ).fetchall()
    conn.close()
    return render_template("blog_list.html", posts=rows)


@app.route("/blog/<slug>")
def blog_detail(slug):
    conn = db.get_db()
    row = conn.execute("SELECT * FROM blog_posts WHERE slug = ?", (slug,)).fetchone()
    conn.close()
    if not row:
        abort(404)
    return render_template("blog_detail.html", p=row)


# Register the admin panel + bot API blueprints
from admin_panel import admin_bp  # noqa: E402
from bot_api import bot_api_bp  # noqa: E402

app.register_blueprint(admin_bp)
app.register_blueprint(bot_api_bp)


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=os.environ.get("FLASK_DEBUG", "0") == "1")
