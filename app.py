import streamlit as st
from PIL import Image 

st.title ("snoppy")

st.header ("En este espacio comienzso a desarrolar mis apps ")
st.write ("facilmente puedo realizar backend y frontemd")
image = Image.open ("imagenmultimodales.jpg")

st.image (image,caption= "interfaces multimodales")
