from PIL import Image
from rembg import remove
from celery_config import app
import time
from fastapi.responses import FileResponse
from fastapi import FastAPI, UploadFile

NO_BG_IMAGE_NAME = "no-bg.png"

@app.task
def remove_br(image):
    try:
        bytes_data = Image.open(image)
        output = remove(bytes_data)
        Image.frombytes("RGBA", output.size, output.tobytes()).save(NO_BG_IMAGE_NAME)
        # return True
    except Exception as e:
        print(e)
        # return False
    
@app.task
def sample_task():
    for i in range(10):
        time.sleep(5)
    print("Task Completed")

# @app.task
# async def combine_bg(image:UploadFile = None, background:UploadFile = None):
#     if not image or not background:
#         return {"message": "No image or no background"}
#     if remove_br(image.file):
#         try:
#             bytes_data = Image.open(NO_BG_IMAGE_NAME)
#             bg = Image.open(background.file)
#             bg.paste(bytes_data, (bg.width//2, bg.height//2), bytes_data)
#             bg.save(NO_BG_IMAGE_NAME, "JPEG", optimize=True,)
#             return FileResponse(NO_BG_IMAGE_NAME)
#         except Exception as e:
#             print(e)
#             return {"message": "Error"}
#     return {"message": "Error"}