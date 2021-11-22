import sys, res
from PyQt5 import QtCore, QtGui, QtWidgets
from testform import Ui_MainWindow
import pandas as pd
import sqlite3
from email_validator import validate_email, EmailNotValidError
conn = sqlite3.connect('test_database.db')


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

class Ui_Form2(object):
    def regUi(self, Form2):
        Form2.setObjectName("Form2")
        Form2.resize(442, 489)
        Form2.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form2.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget2 = move(Form2)
        self.widget2.setGeometry(QtCore.QRect(40, 20, 370, 461))
        self.widget2.setStyleSheet("QPushButton#logbtn{\n"
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
        "QPushButton#minbtn2{\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(255, 255, 255, 104), stop:1 rgba(255, 255, 255, 104));\n"
        "    color:rgba(255, 255, 255, 1);\n"
        "    border-radius:10px;\n"
        "}\n"
        "QPushButton#minbtn2:hover{\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(115, 194, 251, 1), stop:1 rgba(115, 194, 251, 1));\n"
        "}\n"
        "QPushButton#minbtn2:pressed{\n"
        "    padding-left:5px;\n"
        "    padding-top:5px;\n"
        "    background-color:rgba(2, 105, 164, 1);\n"
        "}")
        self.widget2.setObjectName("widget2")
        self.reglbl = QtWidgets.QLabel(self.widget2)
        self.reglbl.setGeometry(QtCore.QRect(20, 10, 331, 441))
        self.reglbl.setStyleSheet("border-image: url(:/images/gears.png);\n"
        "border-radius:20px;")
        self.reglbl.setObjectName("reglbl")
        self.lbl2 = QtWidgets.QLabel(self.widget2)
        self.lbl2.setGeometry(QtCore.QRect(33, 70, 300, 371))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        self.lbl2.setFont(font)
        self.lbl2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 104));\n"
        "border-radius:20px;")
        self.lbl2.setText("")
        self.lbl2.setObjectName("lbl2")
        self.lbl3 = QtWidgets.QLabel(self.widget2)
        self.lbl3.setGeometry(QtCore.QRect(110, 100, 151, 51))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbl3.setFont(font)
        self.lbl3.setStyleSheet("color:rgba(255, 255, 255, 210);")
        self.lbl3.setObjectName("lbl3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit.setGeometry(QtCore.QRect(88, 160, 190, 40))
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
        self.lineEdit2 = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit2.setGeometry(QtCore.QRect(88, 210, 190, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit2.setFont(font)
        self.lineEdit2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 219));\n"
        "color: rgb(0, 128, 188);\n"
        "border-radius:8px;")
        self.lineEdit2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit2.setObjectName("lineEdit2")
        self.regbtn = QtWidgets.QPushButton(self.widget2, clicked = lambda: self.reguser())
        self.regbtn.setGeometry(QtCore.QRect(118, 390, 130, 40))
        self.regbtn.setStyleSheet("color: rgba(250, 250, 250, 1);")
        self.regbtn.setObjectName("regbtn")
        self.closereg = QtWidgets.QPushButton(self.widget2, clicked= lambda: self.closewindow2())
        self.closereg.setGeometry(QtCore.QRect(300, 20, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.closereg.setFont(font)
        self.closereg.setObjectName("closebtn")
        self.minbtn2 = QtWidgets.QPushButton(self.widget2, clicked= lambda: self.minwindow2())
        self.minbtn2.setGeometry(QtCore.QRect(265, 20, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.minbtn2.setFont(font)
        self.minbtn2.setObjectName("minbtn2")
        self.warnlbl = QtWidgets.QLabel(self.widget2)
        self.warnlbl.setGeometry(QtCore.QRect(40, 342, 400, 50))
        font = QtGui.QFont()
        font.setFamily("SF Pro Text")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.warnlbl.setFont(font)
        self.warnlbl.setStyleSheet("color: rgb(255, 129, 129);")
        self.warnlbl.setText("")
        self.warnlbl.setObjectName("warnlbl")
        self.lineEdit3 = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit3.setGeometry(QtCore.QRect(88, 260, 190, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit3.setFont(font)
        self.lineEdit3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 219));\n"
        "color: rgb(0, 128, 188);\n"
        "border-radius:8px;")
        self.lineEdit3.setText("")
        self.lineEdit3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit3.setObjectName("lineEdit3")
        self.lineEdit4 = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit4.setGeometry(QtCore.QRect(88, 310, 190, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit4.setFont(font)
        self.lineEdit4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 219));\n"
        "color: rgb(0, 128, 188);\n"
        "border-radius:8px;")
        self.lineEdit4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit4.setObjectName("lineEdit4")

        self.retranslateUi(Form2)
        self.reglbl.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius = 25, xOffset=0, yOffset=0, color=QtGui.QColor(0, 255, 255, 255)))
        QtCore.QMetaObject.connectSlotsByName(Form2)

    def closewindow2(self):
        Form2.close()

    def minwindow2(self):
        Form2.showMinimized()

    def reguser(self):
        user_name = self.lineEdit.text()
        passwd = self.lineEdit2.text()
        passwd2 = self.lineEdit3.text()
        user_mail = self.lineEdit4.text()
        rights = 'user'
        data_tuple = (user_name, passwd, rights, user_mail)

        upper_case = 0
        lower_case = 0
        number = 0
        symbol = 0

        try:
            for i in passwd:
                if i.isupper():
                    upper_case += 1
                elif i.islower():
                    lower_case += 1
                elif i.isdigit():
                    number += 1
                else:
                    symbol += 1

            if len(passwd) < 8:
                self.warnlbl.setText("     Hasło musi mieć 8 znaków!")

            elif upper_case > 0 and lower_case > 0 and number > 0 and symbol > 0:
                validmail = validate_email(user_mail)
                email = validmail.email

                c = conn.cursor()
                query = """INSERT INTO users(username, password, rights, mail) VALUES (?, ?, ?, ?);"""
                c.execute(query, data_tuple)

                conn.commit()
                self.warnlbl.setText(f'Zarejestrowano nowego użytkownika\n                 {user_name}')

            elif passwd != passwd2:
                self.warnlbl.setText(f'  Powtórzone hasło jest niepoprawne!')

            else:
                self.warnlbl.setText("Hasło musi posiadać dużą i małą\nliterę, cyfrę i znak")

        except sqlite3.IntegrityError:
                self.warnlbl.setText(f'Użytkownik z takimi danymi\n{user_mail}lub {user_name} już istnieje!')

        except EmailNotValidError:
                self.warnlbl.setText(f'     Nieprawny format adresu e-mail!')



    def retranslateUi(self, Form2):
        _translate = QtCore.QCoreApplication.translate
        Form2.setWindowTitle(_translate("Form2", "Form"))
        self.reglbl.setText(_translate("Form2", "TextLabel"))
        self.lbl3.setText(_translate("Form2", "Rejestracja"))
        self.lineEdit.setPlaceholderText(_translate("Form2", "          Nazwa użytkownika"))
        self.lineEdit2.setPlaceholderText(_translate("Form2", "                   Hasło"))
        self.regbtn.setText(_translate("Form2", "Rejestracja"))
        self.closereg.setText(_translate("Form2", "x"))
        self.minbtn2.setText(_translate("Form2", "-"))
        self.lineEdit3.setPlaceholderText(_translate("Form2", "             Powtórz hasło"))
        self.lineEdit4.setPlaceholderText(_translate("Form2", "              Adres e-mail"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form2 = QtWidgets.QWidget()
    ui2 = Ui_Form2()
    ui2.regUi(Form2)
    Form2.show()
    sys.exit(app.exec_())
