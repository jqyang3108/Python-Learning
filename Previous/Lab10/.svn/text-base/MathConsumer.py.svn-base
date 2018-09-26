import sys
from PySide.QtCore import *
from PySide.QtGui import *
from calculator import *

class MathConsumer(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MathConsumer, self).__init__(parent)
        self.setupUi(self)
        self.btnCalculate.pressed.connect(self.opeartion)

    def opeartion(self):
        op1 = self.edtNumber1.text()
        op2 = self.edtNumber2.text()
        type = self.cboOperation.currentIndex()
        answer = 0

        if (op1 == None or op2 == None):
            answer = "E"
        else:
            try:
                if type == 0:
                    answer = float(op1) + float(op2)
                elif type == 1:
                    answer = float(op1) - float(op2)
                elif type == 2:
                    answer = float(op1) * float(op2)
                elif type == 3:
                    answer = float(op1) / float(op2)
            except:
                answer = "E"

        answer = str(answer)
        self.edtResult.setText(answer)


if __name__ == "__main__":
     currentApp = QApplication(sys.argv)
     currentForm = MathConsumer()

     currentForm.show()
     currentApp.exec_()
