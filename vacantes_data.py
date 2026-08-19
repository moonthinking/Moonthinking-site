# -*- coding: utf-8 -*-
"""
Vacantes fijas del sitio publico.

Estas son las vacantes que estan REALMENTE ACTIVAS en la cuenta de
CompuTrabajo de Santiago (verificado en vivo, filtro "Activas"). Se
escriben directamente en el codigo (no viven en la base de datos) para
que NUNCA se pierdan si Render reinicia o borra el sistema de archivos
local del plan gratuito, y para que no se puedan editar por accidente
desde el panel de admin.

Para actualizar esta lista (por ejemplo cuando una vacante se cierre o
se abra una nueva en CompuTrabajo) hay que editar este archivo
directamente en GitHub (o en el codigo) y hacer commit a main; Render la
tomara en el siguiente deploy.
"""

VACANCIES = [
    {
        "slug": "gerente-corporativo",
        "title": "Gerente Corporativo",
        "location": "San Luis Potosí",
        "modality": "Presencial",
        "is_confidential": False,
        "company_label": "Confidencial",
        "salary_display": "$80,000 - $90,000",
        "salary_tier": "blue",
        "positions": 1,
        "objetivo": (
            "Buscamos un gerente general experto en LIDEREAR las áreas de Legal, "
            "Sistemas, Mejora Continua y Compras, asegurando la continuidad "
            "operativa, el cumplimiento normativo y la eficiencia organizacional "
            "de las diferentes unidades de negocio."
        ),
        "responsabilidades": "\n".join([
            "Supervisar el cumplimiento legal y regulatorio de las empresas del grupo.",
            "Gestionar proyectos estratégicos en las áreas de Sistemas, Compras, Legal y Mejora Continua.",
            "Homologar procesos, infraestructura tecnológica y herramientas corporativas.",
            "Implementar indicadores de desempeño y estrategias de mejora continua.",
            "Coordinar equipos multidisciplinarios y dar seguimiento a proyectos corporativos.",
            "Impulsar la eficiencia operativa y la estandarización de procesos.",
        ]),
        "requisitos": "\n".join([
            "Licenciatura en Derecho, Ingeniería Industrial, Sistemas o carrera afín.",
            "Experiencia de 5 a 8 años en posiciones gerenciales.",
            "Experiencia gestionando áreas de soporte corporativo o servicios compartidos.",
            "Liderazgo de equipos multidisciplinarios.",
            "Deseable experiencia en sector energético o hidrocarburos.",
            "Visión estratégica y orientación a resultados.",
        ]),
        "prestaciones": "Sueldo bruto mensual de $80-90,000 · Prestaciones superiores a las de ley · Seguro de Vida · Seguro de Gastos Médicos · Fondo de Ahorro · Apoyo mensual de gasolina · Lunes a viernes 8am-6pm · Zona Centro, SLP",
        "status": "active",
        "published_at": "2026-08-17",
    },
    {
        "slug": "gerente-financiero-corporativo",
        "title": "Gerente Financiero Corporativo - Multiunidades",
        "location": "San Luis Potosí",
        "modality": "Presencial",
        "is_confidential": False,
        "company_label": "Confidencial",
        "salary_display": "$120,000",
        "salary_tier": "gold",
        "positions": 1,
        "objetivo": (
            "Buscamos un Líder experto en la administración y control financiero de "
            "MULTIUNIDADES, así como experto en diseñar y ejecutar la estrategia "
            "financiera corporativa del grupo, asegurando solidez financiera, "
            "cumplimiento fiscal, planeación estratégica, control interno y "
            "generación de información para la toma de decisiones de alta dirección."
        ),
        "responsabilidades": "\n".join([
            "Liderar tesorería, planeación financiera, auditoría interna, contabilidad y estrategia fiscal.",
            "Supervisar estados financieros, presupuestos, flujo de efectivo, rentabilidad y liquidez de las divisiones del grupo.",
            "Dirigir procesos de planeación financiera, análisis de inversiones y evaluación de proyectos estratégicos.",
            "Coordinar cumplimiento fiscal, auditorías internas y externas, control interno y gestión de riesgos.",
            "Consolidar indicadores financieros y reportes ejecutivos para Dirección General.",
            "Supervisar presupuestos anuales, proyecciones financieras y seguimiento de KPI's.",
            "Impulsar eficiencia operativa, economías de escala y mejora de procesos corporativos.",
            "Liderar equipos financieros multidisciplinarios y relación con bancos, auditores y asesores externos.",
        ]),
        "requisitos": "\n".join([
            "Licenciatura y deseable Maestría en Finanzas, Administración o Contaduría.",
            "7 años de experiencia en posiciones financieras de nivel gerencial o corporativo.",
            "Dominio en finanzas, fiscal, contabilidad, auditoría, presupuestos y análisis financiero.",
            "Experiencia en evaluación de inversiones, reporteo estratégico y manejo de ERP (SAP deseable).",
            "Inglés intermedio.",
        ]),
        "prestaciones": "Sueldo bruto mensual hasta $120,000 · Seguro de Gastos Médicos Mayores (SGMM) · Fondo de Ahorro (FA) · Apoyo de transporte · Horario de lunes a viernes 8:30-18:00 · Zona Centro, SLP",
        "status": "active",
        "published_at": "2026-08-13",
    },
    {
        "slug": "gerente-mercado-expansion-precios",
        "title": "Gerente de Mercado - Expansión y Precios",
        "location": "San Luis Potosí",
        "modality": "Presencial",
        "is_confidential": False,
        "company_label": "Confidencial",
        "salary_display": "$30,000 - $40,000",
        "salary_tier": None,
        "positions": 1,
        "objetivo": (
            "Buscamos un líder estratégico que combine visión comercial, "
            "inteligencia de mercado y capacidad de ejecución para impulsar el "
            "crecimiento rentable del negocio. Será clave en la expansión de la "
            "operación y en el desarrollo de estrategias de precios que maximicen "
            "rentabilidad y competitividad."
        ),
        "responsabilidades": "\n".join([
            "Definir y ejecutar estrategias de expansión, evaluando apertura, formato y ubicación de nuevos puntos de venta.",
            "Liderar la estrategia de precios para maximizar rentabilidad y competitividad.",
            "Analizar mercado, competencia, tendencias y comportamiento del consumidor para detectar oportunidades.",
            "Desarrollar iniciativas comerciales enfocadas en incrementar tráfico, conversión y ticket promedio.",
            "Trabajar de manera transversal con Operaciones, Finanzas, Compras y Marketing.",
            "Evaluar el desempeño de unidades y proyectos para asegurar resultados sostenibles.",
            "Elaborar análisis y recomendaciones para apoyar decisiones estratégicas del negocio.",
        ]),
        "requisitos": "\n".join([
            "Experiencia en posiciones estratégicas de mercado, expansión y precios, preferentemente en empresas de Alimentos y/o Retail.",
            "Sólida comprensión del negocio retail: formatos, ubicaciones, precios, categorías y rentabilidad.",
            "Perfil analítico con fuerte orientación a resultados.",
            "Capacidad para convertir información y datos en decisiones comerciales.",
            "Liderazgo, negociación y visión de negocio.",
            "Excel avanzado y manejo de herramientas de análisis y reporteo.",
        ]),
        "prestaciones": "$30,000 a $40,000 mensuales + prestaciones superiores a las de ley",
        "status": "active",
        "published_at": "2026-08-18",
    },
        {
        "slug": "ejecutivo-pauta-digital-marketing",
        "title": "Ejecutivo de Pauta Digital - Marketing",
        "location": "San Luis Potosí",
        "modality": "Presencial",
        "is_confidential": False,
        "company_label": "Confidencial",
        "salary_display": "$20,000",
        "salary_tier": None,
        "positions": 1,
        "objetivo": (
            "Responsable de ejecutar y optimizar la pauta digital del portafolio "
            "de marcas de un grupo automotriz con presencia en varias ciudades "
            "de México, convirtiendo estrategias, presupuestos y materiales ya "
            "definidos en campañas que generen leads al menor costo posible."
        ),
        "responsabilidades": "\n".join([
            "Construir y publicar campañas en Meta Ads, Google Ads y TikTok Ads a partir de los briefs, materiales y presupuestos asignados.",
            "Operar la pauta de un portafolio de marcas automotrices y sus líneas de negocio.",
            "Redactar el texto principal de los anuncios y generar variantes para pruebas A/B.",
            "Ejecutar el flujo de aprobación de campañas: cargar copys, dar seguimiento y liberar.",
            "Controlar el presupuesto asignado y alertar cualquier desviación.",
            "Mantener el dashboard de resultados y validar que los leads lleguen completos al CRM.",
        ]),
        "requisitos": "\n".join([
            "2 a 3 años operando campañas en Meta Ads y Google Ads con cuentas propias (no como apoyo).",
            "Manejo de Meta Business Manager y Google Ads a nivel ejecución.",
            "Google Analytics 4 a nivel lectura y validación de conversiones.",
            "Capacidad de administrar varias cuentas en paralelo sin perder el detalle.",
            "Deseable: certificaciones de Google Ads y Meta Blueprint, experiencia en generación de leads en sectores de ticket alto (automotriz, inmobiliaria, retail).",
        ]),
        "prestaciones": "Sueldo de $20,000 mensuales · Prestaciones de ley · Presupuesto real y marcas consolidadas para operar · Lunes a viernes 9:00-18:00 y sábados hasta medio día · Zona Lomas, SLP",
        "status": "active",
        "published_at": "2026-08-12",
    },
        {
        "slug": "coordinador-comercial-club-deportivo",
        "title": "Coordinador Comercial - Club Deportivo",
        "location": "Soledad de Graciano Sánchez",
        "modality": "Presencial",
        "is_confidential": False,
        "company_label": "Confidencial",
        "salary_display": "$16,000 + comisiones",
        "salary_tier": None,
        "positions": 1,
        "objetivo": (
            "Liderar la estrategia comercial del Club para incrementar la "
            "captación, conversión y retención de membresías, desarrollando un "
            "equipo comercial de alto desempeño y asegurando un crecimiento "
            "sostenible de los ingresos."
        ),
        "responsabilidades": "\n".join([
            "Diseñar y administrar el funnel comercial.",
            "Gestionar la captación de prospectos y el cierre de membresías.",
            "Desarrollar alianzas estratégicas y membresías corporativas.",
            "Identificar oportunidades de crecimiento y mejora comercial.",
            "Liderar, capacitar y desarrollar al equipo de ventas.",
            "Dar seguimiento a indicadores comerciales (KPIs) y al CRM.",
            "Elaborar reportes comerciales y proponer estrategias para mejorar resultados.",
            "Implementar estrategias de fidelización y satisfacción de los miembros.",
            "Coordinar acciones para reducir la cancelación de membresías y fortalecer la experiencia del cliente.",
        ]),
        "requisitos": "\n".join([
            "Licenciatura en Administración, Mercadotecnia, Negocios o carrera afín.",
            "Más de 5 años de experiencia en ventas de servicios B2C.",
            "Experiencia liderando equipos comerciales.",
            "Manejo de CRM, indicadores comerciales y herramientas digitales.",
            "Deseable experiencia en clubes deportivos, fitness, hospitalidad o empresas de servicios.",
        ]),
        "prestaciones": "Sueldo de $16,000 libres mensuales + comisiones · Bonos por cumplimiento de KPIs · Prestaciones de ley (IMSS, INFONAVIT, aguinaldo, vacaciones, prima vacacional) · Horario 9:00-14:00 y 16:00-19:00 lunes a viernes, sábados medio día",
        "status": "active",
        "published_at": "2026-08-13",
    },
    {
        "slug": "lider-capital-humano-club-deportivo",
        "title": "Líder de Capital Humano - Club Deportivo",
        "location": "Soledad de Graciano Sánchez",
        "modality": "Presencial",
        "is_confidential": False,
        "company_label": "Confidencial",
        "salary_display": "$16,000",
        "salary_tier": None,
        "positions": 1,
        "objetivo": (
            "Diseñar, implementar y consolidar la estrategia integral de Talento "
            "y Cultura del Club, combinando la operación de Recursos Humanos con "
            "el desarrollo organizacional para atraer, desarrollar y retener al "
            "mejor talento, y fortalecer una cultura de alto desempeño, "
            "bienestar y servicio."
        ),
        "responsabilidades": "\n".join([
            "Gestionar el ciclo completo de reclutamiento y selección.",
            "Coordinar altas, bajas, expedientes, capacitación e incidencias de nómina.",
            "Administrar descripciones de puesto, headcount y planeación de personal.",
            "Garantizar el cumplimiento de la legislación laboral y procesos administrativos.",
            "Coordinar inducción, convenios universitarios y programas de practicantes.",
            "Implementar programas de coaching y desarrollo para líderes, y diseñar planes de desarrollo individual.",
            "Medir y mejorar el clima organizacional; crear programas de reconocimiento, integración y bienestar.",
            "Automatizar procesos de Recursos Humanos mediante herramientas digitales e inteligencia artificial.",
            "Crear una bolsa permanente de talento e implementar indicadores y procesos escalables para el crecimiento del Club.",
        ]),
        "requisitos": "\n".join([
            "Licenciatura en Psicología, Recursos Humanos, Administración o carrera afín.",
            "Mínimo 4 años de experiencia liderando Recursos Humanos de forma integral.",
            "Experiencia en coaching, desarrollo organizacional o gestión del desempeño.",
            "Conocimiento sólido de legislación laboral mexicana.",
            "Experiencia diseñando e implementando procesos desde cero.",
            "Deseable experiencia en clubes deportivos, hospitalidad, retail o empresas de servicio, y familiaridad con herramientas de IA y automatización.",
        ]),
        "prestaciones": "Sueldo $16,000 libres mensuales · Bonos por cumplimiento de KPIs · Prestaciones de ley (IMSS, INFONAVIT, aguinaldo, vacaciones, prima vacacional) · Horario lunes a viernes 9:00-14:00 y 16:00-19:00, sábados medio día",
        "status": "active",
        "published_at": "2026-08-16",
    },
    {
        "slug": "lider-distribucion-operaciones-hidrocarburos",
        "title": "Líder de Distribución y Operaciones - Hidrocarburos",
        "location": "San Luis Potosí",
        "modality": "Presencial",
        "is_confidential": False,
        "company_label": "Confidencial",
        "salary_display": "$35,000 - $45,000",
        "salary_tier": None,
        "positions": 1,
        "objetivo": (
            "Buscamos un(a) Líder de Distribución y operaciones con experiencia en "
            "logística y control de volumetría dentro de los sectores de "
            "combustibles, gas o industrias afines. Será responsable de coordinar "
            "la operación de distribución, almacenamiento y flota de reparto, "
            "asegurando un óptimo control de inventarios, la trazabilidad del "
            "producto, el cumplimiento operativo y normativo, así como la "
            "eficiencia de los procesos."
        ),
        "responsabilidades": "\n".join([
            "Estandarizar procesos y optimizar el control de inventarios.",
            "Administrar el almacenamiento y la flota de reparto.",
            "Fortalecer los servicios de autoconsumo mediante una atención de alto nivel y relaciones comerciales de largo plazo.",
            "Implementar controles e indicadores que permitan consolidar una operación eficiente, ordenada y escalable.",
        ]),
        "requisitos": "\n".join([
            "Ingeniería Industrial, Mecánica, Logística o carrera afín.",
            "Experiencia en operaciones, logística o distribución de combustibles, gas o productos de manejo volumétrico.",
            "Conocimientos en control de volumetría, inventarios, almacenamiento y administración de flotas.",
            "Experiencia en implementación y seguimiento de procesos, controles e indicadores de desempeño.",
            "Capacidad para coordinar equipos de trabajo y asegurar el cumplimiento de objetivos operativos.",
            "Perfil organizado, analítico, con alta capacidad de resolución de problemas y orientación a resultados.",
        ]),
        "prestaciones": "Sueldo de $35,000 a $45,000 pesos brutos mensuales, de acuerdo con experiencia · Prestaciones superiores a las de ley · Lunes a viernes de 8:00 a.m. a 5:00 p.m.",
        "status": "active",
        "published_at": "2026-08-16",
    },
]


def get_all():
    return VACANCIES


def get_by_slug(slug):
    for v in VACANCIES:
        if v["slug"] == slug:
            return v
    return None
