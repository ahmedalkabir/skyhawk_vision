# fastapi_app.py

import asyncio
import uvicorn
from ultralytics import YOLO

from sse_starlette.sse import EventSourceResponse
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
# from camera_single import Camera
from camera_multi import Camera
from pymavlink import mavutil


# TODO: refactor this shits
master = mavutil.mavlink_connection("/dev/ttyS4", baud=57600)

# Wait a heartbeat before sending commands
# master.wait_heartbeat()

app = FastAPI()

absolute_path = os.path.dirname(os.path.abspath(__file__))

app.mount("/static", StaticFiles(directory=absolute_path +  "/static"), name="static")
templates = Jinja2Templates(directory=absolute_path + "/templates")

camera_status = False
people = 0


async def numbers(minimum, maximum):
    global people
    while True:
        await asyncio.sleep(0.9)
        yield dict(data=people)
    # for i in range(minimum, maximum + 1):
    #     await asyncio.sleep(0.9)
    #     yield dict(data=10)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
   return templates.TemplateResponse('index.html', {"request": request})

def gen(camera: Camera):
    """Video streaming generator function."""
    global people 
    while camera_status:
        frame = camera.get_frame()
        # await queue.put(frame[1])
        people = frame[1]
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame[0] + b'\r\n')


@app.get('/video_feed', response_class=HTMLResponse)
async def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return  StreamingResponse(gen(Camera()),
                    media_type='multipart/x-mixed-replace; boundary=frame')

@app.get('/start_camera')
async def start_camera():
    global camera_status
    camera_status = True
    return {"message": "success"}

@app.get('/stop_camera')
async def stop_camera():
    global camera_status
    camera_status = False
    return {"message": "success"}

@app.get('/arm_drone')
async def arm_drone():
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,
        1, 0, 0, 0, 0, 0, 0)
    master.motors_armed_wait()
    return {"message": "drone armed"}

@app.get('/disarm_drone')
async def disarm_drone():
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,
        0, 0, 0, 0, 0, 0, 0)
    master.motors_disarmed_wait()
    return {"message": "drone disarmed"}

@app.get('/sse-testing')
async def sse():
    generator = numbers(1, 5)
    return EventSourceResponse(generator)


if __name__ == "__main__":
    print('stop: ctrl+c')
    uvicorn.run(app, host="0.0.0.0", port=8000)