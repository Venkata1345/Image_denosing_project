# 🧼 U-Net Image Denoiser

![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?logo=streamlit)
![Model](https://img.shields.io/badge/Model-U--Net-blue)
![Status](https://img.shields.io/badge/Status-Working-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A clean and intuitive web app that removes **salt-and-pepper noise** from images using a **U-Net-based denoising autoencoder**. Built with **TensorFlow + Streamlit**, this project demonstrates the power of deep learning in image restoration.

---

## 🚀 Features

✅ Upload noisy images (grayscale or RGB)  
✅ Real-time denoising via U-Net  
✅ Compare input vs. output side-by-side  
✅ Easily extendable with other models or loss functions

---

## 🧠 Model Comparison

| Metric        | Baseline Autoencoder | U-Net Denoiser |
|---------------|----------------------|----------------|
| **PSNR (↑)**  | 19.33 dB             | **20.30 dB** ✅ |
| **SSIM (↑)**  | 0.6995               | **0.7907** ✅   |
| **MSE (↓)**   | 0.014276             | **0.011804** ✅ |

---

## 🖼 Sample Results

| Noisy Input | U-Net Denoised | Ground Truth |
|-------------|----------------|---------------|
| ![noisy](assets/noisy_example.jpg) | ![denoised](assets/denoised_example.jpg) | ![gt](assets/groundtruth_example.jpg) |



---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/unet-image-denoiser.git
cd unet-image-denoiser

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
