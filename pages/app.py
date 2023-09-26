import os
import streamlit as st ## Importing stream lit
from PIL import Image, ImpageOps ## Importing image holder function
from streamlit_option_menu import option_menu ## Importing option menu, to allow toggling between pages
from camera_input_live import camera_input_live ## Importing camera input function

## Creating a side bar for the user
with st.sidebar:
    selected = option_menu("Kidney Stone Prediction App", ["Home", 'Kidney Stone Predictor', 'Next Steps'], 
        icons=['house-door-fill', 'hospital-fill', 'emoji-smile-fill'], menu_icon="cast", default_index=1)
    selected
    
st.write("Upload an image from your device")
# # image = Image.open('pneumonia inception v3.jpeg')
# # st.image(image, caption='Placeholder image',use_column_width=True)
file = st.file_uploader("", type=["jpg", "png", "jpeg"])


image = camera_input_live()
st.image(image)

