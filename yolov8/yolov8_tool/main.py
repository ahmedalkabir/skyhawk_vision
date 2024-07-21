import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from main_window_ui import Ui_MainWindow
from yolov8_camera import CameraThread

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self._camera = CameraThread(self)
        self._camera.updateFrame.connect(self.set_image)
        self._camera.updateText.connect(self.appendTextCallback)
        self._log_text = self.plainTextEdit

        # default value
        self.cpu_select.setChecked(True)

        self.start_btn.clicked.connect(self.start_camera)
        self.start_with_yolov8.clicked.connect(self.start_with_yolov8_cb)
        self.stop.clicked.connect(self.stop_camera)


    def set_image(self, image):
        scaled_img = image.scaled(self.opencv_object.width(), self.opencv_object.height(), Qt.KeepAspectRatio)
        self.opencv_object.setPixmap(QPixmap.fromImage(scaled_img))

    def start_camera(self):
        self._log_text.appendPlainText('starting camera....')
        if not self._camera.isRunning():
            self._camera.start()

    def stop_camera(self):
        self._log_text.appendPlainText('stopping camera...')
        self._camera.stop()

    def start_with_yolov8_cb(self):
        self._camera.enable_yolov8()
        self._log_text.appendPlainText('starting camera....')
        if not self._camera.isRunning():
            self._camera.start()

    def appendTextCallback(self, text):
        self._log_text.appendPlainText(text)

    def closeEvent(self, event) -> None:
        self._camera.stop()
        # wait unitl the thread exit
        self._camera.wait()


if __name__ == "__main__":
    app = QApplication([])

    main = MainWindow()
    main.resize(640, 640)
    main.show()

    sys.exit(app.exec())
