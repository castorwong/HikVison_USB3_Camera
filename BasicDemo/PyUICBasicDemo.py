# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyUICBasicDemo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1288, 823)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.ComboDevices = QtWidgets.QComboBox(self.centralWidget)
        self.ComboDevices.setEnabled(True)
        self.ComboDevices.setGeometry(QtCore.QRect(230, 10, 500, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ComboDevices.setFont(font)
        self.ComboDevices.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ComboDevices.setObjectName("ComboDevices")
        self.widgetDisplay = QtWidgets.QWidget(self.centralWidget)
        self.widgetDisplay.setGeometry(QtCore.QRect(9, 70, 901, 701))
        self.widgetDisplay.setStyleSheet("border:1px solid rgba(131, 131, 131,75);")
        self.widgetDisplay.setObjectName("widgetDisplay")
        self.groupInit = QtWidgets.QGroupBox(self.centralWidget)
        self.groupInit.setGeometry(QtCore.QRect(920, 20, 351, 121))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.groupInit.setFont(font)
        self.groupInit.setObjectName("groupInit")
        self.bnClose = QtWidgets.QPushButton(self.groupInit)
        self.bnClose.setEnabled(False)
        self.bnClose.setGeometry(QtCore.QRect(260, 30, 80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bnClose.setFont(font)
        self.bnClose.setStyleSheet("QPushButton{\n"
"    border:1px solid rgb(131, 131, 131);\n"
"    border-radius:20px;\n"
"    background-color:rgba(253, 255, 207,100)\n"
"\n"
"    }\n"
" QPushButton:hover{\n"
"     background-color:rgba(253, 255, 207,200)\n"
"     }\n"
"\n"
" \n"
" QPushButton:pressed{\n"
"     background-color:rgba(135, 212, 135, 55)\n"
"     }\n"
"")
        self.bnClose.setObjectName("bnClose")
        self.bnEnum = QtWidgets.QPushButton(self.groupInit)
        self.bnEnum.setGeometry(QtCore.QRect(10, 30, 80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bnEnum.setFont(font)
        self.bnEnum.setStyleSheet("QPushButton{\n"
"    border:1px solid rgb(131, 131, 131);\n"
"    border-radius:20px;\n"
"    background-color:rgba(253, 255, 207,100)\n"
"\n"
"    }\n"
" QPushButton:hover{\n"
"     background-color:rgba(253, 255, 207,200)\n"
"     }\n"
"\n"
" \n"
" QPushButton:pressed{\n"
"     background-color:rgba(135, 212, 135, 55)\n"
"     }\n"
"")
        self.bnEnum.setObjectName("bnEnum")
        self.bnOpen = QtWidgets.QPushButton(self.groupInit)
        self.bnOpen.setGeometry(QtCore.QRect(135, 30, 80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bnOpen.setFont(font)
        self.bnOpen.setStyleSheet("QPushButton{\n"
"    border:1px solid rgb(131, 131, 131);\n"
"    border-radius:20px;\n"
"    background-color:rgba(253, 255, 207,100)\n"
"\n"
"    }\n"
" QPushButton:hover{\n"
"     background-color:rgba(253, 255, 207,200)\n"
"     }\n"
"\n"
" \n"
" QPushButton:pressed{\n"
"     background-color:rgba(135, 212, 135, 55)\n"
"     }\n"
"")
        self.bnOpen.setObjectName("bnOpen")
        self.groupGrab = QtWidgets.QGroupBox(self.centralWidget)
        self.groupGrab.setEnabled(False)
        self.groupGrab.setGeometry(QtCore.QRect(920, 140, 351, 331))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.groupGrab.setFont(font)
        self.groupGrab.setStyleSheet("background-color:rgba(255, 255, 255,0)")
        self.groupGrab.setObjectName("groupGrab")
        self.bnStart = QtWidgets.QPushButton(self.groupGrab)
        self.bnStart.setEnabled(False)
        self.bnStart.setGeometry(QtCore.QRect(30, 40, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bnStart.setFont(font)
        self.bnStart.setStyleSheet("QPushButton{\n"
"    border:1px solid rgb(131, 131, 131);\n"
"    border-radius:20px;\n"
"    background-color:rgba(180, 255, 185, 55)\n"
"\n"
"    }\n"
" QPushButton:hover{\n"
"     background-color:rgba(180, 255, 185, 200)\n"
"     }\n"
"\n"
" \n"
" QPushButton:pressed{\n"
"     background-color:rgba(228, 119, 255, 55)\n"
"     }\n"
"")
        self.bnStart.setObjectName("bnStart")
        self.radioContinueMode = QtWidgets.QRadioButton(self.groupGrab)
        self.radioContinueMode.setGeometry(QtCore.QRect(210, 10, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioContinueMode.setFont(font)
        self.radioContinueMode.setStyleSheet("background-color:rgba(253, 255, 207,0)\n"
"\n"
"")
        self.radioContinueMode.setObjectName("radioContinueMode")
        self.bnStop = QtWidgets.QPushButton(self.groupGrab)
        self.bnStop.setEnabled(False)
        self.bnStop.setGeometry(QtCore.QRect(200, 40, 120, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bnStop.setFont(font)
        self.bnStop.setStyleSheet("QPushButton{\n"
"    border:1px solid rgb(131, 131, 131);\n"
"    border-radius:20px;\n"
"    background-color:rgba(180, 255, 185, 55)\n"
"\n"
"    }\n"
" QPushButton:hover{\n"
"     background-color:rgba(180, 255, 185, 200)\n"
"     }\n"
"\n"
" \n"
" QPushButton:pressed{\n"
"     background-color:rgba(228, 119, 255, 55)\n"
"     }\n"
"")
        self.bnStop.setObjectName("bnStop")
        self.bnSaveImage = QtWidgets.QPushButton(self.groupGrab)
        self.bnSaveImage.setEnabled(False)
        self.bnSaveImage.setGeometry(QtCore.QRect(30, 120, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bnSaveImage.setFont(font)
        self.bnSaveImage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bnSaveImage.setStyleSheet("QPushButton{\n"
"    border:1px solid rgb(131, 131, 131);\n"
"    border-radius:20px;\n"
"    background-color:rgba(180, 255, 185, 55)\n"
"\n"
"    }\n"
" QPushButton:hover{\n"
"     background-color:rgba(180, 255, 185, 200)\n"
"     }\n"
"\n"
" \n"
" QPushButton:pressed{\n"
"     background-color:rgba(228, 119, 255, 55)\n"
"     }\n"
"")
        self.bnSaveImage.setObjectName("bnSaveImage")
        self.bnSaveImage_2 = QtWidgets.QPushButton(self.groupGrab)
        self.bnSaveImage_2.setEnabled(False)
        self.bnSaveImage_2.setGeometry(QtCore.QRect(200, 120, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bnSaveImage_2.setFont(font)
        self.bnSaveImage_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bnSaveImage_2.setStyleSheet("QPushButton{\n"
"    border:1px solid rgb(131, 131, 131);\n"
"    border-radius:20px;\n"
"    background-color:rgba(180, 255, 185, 55)\n"
"\n"
"    }\n"
" QPushButton:hover{\n"
"     background-color:rgba(180, 255, 185, 200)\n"
"     }\n"
"\n"
" \n"
" QPushButton:pressed{\n"
"     background-color:rgba(228, 119, 255, 55)\n"
"     }\n"
"")
        self.bnSaveImage_2.setObjectName("bnSaveImage_2")
        self.Line_FileName = QtWidgets.QLineEdit(self.groupGrab)
        self.Line_FileName.setGeometry(QtCore.QRect(130, 280, 100, 30))
        self.Line_FileName.setStyleSheet("border:1px solid rgb(0, 0, 0);\n"
"border-radius:5px;")
        self.Line_FileName.setObjectName("Line_FileName")
        self.label = QtWidgets.QLabel(self.groupGrab)
        self.label.setGeometry(QtCore.QRect(130, 260, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.SavePath = QtWidgets.QTextBrowser(self.groupGrab)
        self.SavePath.setGeometry(QtCore.QRect(20, 210, 311, 41))
        self.SavePath.setStyleSheet("border:1px solid rgb(0, 0, 0);\n"
"border-radius:5px;")
        self.SavePath.setObjectName("SavePath")
        self.label_2 = QtWidgets.QLabel(self.groupGrab)
        self.label_2.setGeometry(QtCore.QRect(20, 190, 54, 12))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.bnSavePath = QtWidgets.QPushButton(self.groupGrab)
        self.bnSavePath.setEnabled(False)
        self.bnSavePath.setGeometry(QtCore.QRect(20, 269, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bnSavePath.setFont(font)
        self.bnSavePath.setStyleSheet("QPushButton{\n"
"    border:1px solid rgb(131, 131, 131);\n"
"    border-radius:20px;\n"
"    background-color:rgba(180, 255, 185, 55)\n"
"\n"
"    }\n"
" QPushButton:hover{\n"
"     background-color:rgba(180, 255, 185, 200)\n"
"     }\n"
"\n"
" \n"
" QPushButton:pressed{\n"
"     background-color:rgba(228, 119, 255, 55)\n"
"     }\n"
"")
        self.bnSavePath.setObjectName("bnSavePath")
        self.bnSavePathClear = QtWidgets.QPushButton(self.groupGrab)
        self.bnSavePathClear.setEnabled(False)
        self.bnSavePathClear.setGeometry(QtCore.QRect(259, 270, 61, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bnSavePathClear.setFont(font)
        self.bnSavePathClear.setStyleSheet("QPushButton{\n"
"    border:1px solid rgb(131, 131, 131);\n"
"    border-radius:20px;\n"
"    background-color:rgba(180, 255, 185, 55)\n"
"\n"
"    }\n"
" QPushButton:hover{\n"
"     background-color:rgba(180, 255, 185, 200)\n"
"     }\n"
"\n"
" \n"
" QPushButton:pressed{\n"
"     background-color:rgba(228, 119, 255, 55)\n"
"     }\n"
"")
        self.bnSavePathClear.setObjectName("bnSavePathClear")
        self.groupParam = QtWidgets.QGroupBox(self.centralWidget)
        self.groupParam.setEnabled(False)
        self.groupParam.setGeometry(QtCore.QRect(920, 480, 351, 141))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.groupParam.setFont(font)
        self.groupParam.setObjectName("groupParam")
        self.label_5 = QtWidgets.QLabel(self.groupParam)
        self.label_5.setGeometry(QtCore.QRect(0, 90, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.edtGain = QtWidgets.QLineEdit(self.groupParam)
        self.edtGain.setGeometry(QtCore.QRect(70, 100, 71, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.edtGain.setFont(font)
        self.edtGain.setObjectName("edtGain")
        self.label_6 = QtWidgets.QLabel(self.groupParam)
        self.label_6.setGeometry(QtCore.QRect(190, 0, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.edtFrameRate = QtWidgets.QLineEdit(self.groupParam)
        self.edtFrameRate.setGeometry(QtCore.QRect(250, 10, 70, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.edtFrameRate.setFont(font)
        self.edtFrameRate.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-radius:5px;")
        self.edtFrameRate.setObjectName("edtFrameRate")
        self.label_4 = QtWidgets.QLabel(self.groupParam)
        self.label_4.setGeometry(QtCore.QRect(0, 40, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.edtExposureTime = QtWidgets.QLineEdit(self.groupParam)
        self.edtExposureTime.setGeometry(QtCore.QRect(70, 50, 71, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.edtExposureTime.setFont(font)
        self.edtExposureTime.setObjectName("edtExposureTime")
        self.bnSetParam = QtWidgets.QPushButton(self.groupParam)
        self.bnSetParam.setGeometry(QtCore.QRect(260, 50, 80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bnSetParam.setFont(font)
        self.bnSetParam.setStyleSheet("QPushButton{\n"
"    border:1px solid rgb(131, 131, 131);\n"
"    border-radius:20px;\n"
"    background-color:rgba(255, 168, 105, 55)\n"
"\n"
"    }\n"
" QPushButton:hover{\n"
"     background-color:rgba(255, 168, 105, 200)\n"
"     }\n"
"\n"
" \n"
" QPushButton:pressed{\n"
"     background-color:rgba(228, 119, 255, 55)\n"
"     }\n"
"")
        self.bnSetParam.setObjectName("bnSetParam")
        self.label_7 = QtWidgets.QLabel(self.groupParam)
        self.label_7.setGeometry(QtCore.QRect(150, 40, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupParam)
        self.label_8.setGeometry(QtCore.QRect(150, 90, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupParam)
        self.label_9.setGeometry(QtCore.QRect(320, 0, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.groupParam)
        self.label_11.setGeometry(QtCore.QRect(270, 10, 61, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-radius:5px;")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.ImageCounter = QtWidgets.QTextBrowser(self.centralWidget)
        self.ImageCounter.setGeometry(QtCore.QRect(760, 15, 150, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ImageCounter.setFont(font)
        self.ImageCounter.setObjectName("ImageCounter")
        self.groupLight = QtWidgets.QGroupBox(self.centralWidget)
        self.groupLight.setEnabled(False)
        self.groupLight.setGeometry(QtCore.QRect(920, 630, 351, 141))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.groupLight.setFont(font)
        self.groupLight.setObjectName("groupLight")
        self.bnSetLightOff = QtWidgets.QPushButton(self.groupLight)
        self.bnSetLightOff.setGeometry(QtCore.QRect(20, 30, 70, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bnSetLightOff.setFont(font)
        self.bnSetLightOff.setStyleSheet("QPushButton{\n"
"    border:1px solid rgb(131, 131, 131);\n"
"    border-radius:20px;\n"
"    background-color:rgba(139, 129, 255, 55)\n"
"\n"
"    }\n"
" QPushButton:hover{\n"
"     background-color:rgba(139, 129, 255, 200)\n"
"     }\n"
"\n"
" \n"
" QPushButton:pressed{\n"
"     background-color:rgba(228, 119, 255, 55)\n"
"     }\n"
"")
        self.bnSetLightOff.setObjectName("bnSetLightOff")
        self.bnSetLightHalf = QtWidgets.QPushButton(self.groupLight)
        self.bnSetLightHalf.setGeometry(QtCore.QRect(140, 30, 70, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bnSetLightHalf.setFont(font)
        self.bnSetLightHalf.setStyleSheet("QPushButton{\n"
"    border:1px solid rgb(131, 131, 131);\n"
"    border-radius:20px;\n"
"    background-color:rgba(139, 129, 255, 55)\n"
"\n"
"    }\n"
" QPushButton:hover{\n"
"     background-color:rgba(139, 129, 255, 200)\n"
"     }\n"
"\n"
" \n"
" QPushButton:pressed{\n"
"     background-color:rgba(228, 119, 255, 55)\n"
"     }\n"
"")
        self.bnSetLightHalf.setObjectName("bnSetLightHalf")
        self.bnSetLightFull = QtWidgets.QPushButton(self.groupLight)
        self.bnSetLightFull.setGeometry(QtCore.QRect(260, 30, 70, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bnSetLightFull.setFont(font)
        self.bnSetLightFull.setStyleSheet("QPushButton{\n"
"    border:1px solid rgb(131, 131, 131);\n"
"    border-radius:20px;\n"
"    background-color:rgba(139, 129, 255, 55)\n"
"\n"
"    }\n"
" QPushButton:hover{\n"
"     background-color:rgba(139, 129, 255, 200)\n"
"     }\n"
"\n"
" \n"
" QPushButton:pressed{\n"
"     background-color:rgba(228, 119, 255, 55)\n"
"     }\n"
"")
        self.bnSetLightFull.setObjectName("bnSetLightFull")
        self.progressBarLight = QtWidgets.QProgressBar(self.groupLight)
        self.progressBarLight.setGeometry(QtCore.QRect(20, 100, 321, 23))
        self.progressBarLight.setProperty("value", 24)
        self.progressBarLight.setObjectName("progressBarLight")
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupInit.setTitle(_translate("MainWindow", "查找、打开相机"))
        self.bnClose.setText(_translate("MainWindow", "关闭设备"))
        self.bnEnum.setText(_translate("MainWindow", "查找设备"))
        self.bnOpen.setText(_translate("MainWindow", "打开设备"))
        self.groupGrab.setTitle(_translate("MainWindow", "采集、保存"))
        self.bnStart.setText(_translate("MainWindow", "开始采集"))
        self.radioContinueMode.setText(_translate("MainWindow", "连续采集模式"))
        self.bnStop.setText(_translate("MainWindow", "停止采集"))
        self.bnSaveImage.setText(_translate("MainWindow", "存为bmp格式\n"
"(无损)"))
        self.bnSaveImage_2.setText(_translate("MainWindow", "存为jpg格式\n"
"(有压缩)"))
        self.label.setText(_translate("MainWindow", "当前文件名"))
        self.label_2.setText(_translate("MainWindow", "输出路径"))
        self.bnSavePath.setText(_translate("MainWindow", "选路径"))
        self.bnSavePathClear.setText(_translate("MainWindow", "归0"))
        self.groupParam.setTitle(_translate("MainWindow", "相机参数控制"))
        self.label_5.setText(_translate("MainWindow", "手动增益"))
        self.edtGain.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "实际帧率"))
        self.edtFrameRate.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "曝光时间"))
        self.edtExposureTime.setText(_translate("MainWindow", "0"))
        self.bnSetParam.setText(_translate("MainWindow", "设  定\n"
"\n"
"参  数"))
        self.label_7.setText(_translate("MainWindow", "μs  (4-830k)"))
        self.label_8.setText(_translate("MainWindow", "dB  (0.0-23.98)"))
        self.label_9.setText(_translate("MainWindow", "fps"))
        self.groupLight.setTitle(_translate("MainWindow", "照明灯光控制"))
        self.bnSetLightOff.setText(_translate("MainWindow", "关闭"))
        self.bnSetLightHalf.setText(_translate("MainWindow", "半亮"))
        self.bnSetLightFull.setText(_translate("MainWindow", "全亮"))