# from: https://fastapi.tiangolo.com/tutorial/bigger-applications/

from fastapi import FastAPI, Form, File, UploadFile
import pickle
import fastai
from fastai.vision import load_learner
from fastai.vision.image import pil2tensor, open_image
from PIL import Image
from io import BytesIO
import numpy as np
from pydantic import BaseModel
from starlette.responses import FileResponse

# class Prediction(BaseModel):
#     prediction_class: str
#     predictions_idx: np.array
#     prediction_outputs: np.array

app = FastAPI()

# load the fastai-ml model
learner = load_learner(".", "export.pkl")

@app.get("/")
async def root():
    return {"message": "Hello World"}


# https://fastapi.tiangolo.com/tutorial/request-forms/
@app.post("/api/predict")
async def upload(file: UploadFile = File(...)):
    response = {}
    img = convert_to_fastai_image(file)
    pred_class, pred_idx, outputs = learner.predict(img)
    # Types
    # pred_class --> fastai.core.Category
    # pred_idx --> torch.Tensor
    # outputs --> torch.Tensor
    response['pred_class'] = pred_class.obj
    response['pred_idx'] = pred_idx.numpy().tolist()
    response['outputs'] = outputs.numpy().tolist()
    return response

def convert_to_fastai_image(upload_file:UploadFile):
    img = Image.open(upload_file.file).convert('RGB')
    img_tensor = pil2tensor(img,np.float32)
    img_tensor.div_(255)
    return fastai.vision.image.Image(img_tensor)