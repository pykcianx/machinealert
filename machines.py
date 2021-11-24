import sys, res
from PyQt5 import QtCore, QtGui, QtWidgets
from testform import Ui_MainWindow
from registry import Ui_Form2
import pandas as pd
import sqlite3
import time
import threading
conn = sqlite3.connect('machinealert.db')



class move(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super(move, self).__init__(parent)
        self.parent=parent
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragpos = event.globalPos() - self.parent.frameGeometry().topLeft()
            event.accept()
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.parent.move(event.globalPos() - self.dragpos)
            event.accept()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 600)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.dbconn()
        self.widget = move(Form)
        self.widget.setGeometry(QtCore.QRect(40, 20, 370, 560))
        self.widget.setStyleSheet("QPushButton#logbtn{\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 0, 0, 138), stop:1 rgba(0, 0, 0, 138));\n"
        "    color:rgba(0, 136, 255, 215);\n"
        "    border-radius:5px;\n"
        "}\n"
        "QPushButton#logbtn:hover{\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 87, 128, 1), stop:1 rgba(0, 87, 128, 1));\n"
        "}\n"
        "QPushButton#logbtn:pressed{\n"
        "    padding-left:5px;\n"
        "    padding-top:5px;\n"
        "    background-color:rgba(0, 125, 186, 1);\n"
        "}\n"
        "\n"
        "\n"
        "\n"
        "QPushButton#regbtn{\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 0, 0, 138), stop:1 rgba(0, 0, 0, 138));\n"
        "    color:rgba(0, 136, 255, 215);\n"
        "    border-radius:8px;\n"
        "}\n"
        "QPushButton#regbtn:hover{\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 87, 128, 1), stop:1 rgba(0, 87, 128, 1));\n"
        "}\n"
        "QPushButton#regbtn:pressed{\n"
        "    padding-left:5px;\n"
        "    padding-top:5px;\n"
        "    background-color:rgba(0, 125, 186, 1);\n"
        "}\n"
        "\n"
        "\n"
        "QPushButton#recoverybtn{\n"
        "color:rgba(255, 255, 255, 104);\n"
        "    border-radius:8px;\n"
        "}\n"
        "QPushButton#recoverybtn:pressed{\n"
        "    padding-left:1px;\n"
        "    padding-top:1px;\n"
        "}\n"
        "\n"
        "\n"
        "QPushButton#closebtn{\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(255, 255, 255, 104), stop:1 rgba(255, 255, 255, 104));\n"
        "    color:rgba(255, 255, 255, 1);\n"
        "    border-radius:10px;\n"
        "}\n"
        "QPushButton#closebtn:hover{\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(255, 92, 92, 1), stop:1 rgba(255, 92, 92, 1));\n"
        "}\n"
        "QPushButton#closebtn:pressed{\n"
        "    padding-left:5px;\n"
        "    padding-top:5px;\n"
        "    background-color:rgba(237, 41, 57, 1);\n"
        "}\n"
        "\n"
        "\n"
        "QPushButton#minbtn{\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(255, 255, 255, 104), stop:1 rgba(255, 255, 255, 104));\n"
        "    color:rgba(255, 255, 255, 1);\n"
        "    border-radius:10px;\n"
        "}\n"
        "QPushButton#minbtn:hover{\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(115, 194, 251, 1), stop:1 rgba(115, 194, 251, 1));\n"
        "}\n"
        "QPushButton#minbtn:pressed{\n"
        "    padding-left:5px;\n"
        "    padding-top:5px;\n"
        "    background-color:rgba(2, 105, 164, 1);\n"
        "}")
        self.widget.setObjectName("widget")
        self.lbl1 = QtWidgets.QLabel(self.widget)
        self.lbl1.setGeometry(QtCore.QRect(19, 19, 331, 521))
        self.lbl1.setStyleSheet("border-image: url(:/images/gears.png);\n"
        "border-radius:20px;")
        self.lbl1.setObjectName("lbl1")
        self.lbl2 = QtWidgets.QLabel(self.widget)
        self.lbl2.setGeometry(QtCore.QRect(33, 150, 300, 370))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        self.lbl2.setFont(font)
        self.lbl2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 104));\n"
        "border-radius:20px;")
        self.lbl2.setText("")
        self.lbl2.setObjectName("lbl2")
        self.lbl3 = QtWidgets.QLabel(self.widget)
        self.lbl3.setGeometry(QtCore.QRect(138, 180, 101, 51))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbl3.setFont(font)
        self.lbl3.setStyleSheet("color:rgba(255, 255, 255, 210);")
        self.lbl3.setObjectName("lbl3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(88, 240, 190, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 219));\n"
        "color: rgb(0, 128, 188);\n"
        "border-radius:8px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(88, 290, 190, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 219));\n"
        "color: rgb(0, 128, 188);\n"
        "border-radius:8px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lbl4 = QtWidgets.QLabel(self.widget)
        self.lbl4.setGeometry(QtCore.QRect(135, 450, 101, 20))
        self.lbl4.setStyleSheet("color: rgb(250, 250, 250);")
        self.lbl4.setObjectName("lbl4")
        self.logbtn = QtWidgets.QPushButton(self.widget, clicked= lambda: self.login())
        self.logbtn.setGeometry(QtCore.QRect(72, 340, 221, 41))
        font = QtGui.QFont()
        font.setFamily("SF Pro Text")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.logbtn.setFont(font)
        self.logbtn.setStyleSheet("color: rgb(250, 250, 250);")
        self.logbtn.setObjectName("logbtn")
        self.regbtn = QtWidgets.QPushButton(self.widget, clicked= lambda: self.reg())
        self.regbtn.setGeometry(QtCore.QRect(122, 472, 121, 21))
        self.regbtn.setStyleSheet("color: rgba(250, 250, 250, 1);")
        self.regbtn.setObjectName("regbtn")
        self.recoverybtn = QtWidgets.QPushButton(self.widget)
        self.recoverybtn.setGeometry(QtCore.QRect(133, 380, 101, 21))
        self.recoverybtn.setStyleSheet("color:rgba(250, 250, 250, 1);")
        self.recoverybtn.setObjectName("recoverybtn")
        self.closebtn = QtWidgets.QPushButton(self.widget, clicked= lambda: self.closewindow())
        self.closebtn.setGeometry(QtCore.QRect(300, 30, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.closebtn.setFont(font)
        self.closebtn.setObjectName("closebtn")
        self.minbtn = QtWidgets.QPushButton(self.widget, clicked= lambda: self.minwindow())
        self.minbtn.setGeometry(QtCore.QRect(265, 30, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.minbtn.setFont(font)
        self.minbtn.setObjectName("minbtn")
        self.warnlbl = QtWidgets.QLabel(self.widget)
        self.warnlbl.setGeometry(QtCore.QRect(60, 410, 250, 20))
        font = QtGui.QFont()
        font.setFamily("SF Pro Text")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.warnlbl.setFont(font)
        self.warnlbl.setStyleSheet("color: rgb(255, 129, 129);")
        self.warnlbl.setText("")
        self.warnlbl.setObjectName("warnlbl")

        self.retranslateUi(Form)
        self.lbl1.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius = 25, xOffset=0, yOffset=0, color=QtGui.QColor(0, 255, 255, 255)))
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def closewindow(self):
        Form.close()

    def minwindow(self):
        Form.showMinimized()

    def adminwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        Form.close()

    def dbconn(self):
        c = conn.cursor()

        c.execute('''
                CREATE TABLE IF NOT EXISTS machines
                ([machine_id] INTEGER PRIMARY KEY, [machine_name] TEXT, [manufacturer] TEXT, [model] TEXT, [category] TEXT, [checkdate] TEXT, [photo] BLOB)
                ''')
                
        c.execute('''
                CREATE TABLE IF NOT EXISTS users
                ([user_id] INTEGER PRIMARY KEY, [username] TEXT UNIQUE, [password] TEXT, [rights] TEXT, [mail] TEXT UNIQUE)
                ''')
                     
        conn.commit()

    def reg(self):
        self.window2 = QtWidgets.QWidget()
        self.ui2 = Ui_Form2()
        self.ui2.regUi(self.window2)
        self.window2.show()
    
    def change_label(self):
        time.sleep(5)
        self.warnlbl.setText('')
 
    def login(self):
        user = self.lineEdit.text()
        user_pass = self.lineEdit_2.text()  
        x = threading.Thread(target=self.change_label)

        try:
            c = conn.cursor()
            query = f"SELECT username from users WHERE username='{user}' AND password = '{user_pass}' AND rights = 'admin';"
            c.execute(query)

            c2 = conn.cursor()
            query2 = f"SELECT username from users WHERE username='{user}' AND password = '{user_pass}';"
            c2.execute(query2)

            if c.fetchone():
                self.adminwindow()

            elif c2.fetchone():
                print('userwindow')

            else:
                self.warnlbl.setText('Nieprawidłowe dane logowania!')
                x.start()

        except sqlite3.IntegrityError:
            self.warnlbl.setText('Podany użytkownik nie istnieje')
            


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl1.setText(_translate("Form", "TextLabel"))
        self.lbl3.setText(_translate("Form", "Zaloguj"))
        self.lineEdit.setPlaceholderText(_translate("Form", "          Nazwa użytkownika"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "                   Hasło"))
        self.lbl4.setText(_translate("Form", "Nie posiadasz konta?"))
        self.logbtn.setText(_translate("Form", "Logowanie"))
        self.regbtn.setText(_translate("Form", "Rejestracja"))
        self.recoverybtn.setText(_translate("Form", "Odzyskiwanie hasła"))
        self.closebtn.setText(_translate("Form", "x"))
        self.minbtn.setText(_translate("Form", "-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
