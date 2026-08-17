import os
import datetime
import functools

from flask import (
    Blueprint, render_template, request, redirect, url_for, flash,
    session, abort, send_from_directory
)
from werkzeug.utils import secure_filename

import db
from config import ADMIN_PASSWORD, UPLOAD_DIR

admin_bp = Blueprint("admin", __name__, url_prefix="/admin", template_folder="templates/admin")


def admin_required(view):
    @functools.wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("is_admin"):
            return redirect(url_for("admin.login", next=request.path))
        return view(*args, **kwargs)
    return wrapped


@admin_bp.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        pw = request.form.get("password", "")
        if pw == ADMIN_PASSWORD:
            session["is_admin"] = True
            nxt = request.args.get("next") or url_for("admin.dashboard")
            return redirect(nxt)
        error = "Contraseña incorrecta."
    return render_template("admin/login.html", error=error)


@admin_bp.route("/logout")
def logout():
    session.pop("is_admin", None)
    return redirect(url_for("admin.login"))


@admin_bp.route("/")
@admin_required
def dashboard():
    conn = db.get_db()
    counts = {
        "vacancies": conn.execute("SELECT COUNT(*) c FROM vacancies WHERE status='active'").fetchone()["c"],
        "posts": conn.execute("SELECT COUNT(*) c FROM blog_posts WHERE status='published'").fetchone()["c"],
        "leads": conn.execute("SELECT COUNT(*) c FROM leads").fetchone()["c"],
        "applications": conn.execute("SELECT COUNT(*) c FROM applications").fetchone()["c"],
    }
    recent_leads = conn.execute("SELECT * FROM leads ORDER BY created_at DESC LIMIT 5").fetchall()
    recent_apps = conn.execute("SELECT * FROM applications ORDER BY created_at DESC LIMIT 5").fetchall()
    conn.close()
    return render_template("admin/dashboard.html", counts=counts, recent_leads=recent_leads, recent_apps=recent_apps)


# ---------------------------------------------------------------
#  VACANCIES CRUD
# ---------------------------------------------------------------

@admin_bp.route("/vacancies")
@admin_required
def vacancies_list():
    conn = db.get_db()
    rows = conn.execute("SELECT * FROM vacancies ORDER BY created_at DESC").fetchall()
    conn.close()
    return render_template("admin/vacancies_list.html", vacancies=rows)


def _vacancy_form_to_dict(form):
    return {
        "title": form.get("title", "").strip(),
        "location": form.get("location", "").strip() or "San Luis Potosí",
        "modality": form.get("modality", "Presencial"),
        "is_confidential": 1 if form.get("is_confidential") == "on" else 0,
        "company_label": form.get("company_label", "").strip() or "Confidencial",
        "salary_display": form.get("salary_display", "").strip(),
        "salary_tier": form.get("salary_tier") or None,
        "positions": int(form.get("positions") or 1),
        "objetivo": form.get("objetivo", "").strip(),
        "responsabilidades": form.get("responsabilidades", "").strip(),
        "requisitos": form.get("requisitos", "").strip(),
        "prestaciones": form.get("prestaciones", "").strip(),
        "status": form.get("status", "active"),
        "published_at": form.get("published_at") or datetime.date.today().isoformat(),
    }


@admin_bp.route("/vacancies/new", methods=["GET", "POST"])
@admin_required
def vacancy_new():
    if request.method == "POST":
        data = _vacancy_form_to_dict(request.form)
        conn = db.get_db()
        slug = db.unique_slug(conn, "vacancies", db.slugify(data["title"]))
        now = db.now()
        conn.execute(
            "INSERT INTO vacancies (slug,title,location,modality,is_confidential,company_label,"
            "salary_display,salary_tier,positions,objetivo,responsabilidades,requisitos,prestaciones,"
            "status,published_at,created_at,updated_at) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                slug, data["title"], data["location"], data["modality"], data["is_confidential"],
                data["company_label"], data["salary_display"], data["salary_tier"], data["positions"],
                data["objetivo"], data["responsabilidades"], data["requisitos"], data["prestaciones"],
                data["status"], data["published_at"], now, now,
            ),
        )
        conn.commit()
        conn.close()
        flash("Vacante creada.", "success")
        return redirect(url_for("admin.vacancies_list"))
    return render_template("admin/vacancy_form.html", v=None)


@admin_bp.route("/vacancies/<int:vid>/edit", methods=["GET", "POST"])
@admin_required
def vacancy_edit(vid):
    conn = db.get_db()
    row = conn.execute("SELECT * FROM vacancies WHERE id=?", (vid,)).fetchone()
    if not row:
        conn.close()
        abort(404)
    if request.method == "POST":
        data = _vacancy_form_to_dict(request.form)
        slug = db.unique_slug(conn, "vacancies", db.slugify(data["title"]), exclude_id=vid)
        conn.execute(
            "UPDATE vacancies SET slug=?,title=?,location=?,modality=?,is_confidential=?,company_label=?,"
            "salary_display=?,salary_tier=?,positions=?,objetivo=?,responsabilidades=?,requisitos=?,"
            "prestaciones=?,status=?,published_at=?,updated_at=? WHERE id=?",
            (
                slug, data["title"], data["location"], data["modality"], data["is_confidential"],
                data["company_label"], data["salary_display"], data["salary_tier"], data["positions"],
                data["objetivo"], data["responsabilidades"], data["requisitos"], data["prestaciones"],
                data["status"], data["published_at"], db.now(), vid,
            ),
        )
        conn.commit()
        conn.close()
        flash("Vacante actualizada.", "success")
        return redirect(url_for("admin.vacancies_list"))
    conn.close()
    return render_template("admin/vacancy_form.html", v=row)


@admin_bp.route("/vacancies/<int:vid>/delete", methods=["POST"])
@admin_required
def vacancy_delete(vid):
    conn = db.get_db()
    conn.execute("DELETE FROM vacancies WHERE id=?", (vid,))
    conn.commit()
    conn.close()
    flash("Vacante eliminada.", "success")
    return redirect(url_for("admin.vacancies_list"))


# ---------------------------------------------------------------
#  BLOG POSTS CRUD
# ---------------------------------------------------------------

@admin_bp.route("/posts")
@admin_required
def posts_list():
    conn = db.get_db()
    rows = conn.execute("SELECT * FROM blog_posts ORDER BY created_at DESC").fetchall()
    conn.close()
    return render_template("admin/posts_list.html", posts=rows)


def _post_form_to_dict(form):
    return {
        "title": form.get("title", "").strip(),
        "category": form.get("category", "").strip() or "General",
        "reading_time": form.get("reading_time", "").strip() or "5 min de lectura",
        "body": form.get("body", "").strip(),
        "status": form.get("status", "published"),
        "published_at": form.get("published_at") or datetime.date.today().isoformat(),
    }


@admin_bp.route("/posts/new", methods=["GET", "POST"])
@admin_required
def post_new():
    if request.method == "POST":
        data = _post_form_to_dict(request.form)
        conn = db.get_db()
        slug = db.unique_slug(conn, "blog_posts", db.slugify(data["title"]))
        now = db.now()
        conn.execute(
            "INSERT INTO blog_posts (slug,title,category,reading_time,body,status,published_at,created_at,updated_at) "
            "VALUES (?,?,?,?,?,?,?,?,?)",
            (slug, data["title"], data["category"], data["reading_time"], data["body"],
             data["status"], data["published_at"], now, now),
        )
        conn.commit()
        conn.close()
        flash("Artículo creado.", "success")
        return redirect(url_for("admin.posts_list"))
    return render_template("admin/post_form.html", p=None)


@admin_bp.route("/posts/<int:pid>/edit", methods=["GET", "POST"])
@admin_required
def post_edit(pid):
    conn = db.get_db()
    row = conn.execute("SELECT * FROM blog_posts WHERE id=?", (pid,)).fetchone()
    if not row:
        conn.close()
        abort(404)
    if request.method == "POST":
        data = _post_form_to_dict(request.form)
        slug = db.unique_slug(conn, "blog_posts", db.slugify(data["title"]), exclude_id=pid)
        conn.execute(
            "UPDATE blog_posts SET slug=?,title=?,category=?,reading_time=?,body=?,status=?,published_at=?,updated_at=? WHERE id=?",
            (slug, data["title"], data["category"], data["reading_time"], data["body"],
             data["status"], data["published_at"], db.now(), pid),
        )
        conn.commit()
        conn.close()
        flash("Artículo actualizado.", "success")
        return redirect(url_for("admin.posts_list"))
    conn.close()
    return render_template("admin/post_form.html", p=row)


@admin_bp.route("/posts/<int:pid>/delete", methods=["POST"])
@admin_required
def post_delete(pid):
    conn = db.get_db()
    conn.execute("DELETE FROM blog_posts WHERE id=?", (pid,))
    conn.commit()
    conn.close()
    flash("Artículo eliminado.", "success")
    return redirect(url_for("admin.posts_list"))


# ---------------------------------------------------------------
#  LEADS & APPLICATIONS (read-only views)
# ---------------------------------------------------------------

@admin_bp.route("/leads")
@admin_required
def leads_list():
    conn = db.get_db()
    rows = conn.execute("SELECT * FROM leads ORDER BY created_at DESC").fetchall()
    conn.close()
    return render_template("admin/leads_list.html", leads=rows)


@admin_bp.route("/leads/<int:lid>")
@admin_required
def lead_detail(lid):
    conn = db.get_db()
    row = conn.execute("SELECT * FROM leads WHERE id=?", (lid,)).fetchone()
    conn.close()
    if not row:
        abort(404)
    return render_template("admin/lead_detail.html", lead=row)


@admin_bp.route("/applications")
@admin_required
def applications_list():
    conn = db.get_db()
    rows = conn.execute("SELECT * FROM applications ORDER BY created_at DESC").fetchall()
    conn.close()
    return render_template("admin/applications_list.html", applications=rows)


@admin_bp.route("/uploads/<path:filename>")
@admin_required
def uploaded_file(filename):
    return send_from_directory(UPLOAD_DIR, filename, as_attachment=True)


@admin_bp.route("/api-docs")
@admin_required
def api_docs():
    from config import BOT_API_KEY
    return render_template("admin/api_docs.html", api_key=BOT_API_KEY)
