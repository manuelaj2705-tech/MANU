import streamlit as st
from PIL import Image 

st.title("snoppy")

st.header("En este espacio comienzo a desarrollar mis apps")
st.write("Fácilmente puedo realizar backend y frontend")

image = Image.open("imagenmultimodales.jpg")
st.image(image, caption="interfaces multimodales")

texto = st.text_input("Escribir algo", "Este es mi texto")
st.write("El texto escrito es", texto)

st.subheader("Ahora usamos dos columnas")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Esta es la primera columna")
    st.write("Las interfaces multimodales mejoran la experiencia de usuario")
    resp = st.checkbox("Estoy de acuerdo")
    if resp:
        st.write("Correcto")

with col2:
    st.subheader("Esta es la segunda columna")
    modo = st.radio("Qué modalidad", ("visual", "auditiva", "tactil"))
    if modo == "visual":
        st.write("La vista es fundamental para la interfaz")
    if modo == "auditiva":
        st.write("La audición es fundamental")
    if modo == "tactil":
        st.write("Lo táctil es importante")

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
