import streamlit as st
from FilterFunctions import convert_image

st.subheader("Colour to Grayscale Converter")

uploaded_img = st.file_uploader("Upload Image")

# Starting camera from expander
with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    grey_camera_image = convert_image(camera_image)
    st.image(grey_camera_image)
if uploaded_img:
    grey_uploaded_image = convert_image(uploaded_img)
    st.image(grey_uploaded_image)
