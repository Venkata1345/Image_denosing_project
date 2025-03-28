
%%writefile app.py
import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from PIL import Image

# Load the trained U-Net model
model = load_model("unet_denoiser.h5")

st.title("🧼 Image Denoising with U-Net Autoencoder")

uploaded_file = st.file_uploader("Upload a noisy image (grayscale or RGB)", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Read and preprocess
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image.resize((128, 128))) / 255.0
    input_img = np.expand_dims(image_np, axis=0)

    # Predict
    denoised = model.predict(input_img)[0]

    # Display side-by-side
    st.subheader("Comparison")
    col1, col2 = st.columns(2)

    with col1:
        st.image(image_np, caption="Noisy Input", use_column_width=True)

    with col2:
        st.image(denoised, caption="Denoised Output", use_column_width=True)
