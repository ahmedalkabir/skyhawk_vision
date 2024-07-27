import cv2
from cv2.typing import MatLike
from PySide6.QtCore import Qt, QThread, Signal, Slot
from PySide6.QtGui import QAction, QImage, QKeySequence, QPixmap
from ultralytics import YOLO
import time
import torch
import os
from enum import Enum



Device = Enum('Device', ['CPU', 'CUDA', 'RK3588', 'RASPBERRY_PI'])


class Camera:
    def __init__(self, index_camera: int) -> None:
        self._camera_source = index_camera
        self._cap = True

    def open_camera(self) -> bool:
        self._cap = cv2.VideoCapture(self._camera_source)

        if not self._cap.isOpened():
            return True
        
    def open_video(self, path) -> bool:
        self._cap = cv2.VideoCapture(path)
        self._cap.set(cv2.CAP_PROP_FPS, 30)
        if not self._cap.isOpened():
            return True

    def close_camera(self):
        self._cap.release()
        cv2.destroyAllWindows()

    def read_frame(self) -> tuple[bool, MatLike]:
        return self._cap.read()
    
class CameraThread(QThread):
    updateFrame = Signal(QImage)
    updateText = Signal(str)


    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self._status = True
        self._cap = True
        self._camera = Camera(0)
        self._with_yolov8 = False
        self.prev_frame_time = 0
        self.new_frame_time = 0
        self._yolov8_model = False
        self._device = Device.CPU
        self._is_camera: bool = False
        self._path_video: str = ''

    def detect_video(self, path: str):
        self._path_video = path
        print(self._path_video)
        self._is_camera = False

    def detect_camera(self, index: int):
        self._camera = Camera(0)
        self._is_camera = True

    def enable_yolov8(self):
        self.updateText.emit('loading model....')
        self._yolov8_model = YOLO("yolov8n.pt")
        
        if self._device == Device.CPU:
            self.updateText.emit('inference using cpu....')
            self._yolov8_model.to('cpu')
        elif self._device == Device.CUDA:
            self.updateText.emit('inference using cuda....')
            self._yolov8_model.to('cuda')
        elif self._device == Device.RASPBERRY_PI:
            self.updateText.emit('inference using ncnn....')
                        # Export the model to NCNN format
            self._yolov8_model.export(format="ncnn")  # creates 'yolov8n_ncnn_model'

            # Load the exported NCNN model
            ncnn_model = YOLO("yolov8n_ncnn_model")
            self._yolov8_model = ncnn_model
        self._with_yolov8 = True
        self.updateText.emit('model loaded')

    def from_cv2_to_qimage(self, frame, h: int = 0, w: int = 0):
        color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Creating and scaling QImage
        h, w, ch = color_frame.shape
        img = QImage(color_frame.data, w, h, ch * w, QImage.Format_RGB888)
        if h == 0 and w == 0:
            return img
        else:
            scaled_img = img.scaled(w, h, Qt.KeepAspectRatio)
            return scaled_img

    def run(self):
        if self._is_camera:
            self._camera.open_camera()
            self.updateText.emit('camera opened...')
        else:
            self._camera.open_video(self._path_video)
            self.updateFrame.emit('video opened...')
        self._status = True
        while self._status:
            self.new_frame_time = time.time()
            ret, orignal_frame = self._camera.read_frame()
            if not ret:
                continue

            if self._with_yolov8:
                results = self._yolov8_model(orignal_frame)
                # results = self._yolov8_model.track(orignal_frame)
                annotate_frame = results[0].plot()
                fps = 1/(self.new_frame_time-self.prev_frame_time)
                self.prev_frame_time = self.new_frame_time

                fps = int(fps)
                fps_string = str(fps)

                cv2.putText(annotate_frame, fps_string, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)
                self.updateFrame.emit(self.from_cv2_to_qimage(annotate_frame, 400, 400))

                for result in results:
                    print(result.boxes)

            else:
                self.updateFrame.emit(self.from_cv2_to_qimage(orignal_frame, 400, 400))
            
        self._camera.close_camera()

    def stop(self):
        self._status = False

    def select_device(self, dev: Device):
        self._device = dev

    def IsCuda(self) -> bool:
        if torch.cuda.is_available():
            return True
        return False
    
    def IsRK3588CPU(self) -> bool:
        try:
            os_detail = os.uname()
        except Exception as ex:
            pass
        return False
    
    def IsRaspberryPi(self) -> bool:
        try:
            os_detail = os.uname()
            if os_detail.nodename == 'raspberrypi':
                return True
        except Exception as ex:
            return False
        return False