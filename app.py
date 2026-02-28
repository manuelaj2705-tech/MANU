import streamlit as st
from PIL import Image 

st.title("Snoppy")

st.header("¿Quien es Snoppy?")
st.write("Snoopy es un famoso perro de raza Beagle, protagonista junto a Charlie Brown de la icónica tira cómica Peanuts")

image = Image.open("imagenmultimodales.jpg")
st.image(image, caption="Snoppy Sentado")

texto = st.text_input("¿Quieres decirle algo a Snoppy?", "Escribe algo para Snoppy ")
st.write("El texto escrito es para Snoppy")

st.subheader("RESPONDE ESTAS PREGUNTAS")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Esta es la primera columna")
    st.write("Snoopy actúa más como humano que como perro")

    acuerdo = st.checkbox("Estoy de acuerdo")
    desacuerdo = st.checkbox("No estoy de acuerdo")

    if acuerdo:
        st.write("Correcto")

with col2:
    st.subheader("Esta es la segunda columna")

    modo = st.radio(
        "¿En qué medio aparece Snoopy originalmente?",
        ("Tira cómica", "Película", "Videojuego")
    )

    if modo == "Tira cómica":
        st.write("Correcto ✅ 
        Snoopy apareció originalmente en la tira cómica Peanuts")
 
    if modo == "Película":
        st.write("❌ Incorrecto. Las películas llegaron después")

    if modo == "Videojuego":
        st.write("❌ Incorrecto. No fue su primer medio")

st.subheader("Uso botones")
if st.button("Presiona el botón"):
    st.write("Gracias por presionar")
else:
    st.write("No has presionado aún")

st.subheader("selectbox")
in_mod = st.selectbox(
    "selecciona la modalidad",
    ("audio", "visual", "haptico"),
)

if in_mod == "audio":
    set_mod = "reproducir audio"
elif in_mod == "visual":
    set_mod = "reproducir video"
elif in_mod == "haptico":
    set_mod = "Activar vibracion"

st.write("la accion es:", set_mod)
