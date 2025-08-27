BERT Sentiment Analysis API with Flask
A powerful and lightweight web API that uses a fine-tuned BERT model to perform real-time sentiment analysis on movie reviews and other text.

This application is built with Flask and leverages the Hugging Face Transformers library to serve a sophisticated NLP model, capable of understanding context and nuance to classify text as "Positive" or "Negative".

✨ Features
High Accuracy: Utilizes a pre-trained BERT model fine-tuned on the IMDB dataset for superior performance.

RESTful API: Provides a simple and clean /predict endpoint for easy integration with other applications.

Lightweight & Fast: Built with Flask, a micro web framework that is efficient and easy to deploy.

Easy to Run: Includes a .bat script for one-click startup on Windows.

🛠️ Tech Stack
Backend: Python, Flask

NLP Model: BERT (Bidirectional Encoder Representations from Transformers)

Core Libraries: Hugging Face transformers, torch

⚙️ Installation and Setup
Follow these instructions to get the project running on your local machine.

1. Prerequisites
Python 3.8+

Git

2. Clone the Repository
Open your terminal and clone this repository.

git clone https://github.com/balamarimuthu/flask-bert-sentiment.git
cd flask-bert-sentiment

3. Download the Fine-Tuned Model 🧠
The trained BERT model is hosted on Kaggle due to its size. You must download it before running the application.

Download the bert_sentiment_model from Kaggle

After downloading, place the bert_sentiment_model folder in the main project directory. The diagram below shows the files included in the repository.

flask-bert-sentiment/
├── .gitignore
├── app.py
├── bert_model.ipynb
├── local_model.md
├── run_bert_api.bat
└── README.md

4. Set Up a Virtual Environment
It is best practice to use a virtual environment to manage dependencies. This will create a .venv folder in your project, which is already ignored by Git.

# Create the environment
python -m venv .venv

# Activate the environment (on Windows)
.\.venv\Scripts\activate

5. Install Dependencies
Install all the required Python libraries using the requirements.txt file.

pip install -r requirements.txt

🚀 How to Run the API
A convenient batch file is included to start the Flask server.

From your terminal (make sure your virtual environment is activated), run:

.\run_bert_api.bat

Alternatively, you can simply double-click the run_bert_api.bat file in your file explorer.

The server will start, and you will see a message indicating it is running on http://127.0.0.1:5000.

👨‍💻 API Usage
You can interact with the API by sending POST requests to the /predict endpoint. The request body must be a JSON object containing the text you want to analyze.

Example with curl
Here is an example of how to call the API from your terminal using curl:

curl -X POST \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"This movie was a masterpiece. The acting, cinematography, and story were all phenomenal!\"}" \
  http://127.0.0.1:5000/predict

✅ Expected Positive Response:
{
  "sentiment": "Positive"
}

❌ Expected Negative Response:
{
  "sentiment": "Negative"
}

📜 License
This project is licensed under the MIT Li
