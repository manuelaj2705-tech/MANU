import streamlit as st
from PIL import Image 

st.markdown(
    """
    <h1 style='
        font-size:90px;
        text-align:center;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.6);
    '>
        Snoopy
    </h1>
    """,
    unsafe_allow_html=True
)

st.header("¿Quien es Snoppy?")
st.write("Snoopy es un personaje icónico de la tira cómica Peanuts. Aunque es un perro, se comporta como un humano: sueña, imagina historias y vive en su propio mundo creativo. Es conocido por su personalidad divertida, reflexiva y soñadora, lo que lo convierte en un símbolo de la imaginación y la expresión emocional.")

image = Image.open("imagenmultimodales.jpg")
st.image(image, caption="Snoppy Sentado")

texto = st.text_input("¿Quieres decirle algo a Snoppy?", "Escribe algo para Snoppy ")
st.write("El texto escrito es para Snoppy")

st.markdown("### 🔥 **RESPONDE ESTAS PREGUNTAS** 🔥")


col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.subheader("Esta es la primera columna")
    st.write("Snoopy actúa más como humano que como perro")

    acuerdo = st.checkbox("Estoy de acuerdo")
    desacuerdo = st.checkbox("No estoy de acuerdo")

    if acuerdo:
        st.write("Correcto ✅")

with col2:
    st.markdown(
        "<div style='padding-left:50px'>",
        unsafe_allow_html=True
    )

    st.subheader("Esta es la segunda columna")

    modo = st.radio(
        "¿En qué medio aparece Snoopy originalmente?",
        ("Tira cómica", "Película", "Videojuego")
    )

    if modo == "Tira cómica":
        st.write("✅ Correcto. Snoopy apareció originalmente en la tira cómica Peanuts")
    elif modo == "Película":
        st.write("❌ Incorrecto. Las películas llegaron después")
    else:
        st.write("❌ Incorrecto. No fue su primer medio")

    st.markdown("</div>", unsafe_allow_html=True)

st.subheader("Te gusta Snoopy")
if st.button("Presiona el botón si te gusta "):
    st.write("Eres fan #1 de Snoppy ✅ ")
else:
    st.write("No te gusta Snoppy 💔")

st.subheader("Elige una opción")
in_mod = st.selectbox(
    "¿Cómo está Snoopy hoy?",
    ("Feliz 😊", "Soñador ☁️", "Relajado 😌", "Pensativo 🤔"),
)


if in_mod == "Feliz 😊":
    set_mod = "😊 La vida es mejor cuando la bailas, aunque no haya música💃"
elif in_mod == "Soñador ☁️":
    set_mod = "  st.image(
        "https://esp.phoneky.com/wallpapers/?id=w47w2910541",
        use_container_width=True"
elif in_mod == "Relajado 😌":
    set_mod = "Reproducir música suave 🎧"
else:
 set_mod = """❤️ A veces creemos que la felicidad es algo enorme, complicado o lejano.
Pero Snoopy nos recuerda que puede estar en una tarde tranquila,
en una risa sin razón o en permitirnos descansar sin culpa.
No todo tiene que tener sentido hoy.
A veces, simplemente estar… ya es suficiente.❤️"""

st.write( set_mod)
