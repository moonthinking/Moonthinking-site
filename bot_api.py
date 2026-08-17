import functools
import datetime

from flask import Blueprint, request, jsonify, abort

import db
from config import BOT_API_KEY

bot_api_bp = Blueprint("bot_api", __name__, url_prefix="/api/bot")


def require_api_key(view):
    @functools.wraps(view)
    def wrapped(*args, **kwargs):
        key = request.headers.get("X-API-Key", "")
        if not key or key != BOT_API_KEY:
            return jsonify({"error": "unauthorized", "detail": "Missing or invalid X-API-Key header."}), 401
        return view(*args, **kwargs)
    return wrapped


def vacancy_to_json(row):
    return {
        "id": row["id"], "slug": row["slug"], "title": row["title"],
        "location": row["location"], "modality": row["modality"],
        "is_confidential": bool(row["is_confidential"]), "company_label": row["company_label"],
        "salary_display": row["salary_display"], "salary_tier": row["salary_tier"],
        "positions": row["positions"], "objetivo": row["objetivo"],
        "responsabilidades": row["responsabilidades"], "requisitos": row["requisitos"],
        "prestaciones": row["prestaciones"], "status": row["status"],
        "published_at": row["published_at"], "created_at": row["created_at"], "updated_at": row["updated_at"],
    }


def post_to_json(row):
    return {
        "id": row["id"], "slug": row["slug"], "title": row["title"], "category": row["category"],
        "reading_time": row["reading_time"], "body": row["body"], "status": row["status"],
        "published_at": row["published_at"], "created_at": row["created_at"], "updated_at": row["updated_at"],
    }


# ---------------------------------------------------------------
#  VACANCIES
# ---------------------------------------------------------------

@bot_api_bp.route("/vacancies", methods=["GET"])
@require_api_key
def list_vacancies():
    conn = db.get_db()
    rows = conn.execute("SELECT * FROM vacancies ORDER BY created_at DESC").fetchall()
    conn.close()
    return jsonify([vacancy_to_json(r) for r in rows])


@bot_api_bp.route("/vacancies/<int:vid>", methods=["GET"])
@require_api_key
def get_vacancy(vid):
    conn = db.get_db()
    row = conn.execute("SELECT * FROM vacancies WHERE id=?", (vid,)).fetchone()
    conn.close()
    if not row:
        return jsonify({"error": "not_found"}), 404
    return jsonify(vacancy_to_json(row))


REQUIRED_VACANCY_FIELDS = ["title"]


@bot_api_bp.route("/vacancies", methods=["POST"])
@require_api_key
def create_vacancy():
    data = request.get_json(silent=True) or {}
    missing = [f for f in REQUIRED_VACANCY_FIELDS if not data.get(f)]
    if missing:
        return jsonify({"error": "validation_error", "missing": missing}), 400

    conn = db.get_db()
    slug = data.get("slug") or db.slugify(data["title"])
    slug = db.unique_slug(conn, "vacancies", slug)
    now = db.now()
    cur = conn.execute(
        "INSERT INTO vacancies (slug,title,location,modality,is_confidential,company_label,"
        "salary_display,salary_tier,positions,objetivo,responsabilidades,requisitos,prestaciones,"
        "status,published_at,created_at,updated_at) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (
            slug, data["title"], data.get("location", "San Luis Potosí"), data.get("modality", "Presencial"),
            1 if data.get("is_confidential") else 0, data.get("company_label", "Confidencial"),
            data.get("salary_display"), data.get("salary_tier"), int(data.get("positions", 1)),
            data.get("objetivo", ""), data.get("responsabilidades", ""), data.get("requisitos", ""),
            data.get("prestaciones", ""), data.get("status", "active"),
            data.get("published_at") or datetime.date.today().isoformat(), now, now,
        ),
    )
    conn.commit()
    new_id = cur.lastrowid
    row = conn.execute("SELECT * FROM vacancies WHERE id=?", (new_id,)).fetchone()
    conn.close()
    return jsonify(vacancy_to_json(row)), 201


@bot_api_bp.route("/vacancies/<int:vid>", methods=["PUT", "PATCH"])
@require_api_key
def update_vacancy(vid):
    conn = db.get_db()
    row = conn.execute("SELECT * FROM vacancies WHERE id=?", (vid,)).fetchone()
    if not row:
        conn.close()
        return jsonify({"error": "not_found"}), 404

    data = request.get_json(silent=True) or {}
    current = dict(row)
    for field in ["title", "location", "modality", "company_label", "salary_display", "salary_tier",
                  "positions", "objetivo", "responsabilidades", "requisitos", "prestaciones",
                  "status", "published_at"]:
        if field in data:
            current[field] = data[field]
    if "is_confidential" in data:
        current["is_confidential"] = 1 if data["is_confidential"] else 0

    slug = current["slug"]
    if "title" in data and data.get("slug") is None:
        slug = db.unique_slug(conn, "vacancies", db.slugify(data["title"]), exclude_id=vid)
    elif data.get("slug"):
        slug = db.unique_slug(conn, "vacancies", data["slug"], exclude_id=vid)

    conn.execute(
        "UPDATE vacancies SET slug=?,title=?,location=?,modality=?,is_confidential=?,company_label=?,"
        "salary_display=?,salary_tier=?,positions=?,objetivo=?,responsabilidades=?,requisitos=?,"
        "prestaciones=?,status=?,published_at=?,updated_at=? WHERE id=?",
        (
            slug, current["title"], current["location"], current["modality"], current["is_confidential"],
            current["company_label"], current["salary_display"], current["salary_tier"], current["positions"],
            current["objetivo"], current["responsabilidades"], current["requisitos"], current["prestaciones"],
            current["status"], current["published_at"], db.now(), vid,
        ),
    )
    conn.commit()
    updated = conn.execute("SELECT * FROM vacancies WHERE id=?", (vid,)).fetchone()
    conn.close()
    return jsonify(vacancy_to_json(updated))


@bot_api_bp.route("/vacancies/<int:vid>", methods=["DELETE"])
@require_api_key
def delete_vacancy(vid):
    conn = db.get_db()
    row = conn.execute("SELECT id FROM vacancies WHERE id=?", (vid,)).fetchone()
    if not row:
        conn.close()
        return jsonify({"error": "not_found"}), 404
    conn.execute("DELETE FROM vacancies WHERE id=?", (vid,))
    conn.commit()
    conn.close()
    return jsonify({"deleted": True, "id": vid})


# ---------------------------------------------------------------
#  BLOG POSTS
# ---------------------------------------------------------------

@bot_api_bp.route("/posts", methods=["GET"])
@require_api_key
def list_posts():
    conn = db.get_db()
    rows = conn.execute("SELECT * FROM blog_posts ORDER BY created_at DESC").fetchall()
    conn.close()
    return jsonify([post_to_json(r) for r in rows])


@bot_api_bp.route("/posts/<int:pid>", methods=["GET"])
@require_api_key
def get_post(pid):
    conn = db.get_db()
    row = conn.execute("SELECT * FROM blog_posts WHERE id=?", (pid,)).fetchone()
    conn.close()
    if not row:
        return jsonify({"error": "not_found"}), 404
    return jsonify(post_to_json(row))


@bot_api_bp.route("/posts", methods=["POST"])
@require_api_key
def create_post():
    data = request.get_json(silent=True) or {}
    if not data.get("title") or not data.get("body"):
        return jsonify({"error": "validation_error", "missing": [f for f in ["title", "body"] if not data.get(f)]}), 400

    conn = db.get_db()
    slug = data.get("slug") or db.slugify(data["title"])
    slug = db.unique_slug(conn, "blog_posts", slug)
    now = db.now()
    cur = conn.execute(
        "INSERT INTO blog_posts (slug,title,category,reading_time,body,status,published_at,created_at,updated_at) "
        "VALUES (?,?,?,?,?,?,?,?,?)",
        (
            slug, data["title"], data.get("category", "General"), data.get("reading_time", "5 min de lectura"),
            data["body"], data.get("status", "published"),
            data.get("published_at") or datetime.date.today().isoformat(), now, now,
        ),
    )
    conn.commit()
    new_id = cur.lastrowid
    row = conn.execute("SELECT * FROM blog_posts WHERE id=?", (new_id,)).fetchone()
    conn.close()
    return jsonify(post_to_json(row)), 201


@bot_api_bp.route("/posts/<int:pid>", methods=["PUT", "PATCH"])
@require_api_key
def update_post(pid):
    conn = db.get_db()
    row = conn.execute("SELECT * FROM blog_posts WHERE id=?", (pid,)).fetchone()
    if not row:
        conn.close()
        return jsonify({"error": "not_found"}), 404

    data = request.get_json(silent=True) or {}
    current = dict(row)
    for field in ["title", "category", "reading_time", "body", "status", "published_at"]:
        if field in data:
            current[field] = data[field]

    slug = current["slug"]
    if "title" in data and not data.get("slug"):
        slug = db.unique_slug(conn, "blog_posts", db.slugify(data["title"]), exclude_id=pid)
    elif data.get("slug"):
        slug = db.unique_slug(conn, "blog_posts", data["slug"], exclude_id=pid)

    conn.execute(
        "UPDATE blog_posts SET slug=?,title=?,category=?,reading_time=?,body=?,status=?,published_at=?,updated_at=? WHERE id=?",
        (slug, current["title"], current["category"], current["reading_time"], current["body"],
         current["status"], current["published_at"], db.now(), pid),
    )
    conn.commit()
    updated = conn.execute("SELECT * FROM blog_posts WHERE id=?", (pid,)).fetchone()
    conn.close()
    return jsonify(post_to_json(updated))


@bot_api_bp.route("/posts/<int:pid>", methods=["DELETE"])
@require_api_key
def delete_post(pid):
    conn = db.get_db()
    row = conn.execute("SELECT id FROM blog_posts WHERE id=?", (pid,)).fetchone()
    if not row:
        conn.close()
        return jsonify({"error": "not_found"}), 404
    conn.execute("DELETE FROM blog_posts WHERE id=?", (pid,))
    conn.commit()
    conn.close()
    return jsonify({"deleted": True, "id": pid})
