import streamlit as st

st.set_page_config(page_title="Bitácora de Luna", page_icon="💖", layout="wide")

# ---------------------------------------------------------------
# Estilo Y2K sticker: letras gordas con contorno, halftone, destellos
# ---------------------------------------------------------------
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bagel+Fat+One&family=Racing+Sans+One&family=Chakra+Petch:wght@500;600;700&family=Space+Mono:wght@400;700&display=swap');

:root {
    --rosa: #FF8FC7;
    --rosa-claro: #FFD1EA;
    --rosa-hot: #FF4FA8;
    --lila: #D9C2FF;
    --cian: #B8F2FF;
    --azul: #5B7BE0;
    --tinta: #26286E;
    --texto: #2E2468;
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
    font-family: 'Chakra Petch', sans-serif;
    font-weight: 500;
    color: var(--texto);
}

[data-testid="stHeader"] { background: transparent; }
.block-container { padding-top: 2rem; max-width: 1200px; }

/* destellos flotando */
.deco { position: fixed; inset: 0; pointer-events: none; z-index: 0; overflow: hidden; }
.deco span { position: absolute; animation: titilar 3s ease-in-out infinite; color: #fff; -webkit-text-stroke: 1.5px var(--tinta); }
@keyframes titilar { 0%,100% { opacity: .4; transform: scale(.8) rotate(0deg);} 50% { opacity: 1; transform: scale(1.25) rotate(20deg);} }

/* cinta */
.cinta {
    background: var(--tinta); border: 3px solid #fff; border-radius: 999px;
    box-shadow: 0 0 0 3px var(--tinta), 6px 7px 0 3px var(--rosa-hot);
    overflow: hidden; white-space: nowrap; padding: .3rem 0; margin: 0 .4rem 1.6rem .4rem;
    transform: rotate(-1deg); position: relative; z-index: 1;
}
.cinta div { display: inline-block; padding-left: 100%; animation: correr 24s linear infinite;
    font-family: 'Space Mono', monospace; font-weight: 700; font-size: .95rem; letter-spacing: 3px;
    text-transform: uppercase; color: var(--cian); }
@keyframes correr { to { transform: translateX(-100%); } }

/* logo estilo sticker */
.logo { text-align: center; margin: .2rem 0 .6rem 0; position: relative; z-index: 1; }
.logo .tag {
    display: inline-block; background: var(--tinta); color: #fff; font-family: 'Space Mono', monospace; font-weight: 700;
    font-size: .75rem; letter-spacing: 3px; padding: .25rem 1rem; border-radius: 999px; text-transform: uppercase;
    transform: rotate(-3deg); box-shadow: 3px 3px 0 var(--rosa-hot); margin-bottom: .8rem;
}
.titulo {
    font-family: 'Bagel Fat One', 'Racing Sans One', sans-serif; font-weight: 400; margin: 0; line-height: .95;
    font-size: clamp(2.6rem, 9vw, 5.6rem); letter-spacing: 2px; color: var(--rosa);
    -webkit-text-stroke: 10px var(--tinta); paint-order: stroke fill;
    filter: drop-shadow(3px 0 0 #fff) drop-shadow(-3px 0 0 #fff) drop-shadow(0 3px 0 #fff) drop-shadow(0 -3px 0 #fff) drop-shadow(6px 8px 0 var(--tinta));
    transform: skew(-8deg) rotate(-2deg); animation: flota 3.5s ease-in-out infinite;
}
.titulo .l2 { display: block; font-size: .62em; color: var(--cian); margin-top: .12em; }
@keyframes flota {
    0%,100% { transform: skew(-8deg) rotate(-2deg) translateY(0); }
    50% { transform: skew(-8deg) rotate(-2deg) translateY(-7px); }
}
.kanji {
    font-family: 'Racing Sans One', sans-serif; font-size: 1.5rem; letter-spacing: 8px; margin-top: 1rem; color: #fff;
    -webkit-text-stroke: 6px var(--tinta); paint-order: stroke fill; filter: drop-shadow(3px 3px 0 var(--rosa-hot));
}
.separador { text-align: center; font-size: 1.3rem; letter-spacing: 10px; color: #fff; -webkit-text-stroke: 1.5px var(--tinta); margin: .8rem 0 1.2rem 0; position: relative; z-index: 1; }

/* intro tipo sticker */
.intro {
    background: #fff; border: 4px solid var(--tinta); border-radius: 30px 10px 30px 10px; padding: 1.3rem 1.7rem; margin: 1rem 0 2rem 0;
    box-shadow: 0 0 0 4px var(--cian), 8px 9px 0 4px var(--tinta); line-height: 1.7; position: relative; z-index: 1;
}
.intro b { color: var(--rosa-hot); font-family: 'Space Mono', monospace; text-transform: uppercase; letter-spacing: 1px; }

/* tarjetas sticker */
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 2rem 1.8rem; position: relative; z-index: 1; padding: .4rem; }
.ventana {
    --fondo: #FFE0F0; --punto: var(--rosa-hot); --boton: var(--rosa-hot);
    position: relative; overflow: hidden; background: var(--fondo);
    border: 4px solid var(--tinta); border-radius: 30px 10px 30px 10px;
    box-shadow: 0 0 0 4px #fff, 8px 9px 0 4px var(--tinta);
    transform: rotate(-1deg); transition: transform .18s ease, box-shadow .18s ease;
}
.ventana:nth-child(even) { transform: rotate(1deg); border-radius: 10px 30px 10px 30px; }
.ventana:nth-child(3n+2) { --fondo: #EADCFF; --punto: var(--azul); --boton: var(--azul); }
.ventana:nth-child(3n+3) { --fondo: #D6F7FF; --punto: #35B8D8; --boton: #35B8D8; }
.ventana:hover { transform: rotate(0deg) translateY(-6px); box-shadow: 0 0 0 4px #fff, 12px 14px 0 4px var(--tinta); }
/* trama halftone */
.ventana::before {
    content: ""; position: absolute; top: 0; right: 0; width: 70%; height: 65%; pointer-events: none;
    background-image: radial-gradient(var(--punto) 26%, transparent 28%); background-size: 9px 9px; opacity: .5;
    -webkit-mask-image: radial-gradient(circle at 100% 0%, #000 0%, transparent 72%);
    mask-image: radial-gradient(circle at 100% 0%, #000 0%, transparent 72%);
}
/* destello */
.ventana::after {
    content: "✦"; position: absolute; bottom: 6px; right: 14px; font-size: 2.2rem; color: #fff; pointer-events: none;
    -webkit-text-stroke: 1.5px var(--tinta);
}
.cuerpo { position: relative; z-index: 1; padding: 1rem 1.2rem 1.4rem 1.2rem; }
.cabecera { display: flex; align-items: center; justify-content: space-between; margin-bottom: .3rem; }
.pill { background: var(--tinta); color: #fff; font-family: 'Space Mono', monospace; font-weight: 700; font-size: .7rem;
    letter-spacing: 2px; padding: .2rem .75rem; border-radius: 999px; text-transform: uppercase; }
.mini { color: var(--tinta); letter-spacing: 4px; font-size: .9rem; }
.icono { font-size: 2.7rem; text-align: center; margin: .2rem 0 .1rem 0;
    filter: drop-shadow(2px 0 0 #fff) drop-shadow(-2px 0 0 #fff) drop-shadow(0 2px 0 #fff) drop-shadow(0 -2px 0 #fff) drop-shadow(3px 4px 0 var(--tinta)); }
.cuerpo h3 {
    font-family: 'Racing Sans One', 'Chakra Petch', sans-serif; font-weight: 400; font-size: 1.45rem; letter-spacing: 1px;
    text-transform: uppercase; text-align: center; margin: .3rem 0 .7rem 0; color: #fff;
    -webkit-text-stroke: 7px var(--tinta); paint-order: stroke fill; transform: skew(-8deg);
    filter: drop-shadow(3px 3px 0 var(--rosa-hot));
}
.cuerpo p { font-size: .95rem; line-height: 1.55; margin-bottom: 1.1rem; text-align: center; font-weight: 600; }

.btn-wrap { text-align: center; }
.btn {
    display: inline-block; text-decoration: none !important; color: #fff !important; font-family: 'Racing Sans One', sans-serif;
    font-size: 1.05rem; letter-spacing: 2px; text-transform: uppercase; padding: .5rem 1.6rem; background: var(--boton);
    border: 3px solid var(--tinta); border-radius: 999px; box-shadow: 0 0 0 3px #fff, 5px 6px 0 3px var(--tinta);
    text-shadow: 2px 2px 0 var(--tinta); transform: skew(-6deg); transition: transform .1s ease, box-shadow .1s ease;
}
.btn:hover { transform: skew(-6deg) translate(2px, 3px); box-shadow: 0 0 0 3px #fff, 2px 3px 0 3px var(--tinta); }

.destacada { grid-column: 1 / -1; }

[data-testid="stSidebar"] { background: linear-gradient(180deg, #FFC2E2 0%, #E3CCFF 60%, #C9F3FF 100%); border-right: 4px solid var(--tinta); }
[data-testid="stSidebar"] * { color: var(--texto) !important; font-family: 'Chakra Petch', sans-serif; font-weight: 600; }
[data-testid="stSidebar"] h3 { font-family: 'Racing Sans One', sans-serif !important; font-weight: 400 !important; font-size: 1.4rem !important; text-transform: uppercase; }
.side-deco { text-align: center; font-size: 2rem; letter-spacing: 6px; color: #fff !important; -webkit-text-stroke: 1.5px var(--tinta); }
.pie { text-align: center; font-family: 'Racing Sans One', sans-serif; font-size: 1.3rem; letter-spacing: 3px; text-transform: uppercase;
    color: var(--tinta); margin: 1.5rem 0 .5rem 0; position: relative; z-index: 1; }
</style>
"""

DECO = (
    '<div class="deco">'
    '<span style="top:6%;left:5%;font-size:2rem;animation-delay:0s">✦</span>'
    '<span style="top:14%;left:92%;font-size:1.6rem;animation-delay:.6s">♥</span>'
    '<span style="top:30%;left:3%;font-size:1.4rem;animation-delay:1.2s">★</span>'
    '<span style="top:46%;left:95%;font-size:2.2rem;animation-delay:.3s">✦</span>'
    '<span style="top:62%;left:6%;font-size:1.7rem;animation-delay:1.8s">♥</span>'
    '<span style="top:78%;left:90%;font-size:1.5rem;animation-delay:.9s">★</span>'
    '<span style="top:90%;left:12%;font-size:2.1rem;animation-delay:1.5s">✦</span>'
    '<span style="top:8%;left:48%;font-size:1.2rem;animation-delay:2.1s">♥</span>'
    '<span style="top:88%;left:70%;font-size:1.8rem;animation-delay:.4s">✦</span>'
    '</div>'
)

st.markdown(CSS + DECO, unsafe_allow_html=True)

# ---------------------------------------------------------------
# Barra lateral
# ---------------------------------------------------------------
with st.sidebar:
    st.markdown("<div class='side-deco'>♥ ✦ ♥</div>", unsafe_allow_html=True)
    st.subheader("Aplicaciones con Inteligencia Artificial")
    st.write(
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de "
        "datos, automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo "
        "real, lo que resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.markdown("<div class='side-deco'>✦ ★ ✦</div>", unsafe_allow_html=True)
    st.caption("luna 2000 · cargado con éxito ♥")

# ---------------------------------------------------------------
# Encabezado (sin sangría para que Markdown no lo trate como código)
# ---------------------------------------------------------------
ENCABEZADO = (
    '<div class="cinta"><div>★ Radio Luna 94.9 FM ★ ♥ Bitácora online ♥ ✦ 10 portales ✦ '
    '月 ★ Y2K forever ★ ♥ Navega con cuidado, hay mucho brillo ✦</div></div>'
    '<div class="logo">'
    '<span class="tag">★ Radio Luna 94.9 FM ★</span>'
    '<h1 class="titulo">BITÁCORA<span class="l2">de Luna ★</span></h1>'
    '<div class="kanji">月 ルナ ♥ 2000 ✦</div>'
    '</div>'
    '<div class="separador">♥ ✦ ♥ ✦ ♥ ✦ ♥</div>'
    '<div class="intro">♥ <b>Registro 000, transmisión desde la Luna:</b> mientras el mundo '
    'duerme, enciendo mi computadora rosada y entro a una red secreta donde las máquinas '
    'leen imágenes, escuchan audios, descubren emociones en los textos y dibujan nubes con '
    'las palabras más repetidas. En esta bitácora guardé los portales que más me gustaron. '
    'Cada sticker brillante es un acceso directo a un experimento distinto. Haz clic, '
    'explora y, si encuentras algo increíble, anótalo en tu propio diario ✦</div>'
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
        "intro": "La puerta de entrada a la bitácora. Aquí empieza todo: una primera mirada "
                 "al mundo de las aplicaciones de inteligencia artificial que Luna fue "
                 "coleccionando. Si es tu primera visita, comienza por este portal.",
        "url": "https://xhavuua73kp7cddvz9vn4i.streamlit.app",
        "boton": "Entrar",
    },
    {
        "icono": "🔊",
        "titulo": "Text to Speech",
        "intro": "Escribo una frase y una voz digital la pronuncia con estilo. "
                 "Mis mensajes secretos ahora se pueden escuchar.",
        "url": "https://nyxocljendujfzyqz7krmt.streamlit.app",
        "boton": "Escuchar",
    },
    {
        "icono": "🎀",
        "titulo": "Texto a voz",
        "intro": "La versión en español de mi estudio de grabación. "
                 "Escribe en tu idioma y deja que la IA te lea en voz alta.",
        "url": "https://nyxocljendujfzyqz7krmt.streamlit.app",
        "boton": "Hablar",
    },
    {
        "icono": "🔍",
        "titulo": "OCR 1",
        "intro": "Mi escáner mágico: le muestro una imagen con letras y la IA las "
                 "reconoce y las convierte en texto que puedo copiar.",
        "url": "https://pw8rf7frlc7ghrfhcckq4b.streamlit.app",
        "boton": "Escanear",
    },
    {
        "icono": "🎧",
        "titulo": "OCR Audio",
        "intro": "Combina lectura y sonido: extrae el texto de una imagen y luego "
                 "lo transforma en audio. Es como una lectora de bolsillo.",
        "url": "https://ocr-audio-mqs4vjg3fsycboxxf7yz4g.streamlit.app",
        "boton": "Leer y escuchar",
    },
    {
        "icono": "☁️",
        "titulo": "WordCloud",
        "intro": "Un texto se convierte en una nube de palabras. Las más repetidas "
                 "brillan más grandes, como estrellas en el cielo.",
        "url": "https://wordcloud-gxbqwhi2czajvvcap3eieg.streamlit.app",
        "boton": "Crear nube",
    },
    {
        "icono": "💗",
        "titulo": "Análisis de sentimiento",
        "intro": "Un detector de emociones para textos. Le paso una frase y me dice "
                 "si suena feliz, triste o neutral. Un termómetro del corazón.",
        "url": "https://sentimenta-6c2tf2myjwrxelx9jia4qv.streamlit.app",
        "boton": "Sentir",
    },
    {
        "icono": "📈",
        "titulo": "TF-IDF",
        "intro": "Mide qué palabras son realmente importantes en un documento, "
                 "no solo las más repetidas. Matemática con glitter.",
        "url": "https://tdfesp-ogty4wdviudez6v86227fy.streamlit.app",
        "boton": "Analizar",
    },
    {
        "icono": "👁️",
        "titulo": "YOLO",
        "intro": "Visión por computadora en tiempo récord: detecta y señala los "
                 "objetos que aparecen en una imagen, cada uno con su cajita rosa.",
        "url": "https://yolov5-b4hucs4d7ifakwqzncnswo.streamlit.app",
        "boton": "Detectar",
    },
    {
        "icono": "🧠",
        "titulo": "Teachable Machine",
        "intro": "Aquí uso mi propio modelo entrenado: lo apunto a la cámara y "
                 "reconoce lo que le enseñé. Una IA hecha a mi medida.",
        "url": "https://eyujbc4vujdsq8nu5uewvy.streamlit.app",
        "boton": "Probar modelo",
    },
]


def tarjeta(num, app):
    clase = "ventana destacada" if app.get("destacada") else "ventana"
    return (
        f'<div class="{clase}"><div class="cuerpo">'
        f'<div class="cabecera"><span class="pill">Portal {num:02d}</span>'
        f'<span class="mini">♥ ★</span></div>'
        f'<div class="icono">{app["icono"]}</div>'
        f'<h3>{app["titulo"]}</h3>'
        f'<p>{app["intro"]}</p>'
        f'<div class="btn-wrap"><a class="btn" href="{app["url"]}" target="_blank" '
        f'rel="noopener noreferrer">★ {app["boton"]} ★</a></div>'
        f'</div></div>'
    )


st.markdown(
    '<div class="grid">' + "".join(tarjeta(i, a) for i, a in enumerate(APPS, start=1)) + "</div>",
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='separador'>♥ ✦ ♥ ✦ ♥ ✦ ♥</div>"
    "<div class='pie'>fin de la transmisión ✦ 月 ✦ luna 2000 ♥</div>",
    unsafe_allow_html=True,
)
