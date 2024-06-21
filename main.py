from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str



app = FastAPI()
classifier = pipeline("sentiment-analysis")



@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)[0]


@app.post("/detailed_predict/")
def detailed_predict(item: Item):
    result = classifier(item.text)
    return {
        "label": result[0]['label'],
        "score": result[0]['score'],
        "text": item.text
    }
