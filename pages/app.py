import os
import streamlit as st ## Importing stream lit
from PIL import Image ## Importing image holder function
from streamlit_option_menu import option_menu ## Importing option menu, to allow toggling between pages
# from camera_input_live import camera_input_live ## Importing camera input function



## Creating a side bar for the user
with st.sidebar:
    selected = option_menu("Kidney Stone Prediction App", ["Home", 'Kidney Stone Predictor', 'Next Steps'], 
        icons=['house-door-fill', 'hospital-fill', 'emoji-smile-fill'], menu_icon="cast", default_index=1)
    selected
    
st.write("Upload an image from your device Or use the device camera to take an image from your device")
## Make it such that if the user clicks the upload button, the image is uploaded

device_file = st.file_uploader("", type=["jpg", "png", "jpeg"])
if device_file is not None:
    image = Image.open(device_file)
    st.image(image, use_column_width=True)


device_capture = st.camera_input("一二三,茄子!")
if device_capture is not None:
    image = Image.open(device_capture)
st.image(image)

