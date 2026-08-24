# -*- coding: utf-8 -*-
"""
Vacantes fijas del sitio publico.

Estos son los 13 perfiles de vacante "de planta" del sitio: los roles y
sectores que de verdad mas se repiten en el historico real de 603
vacantes de Moonthinking (verificado por rol, nivel y sector), pensados
para quedar fijos en la pagina de Vacantes como perfiles de referencia
(no vacantes puntuales de un cliente especifico). Se escriben
directamente en el codigo (no viven en la base de datos) para que NUNCA
se pierdan si Render reinicia o borra el sistema de archivos local del
plan gratuito, y para que no se puedan editar por accidente desde el
panel de admin.

Para actualizar esta lista hay que editar este archivo directamente en
GitHub (o en el codigo) y hacer commit a main; Render la tomara en el
siguiente deploy.
"""

VACANCIES = [
    {
        "slug": "director-general-grupo-corporativo",
        "title": "Director General - Grupo Corporativo",
        "location": "San Luis Potosí",
        "modality": "Presencial",
        "is_confidential": True,
        "company_label": "Confidencial",
        "salary_display": "$150,000",
        "salary_tier": "gold",
        "positions": 1,
        "objetivo": (
            "Dirigir la operación y estrategia de un grupo con varias unidades "
            "de negocio, garantizando resultados y gobernanza corporativa."
        ),
        "responsabilidades": "\n".join([
            "Definir la estrategia y objetivos del grupo.",
            "Supervisar a los directores de cada unidad de negocio.",
            "Aprobar presupuestos, inversiones y expansión.",
            "Reportar resultados al consejo o a los propietarios.",
        ]),
        "requisitos": "\n".join([
            "8 a 10 años en dirección general o corporativa.",
            "Experiencia liderando múltiples unidades o empresas.",
            "Visión estratégica y financiera.",
        ]),
        "prestaciones": "$150,000 mensuales + prestaciones superiores a la ley + seguro de gastos médicos mayores + auto + bono por resultados.",
        "status": "active",
        "published_at": "2026-08-24",
    },
    {
        "slug": "ejecutivo-ventas-industrial",
        "title": "Ejecutivo de Ventas - Industrial",
        "location": "San Luis Potosí",
        "modality": "Presencial",
        "is_confidential": True,
        "company_label": "Confidencial",
        "salary_display": "$30,000 + comisiones",
        "salary_tier": None,
        "positions": 1,
        "objetivo": (
            "Prospectar, asesorar y cerrar ventas de productos o servicios "
            "industriales con clientes, apoyando las metas comerciales del "
            "equipo."
        ),
        "responsabilidades": "\n".join([
            "Prospectar y dar seguimiento a clientes potenciales.",
            "Asesorar al cliente y elaborar cotizaciones.",
            "Cumplir metas de venta mensuales.",
            "Registrar la actividad comercial en el CRM.",
        ]),
        "requisitos": "\n".join([
            "1 a 2 años en ventas o atención a clientes.",
            "Facilidad de palabra y orientación a resultados.",
            "Manejo básico de CRM/Excel.",
        ]),
        "prestaciones": "$30,000 mensuales + comisiones por cumplimiento + prestaciones de ley.",
        "status": "active",
        "published_at": "2026-08-24",
    },
    {
        "slug": "director-financiero-grupo-corporativo",
        "title": "Director Financiero - Grupo Corporativo",
        "location": "San Luis Potosí",
        "modality": "Presencial",
        "is_confidential": True,
        "company_label": "Confidencial",
        "salary_display": "$120,000",
        "salary_tier": "gold",
        "positions": 1,
        "objetivo": (
            "Dirigir la estrategia financiera de un grupo corporativo, "
            "garantizando rentabilidad, control y cumplimiento."
        ),
        "responsabilidades": "\n".join([
            "Dirigir presupuesto, tesorería y contabilidad del grupo.",
            "Analizar rentabilidad por unidad de negocio.",
            "Gestionar la relación con bancos e inversionistas.",
            "Asesorar a la dirección en decisiones estratégicas.",
        ]),
        "requisitos": "\n".join([
            "6 a 10 años en finanzas, 3+ en puesto de gerencia o dirección.",
            "Normatividad fiscal mexicana y NIF/IFRS.",
            "Liderazgo y pensamiento estratégico.",
        ]),
        "prestaciones": "$120,000 mensuales + prestaciones superiores a la ley + seguro de gastos médicos mayores + bono anual.",
        "status": "active",
        "published_at": "2026-08-24",
    },
    {
        "slug": "coordinador-almacen-salud-insumos-medicos",
        "title": "Coordinador de Almacén - Salud e Insumos Médicos",
        "location": "San Luis Potosí",
        "modality": "Presencial",
        "is_confidential": True,
        "company_label": "Confidencial",
        "salary_display": "$20,000",
        "salary_tier": None,
        "positions": 1,
        "objetivo": (
            "Coordinar la recepción, resguardo y despacho de insumos médicos, "
            "garantizando exactitud de inventario y cumplimiento de rutas de "
            "entrega."
        ),
        "responsabilidades": "\n".join([
            "Coordinar la recepción, acomodo y resguardo de mercancía en almacén.",
            "Supervisar la preparación de pedidos y las rutas de entrega.",
            "Controlar inventarios y reportar diferencias.",
            "Coordinar al personal de almacén a su cargo.",
        ]),
        "requisitos": "\n".join([
            "2 a 4 años en almacén o logística, idealmente en salud/farma.",
            "Manejo de sistemas de inventario (WMS/ERP).",
            "Liderazgo de equipo pequeño de almacén.",
        ]),
        "prestaciones": "$20,000 mensuales + prestaciones de ley + vales de despensa según cliente.",
        "status": "active",
        "published_at": "2026-08-24",
    },
    {
        "slug": "director-operaciones-industriales-manufactura",
        "title": "Director de Operaciones Industriales - Manufactura",
        "location": "San Luis Potosí",
        "modality": "Presencial",
        "is_confidential": True,
        "company_label": "Confidencial",
        "salary_display": "$130,000",
        "salary_tier": "gold",
        "positions": 1,
        "objetivo": (
            "Dirigir la operación industrial completa (producción, "
            "mantenimiento y calidad), maximizando eficiencia, seguridad y "
            "rentabilidad de la planta."
        ),
        "responsabilidades": "\n".join([
            "Dirigir las áreas de producción, mantenimiento, calidad y seguridad.",
            "Definir metas de productividad, costos y eficiencia operativa.",
            "Supervisar el cumplimiento normativo (seguridad industrial, ambiental, STPS).",
            "Liderar a los gerentes de planta y equipos de mejora continua.",
        ]),
        "requisitos": "\n".join([
            "8 a 10 años en dirección de operaciones industriales.",
            "Experiencia en manufactura, producción o procesos industriales.",
            "Liderazgo de plantas o múltiples líneas de producción.",
        ]),
        "prestaciones": "$130,000 mensuales + prestaciones superiores a la ley + seguro de gastos médicos mayores + auto + bono por resultados.",
        "status": "active",
        "published_at": "2026-08-24",
    },
    {
        "slug": "auxiliar-administrativo-contable",
        "title": "Auxiliar Administrativo / Contable",
        "location": "San Luis Potosí",
        "modality": "Presencial",
        "is_confidential": True,
        "company_label": "Confidencial",
        "salary_display": "$20,000",
        "salary_tier": None,
        "positions": 1,
        "objetivo": (
            "Apoyar las actividades administrativas y/o contables diarias, "
            "garantizando orden y seguimiento de la información."
        ),
        "responsabilidades": "\n".join([
            "Apoyar en captura y registro administrativo/contable.",
            "Archivar y dar seguimiento a documentación.",
            "Apoyar en facturación, pagos o cobranza.",
            "Atender trámites de personal y proveedores.",
        ]),
        "requisitos": "\n".join([
            "1 a 2 años en puestos administrativos o contables.",
            "Manejo de Office (Excel básico-intermedio).",
            "Organización y actitud de servicio.",
        ]),
        "prestaciones": "$20,000 mensuales + prestaciones de ley + vales de despensa según cliente.",
        "status": "active",
        "published_at": "2026-08-24",
    },
    {
        "slug": "director-comercial-automotriz",
        "title": "Director Comercial - Automotriz",
        "location": "San Luis Potosí",
        "modality": "Presencial",
        "is_confidential": True,
        "company_label": "Confidencial",
        "salary_display": "$100,000 + bonos",
        "salary_tier": "gold",
        "positions": 1,
        "objetivo": (
            "Liderar la estrategia comercial y el equipo de ventas para "
            "impulsar el crecimiento rentable del negocio."
        ),
        "responsabilidades": "\n".join([
            "Diseñar el plan comercial y las metas de venta.",
            "Liderar y desarrollar al equipo comercial.",
            "Negociar cuentas y clientes estratégicos.",
            "Analizar mercado y competencia.",
        ]),
        "requisitos": "\n".join([
            "5 a 8 años en puestos comerciales, liderando equipos.",
            "Negociación y orientación a resultados.",
            "Excel avanzado y CRM.",
        ]),
        "prestaciones": "$100,000 mensuales + bonos por resultados + prestaciones superiores a la ley + auto o gasolina.",
        "status": "active",
        "published_at": "2026-08-24",
    },
    {
        "slug": "asesor-comercial-concesionarias-automotrices",
        "title": "Asesor Comercial - Concesionarias Automotrices",
        "location": "San Luis Potosí",
        "modality": "Presencial",
        "is_confidential": True,
        "company_label": "Confidencial",
        "salary_display": "Sueldo base + comisiones",
        "salary_tier": None,
        "positions": 1,
        "objetivo": (
            "Atender y asesorar a clientes de la concesionaria, impulsando "
            "ventas de unidades, refacciones o servicio."
        ),
        "responsabilidades": "\n".join([
            "Atender y asesorar a clientes en piso o showroom.",
            "Cumplir metas de venta de unidades y servicios.",
            "Elaborar cotizaciones y dar seguimiento al cierre.",
            "Dar seguimiento postventa al cliente.",
        ]),
        "requisitos": "\n".join([
            "1 a 3 años en ventas o servicio automotriz.",
            "Facilidad de palabra y actitud de servicio.",
            "Manejo de CRM o control de piso de ventas.",
        ]),
        "prestaciones": "Sueldo base + comisiones por cumplimiento + prestaciones de ley.",
        "status": "active",
        "published_at": "2026-08-24",
    },
    {
        "slug": "gerente-capital-humano",
        "title": "Gerente de Capital Humano",
        "location": "San Luis Potosí",
        "modality": "Presencial",
        "is_confidential": True,
        "company_label": "Confidencial",
        "salary_display": "$32,000",
        "salary_tier": None,
        "positions": 1,
        "objetivo": (
            "Diseñar y ejecutar la estrategia de capital humano, garantizando "
            "atracción, desarrollo y retención de talento."
        ),
        "responsabilidades": "\n".join([
            "Liderar reclutamiento, nómina y relaciones laborales.",
            "Diseñar políticas y programas de desarrollo.",
            "Dar seguimiento a clima laboral y rotación.",
            "Garantizar cumplimiento de la Ley Federal del Trabajo.",
        ]),
        "requisitos": "\n".join([
            "4 a 6 años en Capital Humano, como gerente o líder.",
            "Conocimiento de nómina y normatividad laboral.",
            "Negociación y manejo de conflictos.",
        ]),
        "prestaciones": "$32,000 mensuales + prestaciones superiores a la ley + fondo de ahorro.",
        "status": "active",
        "published_at": "2026-08-24",
    },
    {
        "slug": "residente-obra-construccion-infraestructura",
        "title": "Residente de Obra - Construcción e Infraestructura",
        "location": "San Luis Potosí",
        "modality": "Presencial",
        "is_confidential": True,
        "company_label": "Confidencial",
        "salary_display": "$25,000",
        "salary_tier": None,
        "positions": 1,
        "objetivo": (
            "Supervisar la ejecución de obra, garantizando tiempos, "
            "presupuesto, calidad y seguridad."
        ),
        "responsabilidades": "\n".join([
            "Supervisar el avance físico y financiero de la obra.",
            "Coordinar cuadrillas, contratistas y materiales.",
            "Garantizar normativa de construcción y seguridad.",
            "Elaborar reportes y estimaciones de avance.",
        ]),
        "requisitos": "\n".join([
            "3 a 5 años como residente de obra.",
            "Manejo de AutoCAD y MS Project.",
            "Disponibilidad para foráneo según proyecto.",
        ]),
        "prestaciones": "$25,000 mensuales + prestaciones de ley/superiores + viáticos en proyectos foráneos.",
        "status": "active",
        "published_at": "2026-08-24",
    },
    {
        "slug": "gerente-compras-industrial",
        "title": "Gerente de Compras - Industrial",
        "location": "San Luis Potosí",
        "modality": "Presencial",
        "is_confidential": True,
        "company_label": "Confidencial",
        "salary_display": "$40,000",
        "salary_tier": None,
        "positions": 1,
        "objetivo": (
            "Administrar el abastecimiento de la empresa, garantizando costo, "
            "calidad y tiempo de entrega óptimos."
        ),
        "responsabilidades": "\n".join([
            "Negociar condiciones comerciales con proveedores.",
            "Elaborar y dar seguimiento al plan de compras.",
            "Controlar presupuesto y costo de adquisición.",
            "Coordinar con Almacén los niveles de inventario.",
        ]),
        "requisitos": "\n".join([
            "3 a 5 años en compras o abastecimiento.",
            "Negociación y análisis de costos.",
            "Excel avanzado y sistemas de compras/ERP.",
        ]),
        "prestaciones": "$40,000 mensuales + prestaciones superiores a la ley + vales de despensa.",
        "status": "active",
        "published_at": "2026-08-24",
    },
    {
        "slug": "gerente-mantenimiento-flotillas-transporte",
        "title": "Gerente de Mantenimiento y Flotillas - Transporte",
        "location": "San Luis Potosí",
        "modality": "Presencial",
        "is_confidential": True,
        "company_label": "Confidencial",
        "salary_display": "$38,000",
        "salary_tier": None,
        "positions": 1,
        "objetivo": (
            "Administrar el mantenimiento y la disponibilidad de la flotilla, "
            "garantizando seguridad vehicular y cumplimiento normativo de "
            "transporte."
        ),
        "responsabilidades": "\n".join([
            "Supervisar el taller de mantenimiento y la disponibilidad de unidades.",
            "Coordinar programas de mantenimiento preventivo y correctivo.",
            "Garantizar seguridad vehicular y normativa de transporte.",
            "Controlar costos de refacciones, combustible y mantenimiento.",
        ]),
        "requisitos": "\n".join([
            "3 a 5 años en mantenimiento de flotillas o talleres de transporte.",
            "Manejo de indicadores de disponibilidad y costos de flotilla.",
            "Liderazgo de personal técnico y de taller.",
        ]),
        "prestaciones": "$38,000 mensuales + prestaciones superiores a la ley + fondo de ahorro.",
        "status": "active",
        "published_at": "2026-08-24",
    },
    {
        "slug": "contador-general-contralor",
        "title": "Contador General / Contralor",
        "location": "San Luis Potosí",
        "modality": "Presencial",
        "is_confidential": True,
        "company_label": "Confidencial",
        "salary_display": "$35,000",
        "salary_tier": None,
        "positions": 1,
        "objetivo": (
            "Garantizar el registro contable y cumplimiento fiscal de la "
            "empresa, con información financiera confiable y oportuna."
        ),
        "responsabilidades": "\n".join([
            "Elaborar estados financieros y cierres contables.",
            "Garantizar cumplimiento fiscal (ISR, IVA, declaraciones).",
            "Supervisar auxiliares contables y facturación.",
            "Atender auditorías internas/externas y del SAT.",
        ]),
        "requisitos": "\n".join([
            "3 a 5 años en contabilidad general.",
            "Normatividad fiscal mexicana vigente.",
            "CONTPAQi/Aspel/SAP y Excel avanzado.",
        ]),
        "prestaciones": "$35,000 mensuales + prestaciones superiores a la ley + vales de despensa.",
        "status": "active",
        "published_at": "2026-08-24",
    },
]


def get_all():
    return VACANCIES


def get_by_slug(slug):
    for v in VACANCIES:
        if v["slug"] == slug:
            return v
    return None
