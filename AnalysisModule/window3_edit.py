import sys
from PyQt5.QtWidgets import QMessageBox, QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QTextEdit, QAction, QFileDialog, QDesktopWidget, QHBoxLayout, QTextBrowser, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt
import random

import KeyboardDynamicsAnalytics as KDA

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
from matplotlib.widgets import TextBox, Button

fpath = ""
analysisResult = None

class SelectGraph(object):
      
    def initUI2(self, MainWindow) :
                
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 350, 150, 70))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(self.FirstButtonClicked)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 350, 150, 70))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.scdButtonClicked)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 350, 150, 70))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.trdButtonClicked)
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(610, 350, 150, 70))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.frtButtonClicked)

        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(630, 480, 100, 50 ))
        self.backButton.setObjectName("Back")
        #self.backButton.clicked.connect(self.PrevWindow)
        #self.dialog = MyApp(show)
        
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(120, 90, 551, 191))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
 
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

    def retranslateUi(self, MainWindow):
        global fpath
        global analysisResult
        analysisResult = KDA.analyzeKeystrokeData(fpath)
        percent = str((analysisResult[0] + analysisResult[1])/2)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Keystroke Dynamics Analytics"))
        self.pushButton.setText(_translate("MainWindow", "Press-Press Time"))
        self.pushButton_2.setText(_translate("MainWindow", "Press-Release Time"))
        self.pushButton_3.setText(_translate("MainWindow", "Backspace"))
        self.pushButton_4.setText(_translate("MainWindow", "Typo"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "당신의 예상 혈중 알코올 농도는 <br>" + percent +"% 입니다 !!!!"))
        self.menu.setTitle(_translate("MainWindow", "Keystroke Dynamics Analytics"))

    def FirstButtonClicked(self):
        self.next = FirstGraph()
        
    def scdButtonClicked(self):
        self.next = FirstGraph()
        
    def trdButtonClicked(self):
        self.next = FirstGraph()
        
    def frtButtonClicked(self):
        self.next = FirstGraph()



class MyApp(object):


    def initUI(self, MainWindow):
        self.app = QtWidgets.QApplication(sys.argv)
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setGeometry(QtCore.QRect(200, 40, 411, 41))
        self.title.setObjectName("title")
        
        self.text = QtWidgets.QTextBrowser(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(150, 130, 511, 181))
        self.text.setObjectName("text")
        
        self.text_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(160, 331, 491, 31))
        self.text_2.setObjectName("text_2")

        self.openFile = QtWidgets.QAction(self.centralwidget)            
        #self.openFile.triggered.connect(self.showDialog)
        
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(300, 385, 211, 31))
        self.btn1.setObjectName("btn1")
        #self.btn1.clicked.connect(executeFile.showDialog)
        
        self.uploadButton = QtWidgets.QPushButton(self.centralwidget)
        self.uploadButton.setGeometry(QtCore.QRect(310, 430, 87, 31))
        self.uploadButton.setObjectName("uploadButton")
        #self.uploadButton.clicked.connect(self.Second)
        
        
        self.cancelButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton_2.setGeometry(QtCore.QRect(410, 430, 86, 31))
        self.cancelButton_2.setObjectName("cancelButton_2")
        self.cancelButton_2.clicked.connect(self.cancelMethod)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 589, 18))
        self.menubar.setObjectName("menubar")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.app.setStyleSheet("QWidget {background-color: #323232 }")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times new Roman\'; font-size:14pt; font-weight:400; font-style:normal; font-bold:Ture\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> Keystroke Dynamic Analysis</p></body></html>"))
        self.text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times new Roman\'; font-size:10pt; font-weight:400; font-style:normal; font-bold:Ture\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> * Keystroke Dynamics Analysis * </p><br><p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">혈중 알코올 농도에 따른 타자 패턴 분석 도구입니다.</p><p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">배부된 타자 연습 입력 결과 로그를 제출해주세요.</p><br><br><p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- 부산대학교 2019년도 전기 졸업과제 10조</p></body></html>"))
        self.text_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">파일 경로</p></body></html>"))
        self.btn1.setText(_translate("MainWindow", "파일 선택"))
        self.uploadButton.setText(_translate("MainWindow", "등록"))
        self.cancelButton_2.setText(_translate("MainWindow", "취소"))

    def cancelMethod(self):
        QMessageBox.question(self, "message", "취소하시겠습니까?", QMessageBox.Yes,  QMessageBox.Cancel)
        #if buttonReplay == QMessageBox.Yes:
            
        #if buttonReplay == QMessageBox.Cancel:
                   
    def Second(self):
        MainWindow.show()

class FirstGraph(QMainWindow):
    def __init__(self):
            
        #self.app = QtWidgets.QApplication(sys.argv)
        self.initGr1()
        
    def initGr1(self) :
        fig, ax = plt.subplots()            #그래프 
        plt.subplots_adjust(bottom=0.35)
        global analysisResult
        initial_text = "Your PTP is " + ("%.3f" % analysisResult[2]) + "ms, estimated to 0.104 Alcohol-in-blood percentage."

        a = np.arange(0, 600, 50)        #범위

        x = [analysisResult[2]]                       #반환 값 
        y = [analysisResult[0]]

        font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/NanumGothic.ttf").get_name()
        rc('font', family=font_name)


        fig.suptitle("타자 속도", fontsize = 16, fontweight='bold')     #타이틀제목
        plt.xlabel("x")    #x축 라벨
        plt.ylabel("y")    #y축 라벨

        plt.xticks(fontsize = 12, color = '#FF8000')          #눈금 색, 폰트크기
        plt.yticks(fontsize = 12, color = '#FF8000')

        plt.scatter(x, y, c = 'b', s = 150, marker="*", label = 'dot')   #점 그래프
        plt.plot([0,534.541],[0.170274,0], color='#FF8000', linewidth=2, label = 'line graph')   #선 그래프 
        plt.grid(b=True, which ='major', axis='x')      #그리드 그리기


        #박스 설정
        box = {
            'facecolor' : '.85',
            'edgecolor' : 'r',
            'boxstyle'  : 'round'
        }


        plt.text(1.05, 0.8, 'Your PTP: ' + ("%.3f" % analysisResult[2]) + "ms", bbox = box)

        #텍스트 박스 
        axbox = plt.axes([0.1, 0.16, 0.8, 0.09])
        text_box = TextBox(axbox, '', initial=initial_text)


        ''' 화살표 표시(error)
        plt.plot([1.0], [1.0])
        plt.annotate('Your PTP : 343.22ms' xy=(1.0, 1.0), xytext=(0.7, 0.8),
                    arrowprops=dict(facecolor='black', shrink=0.01),
                    )
        '''

        #callback = Prev()
        #axprev = plt.axes([0.80, 0.05, 0.1, 0.075])
        #bprev = Button(axprev, 'Previous')
        #bprev.on_clicked(callback.prev)

        #plt.legend()

        plt.show()

   
class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
        self.myApp = MyApp()
        self.second = SelectGraph()
        #self.secondWindow()
        self.startUI()
        self.app = QtWidgets.QApplication(sys.argv)
        self.stylesheet = """
                
        QWidget
        {
            color: #b1b1b1;
            background-color: #323232;
        }
        QWidget:item:hover
        {
            background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);
            color: #000000;
        }
        QWidget:item:selected
        {
            background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
        }
        
        QWidget:disabled
        {
            color: #404040;
            background-color: #323232;
        }
        QAbstractItemView
        {
            background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);
        }
        QWidget:focus
        {
            /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/
        }
        QLineEdit
        {
            background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);
            padding: 1px;
            border-style: solid;
            border: 1px solid #1e1e1e;
            border-radius: 5;
        }
        QPushButton
        {
            color: #b1b1b1;
            background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);
            border-width: 1px;
            border-color: #1e1e1e;
            border-style: solid;
            border-radius: 6;
            padding: 3px;
            font-size: 12px;
            padding-left: 5px;
            padding-right: 5px;
        }
        QPushButton:pressed
        {
            background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);
        }
        QComboBox
        {
            selection-background-color: #ffaa00;
            background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);
            border-style: solid;
            border: 1px solid #1e1e1e;
            border-radius: 5;
        }
        QComboBox:hover,QPushButton:hover
        {
            border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
        }
        QComboBox:on
        {
            padding-top: 3px;
            padding-left: 4px;
            background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);
            selection-background-color: #ffaa00;
        }
        QComboBox QAbstractItemView
        {
            border: 2px solid darkgray;
            selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
        }
        QComboBox::drop-down
        {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 15px;
            border-left-width: 0px;
            border-left-color: darkgray;
            border-left-style: solid; /* just a single line */
            border-top-right-radius: 3px; /* same radius as the QComboBox */
            border-bottom-right-radius: 3px;
        }
        QComboBox::down-arrow
        {
            image: url(:/down_arrow.png);
        }
        
        QTextEdit:focus
        {
            border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
        }
        QScrollBar:horizontal {
            border: 1px solid #222222;
            background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);
            height: 7px;
            margin: 0px 16px 0 16px;
        }
        QScrollBar::handle:horizontal
        {
            background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);
            min-height: 20px;
            border-radius: 2px;
        }
        QScrollBar::add-line:horizontal {
            border: 1px solid #1b1b19;
            border-radius: 2px;
            background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);
            width: 14px;
            subcontrol-position: right;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:horizontal {
            border: 1px solid #1b1b19;
            border-radius: 2px;
            background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);
            width: 14px;
            subcontrol-position: left;
            subcontrol-origin: margin;
        }
        QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal
        {
            border: 1px solid black;
            width: 1px;
            height: 1px;
            background: white;
        }
        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
        {
            background: none;
        }
        QScrollBar:vertical
        {
            background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);
            width: 7px;
            margin: 16px 0 16px 0;
            border: 1px solid #222222;
        }
        QScrollBar::handle:vertical
        {
            background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);
            min-height: 20px;
            border-radius: 2px;
        }
        QScrollBar::add-line:vertical
        {
            border: 1px solid #1b1b19;
            border-radius: 2px;
            background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
            height: 14px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:vertical
        {
            border: 1px solid #1b1b19;
            border-radius: 2px;
            background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);
            height: 14px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
        QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
        {
            border: 1px solid black;
            width: 1px;
            height: 1px;
            background: white;
        }
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
        {
            background: none;
        }
        QTextEdit
        {
            background-color: #242424;
        }
        QPlainTextEdit
        {
            background-color: #242424;
        }
        
                """
        self.app.setStyleSheet(self.stylesheet)


    def secondWindow(self) :
        
        self.second.initUI2(self)
        self.second.backButton.clicked.connect(self.PrevUI)
        self.show()
        
    def startUI(self):
        self.myApp.initUI(self)
        self.myApp.uploadButton.clicked.connect(self.secondWindow)
        self.myApp.btn1.clicked.connect(self.showDialog)
        self.show()
        
    def showDialog(self):       # 파일 선택 함수
        fname = QFileDialog.getOpenFileName(self, '파일 선택', './')
        global fpath
        fpath = fname[0]
        self.myApp.text_2.setText(fname[0])

    def PrevUI(self):
        self.myApp.initUI(self)
        self.show()

        
if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = MainWindow()
    app.exec_()
    sys.exit(app.exec_())
