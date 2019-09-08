import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication, Qt

class SelectGraph(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI2()
        
    def initUI2(self) :
        title = QLabel('Category',self)
        title.setAlignment(Qt.AlignCenter)

        font_t = title.font()                   #폰트 설정
        font_t.setFamily('Times new Roman')
        font_t.setBold(True)
        font_t.setPointSize(14)
        
        title.setFont(font_t)
        self.resize(600, 600)   
        self.center()
        #카테고리 선택

        self.pushButton = QPushButton("file selection")
        self.pushButton.clicked.connect(self.pushButtonCliked)
        self.label = QLabel()

        #그래프를 보여줄 지표 선택하기 
        ct1 = QCheckBox('타수',self)
        ct1.move(20, 20)
        ct1.toggle()
        #ct1.stateChanged.connect(self.changeTitle)

        ct2 = QCheckBox('키입력시간',self)
        ct2.move(20,30)
        ct2.toggle()

        ct3 = QCheckBox('오타율',self)
        ct3.move(20,40)
        ct3.toggle()

        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)
        layout.addStretch(1)
        self.setLayout(layout)

    def pushButtonCliked(self):
        items = ("상수1", "상수2", "상수3")
        item, ok = QInputDialog.getItem(self, "파일선택.", "파일을 선택하세요.", items, 0, False)
        if ok and item:
            self.label.setText(item)
    def center(self):               #창 중앙에 띄우기
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())  

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
        second.show()

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
    first = MyApp()
    second = SelectGraph()

    sys.exit(app.exec_())
