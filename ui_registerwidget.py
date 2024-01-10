# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registerprOtrx.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)
import resources_rc

class Ui_RegisterWidget(object):
    def setupUi(self, RegisterWidget):
        if not RegisterWidget.objectName():
            RegisterWidget.setObjectName(u"RegisterWidget")
        RegisterWidget.resize(656, 534)
        self.lineEdit_username = QLineEdit(RegisterWidget)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        self.lineEdit_username.setGeometry(QRect(370, 200, 221, 41))
        font = QFont()
        font.setPointSize(12)
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setStyleSheet(u"border:none;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.frame_2 = QFrame(RegisterWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(370, 430, 221, 55))
        self.frame_2.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-top:5px;\n"
"	padding-left:5px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_LoginByWechat = QPushButton(self.frame_2)
        self.btn_LoginByWechat.setObjectName(u"btn_LoginByWechat")
        icon = QIcon()
        icon.addFile(u":/images/images/images/WeChat.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_LoginByWechat.setIcon(icon)
        self.btn_LoginByWechat.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.btn_LoginByWechat)

        self.btn_LoginByQQ = QPushButton(self.frame_2)
        self.btn_LoginByQQ.setObjectName(u"btn_LoginByQQ")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/images/QQ.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_LoginByQQ.setIcon(icon1)
        self.btn_LoginByQQ.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.btn_LoginByQQ)

        self.btn_LoginByQRcode = QPushButton(self.frame_2)
        self.btn_LoginByQRcode.setObjectName(u"btn_LoginByQRcode")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/images/QR-code.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_LoginByQRcode.setIcon(icon2)
        self.btn_LoginByQRcode.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.btn_LoginByQRcode)

        self.label_2 = QLabel(RegisterWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(330, 60, 300, 441))
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-top-right-radius:30px;\n"
"border-bottom-right-radius:30px;")
        self.label_error = QLabel(RegisterWidget)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setGeometry(QRect(430, 330, 151, 21))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_error.setFont(font1)
        self.lineEdit_password = QLineEdit(RegisterWidget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setGeometry(QRect(370, 270, 221, 41))
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet(u"border:none;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.label_3 = QLabel(RegisterWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(410, 130, 131, 51))
        font2 = QFont()
        font2.setFamilies([u"\u5e7c\u5706"])
        font2.setPointSize(23)
        font2.setBold(True)
        self.label_3.setFont(font2)
        self.label = QLabel(RegisterWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 60, 280, 441))
        self.label.setStyleSheet(u"border-image: url(:/images/images/images/login.png);\n"
"border-top-left-radius:30px;\n"
"border-bottom-left-radius:30px;")
        self.btn_login = QPushButton(RegisterWidget)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(370, 400, 221, 41))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.btn_login.setFont(font3)
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0,0,0);\n"
"	color: rgb(255,255,255);\n"
"	border:2px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"padding-top:5px;\n"
"padding-left:5px;\n"
"}")
        self.frame = QFrame(RegisterWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(520, 80, 91, 41))
        self.frame.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"padding-bottom:5px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_minimize = QPushButton(self.frame)
        self.btn_minimize.setObjectName(u"btn_minimize")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_minimize1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon3)

        self.horizontalLayout.addWidget(self.btn_minimize)

        self.btn_close = QPushButton(self.frame)
        self.btn_close.setObjectName(u"btn_close")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_close1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon4)

        self.horizontalLayout.addWidget(self.btn_close)

        self.lineEdit_username_2 = QLineEdit(RegisterWidget)
        self.lineEdit_username_2.setObjectName(u"lineEdit_username_2")
        self.lineEdit_username_2.setGeometry(QRect(370, 210, 221, 41))
        self.lineEdit_username_2.setFont(font)
        self.lineEdit_username_2.setStyleSheet(u"border:none;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.lineEdit_password_2 = QLineEdit(RegisterWidget)
        self.lineEdit_password_2.setObjectName(u"lineEdit_password_2")
        self.lineEdit_password_2.setGeometry(QRect(370, 330, 221, 41))
        self.lineEdit_password_2.setFont(font)
        self.lineEdit_password_2.setStyleSheet(u"border:none;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.lineEdit_password_2.setEchoMode(QLineEdit.Password)
        self.btn_back = QPushButton(RegisterWidget)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(350, 70, 75, 24))

        self.retranslateUi(RegisterWidget)
        self.btn_minimize.clicked.connect(RegisterWidget.showMinimized)
        self.btn_close.clicked.connect(RegisterWidget.close)

        QMetaObject.connectSlotsByName(RegisterWidget)
    # setupUi

    def retranslateUi(self, RegisterWidget):
        RegisterWidget.setWindowTitle(QCoreApplication.translate("RegisterWidget", u"Form", None))
        self.lineEdit_username.setPlaceholderText(QCoreApplication.translate("RegisterWidget", u"\u8d26\u53f7\uff1a", None))
        self.btn_LoginByWechat.setText("")
        self.btn_LoginByQQ.setText("")
        self.btn_LoginByQRcode.setText("")
        self.label_2.setText("")
        self.label_error.setText("")
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("RegisterWidget", u"\u8bbe\u7f6e\u5bc6\u7801\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("RegisterWidget", u"\u6b22\u8fce\u6ce8\u518c", None))
        self.label.setText("")
        self.btn_login.setText(QCoreApplication.translate("RegisterWidget", u"\u6ce8\u518c", None))
        self.btn_minimize.setText("")
        self.btn_close.setText("")
        self.lineEdit_username_2.setPlaceholderText(QCoreApplication.translate("RegisterWidget", u"\u8bbe\u7f6e\u8d26\u53f7\uff1a", None))
        self.lineEdit_password_2.setPlaceholderText(QCoreApplication.translate("RegisterWidget", u"\u786e\u8ba4\u5bc6\u7801\uff1a", None))
        self.btn_back.setText(QCoreApplication.translate("RegisterWidget", u"\u8fd4\u56de\u767b\u5f55", None))
    # retranslateUi

