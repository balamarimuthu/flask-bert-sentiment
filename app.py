
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import BertTokenizer, BertForSequenceClassification
import torch

app = FastAPI()

# Load model and tokenizer from local path
MODEL_PATH = r"C:\Users\balap\for jupyter note book\BERT\bert_sentiment_model"
tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
model = BertForSequenceClassification.from_pretrained(MODEL_PATH)

class InputText(BaseModel):
    text: str
    

@app.post("/predict")
def predict_sentiment(input_text: InputText):
    inputs = tokenizer(input_text.text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    prediction = torch.argmax(logits, dim=1).item()
    sentiment = "Positive" if prediction == 1 else "Negative"
    return {"input": input_text.text, "prediction": sentiment}


  