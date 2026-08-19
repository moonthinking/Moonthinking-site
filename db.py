import sqlite3
import os
import datetime

DB_PATH = os.environ.get("DATABASE_PATH", os.path.join(os.path.dirname(__file__), "moonthinking.db"))

SCHEMA = """
CREATE TABLE IF NOT EXISTS vacancies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    slug TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    location TEXT NOT NULL DEFAULT 'San Luis Potosí',
    modality TEXT NOT NULL DEFAULT 'Presencial',
    is_confidential INTEGER NOT NULL DEFAULT 0,
    company_label TEXT NOT NULL DEFAULT 'Confidencial',
    salary_display TEXT,
    salary_tier TEXT,
    positions INTEGER NOT NULL DEFAULT 1,
    objetivo TEXT,
    responsabilidades TEXT,
    requisitos TEXT,
    prestaciones TEXT,
    status TEXT NOT NULL DEFAULT 'active',
    published_at TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS blog_posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    slug TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    category TEXT NOT NULL,
    reading_time TEXT NOT NULL DEFAULT '5 min de lectura',
    body TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'published',
    published_at TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS site_content (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vacancy_id INTEGER,
    vacancy_title TEXT,
    full_name TEXT, email TEXT, phone TEXT, message TEXT, resume_filename TEXT,
    status TEXT NOT NULL DEFAULT 'new',
    created_at TEXT NOT NULL,
    FOREIGN KEY (vacancy_id) REFERENCES vacancies(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT, contact_name TEXT, contact_phone TEXT, contact_email TEXT,
    position_title TEXT, position_objective TEXT, position_activities TEXT,
    work_days TEXT, work_hours TEXT, modality TEXT, work_location TEXT,
    has_reports TEXT, reports_to TEXT, department_makeup TEXT,
    min_education TEXT, required_experience TEXT, required_knowledge TEXT,
    required_skills TEXT, tools_equipment TEXT, languages TEXT,
    salary TEXT, pay_period TEXT, benefits TEXT, other_pay TEXT,
    needs_vehicle TEXT, payment_method TEXT,
    candidate_personality TEXT, vacancy_type TEXT, has_procedures_manual TEXT,
    additional_comments TEXT, attachment_filename TEXT,
    company_description TEXT, previous_employee_reason TEXT, improvement_feedback TEXT,
    status TEXT NOT NULL DEFAULT 'new',
    created_at TEXT NOT NULL
);
"""


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_db()
    conn.executescript(SCHEMA)
    conn.commit()
    conn.close()


def now():
    return datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z"


def slugify(text):
    import re
    text = text.lower().strip()
    replacements = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ñ": "n", "ü": "u",
    }
    for a, b in replacements.items():
        text = text.replace(a, b)
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "item"


def unique_slug(conn, table, base_slug, exclude_id=None):
    slug = base_slug
    i = 2
    while True:
        q = f"SELECT id FROM {table} WHERE slug = ?"
        params = [slug]
        if exclude_id is not None:
            q += " AND id != ?"
            params.append(exclude_id)
        row = conn.execute(q, params).fetchone()
        if not row:
            return slug
        slug = f"{base_slug}-{i}"
        i += 1
