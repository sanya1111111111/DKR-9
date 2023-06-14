from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem

globBase = []

def addRec():
    num = window.num_E.text()
    name = window.Name_E.text()
    dist = window.dist_E.text()
    size = window.size_E.text()
    sputniks = window.Sput_E.text()

    if '№' in (num+name+dist+size+sputniks): return  True
    try:
        with open("base.txt", "r") as base:
            base1 = base.readlines()
            for line in base1:
                if line.split("№")[0] == num: return True

        with open("base.txt","a") as base:
            base.write(num + "№"+ name + "№" + dist + "№" + size + "№" + sputniks + "\n")

        with open("base.txt", "r") as base:
            globBase = []
            for line in base.readlines():
                globBase.append(line.strip().split("№"))

        window.Display()

    except IOError:
        return True

def RemRec():
    num = window.Num_E.text()

    base2 = []
    try:
        with open("base.txt", "r") as base:
            base1 = base.readlines()
            for line in base1:
                if line.split("№")[0] != num:
                    base2.append(line)
        with open("base.txt", "w") as base:
            base.writelines(base2)

        with open("base.txt", "r") as base:
            globBase = []
            for line in base.readlines():
                globBase.append(line.strip().split("№"))

        window.Display()

    except IOError:
        return True

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('lab9.ui', self)
        self.Add_B.clicked.connect(addRec)
        self.rem_B.clicked.connect(RemRec)

        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setText("Error")
        self.msg.setWindowTitle("Error")

        self.Display()

    def Add(self):
        if addRec():
            self.msg.exec_()
        else:
            self.Display()

    def Remove(self):
        if RemRec():
            self.msg.exec_()
        else:
            self.Display()

    def Display(self):
        with open("base.txt", "r") as base:
            globBase = []
            for line in base.readlines():
                globBase.append(line.strip().split("№"))

        self.tableWidget.setRowCount(len(globBase))
        self.tableWidget.setColumnCount(5)

        for i, row in enumerate(globBase):
            for j, col in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(col))

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())