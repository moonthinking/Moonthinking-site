# -*- coding: utf-8 -*-
"""
Vacantes fijas del sitio publico.

Estas 10 vacantes estan escritas directamente en el codigo (no viven en la
base de datos) para que NUNCA se pierdan si Render reinicia o borra el
sistema de archivos local del plan gratuito, y para que no se puedan editar
por accidente desde el panel de admin. Fueron seleccionadas del historial
completo de CompuTrabajo de Santiago (activas, archivadas y vencidas),
cuidando variedad geografica (San Luis Potosi, Queretaro, Ciudad de Mexico,
Leon) y de tipo de puesto, con 3 posiciones arriba de $100,000 MXN, 4 entre
$60,000-$99,000 MXN y 3 entre $30,000-$60,000 MXN mensuales.

Para actualizar esta lista hay que editar este archivo directamente en
GitHub (o en el codigo) y hacer commit a main; Render la tomara en el
siguiente deploy.
"""

VACANCIES = [
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
        "published_at": "2026-08-17",
    },
    {
        "slug": "director-operaciones-vivienda-en-serie",
        "title": "Director de Operaciones - Vivienda en Serie",
        "location": "Querétaro",
        "modality": "Presencial",
        "is_confidential": False,
        "company_label": "Confidencial",
        "salary_display": "$110,000 - $130,000",
        "salary_tier": "gold",
        "positions": 1,
        "objetivo": (
            "Liderar la operación integral de proyectos de vivienda en serie en la "
            "región de Querétaro, garantizando el cumplimiento de tiempos, "
            "presupuestos y estándares de calidad en cada etapa de construcción y "
            "entrega."
        ),
        "responsabilidades": "\n".join([
            "Dirigir la planeación y ejecución operativa de los desarrollos habitacionales en construcción.",
            "Supervisar avances de obra, calendarios de entrega y cumplimiento de presupuestos.",
            "Coordinar con las áreas de construcción, ventas, gestoría y atención a clientes para asegurar entregas oportunas.",
            "Negociar y dar seguimiento a contratistas, proveedores y subcontratistas clave.",
            "Implementar indicadores de desempeño operativo y estrategias de mejora continua.",
            "Garantizar el cumplimiento de normativas de construcción y seguridad en obra.",
        ]),
        "requisitos": "\n".join([
            "Ingeniería Civil, Arquitectura o carrera afín.",
            "8 años de experiencia en dirección de operaciones dentro del sector de vivienda o desarrollos inmobiliarios.",
            "Experiencia comprobable liderando múltiples frentes de obra de manera simultánea.",
            "Conocimiento en procesos de gestoría, permisos y normativa de construcción.",
            "Liderazgo de equipos multidisciplinarios y visión estratégica de negocio.",
            "Disponibilidad para visitar obra de forma constante.",
        ]),
        "prestaciones": "Prestaciones superiores a las de ley · Vehículo o apoyo de gasolina · Seguro de Gastos Médicos Mayores · Bono por cumplimiento de metas",
        "status": "active",
        "published_at": "2026-08-15",
    },
    {
        "slug": "ceo-director-general-motocicletas",
        "title": "CEO / Director General - Motocicletas",
        "location": "Ciudad de México",
        "modality": "Presencial",
        "is_confidential": False,
        "company_label": "Confidencial",
        "salary_display": "$140,000",
        "salary_tier": "gold",
        "positions": 1,
        "objetivo": (
            "Encabezar la dirección general de la operación de la agencia, "
            "definiendo la estrategia comercial, financiera y operativa para "
            "consolidar el liderazgo de la marca en el mercado de motocicletas."
        ),
        "responsabilidades": "\n".join([
            "Definir y ejecutar la estrategia general del negocio: ventas, servicio, refacciones y financiamiento.",
            "Liderar a los gerentes de área y asegurar el cumplimiento de los objetivos comerciales y financieros.",
            "Supervisar la rentabilidad de la operación, el control de inventarios y la satisfacción del cliente.",
            "Representar a la empresa ante proveedores, distribuidores y la marca representada.",
            "Impulsar la apertura de nuevas líneas de negocio y la expansión de la operación.",
            "Reportar resultados a la Dirección General Corporativa.",
        ]),
        "requisitos": "\n".join([
            "Licenciatura en Administración, Negocios, Ingeniería o afín; deseable Maestría.",
            "8 a 10 años de experiencia en dirección general o gerencia general, preferentemente en el sector automotriz o de motocicletas.",
            "Sólida visión comercial, financiera y de operaciones.",
            "Experiencia liderando equipos multidisciplinarios de alto desempeño.",
            "Orientación a resultados y capacidad de negociación con marcas y distribuidores.",
        ]),
        "prestaciones": "Prestaciones superiores a las de ley · Bono anual por resultados · Seguro de Vida y GMM · Vehículo de la agencia",
        "status": "active",
        "published_at": "2026-08-12",
    },
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
        "published_at": "2026-08-10",
    },
    {
        "slug": "gerente-financiamiento-seguros-automotriz",
        "title": "Gerente de Financiamiento y Seguros - Agencia Automotriz",
        "location": "León",
        "modality": "Presencial",
        "is_confidential": False,
        "company_label": "Confidencial",
        "salary_display": "$65,000 - $75,000",
        "salary_tier": "blue",
        "positions": 1,
        "objetivo": (
            "Liderar el área de financiamiento y seguros de la agencia, "
            "maximizando la penetración de productos financieros y de protección "
            "en cada venta, asegurando el cumplimiento normativo y la satisfacción "
            "del cliente."
        ),
        "responsabilidades": "\n".join([
            "Dirigir la estrategia de colocación de créditos, seguros y productos de protección (F&I).",
            "Negociar y dar seguimiento a las relaciones con instituciones financieras y aseguradoras.",
            "Supervisar y capacitar al equipo de asesores de financiamiento y seguros.",
            "Garantizar el cumplimiento de políticas internas y normativa aplicable en materia financiera.",
            "Analizar indicadores de penetración, rentabilidad y cartera para la toma de decisiones.",
            "Colaborar con el área comercial para maximizar la conversión de financiamiento en cada venta.",
        ]),
        "requisitos": "\n".join([
            "Licenciatura en Administración, Finanzas o carrera afín.",
            "5 años de experiencia en puestos similares dentro del sector automotriz.",
            "Conocimiento de productos de financiamiento, seguros y esquemas F&I.",
            "Habilidades de negociación, liderazgo de equipos y orientación a resultados.",
            "Manejo de indicadores financieros y herramientas de análisis.",
        ]),
        "prestaciones": "Prestaciones de ley y superiores · Esquema de comisiones por colocación · Capacitación continua",
        "status": "active",
        "published_at": "2026-08-08",
    },
    {
        "slug": "subdirector-operativo-comercial-diesel",
        "title": "Subdirector Operativo y Comercial - Comercializadora de Diesel",
        "location": "Ciudad de México",
        "modality": "Presencial",
        "is_confidential": False,
        "company_label": "Confidencial",
        "salary_display": "$75,000 - $85,000",
        "salary_tier": "blue",
        "positions": 1,
        "objetivo": (
            "Dirigir la operación y la estrategia comercial de la comercializadora, "
            "asegurando el crecimiento rentable del negocio, el cumplimiento "
            "normativo del sector energético y la eficiencia de la cadena de "
            "suministro."
        ),
        "responsabilidades": "\n".join([
            "Definir y ejecutar la estrategia comercial y operativa de la comercializadora de diesel.",
            "Supervisar la cadena de suministro: abastecimiento, almacenamiento, distribución y logística.",
            "Liderar la relación comercial con clientes clave, proveedores y autoridades regulatorias.",
            "Garantizar el cumplimiento de la normativa vigente en materia energética y de seguridad.",
            "Analizar indicadores de rentabilidad, volumetría y eficiencia operativa.",
            "Coordinar equipos comerciales, operativos y administrativos.",
        ]),
        "requisitos": "\n".join([
            "Licenciatura en Administración, Ingeniería, Negocios o afín.",
            "6 a 8 años de experiencia en puestos gerenciales dentro del sector energético o de combustibles.",
            "Conocimiento de la normativa aplicable a la comercialización de hidrocarburos.",
            "Visión estratégica, comercial y capacidad de negociación.",
            "Experiencia liderando equipos multidisciplinarios.",
        ]),
        "prestaciones": "Prestaciones superiores a las de ley · Bono por resultados · Seguro de Gastos Médicos Mayores",
        "status": "active",
        "published_at": "2026-08-05",
    },
    {
        "slug": "gerente-servicios-compartidos",
        "title": "Gerente de Servicios Compartidos - Corporativo Multiunidades",
        "location": "San Luis Potosí",
        "modality": "Presencial",
        "is_confidential": False,
        "company_label": "Confidencial",
        "salary_display": "$65,000 - $70,000",
        "salary_tier": "blue",
        "positions": 1,
        "objetivo": (
            "Liderar el modelo de servicios compartidos del corporativo, "
            "estandarizando y optimizando los procesos administrativos, de "
            "sistemas y de soporte para las distintas unidades de negocio del "
            "grupo."
        ),
        "responsabilidades": "\n".join([
            "Dirigir las áreas de servicios compartidos: administración, sistemas, compras y soporte corporativo.",
            "Estandarizar procesos y políticas entre las diferentes unidades de negocio.",
            "Implementar y dar seguimiento a indicadores de desempeño y eficiencia operativa.",
            "Coordinar proyectos de mejora continua y transformación de procesos.",
            "Gestionar la relación con proveedores estratégicos y prestadores de servicios.",
            "Reportar resultados a la Dirección Corporativa.",
        ]),
        "requisitos": "\n".join([
            "Licenciatura en Administración, Ingeniería Industrial o carrera afín.",
            "5 a 7 años de experiencia en posiciones gerenciales dentro de esquemas de servicios compartidos o soporte corporativo.",
            "Experiencia gestionando múltiples unidades de negocio de forma simultánea.",
            "Habilidades de liderazgo, negociación y visión de mejora continua.",
            "Deseable experiencia en sector energético, retail o multiunidades.",
        ]),
        "prestaciones": "Prestaciones superiores a las de ley · Fondo de ahorro · Seguro de Gastos Médicos Mayores",
        "status": "active",
        "published_at": "2026-08-03",
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
        "published_at": "2026-07-30",
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
        "published_at": "2026-07-28",
    },
    {
        "slug": "gerente-regional-estaciones-bajio",
        "title": "Gerente Regional de Estaciones - Bajío",
        "location": "León",
        "modality": "Presencial",
        "is_confidential": False,
        "company_label": "Confidencial",
        "salary_display": "$45,000 - $55,000",
        "salary_tier": None,
        "positions": 1,
        "objetivo": (
            "Dirigir la operación de la red de estaciones de servicio en la "
            "región Bajío, garantizando el cumplimiento de metas comerciales, "
            "estándares de servicio y normativa vigente en cada punto de venta."
        ),
        "responsabilidades": "\n".join([
            "Supervisar la operación diaria de las estaciones de servicio asignadas a la región.",
            "Garantizar el cumplimiento de metas de venta, rentabilidad e indicadores comerciales.",
            "Dar seguimiento a estándares de servicio, imagen e inventarios en cada estación.",
            "Liderar y capacitar a los gerentes y encargados de cada punto de venta.",
            "Asegurar el cumplimiento de normativa en materia de seguridad e hidrocarburos.",
            "Coordinar con proveedores y áreas corporativas para el abasto oportuno.",
        ]),
        "requisitos": "\n".join([
            "Licenciatura en Administración, Ingeniería o carrera afín.",
            "4 a 6 años de experiencia en gerencia regional o multi-unidad, preferentemente en estaciones de servicio o retail.",
            "Disponibilidad para viajar dentro de la región Bajío.",
            "Liderazgo de equipos, orientación a resultados y capacidad de análisis comercial.",
            "Conocimiento de normativa aplicable a estaciones de servicio (deseable).",
        ]),
        "prestaciones": "Prestaciones de ley y superiores · Apoyo de gasolina y viáticos · Bono por cumplimiento de metas",
        "status": "active",
        "published_at": "2026-07-25",
    },
]


def get_all():
    return VACANCIES


def get_by_slug(slug):
    for v in VACANCIES:
        if v["slug"] == slug:
            return v
    return None
