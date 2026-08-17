import os

BASE_DIR = os.path.dirname(__file__)
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "Gmoon2026")
BOT_API_KEY = os.environ.get("BOT_API_KEY", "Ri0kSIMkWslzvhNlvdyA3HSdkJvrnG3z")
WHATSAPP_NUMBER = os.environ.get("WHATSAPP_NUMBER", "524445473916")
WHATSAPP_TEXT = "Hola, me gustaría conocer más sobre sus servicios y vacantes."
