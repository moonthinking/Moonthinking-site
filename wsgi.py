"""Entry point for production WSGI servers (gunicorn, uWSGI, etc).

Example: gunicorn wsgi:app --bind 0.0.0.0:8000 --workers 3
"""
from app import app

if __name__ == "__main__":
    app.run()
