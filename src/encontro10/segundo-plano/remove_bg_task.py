from PIL import Image
from rembg import remove
from celery_config import app as celery_app
# import time
# from fastapi.responses import FileResponse
# from fastapi import FastAPI, UploadFile

NO_BG_IMAGE_NAME = "no-bg.png"

@celery_app.task
def remove_br(image):
    try:
        bytes_data = Image.open(image)
        output = remove(bytes_data)
        Image.frombytes("RGBA", output.size, output.tobytes()).save(NO_BG_IMAGE_NAME)
        # return True
    except Exception as e:
        print(e)
        # return False