import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import qrcode
from io import BytesIO

# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================

st.set_page_config(
    page_title="WEB LAB | Aprende programación",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="auto"
)

# =========================================================
# ENCABEZADO
# =========================================================

st.title("💻 WEB LAB")
st.subheader("Aprende a crear páginas web desde cero")

st.write(
    "Explora el mundo del desarrollo web, descubre sus herramientas "
    "y aprende conceptos básicos de programación."
)

st.info(
    "Una plataforma educativa para aprender, experimentar y crear."
)

# =========================================================
# MENÚ DE NAVEGACIÓN
# =========================================================

st.sidebar.title("🧭 WEB LAB")

seccion = st.sidebar.radio(
    "Navega por los contenidos:",
    [
        "🏠 Inicio",
        "📝 Bloc de notas",
        "🧱 HTML",
        "⚡ JavaScript",
        "🎨 CSS y style.css",
        "🔷 Figuras geométricas",
        "🤖 Vibecoding",
        "🎮 Zona interactiva",
        "📱 Código QR"
    ]
)

st.sidebar.divider()

st.sidebar.markdown("### 📚 Aprende")
st.sidebar.caption(
    "Conoce las herramientas y fundamentos "
    "del desarrollo web."
)

st.sidebar.markdown("### 🎮 Experimenta")
st.sidebar.caption(
    "Pon a prueba tus conocimientos "
    "con actividades interactivas."
)

st.sidebar.divider()

st.sidebar.write("💻 Proyecto educativo WEB LAB")

# =========================================================
# INICIO
# =========================================================

if seccion == "🏠 Inicio":

    st.title("🌐 Bienvenido al mundo del desarrollo web")

    st.write("""
    Las páginas web forman parte de nuestra vida cotidiana.
    Las utilizamos para estudiar, comunicarnos, entretenernos,
    comprar productos y acceder a información.

    Detrás de cada página existen diferentes herramientas
    que permiten organizar su contenido, diseñar su apariencia
    y crear experiencias interactivas.
    """)

    st.success(
        "En WEB LAB aprenderás cómo funcionan las páginas web "
        "y descubrirás herramientas para crear tus propios proyectos."
    )

    st.divider()

    st.header("🧩 Los pilares del desarrollo web")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.subheader("🧱 HTML")

        st.write("""
        Organiza la estructura y el contenido
        de una página web.
        """)

    with col2:

        st.subheader("🎨 CSS")

        st.write("""
        Define colores, tamaños, estilos
        y apariencia visual.
        """)

    with col3:

        st.subheader("⚡ JavaScript")

        st.write("""
        Permite agregar funciones
        e interactividad.
        """)

    st.divider()

    st.header("📚 Explora nuestros contenidos")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 📝 Bloc de notas")

        st.write("""
        Aprende cómo utilizar un editor de texto
        para escribir código.
        """)

        st.markdown("### 🧱 HTML")

        st.write("""
        Descubre cómo se organiza
        el contenido de una página.
        """)

        st.markdown("### ⚡ JavaScript")

        st.write("""
        Conoce cómo funcionan
        las interacciones.
        """)

    with col2:

        st.markdown("### 🎨 CSS")

        st.write("""
        Aprende a personalizar
        la apariencia de una página.
        """)

        st.markdown("### 🔷 Figuras")

        st.write("""
        Descubre cómo representar
        figuras mediante programación.
        """)

        st.markdown("### 🤖 Vibecoding")

        st.write("""
        Explora la creación de proyectos
        utilizando inteligencia artificial.
        """)

    st.divider()

    st.header("🌐 ¿Qué es una página web?")

    st.write("""
    Una página web es un documento digital que puede visualizarse
    mediante un navegador.

    Puede contener textos, imágenes, videos, enlaces,
    animaciones, gráficos y elementos interactivos.

    Las páginas web permiten compartir información,
    ofrecer servicios y conectar personas
    a través de Internet.
    """)

    st.header("💡 ¿Cómo se construye una página web?")

    with st.expander("1. Estructura"):

        st.write("""
        Se organizan los títulos, párrafos, imágenes,
        enlaces y demás contenidos.
        """)

    with st.expander("2. Diseño"):

        st.write("""
        Se definen colores, tamaños, tipografías,
        posiciones y estilos visuales.
        """)

    with st.expander("3. Interactividad"):

        st.write("""
        Se incorporan funciones para que los usuarios
        puedan interactuar con la página.
        """)

# =========================================================
# BLOC DE NOTAS
# =========================================================

elif seccion == "📝 Bloc de notas":

    st.title("📝 Crear páginas web desde el Bloc de notas")

    st.write("""
    El Bloc de notas es un editor de texto sencillo
    que viene incorporado en Windows.

    Permite escribir y guardar texto. También puede utilizarse
    para escribir código de diferentes lenguajes.
    """)

    st.header("📌 Pasos básicos")

    st.markdown("""
    **1. Abrir:** inicia el Bloc de notas desde Windows.

    **2. Escribir:** coloca el contenido o código que deseas crear.

    **3. Guardar:** selecciona la opción Guardar como.

    **4. Nombrar:** escribe el nombre del archivo.

    **5. Elegir ubicación:** selecciona una carpeta
    donde guardar el proyecto.

    **6. Abrir:** utiliza el programa correspondiente
    para visualizar o ejecutar el archivo.
    """)

    st.divider()

    st.header("✅ Ventajas")

    st.markdown("""
    - Es gratuito.
    - Es fácil de utilizar.
    - No necesita herramientas avanzadas.
    - Permite editar texto.
    - Es útil para aprender conceptos básicos.
    """)

    st.header("⚠️ Limitaciones")

    st.markdown("""
    - No tiene autocompletado especializado.
    - No facilita la detección de errores.
    - No incluye herramientas avanzadas.
    - Puede resultar incómodo en proyectos grandes.
    """)

    st.header("💻 Editores de código")

    st.write("""
    Existen programas especializados como Visual Studio Code
    que ofrecen herramientas para organizar proyectos,
    detectar errores y facilitar la escritura de código.
    """)

# =========================================================
# HTML
# =========================================================

elif seccion == "🧱 HTML":

    st.title("🧱 HTML: estructura de una página web")

    st.write("""
    HTML significa HyperText Markup Language,
    o Lenguaje de Marcado de Hipertexto.

    Es utilizado para organizar y estructurar
    el contenido de una página web.
    """)

    st.header("📚 ¿Para qué sirve?")

    st.markdown("""
    - Crear títulos y subtítulos.
    - Organizar párrafos.
    - Insertar imágenes.
    - Crear enlaces.
    - Organizar listas.
    - Crear formularios.
    - Dividir el contenido en secciones.
    """)

    st.divider()

    st.header("🧩 Conceptos fundamentales")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Etiquetas")

        st.write("""
        Identifican los componentes que forman
        parte de un documento.
        """)

        st.subheader("Elementos")

        st.write("""
        Representan componentes como títulos,
        párrafos, imágenes y enlaces.
        """)

    with col2:

        st.subheader("Atributos")

        st.write("""
        Proporcionan información adicional
        sobre determinados elementos.
        """)

        st.subheader("Estructura")

        st.write("""
        Permite organizar los contenidos
        de forma lógica.
        """)

    st.divider()

    st.header("🌐 Importancia de HTML")

    st.write("""
    HTML es uno de los fundamentos del desarrollo web.
    Organiza el contenido y se complementa
    con CSS para los estilos y JavaScript
    para las funcionalidades.
    """)

    st.warning(
        "HTML es un lenguaje de marcado, "
        "no un lenguaje de programación convencional."
    )

# =========================================================
# JAVASCRIPT
# =========================================================

elif seccion == "⚡ JavaScript":

    st.title("⚡ JavaScript: interactividad web")

    st.write("""
    JavaScript es un lenguaje de programación
    que permite agregar interactividad
    y comportamiento dinámico a las páginas web.
    """)

    st.header("🚀 ¿Qué permite realizar?")

    st.markdown("""
    - Responder a acciones de los usuarios.
    - Mostrar mensajes.
    - Validar formularios.
    - Crear animaciones.
    - Actualizar información.
    - Crear juegos.
    - Desarrollar aplicaciones web.
    """)

    st.divider()

    st.header("📱 Ejemplos de uso")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🖱️ Botones")

        st.write("""
        Permiten ejecutar acciones
        cuando el usuario los presiona.
        """)

        st.subheader("📋 Formularios")

        st.write("""
        Ayudan a comprobar la información
        que el usuario introduce.
        """)

    with col2:

        st.subheader("🔍 Búsquedas")

        st.write("""
        Permiten procesar información
        y mostrar resultados.
        """)

        st.subheader("🎮 Juegos")

        st.write("""
        Controlan movimientos,
        puntuaciones y eventos.
        """)

    st.divider()

    st.header("⭐ Importancia")

    st.write("""
    JavaScript permite que las páginas respondan
    a las acciones de los usuarios,
    creando experiencias dinámicas e interactivas.
    """)

# =========================================================
# CSS
# =========================================================

elif seccion == "🎨 CSS y style.css":

    st.title("🎨 CSS: estilos y diseño")

    st.write("""
    CSS significa Cascading Style Sheets,
    o Hojas de Estilo en Cascada.

    Es un lenguaje que permite definir
    la apariencia visual de una página web.
    """)

    st.header("🖌️ ¿Qué se puede modificar?")

    st.markdown("""
    - Colores.
    - Fondos.
    - Tipografías.
    - Tamaños de texto.
    - Bordes.
    - Espaciados.
    - Dimensiones.
    - Posiciones.
    - Diseño adaptable.
    """)

    st.divider()

    st.header("📄 ¿Qué es style.css?")

    st.write("""
    style.css es un nombre común para un archivo
    que contiene reglas CSS.

    En proyectos web tradicionales, permite separar
    los estilos visuales de la estructura y el contenido.
    """)

    st.header("✨ Ventajas de CSS")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Personalización")

        st.write("""
        Facilita modificar colores,
        tamaños y tipografías.
        """)

        st.subheader("Organización")

        st.write("""
        Permite separar la apariencia
        del contenido.
        """)

    with col2:

        st.subheader("Consistencia")

        st.write("""
        Ayuda a mantener estilos similares
        en diferentes secciones.
        """)

        st.subheader("Adaptabilidad")

        st.write("""
        Permite ajustar la presentación
        a distintos dispositivos.
        """)

    st.info(
        "CSS se utiliza principalmente "
        "para la presentación visual."
    )

# =========================================================
# FIGURAS GEOMÉTRICAS
# =========================================================

elif seccion == "🔷 Figuras geométricas":

    st.title("🔷 Figuras geométricas y programación")

    st.write("""
    La programación gráfica permite representar
    figuras, objetos y formas mediante instrucciones.

    Sus características pueden modificarse
    utilizando propiedades y valores.
    """)

    st.header("🟦 El cuadrado")

    st.write("""
    El cuadrado es un polígono de cuatro lados iguales
    y cuatro ángulos rectos.

    En programación gráfica puede representarse
    mediante coordenadas, dimensiones y color.
    """)

    st.header("🔵 El círculo")

    st.write("""
    El círculo es una figura geométrica
    cuyos puntos se encuentran dentro
    de una circunferencia.

    Su representación digital utiliza
    un centro y un radio.
    """)

    st.divider()

    st.header("⚙️ Propiedades modificables")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Tamaño")

        st.write("""
        Permite ampliar o reducir
        las dimensiones de la figura.
        """)

        st.subheader("Color")

        st.write("""
        Modifica el aspecto visual
        de la figura.
        """)

    with col2:

        st.subheader("Posición")

        st.write("""
        Permite cambiar el lugar
        donde se representa.
        """)

        st.subheader("Forma")

        st.write("""
        Permite seleccionar diferentes
        figuras geométricas.
        """)

    st.info("""
    Estas propiedades pueden controlarse mediante
    variables, funciones y herramientas gráficas.
    """)

# =========================================================
# VIBECODING
# =========================================================

elif seccion == "🤖 Vibecoding":

    st.title("🤖 Vibecoding: programación con inteligencia artificial")

    st.write("""
    El Vibecoding es una práctica de desarrollo
    en la que una persona utiliza instrucciones
    escritas en lenguaje natural para solicitar
    a una inteligencia artificial que genere,
    modifique o ayude a corregir código.
    """)

    st.header("🔄 ¿Cómo funciona?")

    st.markdown("""
    **1. Idea:** describe lo que deseas crear.

    **2. Instrucción:** escribe una solicitud clara.

    **3. Generación:** la inteligencia artificial
    crea una propuesta de código.

    **4. Prueba:** ejecuta y verifica el resultado.

    **5. Mejora:** solicita cambios y nuevas funciones.
    """)

    st.divider()

    st.header("✅ Ventajas")

    st.markdown("""
    - Facilita el inicio de proyectos.
    - Ayuda a personas principiantes.
    - Permite experimentar con ideas.
    - Puede agilizar tareas.
    - Facilita crear prototipos.
    """)

    st.header("⚠️ Desafíos")

    st.markdown("""
    - Puede generar código incorrecto.
    - Requiere revisar los resultados.
    - Es necesario verificar la seguridad.
    - No siempre comprende exactamente la solicitud.
    - Es importante comprender el código generado.
    """)

    st.success(
        "La inteligencia artificial puede ser una herramienta "
        "de apoyo, pero la revisión humana sigue siendo importante."
    )

# =========================================================
# ZONA INTERACTIVA
# =========================================================

elif seccion == "🎮 Zona interactiva":

    st.title("🎮 Zona interactiva")

    st.write("""
    ¡Pon a prueba tus conocimientos y experimenta
    con diferentes figuras geométricas!
    """)

    st.divider()

    # -----------------------------------------------------
    # QUIZ
    # -----------------------------------------------------

    st.header("🧠 Quiz de programación")

    preguntas = [
        {
            "pregunta": "¿Qué lenguaje organiza la estructura de una página web?",
            "opciones": ["CSS", "HTML", "Python"],
            "respuesta": "HTML"
        },
        {
            "pregunta": "¿Cuál permite agregar interactividad?",
            "opciones": ["JavaScript", "CSS", "Bloc de notas"],
            "respuesta": "JavaScript"
        },
        {
            "pregunta": "¿Cuál define los estilos visuales?",
            "opciones": ["HTML", "CSS", "SQL"],
            "respuesta": "CSS"
        },
        {
            "pregunta": "¿Qué es el Vibecoding?",
            "opciones": [
                "Un editor de imágenes",
                "Desarrollo con ayuda de inteligencia artificial",
                "Un sistema operativo"
            ],
            "respuesta": "Desarrollo con ayuda de inteligencia artificial"
        },
        {
            "pregunta": "¿Qué programa permite escribir código?",
            "opciones": [
                "Visual Studio Code",
                "Calculadora",
                "Reproductor de música"
            ],
            "respuesta": "Visual Studio Code"
        }
    ]

    respuestas = []

    for i, pregunta in enumerate(preguntas):

        st.markdown(
            f"**Pregunta {i + 1}: {pregunta['pregunta']}**"
        )

        respuesta = st.radio(
            "Selecciona una opción:",
            pregunta["opciones"],
            key=f"quiz_{i}",
            index=None
        )

        respuestas.append(respuesta)

    if st.button("📊 Calcular resultado"):

        if None in respuestas:

            st.warning("Debes responder todas las preguntas.")

        else:

            puntos = sum(
                respuestas[i] == preguntas[i]["respuesta"]
                for i in range(len(preguntas))
            )

            st.metric(
                "Puntuación",
                f"{puntos} / {len(preguntas)}"
            )

            if puntos == 5:

                st.balloons()

                st.success(
                    "¡Excelente! Respondiste todas correctamente."
                )

            elif puntos >= 3:

                st.success(
                    "¡Muy bien! Tienes buenos conocimientos."
                )

            else:

                st.info(
                    "Repasa los temas y vuelve a intentarlo."
                )

            with st.expander("Revisar respuestas"):

                for i, pregunta in enumerate(preguntas):

                    if respuestas[i] == pregunta["respuesta"]:

                        st.write(
                            f"✅ Pregunta {i + 1}: Correcta"
                        )

                    else:

                        st.write(
                            f"❌ Pregunta {i + 1}: "
                            f"La respuesta correcta es "
                            f"{pregunta['respuesta']}"
                        )

    st.divider()

    # -----------------------------------------------------
    # SIMULADOR DE FIGURAS
    # -----------------------------------------------------

    st.header("🎨 Simulador de figuras geométricas")

    st.write("""
    Personaliza una figura modificando
    sus características.
    """)

    figura = st.selectbox(
        "Selecciona una figura:",
        ["Cuadrado", "Círculo"]
    )

    color_nombre = st.selectbox(
        "Selecciona un color:",
        [
            "Azul",
            "Rojo",
            "Verde",
            "Morado",
            "Naranja",
            "Amarillo"
        ]
    )

    tamaño = st.slider(
        "Tamaño de la figura:",
        min_value=1,
        max_value=8,
        value=4
    )

    colores = {
        "Azul": "blue",
        "Rojo": "red",
        "Verde": "green",
        "Morado": "purple",
        "Naranja": "orange",
        "Amarillo": "gold"
    }

    fig, ax = plt.subplots(figsize=(5, 5))

    if figura == "Cuadrado":

        forma = Rectangle(
            (5 - tamaño / 2, 5 - tamaño / 2),
            tamaño,
            tamaño,
            color=colores[color_nombre]
        )

    else:

        forma = Circle(
            (5, 5),
            tamaño / 2,
            color=colores[color_nombre]
        )

    ax.add_patch(forma)

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    ax.set_aspect("equal")
    ax.axis("off")

    st.pyplot(fig)

    st.success(
        f"Figura: {figura} | "
        f"Color: {color_nombre} | "
        f"Tamaño: {tamaño}"
    )

    st.divider()

    # -----------------------------------------------------
    # REFLEXIÓN
    # -----------------------------------------------------

    st.header("💡 Reflexiona")

    st.write("""
    ¿Cómo pueden los lenguajes de programación
    y la inteligencia artificial ayudar
    a crear proyectos digitales?
    """)

    reflexion = st.text_area(
        "Escribe tu reflexión:"
    )

    if st.button("Enviar reflexión"):

        if reflexion.strip():

            st.success(
                "¡Gracias por compartir tu reflexión!"
            )

        else:

            st.warning(
                "Escribe tu reflexión antes de enviarla."
            )

# =========================================================
# CÓDIGO QR
# =========================================================

elif seccion == "📱 Código QR":

    st.title("📱 Comparte WEB LAB")

    st.write("""
    Genera un código QR para que otras personas
    puedan ingresar a tu página web desde sus celulares.
    """)

    st.info("""
    Para que el QR funcione desde otros dispositivos,
    tu página debe estar publicada en Internet.
    """)

    enlace = st.text_input(
        "Introduce el enlace público de tu página:",
        placeholder="https://mi-proyecto.streamlit.app"
    )

    if st.button("Generar código QR"):

        if enlace.startswith("https://") or enlace.startswith("http://"):

            qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=4
            )

            qr.add_data(enlace)
            qr.make(fit=True)

            imagen = qr.make_image(
                fill_color="black",
                back_color="white"
            )

            buffer = BytesIO()

            imagen.save(buffer, format="PNG")

            imagen_bytes = buffer.getvalue()

            st.image(
                imagen_bytes,
                caption="Escanea el QR para ingresar a WEB LAB",
                width=300
            )

            st.success("¡Código QR creado correctamente!")

            st.download_button(
                label="⬇️ Descargar QR",
                data=imagen_bytes,
                file_name="WEB_LAB_QR.png",
                mime="image/png"
            )

            st.write("### Enlace de tu página")

            st.code(enlace)

        else:

            st.error(
                "Introduce un enlace válido que comience "
                "con http:// o https://"
            )

# =========================================================
# PIE DE PÁGINA
# =========================================================

st.divider()

st.caption(
    "💻 WEB LAB | Proyecto educativo sobre programación, "
    "desarrollo web e inteligencia artificial."
)
