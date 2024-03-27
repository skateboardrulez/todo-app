import streamlit as st
from PIL import Image

with st.expander("Start camera"):
    # start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # create a pillow image instance
    img = Image.open(camera_image)

    # convert the pillow image in greyscale
    grey_img = img.convert("L")

    # render the greyscale image on the webpage
    st.image(grey_img)
