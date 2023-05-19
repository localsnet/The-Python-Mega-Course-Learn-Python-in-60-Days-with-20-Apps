import streamlit as st
from PIL import Image
from converter import convert_image

st.title("Color to Grayscale converter")

uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    #Start Camera
    camera_image = st.camera_input("Camera")
album = []
if camera_image:
    album.append(camera_image)
if  uploaded_image:
    album.append(uploaded_image)

for photo in album:
    gray_camera_image = convert_image(photo)
    st.image(gray_camera_image)