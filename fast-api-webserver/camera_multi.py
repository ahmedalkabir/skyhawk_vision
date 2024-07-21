# camera_multi.py

import cv2
from base_camera import BaseCamera
from ultralytics import YOLO


class Camera(BaseCamera):
    def __init__(self):
        super().__init__()

    # over-wride of BaseCamera class frames method
    @staticmethod
    def frames():
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')
        model = YOLO("yolov8n.pt")
        model.to('cpu')
        while True:
            # read current frame
            _, img = camera.read()


            results = model(img)

            annotate_frame = results[0].plot()

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', annotate_frame)[1].tobytes()