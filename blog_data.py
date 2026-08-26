# -*- coding: utf-8 -*-
"""
Artículos fijos del blog público.

Igual que vacantes_data.py, estos 3 artículos están escritos directamente
en el código (no viven en la base de datos) para que no se pierdan con
los reinicios del plan gratuito de Render y para que queden fijos como
contenido de fondo del sitio. Son textos originales (redactados para
Moonthinking, no copiados de ninguna fuente, aunque inspirados en
tendencias y datos públicos de mercado laboral y reclutamiento) sobre
entrevistas, rotación de personal y los beneficios de contratar un
headhunter en México.

Cada artículo tiene un campo "image" con la ruta (relativa a /static)
de su imagen de portada, ubicada en static/img/blog/.

Para agregar o actualizar artículos hay que editar este archivo
directamente en GitHub (o en el código) y hacer commit a main.
"""

POSTS = [
    {
        "slug": "que-evaluan-los-headhunters-en-una-entrevista-2026",
        "title": "Qué evalúan realmente los headhunters en una entrevista en 2026",
        "category": "Entrevistas",
        "reading_time": "3 min de lectura",
        "published_at": "2026-08-18",
        "image": "img/blog/entrevistas-2026.svg",
        "body": "\n\n".join([
            "En 2026 una entrevista con un headhunter ya no se trata de repasar el currículum en voz alta. Para cuando alguien llega a esa conversación, su experiencia y sus referencias ya fueron revisadas de antemano; lo que el reclutador busca en la sala es todo lo que un papel no puede mostrar: cómo piensa la persona, cómo se conduce bajo presión y qué tan real es lo que dice.",
            "Lo primero que se evalúa es la conexión, no la respuesta perfecta. Un candidato que genera confianza, que muestra su valor con naturalidad y que realmente escucha la pregunta antes de contestar deja mejor impresión que alguien con respuestas memorizadas de manual. La madurez con la que se habla de experiencias pasadas también dice mucho: explicar una salida difícil sin caer en el reclamo o el papel de víctima es, para muchos headhunters, una señal más confiable que cualquier logro en el CV.",
            "Los logros cuantificados pesan cada vez más. Decir que se \"lideró un equipo\" dice poco; decir que se redujo un costo en un porcentaje concreto, se incrementaron ventas en un periodo definido o se recortó un tiempo de entrega dice mucho más, y es justo el tipo de evidencia que separa a un candidato promedio de uno que un headhunter recuerda semanas después.",
            "El manejo de herramientas de inteligencia artificial dejó de ser un extra y se convirtió en algo esperado, sobre todo en puestos de mando medio y alto. Ya no basta con saber que existen; los reclutadores preguntan cómo se usan en el trabajo diario y qué tan bien se entienden sus límites, porque eso anticipa qué tan rápido esa persona se adapta a herramientas nuevas dentro de la empresa.",
            "También se pone a prueba el pensamiento crítico y la capacidad de manejar ambigüedad: preguntas sobre decisiones difíciles, prioridades en conflicto o problemas sin una sola respuesta correcta sirven para ver cómo razona alguien cuando no hay un procedimiento que seguir al pie de la letra, algo cada vez más valioso en entornos que cambian rápido.",
            "Por último, la preparación sigue marcando la diferencia, pero de forma distinta a antes: investigar la empresa y el puesto ya se da por hecho, así que lo que distingue a un candidato es llegar con preguntas propias sobre los retos reales del puesto y la cultura del equipo. Al final, una buena entrevista es una evaluación en ambos sentidos, y los headhunters lo saben mejor que nadie: tan importante es encontrar a la persona correcta como que esa persona confirme que la empresa también es la correcta para ella.",
        ]),
    },
    {
        "slug": "alta-rotacion-y-escasez-de-talento-en-mexico",
        "title": "La alta rotación en México y por qué cada vez cuesta más encontrar al candidato correcto",
        "category": "Mercado laboral",
        "reading_time": "3 min de lectura",
        "published_at": "2026-08-18",
        "image": "img/blog/rotacion-mexico.svg",
        "body": "\n\n".join([
            "México vive una paradoja incómoda: nunca había habido tanta necesidad de contratar y, al mismo tiempo, nunca había sido tan difícil quedarse con la gente correcta. Las empresas compiten por talento en un mercado donde encontrar a alguien calificado ya es complicado, y retenerlo una vez contratado lo es todavía más.",
            "Las cifras de rotación lo confirman. Distintos estudios de universidades y agencias de recursos humanos ubican la rotación de personal en México entre las más altas de América Latina, con tasas que van de un 17% general hasta arriba de 24% según el sector, y que en manufactura pueden llegar a superar el 30% anual. Con niveles de desempleo bajos, cada vacante que se abre por una renuncia tarda más en cubrirse y cuesta más resolverla bien.",
            "Las razones detrás de esas renuncias se repiten con pocas variaciones: liderazgo débil, falta de reconocimiento y sueldos que no van a la par de las expectativas del mercado. Son causas que casi nunca se detectan en una entrevista rápida, pero que sí se pueden anticipar con un proceso de selección que valide desde el principio si las expectativas del candidato y la realidad del puesto realmente coinciden.",
            "El costo de no lograrlo es alto y muy concreto. Reemplazar a una persona que se va suele costar entre uno y medio y cinco sueldos mensuales según el nivel del puesto, y cuando la salida ocurre en los primeros meses, ese costo puede rondar los 200,000 pesos por contratación fallida. Una empresa de 500 empleados con una rotación del 20% anual puede perder más de 6 millones de pesos al año solo en reemplazar gente, sin contar el golpe a la productividad mientras el puesto está vacante.",
            "A esto se suma otro problema distinto: no siempre es que falten candidatos, sino que faltan los candidatos con las habilidades correctas. Una parte considerable de las empresas en México reporta dificultades para cubrir sus vacantes, y buena parte de ellas señala que quienes se postulan no tienen las habilidades técnicas o blandas que el puesto exige. La demanda de perfiles con manejo real de inteligencia artificial, por ejemplo, ya compite de tú a tú con la de ingenierías tradicionales, y en ciudades industriales como San Luis Potosí, León o Querétaro la competencia por técnicos especializados es cada vez más intensa.",
            "Todo esto deja una conclusión difícil de ignorar: publicar una vacante y esperar ya no alcanza, ni para encontrar a la persona correcta ni para quedarse con ella. Encontrar talento que además se quede requiere validar desde antes del primer día si el puesto, el sueldo y la cultura de la empresa realmente están alineados con lo que esa persona busca, y eso es exactamente lo que un proceso de selección bien hecho puede hacer distinto frente a la rotación que hoy enfrenta la mayoría de las empresas del país.",
        ]),
    },
    {
        "slug": "beneficios-de-contratar-un-headhunter",
        "title": "Los beneficios reales de contratar un headhunter: velocidad, tiempo y dinero",
        "category": "Beneficios",
        "reading_time": "3 min de lectura",
        "published_at": "2026-08-18",
        "image": "img/blog/beneficios-headhunter.svg",
        "body": "\n\n".join([
            "Una vacante clave que sigue abierta no es un problema que espera en silencio: cuesta dinero todos los días, aunque no aparezca como un renglón claro en ningún estado de resultados. Es una de las razones por las que cada vez más empresas en México dejan de ver al headhunting como un gasto y empiezan a tratarlo como lo que realmente es, una forma de proteger tiempo y dinero que de otra forma se pierden sin que nadie lo note a tiempo.",
            "El costo de una posición vacante casi nunca se limita al sueldo que se ahorra mientras nadie la ocupa. Las decisiones que dependían de esa persona se atrasan, el trabajo se reparte entre un equipo que ya tenía su carga completa, los tiempos de respuesta se alargan y, en puestos comerciales u operativos, se pierden oportunidades concretas de negocio. Con el tiempo, ese desgaste también eleva el riesgo de que alguien más del equipo termine renunciando por la carga extra, lo que convierte una sola vacante en dos.",
            "Aquí es donde la velocidad de un headhunter marca la diferencia real. A diferencia de una búsqueda que arranca de cero el día que se publica la vacante, un proceso de headhunting parte de un mercado ya mapeado y de contacto previo con talento pasivo, esas personas que no están buscando activamente pero que encajan con el perfil. Esa ventaja inicial es justo lo que acorta el tiempo real entre que se abre el puesto y que alguien calificado empieza a trabajar, en lugar de dejar la vacante expuesta durante meses a la espera de que el candidato ideal aplique por su cuenta.",
            "También cambia la forma correcta de comparar el costo. Evaluar solo el honorario de un headhunter frente al costo de contratar por cuenta propia es una comparación incompleta: hay que sumar el tiempo directivo invertido en filtrar candidatos, el costo de la vacante mientras sigue abierta y, sobre todo, el riesgo de una mala contratación. Ese riesgo no es menor: reemplazar a alguien que no funcionó puede costar varios sueldos mensuales y, si la salida ocurre en los primeros meses, obliga a empezar el proceso completo otra vez, con el tiempo perdido que eso implica.",
            "Ahí está el argumento más simple y más contundente a favor de un proceso de búsqueda bien hecho: el tiempo sin la persona indicada en un puesto clave es, literalmente, dinero que no vuelve. No es solo el sueldo que se paga de más por rehacer el proceso, es la operación que no avanzó, las decisiones que se pospusieron y el equipo que trabajó de más mientras tanto. Contratar un headhunter no elimina ese riesgo por completo, pero sí lo reduce de forma medible, y esa es la razón por la que cada vez más empresas en México prefieren pagar por certeza y velocidad antes que seguir apostando el tiempo de espera a que la persona correcta aparezca sola.",
        ]),
    },
]


def get_all():
    return POSTS


def get_by_slug(slug):
    for p in POSTS:
        if p["slug"] == slug:
            return p
    return None
