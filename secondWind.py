import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication, Qt
import random
import numpy as np

def analyzeKeystrokeData(filepath):
	lines = None;
	with open(filepath,"r",encoding="utf-8") as f:
		lines = f.readlines();
	ret = np.random.rand(5)
	return ret

class SelectGraph(object):
        
    def __init__(self):
            
        self.app = QtWidgets.QApplication(sys.argv)
        self.initUI2(MainWindow)
        
    def initUI2(self, MainWindow) :


        self.stylesheet = """
        QPushButton{
                background-color: #4e4e4e;
                color: #ffffff;
        }

        QMainWindow{
                background-color: #ff9900;
        }

        QTextEdit{
                background-color: #ffffff;
        }
        """
        self.app.setStyleSheet(self.stylesheet)
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 350, 121, 111))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(self.FirstButtonClicked)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 350, 121, 111))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.scdButtonClicked)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 350, 121, 111))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.trdButtonClicked)
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(490, 350, 121, 111))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.frtButtonClicked)
        
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(640, 350, 121, 111))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.fthButtonClicked)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(120, 90, 551, 191))
        font = QtGui.QFont()
        font.setPointSize(36)
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

    def retranslateUi(self, MainWindow):
        percent = '59'
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "알콜분석기"))
        self.pushButton.setText(_translate("MainWindow", "타자"))
        self.pushButton_2.setText(_translate("MainWindow", "오타율"))
        self.pushButton_3.setText(_translate("MainWindow", "웅앵"))
        self.pushButton_4.setText(_translate("MainWindow", "어쩌구"))
        self.pushButton_5.setText(_translate("MainWindow", "저쩌구"))
        self.label.setText(_translate("MainWindow", "당신의 Alcohol 농도는 " + percent +" % 입니다 !!!!"))
        self.menu.setTitle(_translate("MainWindow", "알콜분석"))

    def FirstButtonClicked(self):
        print('hello')
        
    def scdButtonClicked(self):
        QMessageBox.about(self, "message", "clicked")
        
    def trdButtonClicked(self):
        QMessageBox.about(self, "message", "clicked")
        
    def frtButtonClicked(self):
        QMessageBox.about(self, "message", "clicked")
        
    def fthButtonClicked(self):
        QMessageBox.about(self, "message", "clicked")
        

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self): 

        title = QLabel('Data Analysis', self)   #화면 Title
        title.setAlignment(Qt.AlignCenter)     

        font_t = title.font()                   #폰트 설정
        font_t.setFamily('Times new Roman')
        font_t.setBold(True)
        font_t.setPointSize(14)
        
        title.setFont(font_t)

        text = QTextBrowser(self)
        text.setText( "예시 문장 화면입니다.")


        self.resize(600, 600)   
        self.center()               #창을 모니터 화면 정중앙으로

        openFile = QAction(self)            
        openFile.triggered.connect(self.showDialog)

      
        btn1 = QPushButton('파일선택', self)        #Qdialog 이용하여 파일 선택
        btn1.setCheckable(True)
        btn1.clicked.connect(self.showDialog)

        uploadButton = QPushButton('등록')          #등록 버튼
        cancelButton = QPushButton('취소')          #취소 버튼
        uploadButton.clicked.connect(self.Second)

        hbox = QHBoxLayout()                        #수평 박스
        hbox.addStretch(1)
        hbox.addWidget(uploadButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)

        vbox = QVBoxLayout()                        #수직 박스 
        vbox.addWidget(title)
        vbox.addStretch(1.3)
        vbox.addWidget(text)
        vbox.addStretch(0.7)
        vbox.addWidget(btn1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        
        self.setLayout(vbox)
        self.show()
        
    def Second(self):
        MainWindow.show()

    def center(self):               #창 중앙에 띄우기
    
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())     
    


    def showDialog(self):       # 파일 선택 함수 
    
        fname = QFileDialog.getOpenFileName(self, '파일 선택', './')
'''
        if fname[0]:                    #불러온 파일 내용을 텍스트 박스에 띄우기
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)
'''


if __name__ == '__main__':

    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    first = MyApp()
    second = SelectGraph()
    second.initUI2(MainWindow)
    sys.exit(app.exec_())
