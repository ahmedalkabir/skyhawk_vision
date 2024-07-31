# camera_multi.py

import cv2
from base_camera import BaseCamera
from ultralytics import YOLO
import os

class Camera(BaseCamera):
    def __init__(self):
        super().__init__()

    # over-wride of BaseCamera class frames method
    @staticmethod
    def frames():
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')
        model = None
        is_it_npu = False
        try:
            from yolov8_npu import YOLOv8NPU
            absolute_path = os.path.dirname(os.path.abspath(__file__))
            model = YOLOv8NPU(absolute_path + '/rk3588_npu_models/yolov8n.rknn', classes=0)

            if not model.start_rknnLite():
                print('failed to enable npu')
                raise Exception("couldn't start RKNN NPU...")
            is_it_npu = True
        except Exception as ex:
            model = YOLO("yolov8n.pt")
            model.to('cpu')

        people = 0 
        annotate_frame = None
        while True:
            # read current frame
            people = 0
            _, img = camera.read()
            if is_it_npu:
                results = model(img)
                people = len(results[0])
                annotate_frame = model.plot(results)
            else:
                results = model(img, classes=0)
                # print(len(results))
                for r in results:
                    boxes = r.boxes
                    for box in boxes:
                        # print(box)
                        if box.cls[0] == 0:
                            people += 1
                annotate_frame = results[0].plot()

            # encode as a jpeg image and return it
            yield (cv2.imencode('.jpg', annotate_frame)[1].tobytes(), people)