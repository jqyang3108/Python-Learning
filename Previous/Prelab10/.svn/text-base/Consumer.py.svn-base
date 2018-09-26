import sys

from PySide.QtGui import *
from BasicUI import *

import re

class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)
        #define the component name and count

        self.nameList = [self.txtComponentName_1, self.txtComponentName_2, self.txtComponentName_3, self.txtComponentName_4, self.txtComponentName_5, self.txtComponentName_6, self.txtComponentName_7, self.txtComponentName_8, self.txtComponentName_9, self.txtComponentName_10,self.txtComponentName_11, self.txtComponentName_12, self.txtComponentName_13, self.txtComponentName_14, self.txtComponentName_15, self.txtComponentName_16, self.txtComponentName_17, self.txtComponentName_18, self.txtComponentName_19, self.txtComponentName_20]
        self.countList = [self.txtComponentCount_1, self.txtComponentCount_2, self.txtComponentCount_3, self.txtComponentCount_4, self.txtComponentCount_5, self.txtComponentCount_6, self.txtComponentCount_7, self.txtComponentCount_8, self.txtComponentCount_9, self.txtComponentCount_10,self.txtComponentCount_11, self.txtComponentCount_12, self.txtComponentCount_13, self.txtComponentCount_14, self.txtComponentCount_15, self.txtComponentCount_16, self.txtComponentCount_17, self.txtComponentCount_18, self.txtComponentCount_19, self.txtComponentCount_20]

        #------------------------------------define----------------------------------
        self.clear()
        #clear button
        self.btnClear.pressed.connect(self.clear)

        #enable save / disable load
        self.txtStudentName.textEdited.connect(self.enableSave)
        self.txtStudentID.textEdited.connect(self.enableSave)
        self.chkGraduate.stateChanged.connect(self.enableSave)
        self.cboCollege.currentIndexChanged.connect(self.enableSave)

        for i in self.nameList:
            i.textEdited.connect(self.enableSave)
        for i in self.countList:
            i.textEdited.connect(self.enableSave)


        #save button
        self.btnSave.clicked.connect(self.saveToFile)

        #load button
        self.btnLoad.clicked.connect(self.loadData)

    def clear(self):
        self.txtStudentName.setText("")
        self.txtStudentID.setText("")
        self.chkGraduate.setChecked(False)
        self.cboCollege.setCurrentIndex(0)

        i = 0
        while (i<len(self.nameList)):
            self.nameList[i].setText("")
            self.countList[i].setText("")
            i+=1

        self.btnLoad.setEnabled(True)
        self.btnSave.setEnabled(False)

    def enableSave(self):
        self.btnLoad.setEnabled(False)
        self.btnSave.setEnabled(True)

    def saveToFile(self):
        fileName = "target"
        fileType = ".xml"
        with open(fileName+fileType, "w") as myFile:
            myFile.writelines('<?xml version="1.0" encoding="UTF-8"?>\n')
            myFile.writelines('<Content>\n')
            myFile.writelines('    <StudentName graduate="{0}">{1}</StudentName>\n'.format(str(self.chkGraduate.isChecked()).lower(),self.txtStudentName.text()))

            myFile.writelines('    <StudentID>{0}</StudentID>\n'.format(self.txtStudentID.text()))
            myFile.writelines('    <College>{0}</College>\n'.format(self.cboCollege.currentText()))
            myFile.writelines('    <Components>\n')
            i = 0
            while(i<len(self.nameList)):
                if(self.nameList[i].text() != "" and self.countList[i].text() != ""):
                    myFile.writelines('        <Component name=\"{}\" count=\"{}\" />\n'.format(self.nameList[i].text(), self.countList[i].text()))
                i+=1

            myFile.writelines('    </Components>\n')
            myFile.writelines('</Content>')
    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.
        *** YOU MUST USE THIS METHOD TO LOAD DATA FILES. ***


        *** This method is required for unit tests! ***
        """
        print("load")
        with open(filePath, "r") as myFile:
            list = myFile.readlines()[2:-2]
        i = 0
        nameList = []
        countList = []
        major = ["-----", "Aerospace Engineering", "Civil Engineering", "Computer Engineering","Electrical Engineering", "Industrial Engineering", "Mechanical Engineering"]
        count = 0
        while(i < len(list)):
            if(i==0):
                read = re.search("\<StudentName graduate=\"(true|false)\"\>(.+?)\</StudentName\>$", list[i])
                gradChk = read.group(1)
                name = read.group(2)
                self.txtStudentName.setText(name)
                if(gradChk=="true"):
                    self.chkGraduate.setChecked(True)
                else:
                    self.chkGraduate.setChecked(False)
            elif(i==1):
                read = re.search("\<StudentID\>(.+?)\</StudentID\>$", list[i])
                id = read.group(1)
                self.txtStudentID.setText(id)
            elif(i==2):
                read = re.search("\<College\>(.+?)\</College\>$", list[i])
                college = read.group(1)
                col = major.index(college)
                self.cboCollege.setCurrentIndex(col)
            elif(i==3):
                i+=1
                continue
            elif(i>3 and i<len(list)):
                read = re.search("\<Component name=\"(.+?)\" count=\"(.+?)\" /\>", list[i])
                name = read.group(1)
                count = read.group(2)
                nameList.append(name)
                countList.append(count)
            else:
                i+=1
                continue
            i+=1
        i=0
        while(i<len(nameList)):
            nameBlank = self.nameList[i]
            nameBlank.setText(nameList[i])
            i+=1
        i=0
        while(i<len(countList)):
            countBlank = self.countList[i]
            countBlank.setText(countList[i])
            i+=1
    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)
        self.enableSave()
if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
