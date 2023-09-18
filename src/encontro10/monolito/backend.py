from PIL import Image
from rembg import remove
from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse

NO_BG_IMAGE_NAME = "no-bg.png"

def remove_br(image):
    try:
        bytes_data = Image.open(image)
        output = remove(bytes_data)
        Image.frombytes("RGBA", output.size, output.tobytes()).save(NO_BG_IMAGE_NAME)
        return True
    except Exception as e:
        print(e)
        return False

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

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





