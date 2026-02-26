import streamlit as st
from PIL import Image 

st.title ("snoppy")

st.header ("En este espacio comienzso a desarrolar mis apps ")
st.write ("facilmente puedo realizar backend y frontemd")
image = Image.open ("imagenmultimodales.jpg")

st.image (image,caption= "interfaces multimodales")


texto = st.text_imput ("Escribir algo" , "Este es mi texto")
st.write ("El texto escrito es ",texto)

st.subheader ("ahora usamos dos columnas")

col1,col2 =st.columnas(2)

with col1:
    st.subheader("Esta es la primera columna")
    st.write ("las interfaces multimodales mejoran la experiencia de usuario ")
    resp= st.checkbox ("estoy de acuerdo")
    if resp:
      st.write("correcto")

with col2:
    st.subheader("Esta es la segunda columna")
    modo= st.radio ("que modalidad", ("visual","auditiva", "tactil"))
    if modo == "visual":
        st.write ("la vista es fundamental para la interfaz")
    if modo == "auditiva ":
        st.write ("la audicion es fundamental ")
    if modo== "tactil":
        st.write ("lo tactil es importante ")

st.subheader ("uso botones ")
if st.button ("presiona el boton"):
    st.write ("gracias por presionar")
else:
      st.write ("no has presinado aun")
