import streamlit as st

st.set_page_config(page_title="Bitácora de Luna", page_icon="💖", layout="wide")

# ---------------------------------------------------------------
# Estilo Y2K / cyber pastel
# ---------------------------------------------------------------
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=VT323&family=Quicksand:wght@500;700&display=swap');

:root {
    --rosa: #FF8FC7;
    --rosa-claro: #FFD1EA;
    --rosa-hot: #FF4FA8;
    --lila: #D9C2FF;
    --cian: #B8F2FF;
    --plata: #F4F0FA;
    --texto: #6B2C57;
}

.stApp {
    background:
        radial-gradient(circle at 12% 18%, #ffffffcc 0 2px, transparent 3px),
        radial-gradient(circle at 78% 12%, #ffffffcc 0 2px, transparent 3px),
        radial-gradient(circle at 40% 70%, #ffffffaa 0 2px, transparent 3px),
        radial-gradient(circle at 90% 80%, #ffffffcc 0 2px, transparent 3px),
        radial-gradient(circle at 25% 92%, #ffffffaa 0 2px, transparent 3px),
        linear-gradient(135deg, #FFD9EE 0%, #FFC2E2 28%, #E3CCFF 62%, #C9F3FF 100%);
    background-size: 220px 220px, 260px 260px, 180px 180px, 300px 300px, 240px 240px, 100% 100%;
    font-family: 'Quicksand', sans-serif;
    color: var(--texto);
}

[data-testid="stHeader"] { background: transparent; }
.block-container { padding-top: 2rem; max-width: 1200px; }

/* estrellitas y corazones flotando */
.deco { position: fixed; inset: 0; pointer-events: none; z-index: 0; overflow: hidden; }
.deco span { position: absolute; animation: titilar 3s ease-in-out infinite; color: #fff; text-shadow: 0 0 8px #FF8FC7, 0 0 14px #fff; }
@keyframes titilar { 0%,100% { opacity: .25; transform: scale(.8) rotate(0deg);} 50% { opacity: 1; transform: scale(1.2) rotate(15deg);} }

/* cinta tipo marquee */
.cinta {
    background: linear-gradient(90deg, #FF8FC7, #D9C2FF, #B8F2FF, #FF8FC7);
    border: 2px solid #fff; border-radius: 999px;
    box-shadow: 0 0 14px #FF8FC7aa, inset 0 2px 4px #ffffffcc;
    overflow: hidden; white-space: nowrap; padding: .25rem 0; margin-bottom: 1rem;
}
.cinta div { display: inline-block; padding-left: 100%; animation: correr 22s linear infinite;
    font-family: 'VT323', monospace; font-size: 1.4rem; color: #fff; text-shadow: 0 0 6px #FF4FA8; }
@keyframes correr { to { transform: translateX(-100%); } }

/* titulo cromado */
.titulo {
    font-family: 'Orbitron', sans-serif; font-weight: 900; text-align: center;
    font-size: clamp(2rem, 6vw, 4rem); letter-spacing: 3px; margin: .3rem 0 0 0;
    background: linear-gradient(180deg, #ffffff 0%, #FFB3DD 40%, #FF4FA8 55%, #FFD1EA 100%);
    -webkit-background-clip: text; background-clip: text; color: transparent;
    -webkit-text-stroke: 1.5px #fff;
    filter: drop-shadow(0 0 10px #FF8FC7) drop-shadow(3px 3px 0 #D9C2FF);
}
.subtitulo { text-align: center; font-family: 'VT323', monospace; font-size: 1.5rem; color: #B03C86; letter-spacing: 2px; }
.separador { text-align: center; font-size: 1.4rem; letter-spacing: 8px; color: #fff; text-shadow: 0 0 8px #FF4FA8; margin: .6rem 0 1rem 0; }

/* ventanas estilo Y2K */
.ventana {
    background: #ffffffd9; border: 2px solid #fff; border-radius: 18px; overflow: hidden;
    box-shadow: 0 0 0 2px #FF8FC7, 0 10px 24px #FF4FA855, 0 0 22px #D9C2FF;
    margin-bottom: .4rem; position: relative; z-index: 1;
    transition: transform .2s ease, box-shadow .2s ease;
}
.ventana:hover { transform: translateY(-5px) scale(1.01); box-shadow: 0 0 0 2px #FF4FA8, 0 14px 30px #FF4FA888, 0 0 30px #B8F2FF; }
.barra {
    display: flex; align-items: center; justify-content: space-between; padding: .35rem .7rem;
    background: linear-gradient(90deg, #FF8FC7 0%, #D9C2FF 60%, #B8F2FF 100%);
    border-bottom: 2px solid #fff; font-family: 'Orbitron', sans-serif; font-size: .72rem; color: #fff;
    text-shadow: 0 0 5px #FF4FA8; letter-spacing: 1px;
}
.barra .puntos span { display: inline-block; width: 12px; height: 12px; border-radius: 50%; margin-left: 4px;
    background: radial-gradient(circle at 30% 30%, #fff, #FF8FC7); border: 1px solid #fff; }
.cuerpo { padding: 1rem 1.1rem 1.2rem 1.1rem; }
.icono { font-size: 2.6rem; text-align: center; filter: drop-shadow(0 0 8px #FF8FC7); }
.cuerpo h3 { font-family: 'Orbitron', sans-serif; font-size: 1.02rem; margin: .2rem 0 .5rem 0; color: var(--texto); text-align: center; }
.cuerpo p { font-size: .95rem; line-height: 1.55; margin-bottom: .9rem; text-align: center; }

.btn-wrap { text-align: center; }
.btn {
    display: inline-block; text-decoration: none !important; color: #fff !important; font-family: 'Orbitron', sans-serif;
    font-weight: 700; font-size: .8rem; letter-spacing: 1px; padding: .5rem 1.3rem; border-radius: 999px;
    background: linear-gradient(180deg, #FFC2E6 0%, #FF4FA8 50%, #FF8FC7 51%, #FFB3DD 100%);
    border: 2px solid #fff; box-shadow: 0 0 12px #FF4FA8aa, inset 0 2px 3px #ffffffcc;
    text-shadow: 0 1px 2px #B03C86;
}
.btn:hover { filter: brightness(1.1); box-shadow: 0 0 18px #FF4FA8, inset 0 2px 3px #fff; }

.destacada { grid-column: 1 / -1; }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 1.2rem; position: relative; z-index: 1; }

.intro {
    background: #ffffffcc; border: 2px solid #fff; border-radius: 22px; padding: 1.2rem 1.6rem; margin: 1rem 0 1.4rem 0;
    box-shadow: 0 0 0 2px #D9C2FF, 0 0 24px #FF8FC799; line-height: 1.7; position: relative; z-index: 1;
}
.intro b { color: #FF4FA8; }

[data-testid="stSidebar"] { background: linear-gradient(180deg, #FFC2E2 0%, #E3CCFF 60%, #C9F3FF 100%); border-right: 2px solid #fff; }
[data-testid="stSidebar"] * { color: var(--texto) !important; }
.side-deco { text-align: center; font-size: 2rem; letter-spacing: 6px; text-shadow: 0 0 8px #fff; }
.pie { text-align: center; font-family: 'VT323', monospace; font-size: 1.5rem; color: #B03C86; margin: 1.5rem 0 .5rem 0; position: relative; z-index: 1; }
</style>
"""

DECO = (
    '<div class="deco">'
    '<span style="top:6%;left:5%;font-size:1.8rem;animation-delay:0s">★</span>'
    '<span style="top:14%;left:92%;font-size:1.4rem;animation-delay:.6s">♥</span>'
    '<span style="top:30%;left:3%;font-size:1.2rem;animation-delay:1.2s">✦</span>'
    '<span style="top:46%;left:95%;font-size:2rem;animation-delay:.3s">★</span>'
    '<span style="top:62%;left:6%;font-size:1.5rem;animation-delay:1.8s">♥</span>'
    '<span style="top:78%;left:90%;font-size:1.3rem;animation-delay:.9s">✧</span>'
    '<span style="top:90%;left:12%;font-size:1.9rem;animation-delay:1.5s">★</span>'
    '<span style="top:8%;left:48%;font-size:1.1rem;animation-delay:2.1s">✦</span>'
    '<span style="top:88%;left:70%;font-size:1.6rem;animation-delay:.4s">♥</span>'
    '</div>'
)

st.markdown(CSS + DECO, unsafe_allow_html=True)

# ---------------------------------------------------------------
# Barra lateral
# ---------------------------------------------------------------
with st.sidebar:
    st.markdown("<div class='side-deco'>♥ ★ ♥</div>", unsafe_allow_html=True)
    st.subheader("Aplicaciones con Inteligencia Artificial")
    st.write(
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de "
        "datos, automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo "
        "real, lo que resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.markdown("<div class='side-deco'>✦ ♡ ✧</div>", unsafe_allow_html=True)
    st.caption("sistema luna.exe cargado con éxito ♥")

# ---------------------------------------------------------------
# Encabezado (sin sangría para que Markdown no lo trate como código)
# ---------------------------------------------------------------
ENCABEZADO = (
    '<div class="cinta"><div>★ BIENVENIDA A LA BITÁCORA DE LUNA ★ ♥ SISTEMA ONLINE ♥ '
    '✦ 10 PORTALES DISPONIBLES ✦ ★ NAVEGA CON CUIDADO, HAY MUCHO BRILLO ★ ♥</div></div>'
    '<h1 class="titulo">BITÁCORA DE LUNA</h1>'
    '<div class="subtitulo">&gt;&gt; diario cyber de una exploradora de IA &lt;&lt;</div>'
    '<div class="separador">♥ ★ ♥ ★ ♥ ★ ♥</div>'
    '<div class="intro">♥ <b>Registro 000, transmisión desde la Luna:</b> mientras el mundo '
    'duerme, enciendo mi computadora rosada y entro a una red secreta donde las máquinas '
    'leen imágenes, escuchan audios, descubren emociones en los textos y dibujan nubes con '
    'las palabras más repetidas. En esta bitácora guardé los portales que más me gustaron. '
    'Cada ventana brillante es un acceso directo a un experimento distinto. Haz clic, '
    'explora y, si encuentras algo increíble, anótalo en tu propio diario ★</div>'
)
st.markdown(ENCABEZADO, unsafe_allow_html=True)

# ---------------------------------------------------------------
# Portales
# ---------------------------------------------------------------
APPS = [
    {
        "destacada": True,
        "icono": "💖",
        "titulo": "Intro",
        "archivo": "intro.exe",
        "intro": "La puerta de entrada a la bitácora. Aquí empieza todo: una primera mirada "
                 "al mundo de las aplicaciones de inteligencia artificial que Luna fue "
                 "coleccionando. Si es tu primera visita, comienza por este portal.",
        "url": "https://xhavuua73kp7cddvz9vn4i.streamlit.app",
        "boton": "ENTRAR",
    },
    {
        "icono": "🔊",
        "titulo": "Text to Speech",
        "archivo": "text_to_speech.exe",
        "intro": "Escribo una frase y una voz digital la pronuncia con estilo. "
                 "Mis mensajes secretos ahora se pueden escuchar.",
        "url": "https://nyxocljendujfzyqz7krmt.streamlit.app",
        "boton": "ESCUCHAR",
    },
    {
        "icono": "🎀",
        "titulo": "Texto a voz",
        "archivo": "texto_a_voz.exe",
        "intro": "La versión en español de mi estudio de grabación. "
                 "Escribe en tu idioma y deja que la IA te lea en voz alta.",
        "url": "https://nyxocljendujfzyqz7krmt.streamlit.app",
        "boton": "HABLAR",
    },
    {
        "icono": "🔍",
        "titulo": "OCR 1",
        "archivo": "ocr_1.exe",
        "intro": "Mi escáner mágico: le muestro una imagen con letras y la IA las "
                 "reconoce y las convierte en texto que puedo copiar.",
        "url": "https://pw8rf7frlc7ghrfhcckq4b.streamlit.app",
        "boton": "ESCANEAR",
    },
    {
        "icono": "🎧",
        "titulo": "OCR Audio",
        "archivo": "ocr_audio.exe",
        "intro": "Combina lectura y sonido: extrae el texto de una imagen y luego "
                 "lo transforma en audio. Es como una lectora de bolsillo.",
        "url": "https://ocr-audio-mqs4vjg3fsycboxxf7yz4g.streamlit.app",
        "boton": "LEER Y ESCUCHAR",
    },
    {
        "icono": "☁️",
        "titulo": "WordCloud",
        "archivo": "wordcloud.exe",
        "intro": "Un texto se convierte en una nube de palabras. Las más repetidas "
                 "brillan más grandes, como estrellas en el cielo.",
        "url": "https://wordcloud-gxbqwhi2czajvvcap3eieg.streamlit.app",
        "boton": "CREAR NUBE",
    },
    {
        "icono": "💗",
        "titulo": "Análisis de sentimiento",
        "archivo": "sentimiento.exe",
        "intro": "Un detector de emociones para textos. Le paso una frase y me dice "
                 "si suena feliz, triste o neutral. Un termómetro del corazón.",
        "url": "https://sentimenta-6c2tf2myjwrxelx9jia4qv.streamlit.app",
        "boton": "SENTIR",
    },
    {
        "icono": "📈",
        "titulo": "TF-IDF",
        "archivo": "tfidf.exe",
        "intro": "Mide qué palabras son realmente importantes en un documento, "
                 "no solo las más repetidas. Matemática con glitter.",
        "url": "https://tdfesp-ogty4wdviudez6v86227fy.streamlit.app",
        "boton": "ANALIZAR",
    },
    {
        "icono": "👁️",
        "titulo": "YOLO",
        "archivo": "yolo.exe",
        "intro": "Visión por computadora en tiempo récord: detecta y señala los "
                 "objetos que aparecen en una imagen, cada uno con su cajita rosa.",
        "url": "https://yolov5-b4hucs4d7ifakwqzncnswo.streamlit.app",
        "boton": "DETECTAR",
    },
    {
        "icono": "🧠",
        "titulo": "Teachable Machine",
        "archivo": "tm.exe",
        "intro": "Aquí uso mi propio modelo entrenado: lo apunto a la cámara y "
                 "reconoce lo que le enseñé. Una IA hecha a mi medida.",
        "url": "https://eyujbc4vujdsq8nu5uewvy.streamlit.app",
        "boton": "PROBAR MODELO",
    },
]


def tarjeta(app):
    clase = "ventana destacada" if app.get("destacada") else "ventana"
    return (
        f'<div class="{clase}">'
        f'<div class="barra"><span>♥ {app["archivo"]}</span>'
        f'<span class="puntos"><span></span><span></span><span></span></span></div>'
        f'<div class="cuerpo">'
        f'<div class="icono">{app["icono"]}</div>'
        f'<h3>{app["titulo"]}</h3>'
        f'<p>{app["intro"]}</p>'
        f'<div class="btn-wrap"><a class="btn" href="{app["url"]}" target="_blank" '
        f'rel="noopener noreferrer">★ {app["boton"]} ★</a></div>'
        f'</div></div>'
    )


st.markdown(
    '<div class="grid">' + "".join(tarjeta(a) for a in APPS) + "</div>",
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='separador'>♥ ★ ♥ ★ ♥ ★ ♥</div>"
    "<div class='pie'>fin de la transmisión ✦ nos vemos en el próximo registro ✦ luna.exe ♥</div>",
    unsafe_allow_html=True,
)
