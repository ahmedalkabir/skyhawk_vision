import uvicorn
from fastapi import FastAPI, Depends, Request
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import cv2
from ultralytics import YOLO

sample_path = "sample_1.mp4"
app = FastAPI()

templates = Jinja2Templates(directory="templates")

def camera_setup():
    print("[camera_setup called]")
    vid = cv2.VideoCapture(0)
    model = YOLO("yolov8n.pt")
    return (vid, model)

def generate(vid):
    cam = vid[0]
    model = vid[1]
    try:
        while True:
            fet, frame = cam.read()

            results = model(frame)
            annotated_frame = results[0].plot()

            binary_string = cv2.imencode('.png', annotated_frame)[1].tobytes()
            yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
                        binary_string + b'\r\n')
    except:
        print("oh no, something bad happened")

def stream_video():
    with open(sample_path, mode='rb') as video:
        yield from video

# @app.get("/source")
# async def source_video():
#     return StreamingResponse(stream_video(), media_type="video/mp4")

@app.get("/cv2-original")
async def video_feed(vid=Depends(camera_setup)):
    return StreamingResponse(generate(vid), media_type="multipart/x-mixed-replace;boundary=frame")

@app.get("/yolov8", response_class=HTMLResponse)
async def yolov8(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.get("/start-yolov8")
async def start_yolov8():
    return {"message": "started"}

@app.get("/")
async def main():
    return {"message": "hello world"}

if __name__ == "__main__":
    uvicorn.run("yolov8_webserver:app", reload=True)