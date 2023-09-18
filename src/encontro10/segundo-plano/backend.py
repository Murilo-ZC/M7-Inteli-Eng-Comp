from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
# from task import remove_br, sample_task, combine_bg
from task import sample_task
from celery_config import app as celery_app
from celery.result import AsyncResult
NO_BG_IMAGE_NAME = "no-bg.png"


app = FastAPI()


@app.get("/")
async def root():
    task_id = sample_task.apply_async()
    return {'MESSAGE': 'Task Submitted', "TASK_ID": task_id.id}

@app.get("/status/{task_id}")
async def status(task_id):
    return {"TASKID": task_id, "STATUS":celery_app.AsyncResult(task_id).state}

@app.post("/remove_bg")
async def remove_bg(image:UploadFile = None):
    if not image:
        return {"message": "No image"}
    if remove_br(image.file):
        return FileResponse(NO_BG_IMAGE_NAME)
    return {"message": "Error"}

@app.post("/combine_bg")
async def combine_bg(image:UploadFile = None, background:UploadFile = None):
    if not image or not background:
        return {"message": "No image or no background"}
    if remove_br(image.file):
        try:
            bytes_data = Image.open(NO_BG_IMAGE_NAME)
            bg = Image.open(background.file)
            bg.paste(bytes_data, (bg.width//2, bg.height//2), bytes_data)
            bg.save(NO_BG_IMAGE_NAME, "JPEG", optimize=True,)
            return FileResponse(NO_BG_IMAGE_NAME)
        except Exception as e:
            print(e)
            return {"message": "Error"}
    return {"message": "Error"}





