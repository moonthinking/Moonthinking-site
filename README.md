# Moonthinking — sitio real

Este es el sitio real de Moonthinking (no el mockup): un sitio Flask + SQLite con el mismo diseño aprobado, más un panel de administración y una API para bots.

## Qué incluye

- Sitio público: Inicio, Soluciones, Nosotros, Quiero contratar (con formulario funcional), Vacantes (lista + detalle + postulación) y Blog (lista + detalle) — todo con el mismo diseño ya aprobado.
- Panel de administración en `/admin`: alta, edición y baja de vacantes y artículos del blog, más las solicitudes de empresas y postulaciones de candidatos que lleguen por los formularios del sitio.
- API para bots en `/api/bot/*`: para que una automatización cree, edite o borre vacantes y artículos sin pasar por el panel.

## Por qué Flask (Python) y no Next.js/React

Este sitio se construyó en el entorno de trabajo de esta sesión, que no tuvo acceso a los registros de paquetes de Node (npm) — solo a lo que ya estaba preinstalado, donde Flask sí estaba disponible. Flask es una elección igual de sólida para "código a la medida": es la base de sitios en producción de todos tamaños, es más simple de desplegar (no requiere paso de "build" ni Node en el servidor), y funciona en cualquier hosting que corra Python. No es una limitación de calidad, fue la herramienta disponible en este entorno.

## Correrlo localmente

Requiere Python 3.10 o superior.

```bash
cd moonthinking-site
pip install -r requirements.txt
cp .env.example .env   # y edita los valores dentro
python3 seed.py        # crea la base de datos y la llena con las 6 vacantes y 6 artículos de ejemplo
python3 app.py         # levanta el sitio en http://localhost:5000
```

Panel de administración: `http://localhost:5000/admin` — la contraseña es `Gmoon2026`.

## Variables de entorno

Ver `.env.example`. Ya vienen con valores reales por default (funcionan sin configurar nada), pero si quieres reforzar la seguridad puedes definirlos como variables de entorno en tu hosting en vez de dejarlos en el código:

- `ADMIN_PASSWORD` — contraseña del panel. Ya está en `Gmoon2026`.
- `SECRET_KEY` — clave para firmar las sesiones. Ya viene generada.
- `BOT_API_KEY` — clave que deben mandar los bots para usar la API. Ya viene generada.
- `WHATSAPP_NUMBER` — número de WhatsApp del botón flotante.
- `RESEND_API_KEY`, `RESEND_FROM`, `RESEND_TO` — para las notificaciones por correo de "Quiero contratar". Ver la sección de abajo.

## Notificaciones por correo ("Quiero contratar" y postulaciones a vacantes)

Dos formularios del sitio mandan un correo de aviso inmediato, además de guardarse siempre en el panel:

- **Quiero contratar**: tiene dos niveles — primero solo pide el contacto básico (empresa, nombre, teléfono, correo, puesto y un comentario breve) con un botón **"Enviar mi contacto"**; abajo hay un botón secundario **"Llenar formato de perfil de la vacante"** que despliega el formulario detallado de 30 campos, por si la empresa prefiere darlo todo desde el inicio. Cualquiera de los dos envíos manda el correo.
- **Postularme** (en cada página de vacante): cuando un candidato aplica, con o sin adjuntar su CV.

Ambos casos:

1. Se guardan de inmediato en el panel de administración (secciones "Solicitudes" y "Postulaciones"), como siempre.
2. Mandan un correo de aviso inmediato a la dirección configurada en `RESEND_TO` (por default `reclutamiento.cv@moonthinking.com`), usando [Resend](https://resend.com).

**Para activar el envío de correos** (si no lo configuras, el sitio sigue funcionando normal, solo no llega el correo — el contacto de todos modos queda guardado en el panel):

1. Crea una cuenta gratis en [resend.com](https://resend.com) (tiene plan gratuito, suficiente para este uso).
2. Dentro de Resend, ve a **Domains** → **Add Domain** y agrega el dominio desde el que quieres mandar los correos (por ejemplo `moonthinking.com`, el mismo de `reclutamiento.cv@moonthinking.com`).
3. Resend te va a dar unos registros DNS (tipo TXT y MX) para verificar que el dominio es tuyo. Agrégalos en el panel de DNS de donde tengas administrado ese dominio — el mismo tipo de paso que agregar el CNAME de Render, solo que aquí son registros distintos (Resend te dice exactamente cuáles).
4. Una vez verificado el dominio (puede tardar unos minutos), ve a **API Keys** → **Create API Key** y copia la clave que empieza con `re_...`.
5. En tu hosting (Render), agrega estas variables de entorno:
   - `RESEND_API_KEY` = la clave que copiaste
   - `RESEND_FROM` = por ejemplo `Moonthinking <notificaciones@moonthinking.com>` (debe usar el dominio que verificaste)
   - `RESEND_TO` = `reclutamiento.cv@moonthinking.com` (o el correo donde quieras recibir los avisos)
6. Guarda — Render va a reiniciar el servicio con las nuevas variables y los correos empezarán a llegar.

Si algún día quieres cambiar a qué correo llegan los avisos, o agregar más de un destinatario, solo hay que ajustar `RESEND_TO` (por ahora manda a una sola dirección; agregar varias es un cambio sencillo cuando lo necesites).

## Desplegar a un hosting real

El sitio ya trae `Procfile`, `wsgi.py` y `requirements.txt`, listos para casi cualquier hosting de Python (Render, Railway, Fly.io, PythonAnywhere, un VPS propio con gunicorn + nginx, etc). Los pasos generales:

1. Sube el proyecto a un repositorio de Git (GitHub/GitLab) o directamente al hosting que elijas.
2. Configura las variables de entorno de la sección anterior en el panel del hosting.
3. El comando de arranque es: `gunicorn wsgi:app --bind 0.0.0.0:$PORT --workers 3` (ya está en el `Procfile`).
4. **No corras `seed.py` en producción** a menos que quieras contenido de ejemplo — el sitio arranca con el panel completamente vacío (sin vacantes ni artículos falsos) y tú cargas ahí las vacantes y artículos reales cuando quieras. `seed.py` solo es útil para pruebas en tu computadora (ver "Correrlo localmente" arriba).

### Importante: dónde vive la base de datos

Este sitio usa SQLite — una base de datos de un solo archivo (`moonthinking.db`), muy simple de operar y perfecta para arrancar. La única precaución: algunos hostings (Render free tier, Heroku, y similares) borran el disco en cada despliegue nuevo, lo que borraría también la base de datos. Si tu hosting hace esto, hay dos soluciones sencillas:

- Usar un "disco persistente" (persistent disk / volume) que casi todos los hostings ofrecen, y apuntar `DATABASE_PATH` a una ruta dentro de ese disco.
- Si el sitio crece y necesitas algo más robusto a futuro, migrar a Postgres (Flask lo soporta con un cambio menor en `db.py`) — no es necesario para empezar.

### Apuntar tu dominio (www.moonthinking.com.mx)

Una vez desplegado el sitio (vas a tener una URL temporal del hosting, tipo `moonthinking.onrender.com`), solo falta apuntar `www.moonthinking.com.mx` hacia esa URL. Cada hosting explica esto en su propia documentación ("custom domain" / "dominio personalizado") — típicamente es agregar un registro CNAME en la configuración DNS de donde tengas registrado el dominio, apuntando `www` hacia la URL que te dé el hosting, y (si quieres que `moonthinking.com.mx` sin el `www` también funcione) un registro A o redirección adicional según lo que pida tu hosting. Dime en qué hosting decides desplegarlo y te doy los pasos exactos con capturas de dónde hacer clic.

## El panel de administración

En `/admin` puedes:

- Ver un resumen con el número de vacantes activas, artículos publicados, solicitudes de empresas y postulaciones recibidas.
- Dar de alta, editar o borrar vacantes (título, ubicación, modalidad, salario, objetivo, responsabilidades, requisitos, prestaciones, y si está activa/borrador/cerrada).
- Dar de alta, editar o borrar artículos del blog (título, categoría, tiempo de lectura, contenido).
- Ver las solicitudes que las empresas mandan desde "Quiero contratar", con todo el detalle del formulario.
- Ver las postulaciones que los candidatos mandan desde cada vacante, con acceso al CV si lo adjuntaron.

Todo pensado para que alguien sin conocimientos técnicos pueda usarlo sin depender de un desarrollador para el día a día.

## La API para bots

Ver `/admin/api-docs` una vez dentro del panel — ahí está la documentación completa con ejemplos. En resumen: cualquier bot o automatización puede crear, leer, editar o borrar vacantes y artículos mandando el encabezado `X-API-Key` con el valor de `BOT_API_KEY`, a los endpoints `/api/bot/vacancies` y `/api/bot/posts`.

## Cosas que quedan pendientes / siguientes pasos sugeridos

- **Roles y usuarios del panel**: hoy el panel usa una sola contraseña compartida. Si más de una persona lo va a usar y quieres saber quién hizo qué cambio, se puede extender a usuarios individuales.
- **Claves de API por bot**: hoy todos los bots comparten una sola clave. Si quieres poder revocar el acceso de un bot específico sin afectar a los demás, se puede extender a una clave por bot.
- **Textos generales del sitio** (los títulos y descripciones de Inicio, Soluciones, Nosotros, Quiero contratar): hoy viven en el código, no en el panel — como se decidió que quedara por ahora. Si más adelante quieres poder editarlos también desde el panel, es una extensión sencilla sobre esta misma base.
- **Enlaces de redes sociales y páginas legales** (Aviso de Privacidad, Términos, Cookies) en el pie de página quedaron como marcadores de posición, igual que en el diseño aprobado — falta construir esas páginas cuando tengan el contenido listo.
