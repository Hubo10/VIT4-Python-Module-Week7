# Form implementation generated from reading ui file 'd:\VsCode_Gitbub\VIT4-Python-Module-Week7\ui\admin_menu.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_admin_menu_MainWindow(object):
    def setupUi(self, admin_menu_MainWindow):
        admin_menu_MainWindow.setObjectName("admin_menu_MainWindow")
        admin_menu_MainWindow.resize(618, 550)
        admin_menu_MainWindow.setMinimumSize(QtCore.QSize(618, 550))
        admin_menu_MainWindow.setMaximumSize(QtCore.QSize(618, 550))
        self.centralwidget = QtWidgets.QWidget(parent=admin_menu_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setMinimumSize(QtCore.QSize(618, 550))
        self.frame.setMaximumSize(QtCore.QSize(618, 550))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.werhere_image_label = QtWidgets.QLabel(parent=self.frame)
        self.werhere_image_label.setGeometry(QtCore.QRect(0, -10, 600, 171))
        self.werhere_image_label.setText("")
        self.werhere_image_label.setPixmap(QtGui.QPixmap("d:\\VsCode_Gitbub\\VIT4-Python-Module-Week7\\ui\\../vit_4_week_7_project/werhere_image.png"))
        self.werhere_image_label.setObjectName("werhere_image_label")
        self.act_check_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.act_check_pushButton.setGeometry(QtCore.QRect(10, 220, 151, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.act_check_pushButton.setFont(font)
        self.act_check_pushButton.setStyleSheet("\n"
"QPushButton:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }\n"
"")
        self.act_check_pushButton.setObjectName("act_check_pushButton")
        self.send_mail_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.send_mail_pushButton.setGeometry(QtCore.QRect(170, 220, 121, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.send_mail_pushButton.setFont(font)
        self.send_mail_pushButton.setStyleSheet("\n"
"QPushButton:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }\n"
"")
        self.send_mail_pushButton.setObjectName("send_mail_pushButton")
        self.preference_admin_menu_pushButton_3 = QtWidgets.QPushButton(parent=self.frame)
        self.preference_admin_menu_pushButton_3.setGeometry(QtCore.QRect(300, 220, 191, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.preference_admin_menu_pushButton_3.setFont(font)
        self.preference_admin_menu_pushButton_3.setStyleSheet("\n"
"QPushButton:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }\n"
"")
        self.preference_admin_menu_pushButton_3.setObjectName("preference_admin_menu_pushButton_3")
        self.exit_pushButton_4 = QtWidgets.QPushButton(parent=self.frame)
        self.exit_pushButton_4.setGeometry(QtCore.QRect(500, 220, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.exit_pushButton_4.setFont(font)
        self.exit_pushButton_4.setStyleSheet("\n"
"QPushButton:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }\n"
"")
        self.exit_pushButton_4.setObjectName("exit_pushButton_4")
        self.admin_menu_tableWidget = QtWidgets.QTableWidget(parent=self.frame)
        self.admin_menu_tableWidget.setGeometry(QtCore.QRect(10, 300, 581, 251))
        self.admin_menu_tableWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI 13")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.admin_menu_tableWidget.setFont(font)
        self.admin_menu_tableWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.admin_menu_tableWidget.setStyleSheet("font: 10pt \"Segoe UI\" bold;")
        self.admin_menu_tableWidget.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.Netherlands))
        self.admin_menu_tableWidget.setObjectName("admin_menu_tableWidget")
        self.admin_menu_tableWidget.setColumnCount(4)
        self.admin_menu_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.admin_menu_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_menu_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_menu_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_menu_tableWidget.setHorizontalHeaderItem(3, item)
        self.admin_menu_tableWidget.horizontalHeader().setDefaultSectionSize(145)
        self.verticalLayout.addWidget(self.frame)
        admin_menu_MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=admin_menu_MainWindow)
        self.statusbar.setObjectName("statusbar")
        admin_menu_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(admin_menu_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(admin_menu_MainWindow)

    def retranslateUi(self, admin_menu_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        admin_menu_MainWindow.setWindowTitle(_translate("admin_menu_MainWindow", "                                                                                  ADMIN MENU"))
        self.act_check_pushButton.setText(_translate("admin_menu_MainWindow", "ACTIVITY CONTROL"))
        self.send_mail_pushButton.setText(_translate("admin_menu_MainWindow", "SEND MAIL"))
        self.preference_admin_menu_pushButton_3.setText(_translate("admin_menu_MainWindow", "PREFERENCE - ADMIN MENU"))
        self.exit_pushButton_4.setText(_translate("admin_menu_MainWindow", "EXIT"))
        item = self.admin_menu_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("admin_menu_MainWindow", "Activity Name"))
        item = self.admin_menu_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("admin_menu_MainWindow", "Start Time"))
        item = self.admin_menu_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("admin_menu_MainWindow", "Participant Mail"))
        item = self.admin_menu_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("admin_menu_MainWindow", "Organizer Mail"))