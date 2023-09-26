import os
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Urine Dipstick Scoring App", ["Home", 'Urine Dipstick Scoring App', 'Next Steps'], 
        icons=['house-door-fill', 'hospital-fill', 'emoji-smile-fill'], menu_icon="cast", default_index=1)
    selected
    
st.write("Upload an image from your device or use the device camera to take an image")
option = st.radio("", ("Upload an image", "Use device camera"))

image = None
if option == "Upload an image":
    device_file = st.file_uploader("", type=["jpg", "png", "jpeg"])
    if device_file is not None:
        image = Image.open(device_file)
        st.image(image, use_column_width=True)
else:
    device_capture = st.camera_input("Take a picture of the dipstick")
    if device_capture is not None:
        image = Image.open(device_capture)
        st.image(image)