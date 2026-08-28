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
import vacantes_data
import blog_data
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


def vacancy_to_view(v):
    """Vacancy dict (from vacantes_data.py, hardcoded and immutable) ->
    template-ready dict with a human-friendly published date label."""
    d = dict(v)
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
    active_vacancies = [vacancy_to_view(v) for v in vacantes_data.get_all() if v.get("status") == "active"]
    # "Vacantes destacadas": lista fija elegida a mano (no automática por sueldo).
    featured_slugs = [
        "director-operaciones-industriales-manufactura",  # Gerente de Producción - Acería
        "director-financiero-grupo-corporativo",           # Director Financiero - Grupo Corporativo
        "director-comercial-automotriz",                   # Director Comercial - Automotriz
    ]
    by_slug = {v.get("slug"): v for v in active_vacancies}
    featured_vacancies = [by_slug[s] for s in featured_slugs if s in by_slug]
    # "Blog": los 3 artículos fijos (vienen de blog_data.py, no de la base de datos).
    latest_posts = blog_data.get_all()
    return render_template("inicio.html", featured_vacancies=featured_vacancies, latest_posts=latest_posts)


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
#
#  Fijas en el código (vacantes_data.py), no vienen de la base de datos:
#  así no se pierden si Render reinicia el filesystem del plan gratuito,
#  y no se pueden modificar por accidente desde el panel de admin.
# ---------------------------------------------------------------

@app.route("/vacantes")
def vacantes():
    q = request.args.get("q", "").strip().lower()
    location = request.args.get("location", "").strip()
    modality = request.args.get("modality", "").strip()
    sort = request.args.get("sort", "recent")

    items = [v for v in vacantes_data.get_all() if v.get("status") == "active"]
    if q:
        items = [v for v in items if q in v["title"].lower()]
    if location:
        items = [v for v in items if v["location"] == location]
    if modality:
        items = [v for v in items if v["modality"] == modality]

    if sort == "salary":
        items = sorted(items, key=lambda v: _salary_value(v.get("salary_display")), reverse=True)
    else:
        items = sorted(items, key=lambda v: v.get("published_at", ""), reverse=True)

    locations = sorted({v["location"] for v in vacantes_data.get_all() if v.get("status") == "active"})

    vacancies_list = [vacancy_to_view(v) for v in items]
    return render_template(
        "vacantes_list.html", vacancies=vacancies_list,
        q=q, location=location, modality=modality, sort=sort, locations=locations,
    )


@app.route("/vacantes/<slug>")
def vacante_detail(slug):
    v = vacantes_data.get_by_slug(slug)
    if not v:
        abort(404)
    return render_template("vacante_detail.html", v=vacancy_to_view(v))


@app.route("/vacantes/<slug>/postularme", methods=["GET", "POST"])
def vacante_apply(slug):
    v_raw = vacantes_data.get_by_slug(slug)
    if not v_raw:
        abort(404)
    v = vacancy_to_view(v_raw)

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

        conn = db.get_db()
        # vacancy_id queda en NULL: estas vacantes ya no viven en la tabla
        # `vacancies`, así que solo guardamos su título de referencia.
        conn.execute(
            "INSERT INTO applications (vacancy_id, vacancy_title, full_name, email, phone, message, resume_filename, created_at) "
            "VALUES (?,?,?,?,?,?,?,?)",
            (None, v_raw["title"], full_name, email, phone, message, resume_filename, db.now()),
        )
        conn.commit()
        conn.close()

        notifications.send_application_email({
            "vacancy_title": v_raw["title"],
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "message": message,
            "resume_filename": resume_filename,
        })

        return render_template("vacante_apply.html", v=v, sent=True)

    return render_template("vacante_apply.html", v=v, sent=False)


@app.route("/enviar-cv", methods=["GET", "POST"])
def enviar_cv():
    """Banco de talento: formulario general para quien quiera dejar su CV
    aunque ninguna vacante activa encaje con su perfil todavía. No está
    ligado a ninguna vacante — se guarda en la misma tabla `applications`
    (vacancy_id = NULL) para que aparezca junto a las demás postulaciones
    en el panel de administración, y se notifica por correo igual que una
    postulación normal."""
    if request.method == "POST":
        resume_filename = None
        f = request.files.get("resume")
        if f and f.filename:
            resume_filename = secure_filename(f"cv-{int(datetime.datetime.utcnow().timestamp())}-{f.filename}")
            f.save(os.path.join(UPLOAD_DIR, resume_filename))

        full_name = request.form.get("full_name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        message = request.form.get("message", "").strip()

        conn = db.get_db()
        conn.execute(
            "INSERT INTO applications (vacancy_id, vacancy_title, full_name, email, phone, message, resume_filename, created_at) "
            "VALUES (?,?,?,?,?,?,?,?)",
            (None, "Aplicación espontánea (banco de talento)", full_name, email, phone, message, resume_filename, db.now()),
        )
        conn.commit()
        conn.close()

        notifications.send_open_application_email({
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "message": message,
            "resume_filename": resume_filename,
        })

        return render_template("enviar_cv.html", sent=True)

    return render_template("enviar_cv.html", sent=False)


# ---------------------------------------------------------------
#  BLOG
#
#  Igual que las vacantes: 3 artículos fijos en el código
#  (blog_data.py), no vienen de la base de datos, para que no se
#  pierdan con los reinicios del plan gratuito de Render.
# ---------------------------------------------------------------

@app.route("/blog")
def blog():
    return render_template("blog_list.html", posts=blog_data.get_all())


@app.route("/blog/<slug>")
def blog_detail(slug):
    p = blog_data.get_by_slug(slug)
    if not p:
        abort(404)
    return render_template("blog_detail.html", p=p)


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
