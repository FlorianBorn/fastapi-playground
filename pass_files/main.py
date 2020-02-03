# from https://fastapi.tiangolo.com/tutorial/first-steps/

from fastapi import FastAPI, File, UploadFile
from starlette.responses import FileResponse
from PIL import Image
from io import BytesIO
import tempfile

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# See: https://fastapi.tiangolo.com/tutorial/request-files/#define-file-parameters
@app.post("/bytes_file/") 
def bytes_file(file: bytes = File(...)): # file is just an arbitrary variable name
    '''
        this function takes an image as input and returns this image as it is
        to test this api open the docs-Api (localhost:8000/docs)
    '''
    with tempfile.NamedTemporaryFile(mode="w+b", suffix=".png", delete=True) as file_out:
        file_out.write(file) # Attention: tmp-files are somehow not deleted after return        
        return FileResponse(file_out.name, media_type="image/png")

# See: https://fastapi.tiangolo.com/tutorial/request-files/#file-parameters-with-uploadfile
@app.post("/upload_file/")
def upload_file(file: UploadFile = File(...)): # file is just an arbitrary variable name
    '''
        this function takes an image as input. Instead of type bytes it has the FastAPI
        type UploadFile, which has same more properties/attributes
        See: https://fastapi.tiangolo.com/tutorial/request-files/#file-parameters-with-uploadfile
    '''
    file_properties = {}
    file_properties['filename'] = file.filename
    file_properties['content_type'] = file.content_type
    return file