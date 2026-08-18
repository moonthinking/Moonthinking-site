"""Email notifications sent via Resend (https://resend.com).

Uses only the Python standard library (urllib) so no extra dependency is
needed in requirements.txt. If RESEND_API_KEY isn't configured, sending is
skipped silently (logged to stdout) — a missing/broken email setup should
never block a lead or application from being saved to the database, since
it's always visible in the admin panel regardless.
"""

import json
import os
import urllib.request
import urllib.error

RESEND_API_KEY = os.environ.get("RESEND_API_KEY", "").strip()
RESEND_FROM = os.environ.get("RESEND_FROM", "Moonthinking <notificaciones@moonthinking.com>").strip()
RESEND_TO = os.environ.get("RESEND_TO", "reclutamiento.cv@moonthinking.com").strip()

# label, field key — in display order for the notification email
LEAD_FIELDS = [
    ("Empresa", "company_name"),
    ("Contacto", "contact_name"),
    ("Teléfono", "contact_phone"),
    ("Correo", "contact_email"),
    ("Puesto a cubrir", "position_title"),
    ("Comentarios / resumen", "additional_comments"),
    ("Objetivo del puesto", "position_objective"),
    ("Actividades principales", "position_activities"),
    ("Días de trabajo", "work_days"),
    ("Horario laboral", "work_hours"),
    ("Modalidad", "modality"),
    ("Lugar de trabajo", "work_location"),
    ("¿Tendrá gente a su cargo?", "has_reports"),
    ("Reporta a", "reports_to"),
    ("Conformación del departamento", "department_makeup"),
    ("Escolaridad mínima", "min_education"),
    ("Experiencia requerida", "required_experience"),
    ("Conocimientos requeridos", "required_knowledge"),
    ("Habilidades requeridas", "required_skills"),
    ("Herramientas / equipo", "tools_equipment"),
    ("Idiomas", "languages"),
    ("Sueldo mensual", "salary"),
    ("Periodo de pago", "pay_period"),
    ("Prestaciones", "benefits"),
    ("Otro concepto de pago", "other_pay"),
    ("¿Necesita vehículo propio?", "needs_vehicle"),
    ("Forma de pago", "payment_method"),
    ("Personalidad del candidato ideal", "candidate_personality"),
    ("Tipo de vacante", "vacancy_type"),
    ("¿Tiene manual de procedimientos?", "has_procedures_manual"),
]


def _send(subject, html):
    if not RESEND_API_KEY:
        print(f"[notifications] RESEND_API_KEY no configurada — no se envió el correo '{subject}', "
              f"pero el registro ya quedó guardado en el panel de administración.")
        return False

    payload = {
        "from": RESEND_FROM,
        "to": [RESEND_TO],
        "subject": subject,
        "html": html,
    }
    req = urllib.request.Request(
        "https://api.resend.com/emails",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {RESEND_API_KEY}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            return resp.status < 300
    except urllib.error.HTTPError as e:
        try:
            detail = e.read().decode("utf-8", errors="replace")
        except Exception:
            detail = "(sin detalle)"
        print(f"[notifications] Error enviando correo '{subject}': HTTP {e.code} — {detail}")
        return False
    except urllib.error.URLError as e:
        print(f"[notifications] Error enviando correo '{subject}': {e}")
        return False


def send_lead_email(lead):
    """Notify the recruitment inbox immediately when someone submits the
    'Quiero contratar' contact form — whether it's just the quick contact
    info or the full detailed format."""
    is_full = bool((lead.get("position_objective") or "").strip() or (lead.get("required_experience") or "").strip())
    kind = "formato completo" if is_full else "contacto rápido"
    company = (lead.get("company_name") or "").strip() or "Empresa sin especificar"
    subject = f"Nuevo contacto ({kind}) — {company}"

    rows = []
    for label, key in LEAD_FIELDS:
        value = (lead.get(key) or "").strip()
        if value:
            rows.append(
                f"<tr><td style='padding:6px 12px;color:#666;vertical-align:top;white-space:nowrap'>{label}</td>"
                f"<td style='padding:6px 12px'>{value}</td></tr>"
            )
    attachment_note = ""
    if lead.get("attachment_filename"):
        attachment_note = "<p style='margin-top:14px;color:#666'>Adjuntaron un archivo — revísalo en el panel de administración, sección Solicitudes.</p>"

    html = f"""
    <div style="font-family:Arial,Helvetica,sans-serif;max-width:640px">
      <h2 style="margin-bottom:4px">Nuevo contacto desde "Quiero contratar"</h2>
      <p style="color:#666;margin-top:0">Tipo: {kind}</p>
      <table style="border-collapse:collapse;width:100%">{''.join(rows)}</table>
      {attachment_note}
      <p style="margin-top:20px;color:#666">Puedes ver el detalle completo y responder desde el panel de administración, sección "Solicitudes".</p>
    </div>
    """
    return _send(subject, html)


def send_application_email(application):
    """Notify the recruitment inbox immediately when a candidate applies to
    a vacancy (with or without attaching their CV) from the 'Postularme'
    form on a vacancy page."""
    name = (application.get("full_name") or "").strip() or "Candidato sin nombre"
    vacancy_title = (application.get("vacancy_title") or "").strip() or "Vacante sin especificar"
    subject = f"Nueva postulación — {name} · {vacancy_title}"

    rows = [
        ("Vacante", vacancy_title),
        ("Nombre completo", application.get("full_name")),
        ("Correo", application.get("email")),
        ("Teléfono", application.get("phone")),
        ("Mensaje", application.get("message")),
    ]
    row_html = []
    for label, value in rows:
        value = (value or "").strip()
        if value:
            row_html.append(
                f"<tr><td style='padding:6px 12px;color:#666;vertical-align:top;white-space:nowrap'>{label}</td>"
                f"<td style='padding:6px 12px'>{value}</td></tr>"
            )

    cv_note = (
        "<p style='margin-top:14px;color:#0a7a3d;font-weight:600'>Adjuntó su CV — descárgalo desde el panel de administración, sección Postulaciones.</p>"
        if application.get("resume_filename")
        else "<p style='margin-top:14px;color:#b8860b'>No adjuntó CV en este formulario.</p>"
    )

    html = f"""
    <div style="font-family:Arial,Helvetica,sans-serif;max-width:640px">
      <h2 style="margin-bottom:4px">Nueva postulación a una vacante</h2>
      <table style="border-collapse:collapse;width:100%">{''.join(row_html)}</table>
      {cv_note}
      <p style="margin-top:20px;color:#666">Puedes ver el detalle completo y descargar el CV desde el panel de administración, sección "Postulaciones".</p>
    </div>
    """
    return _send(subject, html)
