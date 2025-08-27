# 🎬 BERT Sentiment Analysis API with Flask

A powerful and lightweight web API that uses a fine-tuned **BERT model** to perform real-time sentiment analysis on movie reviews and other text.

This application is built with **Flask** and leverages the **Hugging Face Transformers** library to serve a sophisticated NLP model, capable of understanding context and nuance to classify text as **"Positive"** or **"Negative"**.

## ✨ Features

- **High Accuracy** – Pre-trained BERT model fine-tuned on the IMDB dataset
- **RESTful API** – Simple `/predict` endpoint for easy integration
- **Lightweight & Fast** – Built with Flask, easy to deploy anywhere
- **Easy to Run** – Includes a `.bat` script for one-click startup on Windows

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **NLP Model:** BERT (Bidirectional Encoder Representations from Transformers)
- **Core Libraries:** Hugging Face Transformers, PyTorch

## ⚙️ Installation & Setup

### 1. Prerequisites

- Python 3.8+
- Git

### 2. Clone the Repository

```bash
git clone https://github.com/balamarimuthu/flask-bert-sentiment.git
cd flask-bert-sentiment
```

### 3. Download the Fine-Tuned Model 🧠

The trained BERT model is hosted on Kaggle due to its size. You must download it before running the application.

- **Download the `bert__model` from Kaggle**

After downloading, place the `local_model_path` folder in the main project directory.

### 4. Set Up a Virtual Environment

```bash
# Create the environment
python -m venv .venv

# Activate the environment (on Windows)
.\.venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🚀 How to Run the API

A convenient batch file is included to start the Flask server. From your terminal (with the virtual environment activated), run:

```bash
.\run_bert_api.bat
```

The server will start on `http://127.0.0.1:5000`.

## 👨‍💻 API Usage

Send `POST` requests to the `/predict` endpoint with your text.

### Example with `curl`

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"This movie was a masterpiece. The acting, cinematography, and story were all phenomenal!\"}" \
  http://127.0.0.1:5000/predict
```

### ✅ Expected Positive Response:

```json
{
  "sentiment": "Positive"
}
```

## 📜 License

This project is licensed under the MIT License.
