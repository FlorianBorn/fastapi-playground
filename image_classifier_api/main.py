# from: https://fastapi.tiangolo.com/tutorial/bigger-applications/

from fastapi import FastAPI, Form, File
import pickle
import fastai
from fastai.vision import load_learner
from fastai.vision.image import pil2tensor
from PIL import Image
from io import BytesIO
import numpy as np
from pydantic import BaseModel

# class Prediction(BaseModel):
#     prediction_class: str
#     predictions_idx: np.array
#     prediction_outputs: np.array

app = FastAPI()
app.foo = "bar"

with open("export.pkl", 'rb') as model_file:
    model = pickle.load(model_file)
# load the ml model
print(f"model: {dir(model)}")

learner = load_learner(".", "export.pkl")

@app.get("/")
async def root():
    print(dir(learner))
    return {"message": "Hello World"}

@app.get("/api/predict")
@app.post("/api/predict")
async def predict():
    return dir(learner)

# https://fastapi.tiangolo.com/tutorial/request-forms/
@app.post("/image")
async def upload(file: bytes = File(...)):
    response = {}
    #img = Image.frombytes(mode="RGB", size=len(file), data=file)
    img = await Image.open(BytesIO(file)).convert('RGB')
    img_tensor = pil2tensor(img,np.float32)
    print(type(img))
    img = fastai.vision.image.Image(img_tensor)
    pred_class, pred_idx, outputs = learner.predict(img)
    # Types
    # pred_class --> fastai.core.Category
    # pred_idx --> torch.Tensor
    # outputs --> torch.Tensor
    response['pred_class'] = pred_class.obj
    response['pred_idx'] = pred_idx.numpy().tolist()
    response['outputs'] = outputs.numpy().tolist()
    print(pred_class) 
    print(type(pred_class)) # str
    print(type(pred_idx))
    print(type(outputs))
    print(pred_idx.numpy().tolist())
    print(outputs.numpy().tolist())
    return response
    #return(learner.predict(img))
    #print(type(file))
    return("foo")
    #print("hello world")
    #return "foo"
    #return {"file_size": len(file)}
    # print(file)
    # print("ehllo")
    # return {
    #     "file_size": len(file)
    # }
    
    #return "hi"
