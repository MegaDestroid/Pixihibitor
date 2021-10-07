# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import os
import numpy as np
import glob
from sklearn.model_selection import train_test_split
import tensorflow as tf
import tkinter as tk
from tkinter import filedialog
import cv2
import imutils
from PIL import Image
from sklearn.cluster import KMeans
import facefilter.demo1 as ff
global filepath5, filepath4
"""______________________WELCOME WINDOW______________________"""
class Ui_MainWindow1(object):
    def setupUi1(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(805, 452)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bglabel = QtWidgets.QLabel(self.centralwidget)
        self.bglabel.setGeometry(QtCore.QRect(0, 0, 805, 452))
        self.bglabel.setText("")
        self.bglabel.setPixmap(QtGui.QPixmap("C:/Users/vinay/PycharmProjects/untitled/pixibg11.jpg"))
        self.bglabel.setScaledContents(True)
        self.bglabel.setObjectName("bglabel")
        self.titlelabel = QtWidgets.QLabel(self.centralwidget)
        self.titlelabel.setGeometry(QtCore.QRect(30, 90, 291, 101))
        self.titlelabel.setText("")
        self.titlelabel.setPixmap(QtGui.QPixmap("title-white-font1.png"))
        self.titlelabel.setScaledContents(True)
        self.titlelabel.setObjectName("titlelabel")
        self.EditB = QtWidgets.QPushButton(self.centralwidget)
        self.EditB.setGeometry(QtCore.QRect(460, 220, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.EditB.setFont(font)
        self.EditB.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 149, 250, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.EditB.setIconSize(QtCore.QSize(35, 35))
        self.EditB.setObjectName("EditB")
        self.DenoiseB = QtWidgets.QPushButton(self.centralwidget)
        self.DenoiseB.setGeometry(QtCore.QRect(460, 270, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.DenoiseB.setFont(font)
        self.DenoiseB.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 149, 250, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.DenoiseB.setIconSize(QtCore.QSize(35, 35))
        self.DenoiseB.setObjectName("DenoiseB")
        self.BeautiB = QtWidgets.QPushButton(self.centralwidget)
        self.BeautiB.setGeometry(QtCore.QRect(460, 320, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.BeautiB.setFont(font)
        self.BeautiB.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 149, 250, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.BeautiB.setIconSize(QtCore.QSize(35, 35))
        self.BeautiB.setObjectName("BeautiB")
        self.ColorSB = QtWidgets.QPushButton(self.centralwidget)
        self.ColorSB.setGeometry(QtCore.QRect(610, 220, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ColorSB.setFont(font)
        self.ColorSB.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 149, 250, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.ColorSB.setIconSize(QtCore.QSize(35, 35))
        self.ColorSB.setObjectName("ColorSB")
        self.FaceFB = QtWidgets.QPushButton(self.centralwidget)
        self.FaceFB.setGeometry(QtCore.QRect(610, 270, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.FaceFB.setFont(font)
        self.FaceFB.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 149, 250, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.FaceFB.setIconSize(QtCore.QSize(35, 35))
        self.FaceFB.setObjectName("FaceFB")
        self.EncryB = QtWidgets.QPushButton(self.centralwidget)
        self.EncryB.setGeometry(QtCore.QRect(610, 320, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.EncryB.setFont(font)
        self.EncryB.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 149, 250, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.EncryB.setIconSize(QtCore.QSize(35, 35))
        self.EncryB.setObjectName("EncryB")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi1(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.EditB.clicked.connect(Ui_MainWindow1.open2)
        self.DenoiseB.clicked.connect(Ui_MainWindow1.open3)
        self.BeautiB.clicked.connect(Ui_MainWindow1.open4)
        self.ColorSB.clicked.connect(Ui_MainWindow1.open5)
        self.FaceFB.clicked.connect(Ui_MainWindow1.open6)
        self.EncryB.clicked.connect(Ui_MainWindow1.open7)

    def open1(self):
        ui = Ui_MainWindow1()
        ui.setupUi1(w)
        w.show()

    def open2(self):
        ui =Ui_MainWindow2()
        ui.setupUi2(w)
        w.show()

    def open3(self):
        ui = Ui_MainWindow3()
        ui.setupUi3(w)
        w.show()

    def open4(self):
        ui = Ui_MainWindow4()
        ui.setupUi4(w)
        w.show()

    def open5(self):
        ui = Ui_MainWindow5()
        ui.setupUi5(w)
        w.show()

    def open6(self):
        Ui_MainWindow1.pop(Ui_MainWindow1,"Press 'ESC' when you are done.")
        ff.face_filter()

    def open7(self):
        ui = Ui_MainWindow7()
        ui.setupUi7(w)
        w.show()

    def pop(self,t):
        msg=QMessageBox()
        msg.setText(t)
        msg.setWindowTitle("Message")
        msg.setStyleSheet("QLabel{min-width: 270px;min-height: 30px;}")
        msg.exec_()

    def retranslateUi1(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pixihibitor v2.0"))
        self.EditB.setText(_translate("MainWindow", "Edit"))
        self.DenoiseB.setText(_translate("MainWindow", "Denoise Text"))
        self.BeautiB.setText(_translate("MainWindow", "Beautification"))
        self.ColorSB.setText(_translate("MainWindow", "Color Splash"))
        self.FaceFB.setText(_translate("MainWindow", "Face Filters"))
        self.EncryB.setText(_translate("MainWindow", "Encryption"))


"""______________________EDIT WINDOW______________________"""
def crop():
    refPt = []
    cropping = False
    def click_and_crop(event, x, y, flags, param):
        global refPt, cropping
        if event == cv2.EVENT_LBUTTONDOWN:
            refPt = [(x, y)]
            cropping = True

        elif event == cv2.EVENT_LBUTTONUP:
            refPt.append((x, y))
            cropping = False
            cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
            roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
            cv2.imshow("Original", image)
            cv2.imshow("Cropped", roi)
            cv2.imwrite('working.png', roi)
            global filepath4
            filepath4="C:/Users/vinay/PycharmProjects/untitled/working.png"
    image = cv2.imread(filepath4)
    (h, w) = image.shape[:2]
    ratio = w / h
    if h > w:
        h = 500
        w = int(ratio * h)
    elif w > h:
        w = 900
        h = int(w / ratio)
    else:
        w = 500
        h = 500
    image = cv2.resize(image, (w, h), interpolation=cv2.INTER_AREA)
    clone = image.copy()
    cv2.namedWindow("Original")
    cv2.setMouseCallback("Original", click_and_crop)
    cv2.imshow("Original", image)
    cv2.waitKey()
    Ui_MainWindow2.open2(Ui_MainWindow2)
    cv2.destroyAllWindows()

def rotate90r():
    global filepath4
    image = cv2.imread(filepath4)
    (h, w) = image.shape[:2]
    ratio = w / h
    if h > w:
        h = 500
        w = int(ratio * h)
    elif w > h:
        w = 900
        h = int(w / ratio)
    else:
        w = 500
        h = 500
    image = cv2.resize(image, (w, h), interpolation=cv2.INTER_AREA)
    clone = image.copy()
    rotated90 = imutils.rotate_bound(image, 90)
    cv2.imwrite('working.png', rotated90)
    cv2.waitKey()
    filepath4 = "C:/Users/vinay/PycharmProjects/untitled/working.png"
    Ui_MainWindow2.open2(Ui_MainWindow2)

def rotate90l():
    global filepath4
    image = cv2.imread(filepath4)
    (h, w) = image.shape[:2]
    ratio = w / h
    if h > w:
        h = 500
        w = int(ratio * h)
    elif w > h:
        w = 900
        h = int(w / ratio)
    else:
        w = 500
        h = 500
    image = cv2.resize(image, (w, h), interpolation=cv2.INTER_AREA)
    clone = image.copy()
    rotated90 = imutils.rotate_bound(image, 270)
    cv2.imwrite('working.png', rotated90)
    cv2.waitKey()
    filepath4 = "C:/Users/vinay/PycharmProjects/untitled/working.png"
    Ui_MainWindow2.open2(Ui_MainWindow2)

def rotate180():
    global filepath4
    image = cv2.imread(filepath4)
    (h, w) = image.shape[:2]
    ratio = w / h
    if h > w:
        h = 500
        w = int(ratio * h)
    elif w > h:
        w = 900
        h = int(w / ratio)
    else:
        w = 500
        h = 500
    image = cv2.resize(image, (w, h), interpolation=cv2.INTER_AREA)
    clone = image.copy()
    rotated90 = imutils.rotate_bound(image, 180)
    cv2.imwrite('working.png', rotated90)
    cv2.waitKey()
    filepath4 = "C:/Users/vinay/PycharmProjects/untitled/working.png"
    Ui_MainWindow2.open2(Ui_MainWindow2)

def flip():
    global filepath4
    image = cv2.imread(filepath4)
    (h, w) = image.shape[:2]
    ratio = w / h
    if h > w:
        h = 500
        w = int(ratio * h)
    elif w > h:
        w = 900
        h = int(w / ratio)
    else:
        w = 500
        h = 500
    image = cv2.resize(image, (w, h), interpolation=cv2.INTER_AREA)
    clone = image.copy()
    flipHorizontal = cv2.flip(image, 1)
    cv2.imwrite('working.png', flipHorizontal)
    cv2.waitKey()
    filepath4 = "C:/Users/vinay/PycharmProjects/untitled/working.png"
    Ui_MainWindow2.open2(Ui_MainWindow2)

def doodle():
    def colorslid():
        def nothing(x):
            pass
        r = 0
        g = 0
        b = 0
        img = np.zeros((300, 512, 3), np.uint8)
        cv2.namedWindow('image')
        cv2.createTrackbar('R', 'image', 0, 255, nothing)
        cv2.createTrackbar('G', 'image', 0, 255, nothing)
        cv2.createTrackbar('B', 'image', 0, 255, nothing)
        Ui_MainWindow1.pop(Ui_MainWindow1,"Press 'ESC' when you are done.")
        while (1):
            cv2.imshow('image', img)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
            r = cv2.getTrackbarPos('R', 'image')
            g = cv2.getTrackbarPos('G', 'image')
            b = cv2.getTrackbarPos('B', 'image')
            img[:] = [b, g, r]
        cv2.destroyAllWindows()
        print((b, g, r))
        return (b, g, r)

    global drawing,mode
    drawing = False
    mode = True
    color = colorslid()
    def paint_draw(event, former_x, former_y, flags, param):
        global current_former_x, current_former_y, drawing, mode
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            current_former_x, current_former_y = former_x, former_y

        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing == True:
                if mode == True:
                    cv2.line(image, (current_former_x, current_former_y), (former_x, former_y), color, 5)
                    current_former_x = former_x
                    current_former_y = former_y
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            if mode == True:
                cv2.line(image, (current_former_x, current_former_y), (former_x, former_y), color, 5)
                current_former_x = former_x
                current_former_y = former_y
        return former_x, former_y
    global filepath4
    image = cv2.imread(filepath4)
    (h, w) = image.shape[:2]
    ratio = w / h
    h = 500
    w = int(ratio * h)
    image = cv2.resize(image, (w, h), interpolation=cv2.INTER_AREA)
    cv2.namedWindow("OpenCV Paint Brush")
    Ui_MainWindow1.pop(Ui_MainWindow1, "Press 'ESC' when you are done.")
    cv2.setMouseCallback('OpenCV Paint Brush', paint_draw)
    while (1):
        cv2.imshow('OpenCV Paint Brush', image)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:  # Escape KEY
            cv2.imwrite('working.png', image)
            filepath4 = "C:/Users/vinay/PycharmProjects/untitled/working.png"
            Ui_MainWindow2.open2(Ui_MainWindow2)
            break
    cv2.destroyAllWindows()

global addtext
def text1():
    def colorslid():
        def nothing(x):
            pass
        r = 0
        g = 0
        b = 0
        img = np.zeros((300, 512, 3), np.uint8)
        cv2.namedWindow('image')
        cv2.createTrackbar('R', 'image', 0, 255, nothing)
        cv2.createTrackbar('G', 'image', 0, 255, nothing)
        cv2.createTrackbar('B', 'image', 0, 255, nothing)
        Ui_MainWindow1.pop(Ui_MainWindow1,"Press 'ESC' when you are done.")
        while (1):
            cv2.imshow('image', img)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
            r = cv2.getTrackbarPos('R', 'image')
            g = cv2.getTrackbarPos('G', 'image')
            b = cv2.getTrackbarPos('B', 'image')
            img[:] = [b, g, r]
        cv2.destroyAllWindows()
        print((b, g, r))
        return (b, g, r)
    color=colorslid()
    image = cv2.imread(filepath4)
    (h, w) = image.shape[:2]
    ratio = w / h
    if h > w:
        h = 500
        w = int(ratio * h)
    elif w > h:
        w = 900
        h = int(w / ratio)
    else:
        w = 500
        h = 500
    image = cv2.resize(image, (w, h), interpolation=cv2.INTER_AREA)
    global addtext
    def c(event, x, y, flags, para):
        if event == cv2.EVENT_LBUTTONUP:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (x, y)
            fontScale = 1
            fontColor = color
            lineType = 2
            global addtext
            cv2.putText(image, addtext,
                        bottomLeftCornerOfText,
                        font,
                        fontScale,
                        fontColor,
                        lineType)

            cv2.imshow("Add Text", image)
            cv2.imwrite('working.png', image)
            cv2.waitKey()
            global filepath4
            filepath4 = "C:/Users/vinay/PycharmProjects/untitled/working.png"
            Ui_MainWindow2.open2(Ui_MainWindow2)

    clone = image.copy()
    cv2.namedWindow("Add Text")
    cv2.setMouseCallback("Add Text", c)
    cv2.imshow("Add Text", image)
    cv2.waitKey(0)

class Ui_MainWindow2(object):
    root = 0
    # root.withdraw()
    file_path = ""
    def setupUi2(self, MainWindow):
        self.root = tk.Tk()
        self.root.withdraw()
        self.file_path = filedialog.askopenfilename()
        global filepath4
        filepath4 = self.file_path
        global filepath5
        filepath5=filepath4
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(805, 452)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bglabel = QtWidgets.QLabel(self.centralwidget)
        self.bglabel.setGeometry(QtCore.QRect(0, 0, 805, 452))
        self.bglabel.setText("")
        self.bglabel.setPixmap(QtGui.QPixmap("C:/Users/vinay/PycharmProjects/untitled/pixibg11.jpg"))
        self.bglabel.setScaledContents(True)
        self.bglabel.setObjectName("bglabel")
        self.origPicL = QtWidgets.QLabel(self.centralwidget)
        self.origPicL.setGeometry(QtCore.QRect(120, 80, 231, 231))
        self.origPicL.setText("")
        pixmap = QtGui.QPixmap(filepath5)
        pixmap1 = pixmap.scaled(231, 231, QtCore.Qt.KeepAspectRatio)
        self.origPicL.setPixmap(QtGui.QPixmap(pixmap1))
        self.origPicL.setAlignment(QtCore.Qt.AlignCenter)
        self.origPicL.setObjectName("origPicL")
        self.cropB = QtWidgets.QPushButton(self.centralwidget)
        self.cropB.setGeometry(QtCore.QRect(80, 350, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cropB.setFont(font)
        self.cropB.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 149, 250, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.cropB.setIconSize(QtCore.QSize(35, 35))
        self.cropB.setObjectName("cropB")
        self.editPicL = QtWidgets.QLabel(self.centralwidget)
        self.editPicL.setGeometry(QtCore.QRect(430, 80, 231, 231))
        self.editPicL.setText("")
        self.editPicL.setObjectName("editPicL")
        pixmap = QtGui.QPixmap(filepath4)
        pixmap1 = pixmap.scaled(231, 231, QtCore.Qt.KeepAspectRatio)
        self.editPicL.setPixmap(QtGui.QPixmap(pixmap1))
        self.editPicL.setAlignment(QtCore.Qt.AlignCenter)
        self.flipB = QtWidgets.QPushButton(self.centralwidget)
        self.flipB.setGeometry(QtCore.QRect(210, 350, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.flipB.setFont(font)
        self.flipB.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 149, 250, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.flipB.setIconSize(QtCore.QSize(35, 35))
        self.flipB.setObjectName("flipB")
        self.rotateB = QtWidgets.QPushButton(self.centralwidget)
        self.rotateB.setGeometry(QtCore.QRect(350, 350, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rotateB.setFont(font)
        self.rotateB.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 149, 250, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.rotateB.setIconSize(QtCore.QSize(35, 35))
        self.rotateB.setObjectName("rotateB")
        self.drawB = QtWidgets.QPushButton(self.centralwidget)
        self.drawB.setGeometry(QtCore.QRect(490, 350, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.drawB.setFont(font)
        self.drawB.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 149, 250, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.drawB.setIconSize(QtCore.QSize(35, 35))
        self.drawB.setObjectName("drawB")
        self.textB = QtWidgets.QPushButton(self.centralwidget)
        self.textB.setGeometry(QtCore.QRect(620, 350, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textB.setFont(font)
        self.textB.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 149, 250, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.textB.setIconSize(QtCore.QSize(35, 35))
        self.textB.setObjectName("textB")
        self.origL = QtWidgets.QLabel(self.centralwidget)
        self.origL.setGeometry(QtCore.QRect(180, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.origL.setFont(font)
        self.origL.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(100, 0, 100, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.origL.setScaledContents(True)
        self.origL.setAlignment(QtCore.Qt.AlignCenter)
        self.origL.setObjectName("origL")
        self.editL = QtWidgets.QLabel(self.centralwidget)
        self.editL.setGeometry(QtCore.QRect(490, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.editL.setFont(font)
        self.editL.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(100, 0, 100, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.editL.setScaledContents(True)
        self.editL.setAlignment(QtCore.Qt.AlignCenter)
        self.editL.setObjectName("editL")
        self.rotateCB = QtWidgets.QComboBox(self.centralwidget)
        self.rotateCB.setGeometry(QtCore.QRect(350, 400, 101, 21))
        self.rotateCB.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 149, 250, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.rotateCB.setObjectName("rotateCB")
        # self.rotateCB.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        # self.rotateCB.setAlignment(QtCore.Qt.AlignCenter)
        self.rotateCB.addItem("")
        self.rotateCB.addItem("")
        self.rotateCB.addItem("")
        self.textLE = QtWidgets.QLineEdit(self.centralwidget)
        self.textLE.setGeometry(QtCore.QRect(620, 400, 101, 20))
        self.textLE.setStyleSheet("color:black;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 149, 250, 0.5);\n"
"\n"
"")
        self.textLE.setObjectName("textLE")
        self.textLE.setAlignment(QtCore.Qt.AlignCenter)
        self.backB = QtWidgets.QPushButton(self.centralwidget)
        self.backB.setGeometry(QtCore.QRect(690, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.backB.setFont(font)
        self.backB.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 149, 250, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.backB.setIconSize(QtCore.QSize(35, 35))
        self.backB.setObjectName("backB")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi2(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        def rotat():
            global rotlist
            rotlist = str(self.rotateCB.currentText())
            if rotlist=="Left":
                rotate90l()
            elif rotlist=="Right":
                rotate90r()
            elif rotlist=="Upside Down":
                rotate180()
        def text():
            global addtext
            addtext=self.textLE.text()
            text1()
        self.cropB.clicked.connect(crop)
        self.flipB.clicked.connect(flip)
        self.rotateB.clicked.connect(rotat)
        self.drawB.clicked.connect(doodle)
        self.textB.clicked.connect(text)
        self.backB.clicked.connect(Ui_MainWindow1.open1)

    def setupUi22(self, MainWindow):
        global filepath4
        global filepath5
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(805, 452)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bglabel = QtWidgets.QLabel(self.centralwidget)
        self.bglabel.setGeometry(QtCore.QRect(0, 0, 805, 452))
        self.bglabel.setText("")
        self.bglabel.setPixmap(QtGui.QPixmap("C:/Users/vinay/PycharmProjects/untitled/pixibg11.jpg"))
        self.bglabel.setScaledContents(True)
        self.bglabel.setObjectName("bglabel")
        self.origPicL = QtWidgets.QLabel(self.centralwidget)
        self.origPicL.setGeometry(QtCore.QRect(120, 80, 231, 231))
        self.origPicL.setText("")
        pixmap = QtGui.QPixmap(filepath5)
        pixmap1 = pixmap.scaled(231, 231, QtCore.Qt.KeepAspectRatio)
        self.origPicL.setPixmap(QtGui.QPixmap(pixmap1))
        self.origPicL.setAlignment(QtCore.Qt.AlignCenter)
        self.origPicL.setObjectName("origPicL")
        self.cropB = QtWidgets.QPushButton(self.centralwidget)
        self.cropB.setGeometry(QtCore.QRect(80, 350, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cropB.setFont(font)
        self.cropB.setStyleSheet("color:white;\n"
                                 "border-style: solid;\n"
                                 "border-width: 1px;\n"
                                 "border-radius: 10px;\n"
                                 "border-color: rgba(0, 149, 250, 0.5);\n"
                                 "background-color:rgba(0, 40, 240, 0.7);\n"
                                 "")
        self.cropB.setIconSize(QtCore.QSize(35, 35))
        self.cropB.setObjectName("cropB")
        self.editPicL = QtWidgets.QLabel(self.centralwidget)
        self.editPicL.setGeometry(QtCore.QRect(430, 80, 231, 231))
        self.editPicL.setText("")
        self.editPicL.setObjectName("editPicL")
        pixmap = QtGui.QPixmap(filepath4)
        pixmap1 = pixmap.scaled(231, 231, QtCore.Qt.KeepAspectRatio)
        self.editPicL.setPixmap(QtGui.QPixmap(pixmap1))
        self.editPicL.setAlignment(QtCore.Qt.AlignCenter)
        self.flipB = QtWidgets.QPushButton(self.centralwidget)
        self.flipB.setGeometry(QtCore.QRect(210, 350, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.flipB.setFont(font)
        self.flipB.setStyleSheet("color:white;\n"
                                 "border-style: solid;\n"
                                 "border-width: 1px;\n"
                                 "border-radius: 10px;\n"
                                 "border-color: rgba(0, 149, 250, 0.5);\n"
                                 "background-color:rgba(0, 40, 240, 0.7);\n"
                                 "")
        self.flipB.setIconSize(QtCore.QSize(35, 35))
        self.flipB.setObjectName("flipB")
        self.rotateB = QtWidgets.QPushButton(self.centralwidget)
        self.rotateB.setGeometry(QtCore.QRect(350, 350, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rotateB.setFont(font)
        self.rotateB.setStyleSheet("color:white;\n"
                                   "border-style: solid;\n"
                                   "border-width: 1px;\n"
                                   "border-radius: 10px;\n"
                                   "border-color: rgba(0, 149, 250, 0.5);\n"
                                   "background-color:rgba(0, 40, 240, 0.7);\n"
                                   "")
        self.rotateB.setIconSize(QtCore.QSize(35, 35))
        self.rotateB.setObjectName("rotateB")
        self.drawB = QtWidgets.QPushButton(self.centralwidget)
        self.drawB.setGeometry(QtCore.QRect(490, 350, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.drawB.setFont(font)
        self.drawB.setStyleSheet("color:white;\n"
                                 "border-style: solid;\n"
                                 "border-width: 1px;\n"
                                 "border-radius: 10px;\n"
                                 "border-color: rgba(0, 149, 250, 0.5);\n"
                                 "background-color:rgba(0, 40, 240, 0.7);\n"
                                 "")
        self.drawB.setIconSize(QtCore.QSize(35, 35))
        self.drawB.setObjectName("drawB")
        self.textB = QtWidgets.QPushButton(self.centralwidget)
        self.textB.setGeometry(QtCore.QRect(620, 350, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textB.setFont(font)
        self.textB.setStyleSheet("color:white;\n"
                                 "border-style: solid;\n"
                                 "border-width: 1px;\n"
                                 "border-radius: 10px;\n"
                                 "border-color: rgba(0, 149, 250, 0.5);\n"
                                 "background-color:rgba(0, 40, 240, 0.7);\n"
                                 "")
        self.textB.setIconSize(QtCore.QSize(35, 35))
        self.textB.setObjectName("textB")
        self.origL = QtWidgets.QLabel(self.centralwidget)
        self.origL.setGeometry(QtCore.QRect(180, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.origL.setFont(font)
        self.origL.setStyleSheet("color:white;\n"
                                 "border-style: solid;\n"
                                 "border-width: 1px;\n"
                                 "border-color: rgba(100, 0, 100, 0.5);\n"
                                 "background-color:rgba(0, 40, 240, 0.7);\n"
                                 "")
        self.origL.setScaledContents(True)
        self.origL.setAlignment(QtCore.Qt.AlignCenter)
        self.origL.setObjectName("origL")
        self.editL = QtWidgets.QLabel(self.centralwidget)
        self.editL.setGeometry(QtCore.QRect(490, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.editL.setFont(font)
        self.editL.setStyleSheet("color:white;\n"
                                 "border-style: solid;\n"
                                 "border-width: 1px;\n"
                                 "border-color: rgba(100, 0, 100, 0.5);\n"
                                 "background-color:rgba(0, 40, 240, 0.7);\n"
                                 "")
        self.editL.setScaledContents(True)
        self.editL.setAlignment(QtCore.Qt.AlignCenter)
        self.editL.setObjectName("editL")
        self.rotateCB = QtWidgets.QComboBox(self.centralwidget)
        self.rotateCB.setGeometry(QtCore.QRect(350, 400, 101, 21))
        self.rotateCB.setStyleSheet("color:white;\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-radius: 10px;\n"
                                    "border-color: rgba(0, 149, 250, 0.5);\n"
                                    "background-color:rgba(0, 40, 240, 0.7);\n"
                                    "")
        self.rotateCB.setObjectName("rotateCB")
        self.rotateCB.addItem("")
        self.rotateCB.addItem("")
        self.rotateCB.addItem("")
        self.textLE = QtWidgets.QLineEdit(self.centralwidget)
        self.textLE.setGeometry(QtCore.QRect(620, 400, 101, 20))
        self.textLE.setStyleSheet("color:black;\n"
                                  "border-style: solid;\n"
                                  "border-width: 1px;\n"
                                  "border-radius: 10px;\n"
                                  "border-color: rgba(0, 149, 250, 0.5);\n"
                                  "\n"
                                  "")
        self.textLE.setObjectName("textLE")
        self.textLE.setAlignment(QtCore.Qt.AlignCenter)
        self.backB = QtWidgets.QPushButton(self.centralwidget)
        self.backB.setGeometry(QtCore.QRect(690, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.backB.setFont(font)
        self.backB.setStyleSheet("color:white;\n"
                                 "border-style: solid;\n"
                                 "border-width: 1px;\n"
                                 "border-radius: 10px;\n"
                                 "border-color: rgba(0, 149, 250, 0.5);\n"
                                 "background-color:rgba(0, 40, 240, 0.7);\n"
                                 "")
        self.backB.setIconSize(QtCore.QSize(35, 35))
        self.backB.setObjectName("backB")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi2(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def rotat():
            global rotlist
            rotlist = str(self.rotateCB.currentText())
            if rotlist == "Left":
                rotate90l()
            elif rotlist == "Right":
                rotate90r()
            elif rotlist == "Upside Down":
                rotate180()

        def text():
            global addtext
            addtext = self.textLE.text()
            text1()

        self.cropB.clicked.connect(crop)
        self.flipB.clicked.connect(flip)
        self.rotateB.clicked.connect(rotat)
        self.drawB.clicked.connect(doodle)
        self.textB.clicked.connect(text)
        self.backB.clicked.connect(Ui_MainWindow1.open1)

    def open2(self):
        print("aaaaaa")
        ui = Ui_MainWindow2()
        ui.setupUi22(w)
        w.show()

    def retranslateUi2(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pixihibitor v2.0 - Edit"))
        self.cropB.setText(_translate("MainWindow", "Crop"))
        self.flipB.setText(_translate("MainWindow", "Flip"))
        self.rotateB.setText(_translate("MainWindow", "Rotate"))
        self.drawB.setText(_translate("MainWindow", "Draw"))
        self.textB.setText(_translate("MainWindow", "Text"))
        self.origL.setText(_translate("MainWindow", "Original"))
        self.editL.setText(_translate("MainWindow", "Edited"))
        self.rotateCB.setItemText(0, _translate("MainWindow", "Left"))
        self.rotateCB.setItemText(1, _translate("MainWindow", "Right"))
        self.rotateCB.setItemText(2, _translate("MainWindow", "Upside Down"))
        self.backB.setText(_translate("MainWindow", "Back"))


"""______________________DENOISE WINDOW______________________"""
def textden(file_path):
    global filepath4
    train_imgs = glob.glob("C:/Users/vinay/PycharmProjects/untitled/denoising-dirty-documents/train/train/*.png")
    train_imgs.sort()
    train_cleaned_imgs = glob.glob(
        "C:/Users/vinay/PycharmProjects/untitled/denoising-dirty-documents/train_cleaned/train_cleaned/*.png")
    train_cleaned_imgs.sort()
    test_imgs = glob.glob(file_path)

    PATCH_WIDTH_HALF = 4
    PATCH_WIDTH = PATCH_WIDTH_HALF * 2 + 1

    # def train_patch_generator(train_imgs, train_cleaned_imgs, epochs=5):
    #     for _ in range(epochs):
    #         for train_file, train_cleaned_file in zip(train_imgs, train_cleaned_imgs):
    #             patches = []
    #             labels = []
    #
    #             train_img = cv2.imread(train_file, cv2.IMREAD_GRAYSCALE)
    #             train_cleaned_img = cv2.imread(train_cleaned_file, cv2.IMREAD_GRAYSCALE)
    #             train_cleaned_img = cv2.threshold(train_cleaned_img, 200, 255, cv2.THRESH_BINARY)[1]
    #             train_img_ext = cv2.copyMakeBorder(train_img, PATCH_WIDTH_HALF, PATCH_WIDTH_HALF, PATCH_WIDTH_HALF,
    #                                                PATCH_WIDTH_HALF, cv2.BORDER_REPLICATE)
    #             for i in range(train_img.shape[0]):
    #                 for j in range(train_img.shape[1]):
    #                     label = train_cleaned_img[i][j]
    #                     patch_c1 = train_img_ext[i:i + PATCH_WIDTH, j:j + PATCH_WIDTH].astype(np.float32) / 255.
    #                     patches.append(np.expand_dims(patch_c1, axis=2))
    #                     labels.append(label / 255.)
    #             patches = np.array(patches)  # patches.shape
    #             labels = np.array(labels)  # labels.shape
    #             yield (patches, labels)

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Conv2D(32, kernel_size=(3, 3), strides=(1, 1), padding='same',
                                     activation='relu', input_shape=(PATCH_WIDTH, PATCH_WIDTH, 1)))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(512, activation='relu'))
    model.add(tf.keras.layers.Dense(256, activation='relu'))
    model.add(tf.keras.layers.Dropout(rate=0.5))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    model.compile(loss=tf.keras.losses.binary_crossentropy,
                  optimizer=tf.keras.optimizers.Adam(lr=0.002),
                  metrics=['mse'])

    # partial_train_imgs, validate_imgs, partial_train_labels, validate_labels = train_test_split(train_imgs,
    #                                                                                             train_cleaned_imgs,
    #                                                                                             test_size=0.1)
    # score = model.evaluate_generator(train_patch_generator(validate_imgs, validate_labels, 1),
    #                                  steps=len(validate_labels))
    mode = tf.keras.models.load_model("my_model1.h5")
    mode.summary()

    def test_patch_generator(test_imgs):
        for test_file in test_imgs:
            patches = []
            test_img = cv2.imread(test_file, cv2.IMREAD_GRAYSCALE)
            test_img_ext = cv2.copyMakeBorder(test_img, PATCH_WIDTH_HALF, PATCH_WIDTH_HALF, PATCH_WIDTH_HALF,
                                              PATCH_WIDTH_HALF, cv2.BORDER_REPLICATE)
            for i in range(test_img.shape[0]):
                for j in range(test_img.shape[1]):
                    patch_c1 = test_img_ext[i:i + PATCH_WIDTH, j:j + PATCH_WIDTH].astype(np.float32) / 255.

                    patches.append(np.expand_dims(patch_c1, axis=2))
            patches = np.array(patches)
            yield patches

    img = cv2.imread(test_imgs[0], cv2.IMREAD_GRAYSCALE)
    predicted_mask = mode.predict_generator(
        generator=test_patch_generator([test_imgs[0]]),
        steps=1).reshape(img.shape).clip(0, 1).round()
    predicted = cv2.bitwise_and(img, 255, mask=(1 - predicted_mask).astype(np.uint8))
    predicted = cv2.bitwise_or(predicted, 255, mask=predicted_mask.astype(np.uint8))
    cv2.imwrite('working.png', predicted)
    cv2.waitKey()
    filepath4 = "C:/Users/vinay/PycharmProjects/untitled/working.png"
    Ui_MainWindow3.open3(Ui_MainWindow3)

class Ui_MainWindow3(object):
    root = 0
    # root.withdraw()
    file_path = ""
    def setupUi3(self, MainWindow):
        self.root = tk.Tk()
        self.root.withdraw()
        self.file_path = filedialog.askopenfilename()
        global filepath4
        filepath4 = self.file_path
        global filepath5
        filepath5 = filepath4
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(805, 452)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bglabel = QtWidgets.QLabel(self.centralwidget)
        self.bglabel.setGeometry(QtCore.QRect(0, 0, 805, 452))
        self.bglabel.setText("")
        self.bglabel.setPixmap(QtGui.QPixmap("C:/Users/vinay/PycharmProjects/untitled/pixibg11.jpg"))
        self.bglabel.setScaledContents(True)
        self.bglabel.setObjectName("bglabel")
        self.origPicL = QtWidgets.QLabel(self.centralwidget)
        self.origPicL.setGeometry(QtCore.QRect(120, 90, 231, 231))
        self.origPicL.setText("")
        pixmap = QtGui.QPixmap(filepath5)
        pixmap1 = pixmap.scaled(231, 231, QtCore.Qt.KeepAspectRatio)
        self.origPicL.setPixmap(QtGui.QPixmap(pixmap1))
        self.origPicL.setAlignment(QtCore.Qt.AlignCenter)
        # self.origPicL.setScaledContents(True)
        self.origPicL.setObjectName("origPicL")
        self.editPicL = QtWidgets.QLabel(self.centralwidget)
        self.editPicL.setGeometry(QtCore.QRect(430, 90, 231, 231))
        self.editPicL.setText("")
        pixmap = QtGui.QPixmap(filepath4)
        pixmap1 = pixmap.scaled(231, 231, QtCore.Qt.KeepAspectRatio)
        self.editPicL.setPixmap(QtGui.QPixmap(pixmap1))
        self.editPicL.setAlignment(QtCore.Qt.AlignCenter)
        self.editPicL.setObjectName("editPicL")
        self.denoiseB = QtWidgets.QPushButton(self.centralwidget)
        self.denoiseB.setGeometry(QtCore.QRect(350, 370, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.denoiseB.setFont(font)
        self.denoiseB.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 149, 250, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.denoiseB.setIconSize(QtCore.QSize(35, 35))
        self.denoiseB.setObjectName("denoiseB")
        self.origL = QtWidgets.QLabel(self.centralwidget)
        self.origL.setGeometry(QtCore.QRect(180, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.origL.setFont(font)
        self.origL.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(100, 0, 100, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.origL.setScaledContents(True)
        self.origL.setAlignment(QtCore.Qt.AlignCenter)
        self.origL.setObjectName("origL")
        self.editL = QtWidgets.QLabel(self.centralwidget)
        self.editL.setGeometry(QtCore.QRect(490, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.editL.setFont(font)
        self.editL.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(100, 0, 100, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.editL.setScaledContents(True)
        self.editL.setAlignment(QtCore.Qt.AlignCenter)
        self.editL.setObjectName("editL")
        self.denoiseB_2 = QtWidgets.QPushButton(self.centralwidget)
        self.denoiseB_2.setGeometry(QtCore.QRect(690, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.denoiseB_2.setFont(font)
        self.denoiseB_2.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 149, 250, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.denoiseB_2.setIconSize(QtCore.QSize(35, 35))
        self.denoiseB_2.setObjectName("denoiseB_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi3(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.denoiseB.clicked.connect(Ui_MainWindow3.textden1)
        self.denoiseB_2.clicked.connect(Ui_MainWindow1.open1)

    def setupUi33(self, MainWindow):
        global filepath4
        global filepath5
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(805, 452)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bglabel = QtWidgets.QLabel(self.centralwidget)
        self.bglabel.setGeometry(QtCore.QRect(0, 0, 805, 452))
        self.bglabel.setText("")
        self.bglabel.setPixmap(QtGui.QPixmap("C:/Users/vinay/PycharmProjects/untitled/pixibg11.jpg"))
        self.bglabel.setScaledContents(True)
        self.bglabel.setObjectName("bglabel")
        self.origPicL = QtWidgets.QLabel(self.centralwidget)
        self.origPicL.setGeometry(QtCore.QRect(120, 90, 231, 231))
        self.origPicL.setText("")
        pixmap = QtGui.QPixmap(filepath5)
        pixmap1 = pixmap.scaled(231, 231, QtCore.Qt.KeepAspectRatio)
        self.origPicL.setPixmap(QtGui.QPixmap(pixmap1))
        self.origPicL.setAlignment(QtCore.Qt.AlignCenter)
        # self.origPicL.setScaledContents(True)
        self.origPicL.setObjectName("origPicL")
        self.editPicL = QtWidgets.QLabel(self.centralwidget)
        self.editPicL.setGeometry(QtCore.QRect(430, 90, 231, 231))
        self.editPicL.setText("")
        pixmap = QtGui.QPixmap(filepath4)
        pixmap1 = pixmap.scaled(231, 231, QtCore.Qt.KeepAspectRatio)
        self.editPicL.setPixmap(QtGui.QPixmap(pixmap1))
        self.editPicL.setAlignment(QtCore.Qt.AlignCenter)
        self.editPicL.setObjectName("editPicL")
        self.denoiseB = QtWidgets.QPushButton(self.centralwidget)
        self.denoiseB.setGeometry(QtCore.QRect(350, 370, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.denoiseB.setFont(font)
        self.denoiseB.setStyleSheet("color:white;\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-radius: 10px;\n"
                                    "border-color: rgba(0, 149, 250, 0.5);\n"
                                    "background-color:rgba(0, 40, 240, 0.7);\n"
                                    "")
        self.denoiseB.setIconSize(QtCore.QSize(35, 35))
        self.denoiseB.setObjectName("denoiseB")
        self.origL = QtWidgets.QLabel(self.centralwidget)
        self.origL.setGeometry(QtCore.QRect(180, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.origL.setFont(font)
        self.origL.setStyleSheet("color:white;\n"
                                 "border-style: solid;\n"
                                 "border-width: 1px;\n"
                                 "border-color: rgba(100, 0, 100, 0.5);\n"
                                 "background-color:rgba(0, 40, 240, 0.7);\n"
                                 "")
        self.origL.setScaledContents(True)
        self.origL.setAlignment(QtCore.Qt.AlignCenter)
        self.origL.setObjectName("origL")
        self.editL = QtWidgets.QLabel(self.centralwidget)
        self.editL.setGeometry(QtCore.QRect(490, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.editL.setFont(font)
        self.editL.setStyleSheet("color:white;\n"
                                 "border-style: solid;\n"
                                 "border-width: 1px;\n"
                                 "border-color: rgba(100, 0, 100, 0.5);\n"
                                 "background-color:rgba(0, 40, 240, 0.7);\n"
                                 "")
        self.editL.setScaledContents(True)
        self.editL.setAlignment(QtCore.Qt.AlignCenter)
        self.editL.setObjectName("editL")
        self.denoiseB_2 = QtWidgets.QPushButton(self.centralwidget)
        self.denoiseB_2.setGeometry(QtCore.QRect(690, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.denoiseB_2.setFont(font)
        self.denoiseB_2.setStyleSheet("color:white;\n"
                                      "border-style: solid;\n"
                                      "border-width: 1px;\n"
                                      "border-radius: 10px;\n"
                                      "border-color: rgba(0, 149, 250, 0.5);\n"
                                      "background-color:rgba(0, 40, 240, 0.7);\n"
                                      "")
        self.denoiseB_2.setIconSize(QtCore.QSize(35, 35))
        self.denoiseB_2.setObjectName("denoiseB_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi3(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.denoiseB.clicked.connect(Ui_MainWindow3.textden1)
        self.denoiseB_2.clicked.connect(Ui_MainWindow1.open1)

    def textden1(self):
        textden(filepath4)

    def open3(self):
        print("aaaaaa")
        ui = Ui_MainWindow3()
        ui.setupUi33(w)
        w.show()

    def retranslateUi3(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pixihibitor v2.0 - Denoise Text"))
        self.denoiseB.setText(_translate("MainWindow", "De-Noise"))
        self.origL.setText(_translate("MainWindow", "Original"))
        self.editL.setText(_translate("MainWindow", "Edited"))
        self.denoiseB_2.setText(_translate("MainWindow", "Back"))


"""______________________BEAUTIFICATION WINDOW______________________"""
class NST:
    def nstpython(self,img,m):
        global filepath4
        args = {"model":m,"image":img}
        # print("[INFO] loading style transfer model...")
        net = cv2.dnn.readNetFromTorch(args["model"])
        model=""
        image = cv2.imread(args["image"])
        image = imutils.resize(image, width=600)
        (h, w) = image.shape[:2]
        blob = cv2.dnn.blobFromImage(image, 1.0, (w, h),
            (103.939, 116.779, 123.680), swapRB=False, crop=False)
        net.setInput(blob)
        output = net.forward()
        output = output.reshape((3, output.shape[2], output.shape[3]))
        output[0] += 103.939
        output[1] += 116.779
        output[2] += 123.680
        output /= 255.0
        output = output.transpose(1, 2, 0)
        (h,w)=output.shape[:2]
        ratio=w/h
        if h>w:
            h=500
            w=int(ratio*h)
        elif w>h:
            w=900
            h=int(w/ratio)
        else:
            w=500
            h=500
        output = cv2.resize(output, (w, h), interpolation=cv2.INTER_AREA)
        cv2.imwrite('working.png', 255*output)
        cv2.waitKey()
        filepath4 = "C:/Users/vinay/PycharmProjects/untitled/working.png"
        Ui_MainWindow4.open4(Ui_MainWindow4)

class Ui_MainWindow4(object):
    root = 0
    # root.withdraw()
    file_path = ""
    list1 = ""
    model = "a"
    img = "a"
    def setupUi4(self, MainWindow):
        self.root = tk.Tk()
        self.root.withdraw()

        self.file_path = filedialog.askopenfilename()
        self.list1 = os.listdir(
            "C:/Users/vinay/PycharmProjects/untitled/neural-style-transfer/models/instance_norm")
        self.model = "a"
        self.img = "a"
        global filepath4
        filepath4 = self.file_path
        global filepath5
        filepath5 = filepath4
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 452)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bglabel = QtWidgets.QLabel(self.centralwidget)
        self.bglabel.setGeometry(QtCore.QRect(0, 0, 811, 451))
        self.bglabel.setText("")
        self.bglabel.setPixmap(QtGui.QPixmap("C:/Users/vinay/PycharmProjects/untitled/pixibg11.jpg"))
        self.bglabel.setScaledContents(True)
        self.bglabel.setObjectName("bglabel")
        self.origPicL = QtWidgets.QLabel(self.centralwidget)
        self.origPicL.setGeometry(QtCore.QRect(120, 80, 231, 231))
        self.origPicL.setText("")
        pixmap = QtGui.QPixmap(filepath5)
        pixmap1 = pixmap.scaled(231, 231, QtCore.Qt.KeepAspectRatio)
        self.origPicL.setPixmap(QtGui.QPixmap(pixmap1))
        self.origPicL.setAlignment(QtCore.Qt.AlignCenter)
        self.origPicL.setObjectName("origPicL")
        self.editPicL = QtWidgets.QLabel(self.centralwidget)
        self.editPicL.setGeometry(QtCore.QRect(430, 80, 231, 231))
        self.editPicL.setText("")
        pixmap = QtGui.QPixmap(filepath4)
        pixmap1 = pixmap.scaled(231, 231, QtCore.Qt.KeepAspectRatio)
        self.editPicL.setPixmap(QtGui.QPixmap(pixmap1))
        self.editPicL.setAlignment(QtCore.Qt.AlignCenter)
        self.editPicL.setObjectName("editPicL")
        self.applyB = QtWidgets.QPushButton(self.centralwidget)
        self.applyB.setGeometry(QtCore.QRect(510, 360, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.applyB.setFont(font)
        self.applyB.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 149, 250, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.applyB.setIconSize(QtCore.QSize(35, 35))
        self.applyB.setObjectName("applyB")
        self.origL = QtWidgets.QLabel(self.centralwidget)
        self.origL.setGeometry(QtCore.QRect(180, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.origL.setFont(font)
        self.origL.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(100, 0, 100, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.origL.setScaledContents(True)
        self.origL.setAlignment(QtCore.Qt.AlignCenter)
        self.origL.setObjectName("origL")
        self.editL = QtWidgets.QLabel(self.centralwidget)
        self.editL.setGeometry(QtCore.QRect(490, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.editL.setFont(font)
        self.editL.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(100, 0, 100, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.editL.setScaledContents(True)
        self.editL.setAlignment(QtCore.Qt.AlignCenter)
        self.editL.setObjectName("editL")
        self.listCB = QtWidgets.QComboBox(self.centralwidget)
        self.listCB.setGeometry(QtCore.QRect(230, 360, 261, 41))
        self.listCB.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 149, 250, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);")
        self.listCB.setObjectName("listCB")
        self.listCB.clear()
        self.listCB.addItems(self.list1)
        self.backB = QtWidgets.QPushButton(self.centralwidget)
        self.backB.setGeometry(QtCore.QRect(690, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.backB.setFont(font)
        self.backB.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 149, 250, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.backB.setIconSize(QtCore.QSize(35, 35))
        self.backB.setObjectName("backB")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi4(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        def begg():
            self.model = "C:/Users/vinay/PycharmProjects/untitled/neural-style-transfer/models/instance_norm/" + str(self.listCB.currentText())
            NST.nstpython(NST,filepath4,self.model)

        self.applyB.clicked.connect(begg)
        self.backB.clicked.connect(Ui_MainWindow1.open1)

    def setupUi44(self, MainWindow):
        self.list1 = os.listdir(
            "C:/Users/vinay/PycharmProjects/untitled/neural-style-transfer/models/instance_norm")
        self.model = "a"
        self.img = "a"
        global filepath4
        global filepath5
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 452)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bglabel = QtWidgets.QLabel(self.centralwidget)
        self.bglabel.setGeometry(QtCore.QRect(0, 0, 811, 451))
        self.bglabel.setText("")
        self.bglabel.setPixmap(QtGui.QPixmap("C:/Users/vinay/PycharmProjects/untitled/pixibg11.jpg"))
        self.bglabel.setScaledContents(True)
        self.bglabel.setObjectName("bglabel")
        self.origPicL = QtWidgets.QLabel(self.centralwidget)
        self.origPicL.setGeometry(QtCore.QRect(120, 80, 231, 231))
        self.origPicL.setText("")
        pixmap = QtGui.QPixmap(filepath5)
        pixmap1 = pixmap.scaled(231, 231, QtCore.Qt.KeepAspectRatio)
        self.origPicL.setPixmap(QtGui.QPixmap(pixmap1))
        self.origPicL.setAlignment(QtCore.Qt.AlignCenter)
        self.origPicL.setObjectName("origPicL")
        self.editPicL = QtWidgets.QLabel(self.centralwidget)
        self.editPicL.setGeometry(QtCore.QRect(430, 80, 231, 231))
        self.editPicL.setText("")
        pixmap = QtGui.QPixmap(filepath4)
        pixmap1 = pixmap.scaled(231, 231, QtCore.Qt.KeepAspectRatio)
        self.editPicL.setPixmap(QtGui.QPixmap(pixmap1))
        self.editPicL.setAlignment(QtCore.Qt.AlignCenter)
        # self.editPicL.setScaledContents(True)
        self.editPicL.setObjectName("editPicL")
        self.applyB = QtWidgets.QPushButton(self.centralwidget)
        self.applyB.setGeometry(QtCore.QRect(510, 360, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.applyB.setFont(font)
        self.applyB.setStyleSheet("color:white;\n"
                                  "border-style: solid;\n"
                                  "border-width: 1px;\n"
                                  "border-radius: 10px;\n"
                                  "border-color: rgba(0, 149, 250, 0.5);\n"
                                  "background-color:rgba(0, 40, 240, 0.7);\n"
                                  "")
        self.applyB.setIconSize(QtCore.QSize(35, 35))
        self.applyB.setObjectName("applyB")
        self.origL = QtWidgets.QLabel(self.centralwidget)
        self.origL.setGeometry(QtCore.QRect(180, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.origL.setFont(font)
        self.origL.setStyleSheet("color:white;\n"
                                 "border-style: solid;\n"
                                 "border-width: 1px;\n"
                                 "border-color: rgba(100, 0, 100, 0.5);\n"
                                 "background-color:rgba(0, 40, 240, 0.7);\n"
                                 "")
        self.origL.setScaledContents(True)
        self.origL.setAlignment(QtCore.Qt.AlignCenter)
        self.origL.setObjectName("origL")
        self.editL = QtWidgets.QLabel(self.centralwidget)
        self.editL.setGeometry(QtCore.QRect(490, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.editL.setFont(font)
        self.editL.setStyleSheet("color:white;\n"
                                 "border-style: solid;\n"
                                 "border-width: 1px;\n"
                                 "border-color: rgba(100, 0, 100, 0.5);\n"
                                 "background-color:rgba(0, 40, 240, 0.7);\n"
                                 "")
        self.editL.setScaledContents(True)
        self.editL.setAlignment(QtCore.Qt.AlignCenter)
        self.editL.setObjectName("editL")
        self.listCB = QtWidgets.QComboBox(self.centralwidget)
        self.listCB.setGeometry(QtCore.QRect(230, 360, 261, 41))
        self.listCB.setStyleSheet("color:white;\n"
                                  "border-style: solid;\n"
                                  "border-width: 1px;\n"
                                  "border-radius: 10px;\n"
                                  "border-color: rgba(0, 149, 250, 0.5);\n"
                                  "background-color:rgba(0, 40, 240, 0.7);")
        self.listCB.setObjectName("listCB")
        self.listCB.clear()
        self.listCB.addItems(self.list1)
        self.backB = QtWidgets.QPushButton(self.centralwidget)
        self.backB.setGeometry(QtCore.QRect(690, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.backB.setFont(font)
        self.backB.setStyleSheet("color:white;\n"
                                 "border-style: solid;\n"
                                 "border-width: 1px;\n"
                                 "border-radius: 10px;\n"
                                 "border-color: rgba(0, 149, 250, 0.5);\n"
                                 "background-color:rgba(0, 40, 240, 0.7);\n"
                                 "")
        self.backB.setIconSize(QtCore.QSize(35, 35))
        self.backB.setObjectName("backB")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi4(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def begg():
            self.model = "C:/Users/vinay/PycharmProjects/untitled/neural-style-transfer/models/instance_norm/" + str(
                self.listCB.currentText())
            NST.nstpython(NST, filepath4, self.model)

        self.applyB.clicked.connect(begg)
        self.backB.clicked.connect(Ui_MainWindow1.open1)

    def open4(self):
        print("aaaaaa")
        ui = Ui_MainWindow4()
        ui.setupUi44(w)
        w.show()

    def retranslateUi4(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pixihibitor v2.0 - Beautification"))
        self.applyB.setText(_translate("MainWindow", "Apply"))
        self.origL.setText(_translate("MainWindow", "Original"))
        self.editL.setText(_translate("MainWindow", "Edited"))
        self.backB.setText(_translate("MainWindow", "Back"))


"""______________________COLOR SPLASH WINDOW______________________"""
class colorsplash:
    def colorsplashmethod(self,img,n):
        global filepath4
        im=cv2.imread(img)
        im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
        (h,w)=im.shape[:2]
        ratio = w / h
        if h > w:
            h = 500
            w = int(ratio * h)
        elif w > h:
            w = 900
            h = int(w / ratio)
        else:
            w = 500
            h = 500
        im = cv2.resize(im, (w, h), interpolation=cv2.INTER_AREA)
        original_pixels=im.shape
        pixel = im.reshape((h*w,3))
        dominant_color= int(n)
        km= KMeans(n_clusters= dominant_color)
        km.fit(pixel)
        centers = km.cluster_centers_
        centers = np.array(centers, dtype='uint8')
        i = 1
        color = []
        for x in centers:
            i += 1
            color.append(x)

            a = np.zeros((100, 100, 3), dtype='uint8')
            a[:, :, :] = x
        new_pixel= np.zeros(((h*w),3),dtype='uint8')

        color
        km.labels_
        # print(km.labels_)
        for i in range(new_pixel.shape[0]):
            new_pixel[i]=color[km.labels_[i]]
        new_pixel=new_pixel.reshape(original_pixels)
        cv2.imwrite('working.png', cv2.cvtColor(new_pixel, cv2.COLOR_BGR2RGB))
        cv2.waitKey()
        filepath4 = "C:/Users/vinay/PycharmProjects/untitled/working.png"
        Ui_MainWindow5.open5(Ui_MainWindow5)

class Ui_MainWindow5(object):
    root = 0
    # root.withdraw()
    file_path = ""
    def setupUi5(self, MainWindow):
        self.root = tk.Tk()
        self.root.withdraw()
        self.file_path = filedialog.askopenfilename()
        global filepath4
        filepath4 = self.file_path
        global filepath5
        filepath5 = filepath4
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(805, 452)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bglabel = QtWidgets.QLabel(self.centralwidget)
        self.bglabel.setGeometry(QtCore.QRect(0, 0, 805, 452))
        self.bglabel.setText("")
        self.bglabel.setPixmap(QtGui.QPixmap("C:/Users/vinay/PycharmProjects/untitled/pixibg11.jpg"))
        self.bglabel.setScaledContents(True)
        self.bglabel.setObjectName("bglabel")
        self.origPicL = QtWidgets.QLabel(self.centralwidget)
        self.origPicL.setGeometry(QtCore.QRect(120, 80, 231, 231))
        self.origPicL.setText("")
        pixmap = QtGui.QPixmap(filepath5)
        pixmap1 = pixmap.scaled(231, 231, QtCore.Qt.KeepAspectRatio)
        self.origPicL.setPixmap(QtGui.QPixmap(pixmap1))
        self.origPicL.setAlignment(QtCore.Qt.AlignCenter)
        # self.origPicL.setScaledContents(True)
        self.origPicL.setObjectName("origPicL")
        self.editPicL = QtWidgets.QLabel(self.centralwidget)
        self.editPicL.setGeometry(QtCore.QRect(430, 80, 231, 231))
        self.editPicL.setText("")
        # self.editPicL.setScaledContents(True)
        pixmap = QtGui.QPixmap(filepath4)
        pixmap1 = pixmap.scaled(231, 231, QtCore.Qt.KeepAspectRatio)
        self.editPicL.setPixmap(QtGui.QPixmap(pixmap1))
        self.editPicL.setAlignment(QtCore.Qt.AlignCenter)
        self.editPicL.setObjectName("editPicL")
        self.applyB = QtWidgets.QPushButton(self.centralwidget)
        self.applyB.setGeometry(QtCore.QRect(510, 360, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.applyB.setFont(font)
        self.applyB.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 149, 250, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.applyB.setIconSize(QtCore.QSize(35, 35))
        self.applyB.setObjectName("applyB")
        self.origL = QtWidgets.QLabel(self.centralwidget)
        self.origL.setGeometry(QtCore.QRect(180, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.origL.setFont(font)
        self.origL.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(100, 0, 100, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.origL.setScaledContents(True)
        self.origL.setAlignment(QtCore.Qt.AlignCenter)
        self.origL.setObjectName("origL")
        self.editL = QtWidgets.QLabel(self.centralwidget)
        self.editL.setGeometry(QtCore.QRect(490, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.editL.setFont(font)
        self.editL.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(100, 0, 100, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.editL.setScaledContents(True)
        self.editL.setAlignment(QtCore.Qt.AlignCenter)
        self.editL.setObjectName("editL")
        self.listCB = QtWidgets.QComboBox(self.centralwidget)
        self.listCB.setGeometry(QtCore.QRect(230, 360, 261, 41))
        self.listCB.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 149, 250, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);")
        self.listCB.setObjectName("listCB")
        list2=["2","3","4","5","6","7","8","9","10"]
        self.listCB.clear()
        self.listCB.addItems(list2)
        self.backB = QtWidgets.QPushButton(self.centralwidget)
        self.backB.setGeometry(QtCore.QRect(690, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.backB.setFont(font)
        self.backB.setStyleSheet("color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 149, 250, 0.5);\n"
"background-color:rgba(0, 40, 240, 0.7);\n"
"")
        self.backB.setIconSize(QtCore.QSize(35, 35))
        self.backB.setObjectName("backB")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi5(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        def star():
            number=str(self.listCB.currentText())
            colorsplash.colorsplashmethod(colorsplash,filepath4,number)

        self.applyB.clicked.connect(star)
        self.backB.clicked.connect(Ui_MainWindow1.open1)

    def setupUi55(self, MainWindow):
        global filepath4
        global filepath5
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(805, 452)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bglabel = QtWidgets.QLabel(self.centralwidget)
        self.bglabel.setGeometry(QtCore.QRect(0, 0, 805, 452))
        self.bglabel.setText("")
        self.bglabel.setPixmap(QtGui.QPixmap("C:/Users/vinay/PycharmProjects/untitled/pixibg11.jpg"))
        self.bglabel.setScaledContents(True)
        self.bglabel.setObjectName("bglabel")
        self.origPicL = QtWidgets.QLabel(self.centralwidget)
        self.origPicL.setGeometry(QtCore.QRect(120, 80, 231, 231))
        self.origPicL.setText("")
        pixmap = QtGui.QPixmap(filepath5)
        pixmap1 = pixmap.scaled(231, 231, QtCore.Qt.KeepAspectRatio)
        self.origPicL.setPixmap(QtGui.QPixmap(pixmap1))
        self.origPicL.setAlignment(QtCore.Qt.AlignCenter)
        # self.origPicL.setScaledContents(True)
        self.origPicL.setObjectName("origPicL")
        self.editPicL = QtWidgets.QLabel(self.centralwidget)
        self.editPicL.setGeometry(QtCore.QRect(430, 80, 231, 231))
        self.editPicL.setText("")
        pixmap = QtGui.QPixmap(filepath4)
        pixmap1 = pixmap.scaled(231, 231, QtCore.Qt.KeepAspectRatio)
        self.editPicL.setPixmap(QtGui.QPixmap(pixmap1))
        self.editPicL.setAlignment(QtCore.Qt.AlignCenter)
        self.editPicL.setObjectName("editPicL")
        self.applyB = QtWidgets.QPushButton(self.centralwidget)
        self.applyB.setGeometry(QtCore.QRect(510, 360, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.applyB.setFont(font)
        self.applyB.setStyleSheet("color:white;\n"
                                  "border-style: solid;\n"
                                  "border-width: 1px;\n"
                                  "border-radius: 10px;\n"
                                  "border-color: rgba(0, 149, 250, 0.5);\n"
                                  "background-color:rgba(0, 40, 240, 0.7);\n"
                                  "")
        self.applyB.setIconSize(QtCore.QSize(35, 35))
        self.applyB.setObjectName("applyB")
        self.origL = QtWidgets.QLabel(self.centralwidget)
        self.origL.setGeometry(QtCore.QRect(180, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.origL.setFont(font)
        self.origL.setStyleSheet("color:white;\n"
                                 "border-style: solid;\n"
                                 "border-width: 1px;\n"
                                 "border-color: rgba(100, 0, 100, 0.5);\n"
                                 "background-color:rgba(0, 40, 240, 0.7);\n"
                                 "")
        self.origL.setScaledContents(True)
        self.origL.setAlignment(QtCore.Qt.AlignCenter)
        self.origL.setObjectName("origL")
        self.editL = QtWidgets.QLabel(self.centralwidget)
        self.editL.setGeometry(QtCore.QRect(490, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.editL.setFont(font)
        self.editL.setStyleSheet("color:white;\n"
                                 "border-style: solid;\n"
                                 "border-width: 1px;\n"
                                 "border-color: rgba(100, 0, 100, 0.5);\n"
                                 "background-color:rgba(0, 40, 240, 0.7);\n"
                                 "")
        self.editL.setScaledContents(True)
        self.editL.setAlignment(QtCore.Qt.AlignCenter)
        self.editL.setObjectName("editL")
        self.listCB = QtWidgets.QComboBox(self.centralwidget)
        self.listCB.setGeometry(QtCore.QRect(230, 360, 261, 41))
        self.listCB.setStyleSheet("color:white;\n"
                                  "border-style: solid;\n"
                                  "border-width: 1px;\n"
                                  "border-radius: 10px;\n"
                                  "border-color: rgba(0, 149, 250, 0.5);\n"
                                  "background-color:rgba(0, 40, 240, 0.7);")
        self.listCB.setObjectName("listCB")
        list2 = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.listCB.clear()
        self.listCB.addItems(list2)
        self.backB = QtWidgets.QPushButton(self.centralwidget)
        self.backB.setGeometry(QtCore.QRect(690, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.backB.setFont(font)
        self.backB.setStyleSheet("color:white;\n"
                                 "border-style: solid;\n"
                                 "border-width: 1px;\n"
                                 "border-radius: 10px;\n"
                                 "border-color: rgba(0, 149, 250, 0.5);\n"
                                 "background-color:rgba(0, 40, 240, 0.7);\n"
                                 "")
        self.backB.setIconSize(QtCore.QSize(35, 35))
        self.backB.setObjectName("backB")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi5(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def star():
            number = str(self.listCB.currentText())
            colorsplash.colorsplashmethod(colorsplash, filepath4, number)

        self.applyB.clicked.connect(star)
        self.backB.clicked.connect(Ui_MainWindow1.open1)

    def open5(self):
        print("aaaaaa")
        ui = Ui_MainWindow5()
        ui.setupUi55(w)
        w.show()

    def retranslateUi5(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pixihibitor v2.0 - Color Splash"))
        self.applyB.setText(_translate("MainWindow", "Apply"))
        self.origL.setText(_translate("MainWindow", "Original"))
        self.editL.setText(_translate("MainWindow", "Edited"))
        self.backB.setText(_translate("MainWindow", "Back"))


"""______________________ENCRYPTION WINDOW______________________"""
def genData(data):
    newd = []

    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd

def modPix(pix, data):
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)
    for i in range(lendata):

        pix = [value for value in imdata.__next__()[:3] +
               imdata.__next__()[:3] +
               imdata.__next__()[:3]]
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j] % 2 != 0):
                pix[j] -= 1
            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if (pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1
                # pix[j] -= 1
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                if (pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1
        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1
        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]

def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)
    for pixel in modPix(newimg.getdata(), data):
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1

def encode(img, data):
    image = Image.open(img, 'r')
    newimg = image.copy()
    encode_enc(newimg, data)
    newimg.save("working.png")

def decode(img):
    image = Image.open(img, 'r')
    data = ''
    imgdata = iter(image.getdata())
    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                  imgdata.__next__()[:3] +
                  imgdata.__next__()[:3]]
        binstr = ''
        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'
        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            # print(data)
            return data

class Ui_MainWindow7(object):
    def setupUi7(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(805, 452)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bglabel = QtWidgets.QLabel(self.centralwidget)
        self.bglabel.setGeometry(QtCore.QRect(0, 0, 805, 452))
        self.bglabel.setText("")
        self.bglabel.setPixmap(QtGui.QPixmap("C:/Users/vinay/PycharmProjects/untitled/pixibg11.jpg"))
        self.bglabel.setScaledContents(True)
        self.bglabel.setObjectName("bglabel")
        self.brow1B = QtWidgets.QPushButton(self.centralwidget)
        self.brow1B.setGeometry(QtCore.QRect(100, 130, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.brow1B.setFont(font)
        self.brow1B.setStyleSheet("color:white;\n"
                                  "border-style: solid;\n"
                                  "border-width: 1px;\n"
                                  "border-radius: 10px;\n"
                                  "border-color: rgba(0, 149, 250, 0.5);\n"
                                  "background-color:rgba(0, 40, 240, 0.7);\n"
                                  "\n"
                                  "")
        self.brow1B.setIconSize(QtCore.QSize(35, 35))
        self.brow1B.setObjectName("brow1B")
        self.encryB = QtWidgets.QPushButton(self.centralwidget)
        self.encryB.setGeometry(QtCore.QRect(150, 390, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.encryB.setFont(font)
        self.encryB.setStyleSheet("color:white;\n"
                                  "border-style: solid;\n"
                                  "border-width: 1px;\n"
                                  "border-radius: 10px;\n"
                                  "border-color: rgba(0, 149, 250, 0.5);\n"
                                  "background-color:rgba(0, 40, 240, 0.7);\n"
                                  "\n"
                                  "")
        self.encryB.setIconSize(QtCore.QSize(35, 35))
        self.encryB.setObjectName("encryB")
        self.decryB = QtWidgets.QPushButton(self.centralwidget)
        self.decryB.setGeometry(QtCore.QRect(510, 390, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.decryB.setFont(font)
        self.decryB.setStyleSheet("color:white;\n"
                                  "border-style: solid;\n"
                                  "border-width: 1px;\n"
                                  "border-radius: 10px;\n"
                                  "border-color: rgba(0, 149, 250, 0.5);\n"
                                  "background-color:rgba(0, 40, 240, 0.7);\n"
                                  "\n"
                                  "")
        self.decryB.setIconSize(QtCore.QSize(35, 35))
        self.decryB.setObjectName("decryB")
        self.encryL = QtWidgets.QLabel(self.centralwidget)
        self.encryL.setGeometry(QtCore.QRect(100, 40, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.encryL.setFont(font)
        self.encryL.setStyleSheet("color:white;\n"
                                  "border-style: solid;\n"
                                  "border-width: 1px;\n"
                                  "border-color: rgba(100, 0, 100, 0.5);\n"
                                  "background-color:rgba(0, 40, 240, 0.7);\n"
                                  "")
        self.encryL.setScaledContents(True)
        self.encryL.setAlignment(QtCore.Qt.AlignCenter)
        self.encryL.setObjectName("encryL")
        self.decryL = QtWidgets.QLabel(self.centralwidget)
        self.decryL.setGeometry(QtCore.QRect(430, 40, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.decryL.setFont(font)
        self.decryL.setStyleSheet("color:white;\n"
                                  "border-style: solid;\n"
                                  "border-width: 1px;\n"
                                  "border-color: rgba(100, 0, 100, 0.5);\n"
                                  "background-color:rgba(0, 40, 240, 0.7);\n"
                                  "")
        self.decryL.setScaledContents(True)
        self.decryL.setAlignment(QtCore.Qt.AlignCenter)
        self.decryL.setObjectName("decryL")
        self.textLE = QtWidgets.QLineEdit(self.centralwidget)
        self.textLE.setGeometry(QtCore.QRect(100, 310, 241, 41))
        self.textLE.setStyleSheet("border-style: solid;\n"
                                  "border-width: 1px;\n"
                                  "border-radius: 10px;\n"
                                  "border-color: rgba(0, 149, 250, 0.5);\n"
                                  "\n"
                                  "")
        self.textLE.setObjectName("textLE")
        self.backB = QtWidgets.QPushButton(self.centralwidget)
        self.backB.setGeometry(QtCore.QRect(690, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.backB.setFont(font)
        self.backB.setStyleSheet("color:white;\n"
                                 "border-style: solid;\n"
                                 "border-width: 1px;\n"
                                 "border-radius: 10px;\n"
                                 "border-color: rgba(0, 149, 250, 0.5);\n"
                                 "background-color:rgba(0, 40, 240, 0.7);\n"
                                 "\n"
                                 "")
        self.backB.setIconSize(QtCore.QSize(35, 35))
        self.backB.setObjectName("backB")
        self.imag1L = QtWidgets.QLabel(self.centralwidget)
        self.imag1L.setGeometry(QtCore.QRect(100, 180, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.imag1L.setFont(font)
        self.imag1L.setStyleSheet("color:white;\n"
                                  "border-style: solid;\n"
                                  "border-width: 1px;\n"
                                  "border-color: rgba(100, 0, 100, 0.5);\n"
                                  "background-color:rgba(0, 40, 240, 0.7);\n"
                                  "")
        self.imag1L.setScaledContents(True)
        self.imag1L.setAlignment(QtCore.Qt.AlignCenter)
        self.imag1L.setObjectName("imag1L")
        self.textL = QtWidgets.QLabel(self.centralwidget)
        self.textL.setGeometry(QtCore.QRect(100, 260, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.textL.setFont(font)
        self.textL.setStyleSheet("color:white;\n"
                                 "border-style: solid;\n"
                                 "border-width: 1px;\n"
                                 "border-color: rgba(100, 0, 100, 0.5);\n"
                                 "background-color:rgba(0, 40, 240, 0.7);\n"
                                 "")
        self.textL.setScaledContents(True)
        self.textL.setAlignment(QtCore.Qt.AlignCenter)
        self.textL.setObjectName("textL")
        self.brow2B = QtWidgets.QPushButton(self.centralwidget)
        self.brow2B.setGeometry(QtCore.QRect(430, 130, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.brow2B.setFont(font)
        self.brow2B.setStyleSheet("color:white;\n"
                                  "border-style: solid;\n"
                                  "border-width: 1px;\n"
                                  "border-radius: 10px;\n"
                                  "border-color: rgba(0, 149, 250, 0.5);\n"
                                  "background-color:rgba(0, 40, 240, 0.7);\n"
                                  "\n"
                                  "")
        self.brow2B.setIconSize(QtCore.QSize(35, 35))
        self.brow2B.setObjectName("brow2B")
        self.imag2L = QtWidgets.QLabel(self.centralwidget)
        self.imag2L.setGeometry(QtCore.QRect(430, 180, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.imag2L.setFont(font)
        self.imag2L.setStyleSheet("color:white;\n"
                                  "border-style: solid;\n"
                                  "border-width: 1px;\n"
                                  "border-color: rgba(100, 0, 100, 0.5);\n"
                                  "background-color:rgba(0, 40, 240, 0.7);\n"
                                  "")
        self.imag2L.setScaledContents(True)
        self.imag2L.setAlignment(QtCore.Qt.AlignCenter)
        self.imag2L.setObjectName("imag2L")
        self.decrtextL = QtWidgets.QLabel(self.centralwidget)
        self.decrtextL.setGeometry(QtCore.QRect(430, 260, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.decrtextL.setFont(font)
        self.decrtextL.setStyleSheet("color:white;\n"
                                     "border-style: solid;\n"
                                     "border-width: 1px;\n"
                                     "border-color: rgba(100, 0, 100, 0.5);\n"
                                     "background-color:rgba(0, 40, 240, 0.7);\n"
                                     "")
        self.decrtextL.setScaledContents(True)
        self.decrtextL.setAlignment(QtCore.Qt.AlignCenter)
        self.decrtextL.setObjectName("decrtextL")
        self.answerL = QtWidgets.QLabel(self.centralwidget)
        self.answerL.setGeometry(QtCore.QRect(430, 310, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.answerL.setFont(font)
        self.answerL.setStyleSheet("color:white;\n"
                                   "border-style: solid;\n"
                                   "border-width: 1px;\n"
                                   "border-radius: 10px;\n"
                                   "border-color: rgba(0, 149, 250, 0.5);\n"
                                   "background-color:rgba(0, 40, 240, 0.7);")
        self.answerL.setText("")
        self.answerL.setScaledContents(True)
        self.answerL.setAlignment(QtCore.Qt.AlignCenter)
        self.answerL.setObjectName("answerL")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def browimenc():
            global filepath4
            root = tk.Tk()
            root.withdraw()
            filepath4 = filedialog.askopenfilename()
            self.imag1L.setText(filepath4.split("/")[-1])

        def browimdec():
            global filepath5
            root = tk.Tk()
            root.withdraw()
            filepath5 = filedialog.askopenfilename()
            self.imag2L.setText(filepath5.split("/")[-1])

        def decryptoperation():
            global filepath5
            t = decode(filepath5)
            self.answerL.setText(t)

        def encryptoperation():
            global filepath4
            global addtext
            addtext = self.textLE.text()
            encode(filepath4, addtext)

        self.brow1B.clicked.connect(browimenc)
        self.brow2B.clicked.connect(browimdec)
        self.encryB.clicked.connect(encryptoperation)
        self.decryB.clicked.connect(decryptoperation)
        self.backB.clicked.connect(Ui_MainWindow1.open1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pixihibitor v2.0 - Encryption"))
        self.brow1B.setText(_translate("MainWindow", "Browse Image"))
        self.encryB.setText(_translate("MainWindow", "Encrypt"))
        self.decryB.setText(_translate("MainWindow", "Decrypt"))
        self.encryL.setText(_translate("MainWindow", "Encryption"))
        self.decryL.setText(_translate("MainWindow", "Decryption"))
        self.backB.setText(_translate("MainWindow", "Back"))
        self.imag1L.setText(_translate("MainWindow", "No Image Selected"))
        self.textL.setText(_translate("MainWindow", "Add Text"))
        self.brow2B.setText(_translate("MainWindow", "Browse Image"))
        self.imag2L.setText(_translate("MainWindow", "No Image Selected"))
        self.decrtextL.setText(_translate("MainWindow", "Decrypted Text"))

app=QApplication(sys.argv)
w=QMainWindow()
ui=Ui_MainWindow1()
ui.setupUi1(w)
w.show()
sys.exit(app.exec_())
