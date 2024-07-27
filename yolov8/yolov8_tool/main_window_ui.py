# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowYZrQcn.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(793, 845)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.opencv_object = QLabel(self.centralwidget)
        self.opencv_object.setObjectName(u"opencv_object")
        self.opencv_object.setMinimumSize(QSize(400, 400))

        self.verticalLayout_5.addWidget(self.opencv_object)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.open_video_source_btn = QPushButton(self.centralwidget)
        self.open_video_source_btn.setObjectName(u"open_video_source_btn")

        self.horizontalLayout_3.addWidget(self.open_video_source_btn)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.camera_source = QRadioButton(self.groupBox)
        self.camera_source.setObjectName(u"camera_source")

        self.horizontalLayout_4.addWidget(self.camera_source)

        self.video_source = QRadioButton(self.groupBox)
        self.video_source.setObjectName(u"video_source")

        self.horizontalLayout_4.addWidget(self.video_source)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addWidget(self.groupBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.horizontalLayout.addWidget(self.plainTextEdit)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.start_btn = QPushButton(self.centralwidget)
        self.start_btn.setObjectName(u"start_btn")

        self.verticalLayout.addWidget(self.start_btn)

        self.start_with_yolov8 = QPushButton(self.centralwidget)
        self.start_with_yolov8.setObjectName(u"start_with_yolov8")

        self.verticalLayout.addWidget(self.start_with_yolov8)

        self.stop = QPushButton(self.centralwidget)
        self.stop.setObjectName(u"stop")

        self.verticalLayout.addWidget(self.stop)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.cpu_select = QRadioButton(self.groupBox_2)
        self.cpu_select.setObjectName(u"cpu_select")

        self.verticalLayout_2.addWidget(self.cpu_select)

        self.cuda_select = QRadioButton(self.groupBox_2)
        self.cuda_select.setObjectName(u"cuda_select")

        self.verticalLayout_2.addWidget(self.cuda_select)

        self.npu_select = QRadioButton(self.groupBox_2)
        self.npu_select.setObjectName(u"npu_select")

        self.verticalLayout_2.addWidget(self.npu_select)

        self.ncnn_select = QRadioButton(self.groupBox_2)
        self.ncnn_select.setObjectName(u"ncnn_select")

        self.verticalLayout_2.addWidget(self.ncnn_select)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addWidget(self.groupBox_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 793, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"YoLoV8 Tool", None))
        self.opencv_object.setText(QCoreApplication.translate("MainWindow", u"OpenCV", None))
        self.open_video_source_btn.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Source", None))
        self.camera_source.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.video_source.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"Detect", None))
        self.start_with_yolov8.setText(QCoreApplication.translate("MainWindow", u"Detect with yolov8", None))
        self.stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Inference Source", None))
        self.cpu_select.setText(QCoreApplication.translate("MainWindow", u"CPU ", None))
        self.cuda_select.setText(QCoreApplication.translate("MainWindow", u"CUDA (Nividia Only)", None))
        self.npu_select.setText(QCoreApplication.translate("MainWindow", u"NPU (RK3855s only)", None))
        self.ncnn_select.setText(QCoreApplication.translate("MainWindow", u"NCNN (Raspberry Pi)", None))
    # retranslateUi

