# 🧠 AI Handwritten CAPTCHA Verification

<div align="center">

### A Deep Learning–Powered Handwritten Digit CAPTCHA System

<p>
  <b>Draw a digit → AI recognizes it → CAPTCHA verifies the response</b>
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Backend-000000?logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?logo=pytorch&logoColor=white" alt="PyTorch">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?logo=opencv&logoColor=white" alt="OpenCV">
  <img src="https://img.shields.io/badge/EfficientNetV2B0-Model-FF6F00" alt="EfficientNetV2B0">
  <img src="https://img.shields.io/badge/MobileNetV2-Model-4285F4" alt="MobileNetV2">
</p>

<p>
  <a href="#-overview">Overview</a> •
  <a href="#-features">Features</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-models">Models</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-how-it-works">How It Works</a> •
  <a href="#-results">Results</a>
</p>

</div>

---

## 📌 Overview

**AI Handwritten CAPTCHA Verification** is a full-stack AI application that combines **deep learning, computer vision, and web technologies** to create an interactive CAPTCHA verification system.

Instead of asking users to identify distorted text or select images, the system generates a target digit and asks the user to **draw that digit on an HTML5 canvas**. The drawing is sent to a Flask backend, preprocessed, and classified using trained deep-learning models.

The predicted digit is then compared with the CAPTCHA target. A confidence threshold is also applied before the system accepts the verification.

### Why this project?

Traditional CAPTCHA systems can be inconvenient for users and increasingly challenging for accessibility. This project explores an alternative approach where a user interacts naturally with a drawing canvas while an AI model performs the recognition task.

---

## ✨ Key Features

- 🎨 **Interactive Drawing Canvas** — Draw digits directly in the browser.
- 🤖 **Deep Learning Recognition** — Uses trained EfficientNetV2B0 and MobileNetV2 models.
- 🔐 **CAPTCHA Verification** — Verifies whether the drawn digit matches the generated target.
- 📊 **Confidence-Based Validation** — Rejects predictions when model confidence is below the configured threshold.
- ⚡ **Real-Time Inference** — Models are loaded once when the Flask application starts.
- 🖼️ **Computer Vision Preprocessing** — Cropping, padding, resizing, tensor conversion, and normalization.
- 🧪 **Model Evaluation** — Includes accuracy/loss curves, confusion matrices, ROC curves, and classification reports.
- 🧩 **Modular Architecture** — Separates Flask routing, preprocessing, prediction, and CAPTCHA generation logic.
- 💻 **CPU/GPU Support** — Automatically uses CUDA when an available NVIDIA GPU is detected.
- 🌐 **REST API** — Provides endpoints for CAPTCHA generation and digit prediction.

---

## 🏗️ Architecture

```text
┌───────────────────────────────┐
│         Web Browser           │
│                               │
│   HTML / CSS / JavaScript     │
│        HTML5 Canvas           │
└───────────────┬───────────────┘
                │
                │ Base64 Image
                ▼
┌───────────────────────────────┐
│          Flask API            │
│                               │
│  /api/captcha                 │
│  /api/predict                 │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│     Image Preprocessing       │
│                               │
│  • Decode Base64              │
│  • RGBA → RGB                 │
│  • Find digit bounding box    │
│  • Crop + Padding             │
│  • Resize to 64 × 64          │
│  • Normalize image tensor     │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│      Deep Learning Models     │
│                               │
│   EfficientNetV2B0            │
│            OR                 │
│   MobileNetV2                 │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│      Prediction Engine        │
│                               │
│  Predicted Digit + Confidence │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│      CAPTCHA Verification     │
│                               │
│ predicted == target           │
│        AND                    │
│ confidence ≥ threshold        │
└───────────────┬───────────────┘
                │
          ┌─────┴─────┐
          ▼           ▼
      ✅ Verified   ❌ Failed
```

---

## 🧠 How It Works

### 1. Generate CAPTCHA

The backend generates a target digit for the CAPTCHA challenge.

```text
Target: 7
```

### 2. User Draws the Digit

The user draws the target digit on the browser's canvas.

```text
User → Draws "7"
```

### 3. Image Preprocessing

The canvas image is sent as Base64 data and processed before inference:

- Decode the Base64 image
- Handle transparency/RGBA input
- Convert to RGB
- Detect the digit bounding box
- Crop the drawing
- Add padding
- Resize to `64 × 64`
- Convert to PyTorch tensor
- Apply normalization

### 4. AI Prediction

The processed image is passed to the selected trained model.

The model returns:

```text
Predicted Digit: 7
Confidence: 0.XX
```

### 5. Verification

The system verifies the CAPTCHA only when:

```text
Predicted Digit == Target Digit
AND
Confidence >= 0.40
```

Otherwise, verification fails.

---

## 🤖 Models

The project evaluates two lightweight image-classification architectures:

| Model | Purpose |
|---|---|
| **EfficientNetV2B0** | High-performance image classification |
| **MobileNetV2** | Lightweight and efficient inference |

Both models use a custom classification head for **10 digit classes (0–9)**.

### EfficientNetV2B0

The project builds EfficientNetV2B0 with a custom head:

```text
EfficientNetV2B0
      ↓
512-unit Fully Connected Layer
      ↓
Batch Normalization
      ↓
ReLU
      ↓
Dropout
      ↓
10-Class Output
```

### MobileNetV2

MobileNetV2 is used as a more lightweight alternative:

```text
MobileNetV2
      ↓
Dropout
      ↓
512-unit Fully Connected Layer
      ↓
Batch Normalization
      ↓
ReLU
      ↓
Dropout
      ↓
10-Class Output
```

---

## 📊 Model Evaluation

The repository contains evaluation artifacts for the trained models, including:

- Accuracy curves
- Loss curves
- Confusion matrices
- ROC curves
- Classification reports
- Model comparison CSV files
- Trained PyTorch `.pth` weights

These artifacts make it possible to compare model performance rather than treating the project as a black-box classifier.

> **Tip:** Add the final accuracy/F1-score values from your `final_model_comparison.csv` here before publishing your resume/portfolio version. This keeps the README fully evidence-based.

---

## 🛠️ Tech Stack

### AI / Machine Learning
- Python
- PyTorch
- Torchvision
- timm
- EfficientNetV2B0
- MobileNetV2

### Computer Vision
- OpenCV
- Pillow
- Image preprocessing
- Tensor normalization

### Backend
- Flask
- Flask-CORS
- REST API

### Frontend
- HTML5
- CSS
- JavaScript
- HTML5 Canvas

### Development / Experimentation
- Google Colab
- Jupyter Notebook
- Git
- GitHub

---

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/adityaB-code100/handwritten-Digit.git
cd handwritten-Digit
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Install dependencies

For the application:

```bash
cd Project
pip install -r requirements.txt
```

If you are using a CUDA-enabled PyTorch environment, install the appropriate PyTorch build for your GPU from the official PyTorch installation instructions.

### 4. Run the Flask application

```bash
python app.py
```

The application will start on:

```text
http://localhost:5000
```

Open the URL in your browser and interact with the CAPTCHA canvas.

---

## 🔌 API Endpoints

### `GET /api/captcha`

Generates a new CAPTCHA challenge.

Example response:

```json
{
  "status": "success",
  "captcha_digit": 7
}
```

### `POST /api/predict`

Receives the user's canvas image and verifies the CAPTCHA.

Example request:

```json
{
  "image": "data:image/png;base64,...",
  "target_digit": 7,
  "model_name": "EfficientNetV2B0"
}
```

Example response:

```json
{
  "status": "success",
  "predicted_digit": 7,
  "confidence": 0.95,
  "is_verified": true,
  "message": "Verification Successful"
}
```

---

## 🔬 Machine Learning Pipeline

```text
Dataset
   ↓
Data Preparation
   ↓
Image Resizing / Normalization
   ↓
Model Training
   ↓
EfficientNetV2B0 + MobileNetV2
   ↓
Validation & Testing
   ↓
Confusion Matrix
   ↓
ROC Curve
   ↓
Classification Report
   ↓
Model Comparison
   ↓
Deployment through Flask
```

---

## 🎯 Engineering Highlights

This project demonstrates practical experience beyond model training:

- Designing an end-to-end ML application
- Integrating trained models into a production-style backend
- Building an image-processing pipeline for user-generated input
- Serving PyTorch models through Flask
- Implementing model confidence thresholds
- Handling CPU/GPU inference dynamically
- Connecting frontend canvas input with a backend AI service
- Evaluating multiple CNN architectures
- Organizing model artifacts and experiment results

---


---

## 🎓 Project Applications

The architecture can be extended to:

- Human-verification systems
- Educational handwriting recognition
- Handwritten digit recognition
- Interactive AI demonstrations
- Computer-vision based authentication experiments
- Human-computer interaction research

---

## 👨‍💻 Author

**Aditya Bandewar**

Computer Science & Engineering Student  
Interested in **Artificial Intelligence, Machine Learning, Computer Vision, and Full-Stack Development**.

- GitHub: [@adityaB-code100](https://github.com/adityaB-code100)
- Portfolio: [aditya-bandewar.vercel.app](https://aditya-bandewar.vercel.app/)

---

## ⭐ Support

If you find this project interesting, consider giving the repository a ⭐ on GitHub.

---

<div align="center">

### Built with Python, PyTorch, Flask & Computer Vision ❤️

**AI + Computer Vision + Full-Stack Development**

</div>
