import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication, Qt

class SelectGraph(object):
        
    def initUI2(self,secondwindow) :
        title = QLabel('Category',self)
        title.setAlignment(Qt.AlignCenter)

        font_t = title.font()                   #폰트 설정
        font_t.setFamily('Times new Roman')
        font_t.setBold(True)
        font_t.setPointSize(14)
        
        title.setFont(font_t)
          
        #카테고리 선택

        self.pushButton = QPushButton("file selection")
        #self.pushButton.clicked.connect(self.pushButtonClicked)
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


        self.show()

        def pushButtonCliked(self):
            self.items = ("상수1", "상수2", "상수3")
            self.item, self.ok = QInputDialog.getItem(self, "파일선택.", "파일을 선택하세요.", items, 0, False)
            if ok and item:
                self.label.setText(item)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    secondwindow = QtWidgets.QMainWindow()
    secondwindow.show()
    sys.exit(app.exec_())


                
