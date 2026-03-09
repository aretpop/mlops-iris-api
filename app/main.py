import pickle
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

# Load model artifact
with open("app/model.pkl", "rb") as f:
    artifact = pickle.load(f)

model = artifact["model"]
features = artifact["features"]

app = FastAPI()


class IrisFeatures(BaseModel):

    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/")
def home():
    return {"message": "Iris ML API running"}


@app.post("/predict")
def predict(data: IrisFeatures):

    input_data = np.array([
        [
            data.sepal_length,
            data.sepal_width,
            data.petal_length,
            data.petal_width
        ]
    ])

    prediction = model.predict(input_data)[0]

    return {
        "prediction": int(prediction)
    }