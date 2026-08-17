"""Populate the database with sample vacancies/blog posts matching the approved design mockup.
This is ONLY for local testing/demos. Do NOT run this on your production site — it starts empty
on purpose, so you never launch with placeholder/fake vacancies. Load real content from /admin instead.
Safe to re-run — it skips rows that already exist (by slug).
"""
import datetime

import db

TODAY = datetime.date.today()


def days_ago(n):
    return (TODAY - datetime.timedelta(days=n)).isoformat()


VACANCIES = [
    {
        "title": "Gerente de Expansión de Operaciones de Servicio",
        "location": "San Luis Potosí", "modality": "Presencial",
        "salary_display": "$65,000 MXN", "salary_tier": "blue",
        "published_at": days_ago(2), "is_confidential": 0, "company_label": "Confidencial",
        "positions": 1,
        "objetivo": "Liderar la expansión de las operaciones de servicio de la compañía en la región, asegurando el cumplimiento de los indicadores comerciales y operativos definidos por la dirección.",
        "responsabilidades": "Diseñar e implementar la estrategia de expansión regional\nLiderar al equipo de operaciones de servicio\nDar seguimiento a indicadores comerciales y de rentabilidad\nCoordinar con las áreas de ventas y operaciones",
        "requisitos": "5+ años de experiencia en puestos similares\nExperiencia liderando equipos multidisciplinarios\nDisponibilidad para viajar dentro de la región",
        "prestaciones": "De ley, más prestaciones superiores — detalle a confirmar durante el proceso.",
    },
    {
        "title": "Analista Financiero",
        "location": "San Luis Potosí", "modality": "Presencial",
        "salary_display": "$40,000 MXN", "salary_tier": None,
        "published_at": days_ago(3), "is_confidential": 0, "company_label": "Confidencial",
        "positions": 1,
        "objetivo": "Apoyar el análisis financiero y la elaboración de reportes que sustenten la toma de decisiones de la dirección.",
        "responsabilidades": "Elaborar reportes financieros periódicos\nDar seguimiento al presupuesto y variaciones contra lo real\nApoyar en el cierre contable mensual\nAnalizar indicadores de rentabilidad y flujo de efectivo",
        "requisitos": "Licenciatura en Finanzas, Contaduría o afín\n2+ años de experiencia en análisis financiero\nManejo avanzado de Excel",
        "prestaciones": "De ley, más prestaciones superiores — detalle a confirmar durante el proceso.",
    },
    {
        "title": "Auxiliar Contable",
        "location": "San Luis Potosí", "modality": "Presencial",
        "salary_display": "$20,000 MXN", "salary_tier": None,
        "published_at": days_ago(3), "is_confidential": 0, "company_label": "Confidencial",
        "positions": 1,
        "objetivo": "Apoyar las labores contables diarias de la empresa bajo la supervisión del área de contabilidad.",
        "responsabilidades": "Registrar pólizas contables\nConciliar cuentas bancarias\nApoyar en la generación de reportes fiscales\nArchivar y organizar documentación contable",
        "requisitos": "Estudios en Contaduría (truncados o en curso)\n1+ año de experiencia en un puesto similar\nConocimiento básico de paquetes contables",
        "prestaciones": "De ley.",
    },
    {
        "title": "Coordinador Comercial",
        "location": "San Luis Potosí", "modality": "Híbrida",
        "salary_display": "$65,000 MXN", "salary_tier": "blue",
        "published_at": days_ago(7), "is_confidential": 0, "company_label": "Confidencial",
        "positions": 1,
        "objetivo": "Coordinar al equipo comercial y dar seguimiento a los objetivos de ventas de la organización.",
        "responsabilidades": "Coordinar al equipo de ventas y dar seguimiento a sus metas\nElaborar reportes de desempeño comercial\nApoyar en la definición de estrategias comerciales\nDar seguimiento a cuentas clave",
        "requisitos": "3+ años de experiencia coordinando equipos comerciales\nExperiencia en manejo de indicadores de ventas\nDisponibilidad para viajar ocasionalmente",
        "prestaciones": "De ley, más esquema de comisiones — detalle a confirmar durante el proceso.",
    },
    {
        "title": "Vacante confidencial — Industria manufacturera",
        "location": "San Luis Potosí", "modality": "Presencial",
        "salary_display": "$40,000 MXN", "salary_tier": None,
        "published_at": days_ago(4), "is_confidential": 1, "company_label": "Confidencial",
        "positions": 1,
        "objetivo": "Posición dentro de una empresa del sector manufacturero — el detalle completo se comparte durante el proceso de selección.",
        "responsabilidades": "El detalle de responsabilidades se comparte durante el proceso, dada la confidencialidad de la posición.",
        "requisitos": "Experiencia previa en el sector manufacturero (deseable)",
        "prestaciones": "De ley, más prestaciones superiores — detalle a confirmar durante el proceso.",
    },
    {
        "title": "Gerente de Planta",
        "location": "San Luis Potosí", "modality": "Presencial",
        "salary_display": "$120,000 MXN", "salary_tier": "gold",
        "published_at": days_ago(5), "is_confidential": 0, "company_label": "Confidencial",
        "positions": 1,
        "objetivo": "Dirigir la operación integral de la planta, asegurando el cumplimiento de los objetivos de producción, calidad y seguridad.",
        "responsabilidades": "Dirigir la operación diaria de la planta\nAsegurar el cumplimiento de metas de producción y calidad\nLiderar los equipos de manufactura, mantenimiento y calidad\nDar seguimiento a indicadores de seguridad industrial",
        "requisitos": "8+ años de experiencia en manufactura, 3+ en un puesto de dirección de planta\nExperiencia liderando equipos numerosos\nConocimiento de sistemas de gestión de calidad",
        "prestaciones": "De ley, más prestaciones superiores — detalle a confirmar durante el proceso.",
    },
]

POSTS = [
    {
        "title": "Cómo estructurar una entrevista por competencias",
        "category": "Contratación", "reading_time": "5 min de lectura",
        "published_at": days_ago(2),
        "body": (
            "Una entrevista por competencias busca evidencia concreta de cómo la persona actuó en situaciones reales, "
            "en lugar de opiniones generales sobre su experiencia. Es una de las herramientas más confiables para "
            "predecir desempeño futuro.\n\n"
            "El comportamiento pasado, en situaciones comparables, es uno de los mejores indicadores del comportamiento "
            "futuro. Preguntar por ejemplos específicos —no hipótesis— reduce el margen de error en la evaluación.\n\n"
            "Para estructurarla bien conviene definir las competencias clave del puesto antes de la entrevista, pedir "
            "ejemplos concretos de situación, acción y resultado, profundizar con preguntas de seguimiento en lugar de "
            "quedarse con la primera respuesta, y evaluar con los mismos criterios a todos los candidatos del proceso."
        ),
    },
    {
        "title": "Lo que los candidatos evalúan antes de aceptar una oferta",
        "category": "Mercado laboral", "reading_time": "4 min de lectura",
        "published_at": days_ago(6),
        "body": (
            "El sueldo sigue siendo un factor decisivo, pero rara vez es el único. La claridad sobre el puesto, el "
            "equipo y el estilo de liderazgo directo pesa cada vez más en la decisión final de un candidato.\n\n"
            "Procesos de selección largos, poca comunicación sobre el avance, o falta de claridad sobre las "
            "condiciones de la oferta son señales que hacen dudar incluso a candidatos muy interesados.\n\n"
            "Las empresas que comunican con claridad qué esperan del puesto, cómo es el equipo y cuál es el siguiente "
            "paso del proceso tienden a cerrar más rápido a los candidatos que realmente les interesan."
        ),
    },
    {
        "title": "Señales de que tu empresa necesita un Recruitment Partner",
        "category": "Recursos Humanos", "reading_time": "6 min de lectura",
        "published_at": days_ago(10),
        "body": (
            "Cuando las vacantes se acumulan y el equipo interno de Recursos Humanos no da abasto para cubrirlas con "
            "la calidad y velocidad que el negocio necesita, suele ser momento de considerar un esquema de "
            "Recruitment Partner.\n\n"
            "Algunas señales comunes: procesos de contratación que se alargan más de lo esperado, posiciones que se "
            "vuelven a abrir por baja rotación, o un crecimiento acelerado que exige contratar varias posiciones al "
            "mismo tiempo.\n\n"
            "Un Recruitment Partner se integra como una extensión del equipo interno, dando continuidad y "
            "seguimiento cercano a los procesos de búsqueda, sin que la operación diaria de Recursos Humanos se vea "
            "comprometida."
        ),
    },
    {
        "title": "Cómo saber si necesitas Executive Search o Professional Search",
        "category": "Reclutamiento", "reading_time": "4 min de lectura",
        "published_at": days_ago(14),
        "body": (
            "No todas las vacantes requieren el mismo enfoque de búsqueda. La diferencia entre Executive Search y "
            "Professional Search está en el nivel de la posición y en la estrategia necesaria para llegar al "
            "candidato correcto.\n\n"
            "Executive Search está pensado para posiciones de alta dirección y liderazgo estratégico, donde la "
            "confidencialidad y el headhunting directo son esenciales. Professional Search, en cambio, está "
            "diseñado para coordinaciones, jefaturas y gerencias — las posiciones que mueven la operación día a día.\n\n"
            "Si la posición que buscas cubrir define el rumbo de la organización, probablemente necesitas Executive "
            "Search. Si es una posición operativa o de mando medio, Professional Search es el enfoque adecuado."
        ),
    },
    {
        "title": "Qué preguntar antes de contratar una agencia de reclutamiento",
        "category": "Empresas", "reading_time": "5 min de lectura",
        "published_at": days_ago(18),
        "body": (
            "No todas las agencias de reclutamiento trabajan igual, y elegir mal puede costar tiempo y dinero. Antes "
            "de contratar una, vale la pena hacer algunas preguntas clave.\n\n"
            "¿Cómo es su proceso de búsqueda y evaluación? ¿Entrevistan ellos mismos a los candidatos antes de "
            "presentártelos, o solo filtran currículums? ¿Qué pasa si la contratación no funciona dentro de los "
            "primeros meses?\n\n"
            "Una agencia seria puede explicarte con claridad su metodología, mostrar resultados anteriores y "
            "ofrecerte algún tipo de garantía sobre la colocación. Si no puede responder con claridad estas "
            "preguntas, probablemente no es el partner adecuado."
        ),
    },
    {
        "title": "Retener talento: lo que realmente pesa además del sueldo",
        "category": "Liderazgo", "reading_time": "6 min de lectura",
        "published_at": days_ago(21),
        "body": (
            "Subir el sueldo puede resolver una salida en el corto plazo, pero rara vez resuelve la causa de fondo. "
            "La mayoría de las personas no se van solo por dinero.\n\n"
            "La relación con su jefe directo, la claridad sobre su crecimiento dentro de la empresa, y sentir que su "
            "trabajo tiene un impacto real suelen pesar tanto o más que la compensación.\n\n"
            "Las empresas que retienen mejor a su talento no son necesariamente las que más pagan, sino las que dan "
            "seguimiento cercano, ofrecen claridad sobre el desarrollo profesional, y construyen un ambiente donde "
            "las personas quieren quedarse."
        ),
    },
]


def run():
    db.init_db()
    conn = db.get_db()
    now = db.now()

    created_v, created_p = 0, 0
    for item in VACANCIES:
        slug = db.slugify(item["title"])
        exists = conn.execute("SELECT id FROM vacancies WHERE slug=?", (slug,)).fetchone()
        if exists:
            continue
        conn.execute(
            "INSERT INTO vacancies (slug,title,location,modality,is_confidential,company_label,"
            "salary_display,salary_tier,positions,objetivo,responsabilidades,requisitos,prestaciones,"
            "status,published_at,created_at,updated_at) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                slug, item["title"], item["location"], item["modality"], item["is_confidential"],
                item["company_label"], item["salary_display"], item["salary_tier"], item["positions"],
                item["objetivo"], item["responsabilidades"], item["requisitos"], item["prestaciones"],
                "active", item["published_at"], now, now,
            ),
        )
        created_v += 1

    for item in POSTS:
        slug = db.slugify(item["title"])
        exists = conn.execute("SELECT id FROM blog_posts WHERE slug=?", (slug,)).fetchone()
        if exists:
            continue
        conn.execute(
            "INSERT INTO blog_posts (slug,title,category,reading_time,body,status,published_at,created_at,updated_at) "
            "VALUES (?,?,?,?,?,?,?,?,?)",
            (slug, item["title"], item["category"], item["reading_time"], item["body"],
             "published", item["published_at"], now, now),
        )
        created_p += 1

    conn.commit()
    conn.close()
    print(f"Seed complete: {created_v} vacancies created, {created_p} blog posts created "
          f"(existing rows were skipped).")


if __name__ == "__main__":
    run()
