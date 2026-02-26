import streamlit as st
from PIl import image 

st.title ("snoppy")

st.header ("En este espacio comienzso a desarrolar mis apps ")
st.write ("facilmente puedo realizar backend y frontemd")
image = image.open ("imagenmultimodales.jpg")

st.image (image,caption= "interfaces multimodales")
