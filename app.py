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


# ---------------------------------------------------------------
#  PUBLIC PAGES
# ---------------------------------------------------------------

@app.route("/")
def inicio():
    # "Blog": los 3 artículos fijos (vienen de blog_data.py, no de la base de datos).
    latest_posts = blog_data.get_all()
    return render_template("inicio.html", latest_posts=latest_posts)


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


@app.route("/enviar-cv", methods=["GET", "POST"])
def enviar_cv():
    """Formulario único de postulación: Santiago publica las vacantes fuera
    del sitio (Facebook, LinkedIn, Instagram, WhatsApp, CompuTrabajo), así
    que aquí el candidato escribe a mano para cuál vacante aplica en vez de
    elegirla de una lista en el sitio (por eso ya no existe /vacantes: esa
    lista se desincronizaba constantemente de lo que en verdad estaba
    publicado afuera). Todo se guarda en la misma tabla `applications`
    (vacancy_id = NULL, vacancy_title = el texto que escribió el
    candidato) para que aparezca en el panel de administración, y se
    notifica por correo igual que antes."""
    if request.method == "POST":
        resume_filename = None
        f = request.files.get("resume")
        if f and f.filename:
            resume_filename = secure_filename(f"cv-{int(datetime.datetime.utcnow().timestamp())}-{f.filename}")
            f.save(os.path.join(UPLOAD_DIR, resume_filename))

        full_name = request.form.get("full_name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        applied_vacancy = request.form.get("applied_vacancy", "").strip()
        message = request.form.get("message", "").strip()

        conn = db.get_db()
        conn.execute(
            "INSERT INTO applications (vacancy_id, vacancy_title, full_name, email, phone, message, resume_filename, created_at) "
            "VALUES (?,?,?,?,?,?,?,?)",
            (None, applied_vacancy or "No especificada", full_name, email, phone, message, resume_filename, db.now()),
        )
        conn.commit()
        conn.close()

        notifications.send_open_application_email({
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "applied_vacancy": applied_vacancy,
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
