# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainyFGgxC.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QProgressBar, QPushButton,
    QRadioButton, QSizePolicy, QSpinBox, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1070, 729)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.verticalLayout_18 = QVBoxLayout(self.styleSheet)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"background-image: url(:/images/images/images/DataPilot.png);")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_FeatureProcessing = QPushButton(self.topMenu)
        self.btn_FeatureProcessing.setObjectName(u"btn_FeatureProcessing")
        sizePolicy.setHeightForWidth(self.btn_FeatureProcessing.sizePolicy().hasHeightForWidth())
        self.btn_FeatureProcessing.setSizePolicy(sizePolicy)
        self.btn_FeatureProcessing.setMinimumSize(QSize(0, 45))
        self.btn_FeatureProcessing.setFont(font)
        self.btn_FeatureProcessing.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_FeatureProcessing.setLayoutDirection(Qt.LeftToRight)
        self.btn_FeatureProcessing.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_8.addWidget(self.btn_FeatureProcessing)

        self.btn_FeatureSelection = QPushButton(self.topMenu)
        self.btn_FeatureSelection.setObjectName(u"btn_FeatureSelection")
        sizePolicy.setHeightForWidth(self.btn_FeatureSelection.sizePolicy().hasHeightForWidth())
        self.btn_FeatureSelection.setSizePolicy(sizePolicy)
        self.btn_FeatureSelection.setMinimumSize(QSize(0, 45))
        self.btn_FeatureSelection.setFont(font)
        self.btn_FeatureSelection.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_FeatureSelection.setLayoutDirection(Qt.LeftToRight)
        self.btn_FeatureSelection.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-feature-selection1.png);")

        self.verticalLayout_8.addWidget(self.btn_FeatureSelection)

        self.btn_ModelTraining = QPushButton(self.topMenu)
        self.btn_ModelTraining.setObjectName(u"btn_ModelTraining")
        sizePolicy.setHeightForWidth(self.btn_ModelTraining.sizePolicy().hasHeightForWidth())
        self.btn_ModelTraining.setSizePolicy(sizePolicy)
        self.btn_ModelTraining.setMinimumSize(QSize(0, 45))
        self.btn_ModelTraining.setFont(font)
        self.btn_ModelTraining.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ModelTraining.setLayoutDirection(Qt.LeftToRight)
        self.btn_ModelTraining.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-model.png);")

        self.verticalLayout_8.addWidget(self.btn_ModelTraining)

        self.btn_ResultAnalysis = QPushButton(self.topMenu)
        self.btn_ResultAnalysis.setObjectName(u"btn_ResultAnalysis")
        self.btn_ResultAnalysis.setMinimumSize(QSize(0, 45))
        self.btn_ResultAnalysis.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-result-analysis1.png);")

        self.verticalLayout_8.addWidget(self.btn_ResultAnalysis)

        self.btn_FeatureGeneration = QPushButton(self.topMenu)
        self.btn_FeatureGeneration.setObjectName(u"btn_FeatureGeneration")
        sizePolicy.setHeightForWidth(self.btn_FeatureGeneration.sizePolicy().hasHeightForWidth())
        self.btn_FeatureGeneration.setSizePolicy(sizePolicy)
        self.btn_FeatureGeneration.setMinimumSize(QSize(0, 45))
        self.btn_FeatureGeneration.setFont(font)
        self.btn_FeatureGeneration.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_FeatureGeneration.setLayoutDirection(Qt.LeftToRight)
        self.btn_FeatureGeneration.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_8.addWidget(self.btn_FeatureGeneration)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_theme = QPushButton(self.rightButtons)
        self.btn_theme.setObjectName(u"btn_theme")
        self.btn_theme.setMinimumSize(QSize(28, 28))
        self.btn_theme.setMaximumSize(QSize(28, 28))
        self.btn_theme.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-theme1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_theme.setIcon(icon1)
        self.btn_theme.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_theme)

        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon2)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon3)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon4)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.page1_Home = QWidget()
        self.page1_Home.setObjectName(u"page1_Home")
        self.page1_Home.setStyleSheet(u"")
        self.verticalLayout_29 = QVBoxLayout(self.page1_Home)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.widget = QWidget(self.page1_Home)
        self.widget.setObjectName(u"widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy3)
        self.widget.setStyleSheet(u"QWidget {\n"
"    background-image: url(:/images/images/images/HomePage_bg.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.btn_downloadDatabase = QPushButton(self.widget)
        self.btn_downloadDatabase.setObjectName(u"btn_downloadDatabase")
        self.btn_downloadDatabase.setGeometry(QRect(650, 30, 286, 211))
        self.btn_downloadDatabase.setStyleSheet(u"QPushButton {\n"
"image: url(:/images/images/images/crystal_structure.png);\n"
"  background-color: #4CAF50;  /* \u7eff\u8272\u80cc\u666f */\n"
"  border-style: outset;       /* \u8fb9\u6846\u6837\u5f0f */\n"
"  border-width: 2px;          /* \u8fb9\u6846\u5bbd\u5ea6 */\n"
"  border-radius: 10px;        /* \u5706\u89d2\u8fb9\u6846 */\n"
"  border-color: #4CAF50;      /* \u8fb9\u6846\u989c\u8272 */\n"
"  font: bold 20px;            /* \u52a0\u7c97\u5b57\u4f53\u548c\u5b57\u4f53\u5927\u5c0f */\n"
"  min-width: 10em;            /* \u6700\u5c0f\u5bbd\u5ea6 */\n"
"  padding: 6px;               /* \u6587\u5b57\u5468\u56f4\u7684\u586b\u5145 */\n"
"  color: #8B008B;               /* \u6587\u5b57\u989c\u8272\u4e3a\u767d\u8272 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #45a049;  /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272\u53d8\u6df1 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #388e3c;  /* \u6309\u94ae\u88ab\u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272\u53d8\u5f97"
                        "\u66f4\u6df1 */\n"
"  border-style: inset;        /* \u6309\u94ae\u88ab\u6309\u4e0b\u65f6\u7684\u8fb9\u6846\u6837\u5f0f */\n"
"}")
        self.btn_videoTutorial = QPushButton(self.widget)
        self.btn_videoTutorial.setObjectName(u"btn_videoTutorial")
        self.btn_videoTutorial.setGeometry(QRect(650, 250, 286, 151))
        self.btn_videoTutorial.setStyleSheet(u"QPushButton {\n"
"image: url(:/images/images/images/Tutorial.png);\n"
"  background-color: #4CAF50;  /* \u7eff\u8272\u80cc\u666f */\n"
"  border-style: outset;       /* \u8fb9\u6846\u6837\u5f0f */\n"
"  border-width: 2px;          /* \u8fb9\u6846\u5bbd\u5ea6 */\n"
"  border-radius: 10px;        /* \u5706\u89d2\u8fb9\u6846 */\n"
"  border-color: #4CAF50;      /* \u8fb9\u6846\u989c\u8272 */\n"
"  font: bold 20px;            /* \u52a0\u7c97\u5b57\u4f53\u548c\u5b57\u4f53\u5927\u5c0f */\n"
"  min-width: 10em;            /* \u6700\u5c0f\u5bbd\u5ea6 */\n"
"  padding: 6px;               /* \u6587\u5b57\u5468\u56f4\u7684\u586b\u5145 */\n"
"  color: #8B008B;               /* \u6587\u5b57\u989c\u8272\u4e3a\u767d\u8272 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #45a049;  /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272\u53d8\u6df1 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #388e3c;  /* \u6309\u94ae\u88ab\u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272\u53d8\u5f97\u66f4"
                        "\u6df1 */\n"
"  border-style: inset;        /* \u6309\u94ae\u88ab\u6309\u4e0b\u65f6\u7684\u8fb9\u6846\u6837\u5f0f */\n"
"}\n"
"")

        self.verticalLayout_29.addWidget(self.widget)

        self.stackedWidget.addWidget(self.page1_Home)
        self.page2_FeatureProcessing = QWidget()
        self.page2_FeatureProcessing.setObjectName(u"page2_FeatureProcessing")
        self.page2_FeatureProcessing.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.page2_FeatureProcessing)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.page2_FeatureProcessing)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_1)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineedit_imported_filename = QLineEdit(self.frame_content_wid_1)
        self.lineedit_imported_filename.setObjectName(u"lineedit_imported_filename")
        self.lineedit_imported_filename.setMinimumSize(QSize(0, 30))
        self.lineedit_imported_filename.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineedit_imported_filename, 0, 1, 1, 1)

        self.btn_open_local_file = QPushButton(self.frame_content_wid_1)
        self.btn_open_local_file.setObjectName(u"btn_open_local_file")
        self.btn_open_local_file.setMinimumSize(QSize(150, 30))
        self.btn_open_local_file.setFont(font)
        self.btn_open_local_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open_local_file.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open_local_file.setIcon(icon5)

        self.gridLayout.addWidget(self.btn_open_local_file, 0, 0, 1, 1)

        self.btn_FeatureProcessing_2 = QPushButton(self.frame_content_wid_1)
        self.btn_FeatureProcessing_2.setObjectName(u"btn_FeatureProcessing_2")
        self.btn_FeatureProcessing_2.setMinimumSize(QSize(150, 30))
        self.btn_FeatureProcessing_2.setFont(font)
        self.btn_FeatureProcessing_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_FeatureProcessing_2.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-data-process.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_FeatureProcessing_2.setIcon(icon6)

        self.gridLayout.addWidget(self.btn_FeatureProcessing_2, 0, 2, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)

        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 50))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_title_wid_1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_missing_values_handling = QLabel(self.frame_title_wid_1)
        self.label_missing_values_handling.setObjectName(u"label_missing_values_handling")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_missing_values_handling.sizePolicy().hasHeightForWidth())
        self.label_missing_values_handling.setSizePolicy(sizePolicy4)

        self.horizontalLayout_7.addWidget(self.label_missing_values_handling)

        self.combobox_missing_values_handling = QComboBox(self.frame_title_wid_1)
        self.combobox_missing_values_handling.addItem("")
        self.combobox_missing_values_handling.addItem("")
        self.combobox_missing_values_handling.addItem("")
        self.combobox_missing_values_handling.addItem("")
        self.combobox_missing_values_handling.addItem("")
        self.combobox_missing_values_handling.addItem("")
        self.combobox_missing_values_handling.addItem("")
        self.combobox_missing_values_handling.addItem("")
        self.combobox_missing_values_handling.setObjectName(u"combobox_missing_values_handling")

        self.horizontalLayout_7.addWidget(self.combobox_missing_values_handling)

        self.label_outlier_handling = QLabel(self.frame_title_wid_1)
        self.label_outlier_handling.setObjectName(u"label_outlier_handling")
        sizePolicy4.setHeightForWidth(self.label_outlier_handling.sizePolicy().hasHeightForWidth())
        self.label_outlier_handling.setSizePolicy(sizePolicy4)

        self.horizontalLayout_7.addWidget(self.label_outlier_handling)

        self.combobox_outlier_handling = QComboBox(self.frame_title_wid_1)
        self.combobox_outlier_handling.addItem("")
        self.combobox_outlier_handling.addItem("")
        self.combobox_outlier_handling.addItem("")
        self.combobox_outlier_handling.addItem("")
        self.combobox_outlier_handling.addItem("")
        self.combobox_outlier_handling.addItem("")
        self.combobox_outlier_handling.setObjectName(u"combobox_outlier_handling")

        self.horizontalLayout_7.addWidget(self.combobox_outlier_handling)

        self.label_categorical_handling = QLabel(self.frame_title_wid_1)
        self.label_categorical_handling.setObjectName(u"label_categorical_handling")
        sizePolicy4.setHeightForWidth(self.label_categorical_handling.sizePolicy().hasHeightForWidth())
        self.label_categorical_handling.setSizePolicy(sizePolicy4)

        self.horizontalLayout_7.addWidget(self.label_categorical_handling)

        self.combobox_categorical_handling = QComboBox(self.frame_title_wid_1)
        self.combobox_categorical_handling.addItem("")
        self.combobox_categorical_handling.addItem("")
        self.combobox_categorical_handling.addItem("")
        self.combobox_categorical_handling.addItem("")
        self.combobox_categorical_handling.addItem("")
        self.combobox_categorical_handling.addItem("")
        self.combobox_categorical_handling.addItem("")
        self.combobox_categorical_handling.setObjectName(u"combobox_categorical_handling")

        self.horizontalLayout_7.addWidget(self.combobox_categorical_handling)

        self.label_data_normalization_handling = QLabel(self.frame_title_wid_1)
        self.label_data_normalization_handling.setObjectName(u"label_data_normalization_handling")
        sizePolicy4.setHeightForWidth(self.label_data_normalization_handling.sizePolicy().hasHeightForWidth())
        self.label_data_normalization_handling.setSizePolicy(sizePolicy4)

        self.horizontalLayout_7.addWidget(self.label_data_normalization_handling)

        self.combobox_data_normalization_handling = QComboBox(self.frame_title_wid_1)
        self.combobox_data_normalization_handling.addItem("")
        self.combobox_data_normalization_handling.addItem("")
        self.combobox_data_normalization_handling.addItem("")
        self.combobox_data_normalization_handling.addItem("")
        self.combobox_data_normalization_handling.addItem("")
        self.combobox_data_normalization_handling.addItem("")
        self.combobox_data_normalization_handling.setObjectName(u"combobox_data_normalization_handling")

        self.horizontalLayout_7.addWidget(self.combobox_data_normalization_handling)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)


        self.verticalLayout_19.addWidget(self.frame_div_content_1)

        self.frame_2 = QFrame(self.row_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.tabWidgetMLRawData = QTabWidget(self.frame_2)
        self.tabWidgetMLRawData.setObjectName(u"tabWidgetMLRawData")
        self.tabWidgetMLRawData.setAutoFillBackground(False)
        self.tabWidgetMLRawData.setStyleSheet(u"QTabBar::tab {\n"
"    border: 2px solid gray;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 30ex;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: #636363;\n"
"    border-color: \uff03000000;\n"
"	font-weight: bold;\n"
"	border: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-bottom-color: white; /* same as pane color */\n"
"}\n"
"")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayout_25 = QVBoxLayout(self.tab_1)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.tablewidget_raw_data = QTableWidget(self.tab_1)
        self.tablewidget_raw_data.setObjectName(u"tablewidget_raw_data")

        self.verticalLayout_25.addWidget(self.tablewidget_raw_data)

        self.tabWidgetMLRawData.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_24 = QVBoxLayout(self.tab_2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.tablewidget_data_missing_handled = QTableWidget(self.tab_2)
        self.tablewidget_data_missing_handled.setObjectName(u"tablewidget_data_missing_handled")

        self.verticalLayout_24.addWidget(self.tablewidget_data_missing_handled)

        self.tabWidgetMLRawData.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_21 = QVBoxLayout(self.tab_3)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.tablewidget_data_outlier_handled = QTableWidget(self.tab_3)
        self.tablewidget_data_outlier_handled.setObjectName(u"tablewidget_data_outlier_handled")

        self.verticalLayout_21.addWidget(self.tablewidget_data_outlier_handled)

        self.tabWidgetMLRawData.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_23 = QVBoxLayout(self.tab_4)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.tablewidget_data_categorical_handled = QTableWidget(self.tab_4)
        self.tablewidget_data_categorical_handled.setObjectName(u"tablewidget_data_categorical_handled")

        self.verticalLayout_23.addWidget(self.tablewidget_data_categorical_handled)

        self.tabWidgetMLRawData.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_22 = QVBoxLayout(self.tab_5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.tablewidget_data_normalization_handled = QTableWidget(self.tab_5)
        self.tablewidget_data_normalization_handled.setObjectName(u"tablewidget_data_normalization_handled")

        self.verticalLayout_22.addWidget(self.tablewidget_data_normalization_handled)

        self.tabWidgetMLRawData.addTab(self.tab_5, "")

        self.verticalLayout_16.addWidget(self.tabWidgetMLRawData)

        self.progressBar = QProgressBar(self.frame_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_16.addWidget(self.progressBar)


        self.verticalLayout_19.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.row_1)

        self.stackedWidget.addWidget(self.page2_FeatureProcessing)
        self.page3_FeatureSelection = QWidget()
        self.page3_FeatureSelection.setObjectName(u"page3_FeatureSelection")
        self.verticalLayout_20 = QVBoxLayout(self.page3_FeatureSelection)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.row_4 = QFrame(self.page3_FeatureSelection)
        self.row_4.setObjectName(u"row_4")
        self.row_4.setMinimumSize(QSize(0, 150))
        self.row_4.setFrameShape(QFrame.StyledPanel)
        self.row_4.setFrameShadow(QFrame.Raised)
        self.checkBox = QCheckBox(self.row_4)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(50, 10, 181, 31))
        self.checkBox_3 = QCheckBox(self.row_4)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(270, 10, 211, 31))
        self.checkBox_4 = QCheckBox(self.row_4)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(530, 10, 211, 31))
        self.treeWidget_featureSelection = QTreeWidget(self.row_4)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget_featureSelection)
        __qtreewidgetitem1 = QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem1.setCheckState(0, Qt.Unchecked);
        __qtreewidgetitem2 = QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem3 = QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem3.setCheckState(0, Qt.Unchecked);
        __qtreewidgetitem4 = QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem4.setCheckState(0, Qt.Unchecked);
        __qtreewidgetitem5 = QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem5.setCheckState(0, Qt.Unchecked);
        __qtreewidgetitem6 = QTreeWidgetItem(self.treeWidget_featureSelection)
        __qtreewidgetitem6.setCheckState(0, Qt.Unchecked);
        __qtreewidgetitem7 = QTreeWidgetItem(self.treeWidget_featureSelection)
        __qtreewidgetitem7.setCheckState(0, Qt.Unchecked);
        self.treeWidget_featureSelection.setObjectName(u"treeWidget_featureSelection")
        self.treeWidget_featureSelection.setGeometry(QRect(40, 60, 256, 192))
        self.btn_eatureSelection = QPushButton(self.row_4)
        self.btn_eatureSelection.setObjectName(u"btn_eatureSelection")
        self.btn_eatureSelection.setGeometry(QRect(580, 460, 75, 24))
        self.tabWidget_FeatureSelectionData = QTabWidget(self.row_4)
        self.tabWidget_FeatureSelectionData.setObjectName(u"tabWidget_FeatureSelectionData")
        self.tabWidget_FeatureSelectionData.setGeometry(QRect(360, 60, 541, 351))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget_FeatureSelectionData.addTab(self.tab, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget_FeatureSelectionData.addTab(self.tab_6, "")

        self.verticalLayout_20.addWidget(self.row_4)

        self.stackedWidget.addWidget(self.page3_FeatureSelection)
        self.page4_ModelTraining = QWidget()
        self.page4_ModelTraining.setObjectName(u"page4_ModelTraining")
        self.treeWidget = QTreeWidget(self.page4_ModelTraining)
        __qtreewidgetitem8 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem8)
        QTreeWidgetItem(__qtreewidgetitem8)
        QTreeWidgetItem(__qtreewidgetitem8)
        QTreeWidgetItem(__qtreewidgetitem8)
        QTreeWidgetItem(__qtreewidgetitem8)
        QTreeWidgetItem(__qtreewidgetitem8)
        QTreeWidgetItem(__qtreewidgetitem8)
        QTreeWidgetItem(__qtreewidgetitem8)
        QTreeWidgetItem(__qtreewidgetitem8)
        QTreeWidgetItem(__qtreewidgetitem8)
        __qtreewidgetitem9 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem9)
        QTreeWidgetItem(__qtreewidgetitem9)
        QTreeWidgetItem(__qtreewidgetitem9)
        QTreeWidgetItem(__qtreewidgetitem9)
        QTreeWidgetItem(__qtreewidgetitem9)
        QTreeWidgetItem(__qtreewidgetitem9)
        QTreeWidgetItem(__qtreewidgetitem9)
        QTreeWidgetItem(__qtreewidgetitem9)
        QTreeWidgetItem(__qtreewidgetitem9)
        QTreeWidgetItem(__qtreewidgetitem9)
        QTreeWidgetItem(__qtreewidgetitem9)
        QTreeWidgetItem(__qtreewidgetitem9)
        __qtreewidgetitem10 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem10)
        QTreeWidgetItem(__qtreewidgetitem10)
        QTreeWidgetItem(__qtreewidgetitem10)
        QTreeWidgetItem(__qtreewidgetitem10)
        QTreeWidgetItem(__qtreewidgetitem10)
        QTreeWidgetItem(__qtreewidgetitem10)
        QTreeWidgetItem(__qtreewidgetitem10)
        QTreeWidgetItem(__qtreewidgetitem10)
        __qtreewidgetitem11 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem11)
        QTreeWidgetItem(__qtreewidgetitem11)
        QTreeWidgetItem(__qtreewidgetitem11)
        QTreeWidgetItem(__qtreewidgetitem11)
        QTreeWidgetItem(__qtreewidgetitem11)
        QTreeWidgetItem(__qtreewidgetitem11)
        QTreeWidgetItem(__qtreewidgetitem11)
        QTreeWidgetItem(__qtreewidgetitem11)
        QTreeWidgetItem(__qtreewidgetitem11)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(9, 9, 501, 131))
        self.groupBox_4 = QGroupBox(self.page4_ModelTraining)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(40, 180, 299, 106))
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy5)
        self.groupBox_4.setStyleSheet(u"QGroupBox{\n"
"    border: 2px solid rgb(17, 17, 17);\n"
"    border-radius: 10px;\n"
"    margin-top: 0.5em;\n"
"	font-family: \"\u9ed1\u4f53\";\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.formLayout = QFormLayout(self.groupBox_4)
        self.formLayout.setObjectName(u"formLayout")
        self.radioButton = QRadioButton(self.groupBox_4)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.radioButton)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.radioButton_3 = QRadioButton(self.groupBox_4)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_6.addWidget(self.radioButton_3)

        self.spinBox_4 = QSpinBox(self.groupBox_4)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setStyleSheet(u"QSpinBox {\n"
"    border: none;\n"
"    border-radius: 2px;\n"
"    background-color: white;\n"
"}\n"
"")
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setValue(1)

        self.horizontalLayout_6.addWidget(self.spinBox_4)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_6)

        self.radioButton_4 = QRadioButton(self.groupBox_4)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.radioButton_4)

        self.spinBox = QSpinBox(self.groupBox_4)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setStyleSheet(u"QSpinBox {\n"
"    border: none;\n"
"    border-radius: 2px;\n"
"    background-color: white;\n"
"}\n"
"")
        self.spinBox.setMinimum(2)
        self.spinBox.setValue(5)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinBox)

        self.radioButton_5 = QRadioButton(self.groupBox_4)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.radioButton_5)

        self.spinBox_2 = QSpinBox(self.groupBox_4)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setStyleSheet(u"QSpinBox {\n"
"    border: none;\n"
"    border-radius: 2px;\n"
"    background-color: white;\n"
"}\n"
"")
        self.spinBox_2.setMinimum(2)
        self.spinBox_2.setValue(5)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spinBox_2)

        self.groupBox_7 = QGroupBox(self.page4_ModelTraining)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(480, 210, 331, 106))
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy6)
        self.groupBox_7.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_7.setStyleSheet(u"QGroupBox{\n"
"    border: 2px solid rgb(17, 17, 17);\n"
"    border-radius: 10px;\n"
"    margin-top: 0.5em;\n"
"	font-family: \"\u9ed1\u4f53\";\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.verticalLayout_26 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(self.groupBox_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_7)

        self.doubleSpinBox = QDoubleSpinBox(self.groupBox_7)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setStyleSheet(u"QDoubleSpinBox {\n"
"    border: none;\n"
"    border-radius: 2px;\n"
"    background-color: white;\n"
"}\n"
"")
        self.doubleSpinBox.setMinimum(0.010000000000000)
        self.doubleSpinBox.setMaximum(0.990000000000000)
        self.doubleSpinBox.setSingleStep(0.010000000000000)
        self.doubleSpinBox.setValue(0.200000000000000)

        self.horizontalLayout_10.addWidget(self.doubleSpinBox)

        self.horizontalLayout_10.setStretch(0, 7)
        self.horizontalLayout_10.setStretch(1, 10)

        self.verticalLayout_26.addLayout(self.horizontalLayout_10)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox_5 = QCheckBox(self.groupBox_7)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setFont(font)
        self.checkBox_5.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBox_5, 0, 0, 1, 1)

        self.checkBox_6 = QCheckBox(self.groupBox_7)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setFont(font)

        self.gridLayout_2.addWidget(self.checkBox_6, 0, 1, 1, 1)

        self.checkBox_7 = QCheckBox(self.groupBox_7)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setFont(font)

        self.gridLayout_2.addWidget(self.checkBox_7, 0, 2, 1, 1)

        self.checkBox_8 = QCheckBox(self.groupBox_7)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setFont(font)
        self.checkBox_8.setAutoExclusive(False)

        self.gridLayout_2.addWidget(self.checkBox_8, 1, 0, 1, 1)

        self.checkBox_9 = QCheckBox(self.groupBox_7)
        self.checkBox_9.setObjectName(u"checkBox_9")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.checkBox_9.sizePolicy().hasHeightForWidth())
        self.checkBox_9.setSizePolicy(sizePolicy7)
        self.checkBox_9.setMinimumSize(QSize(95, 0))
        self.checkBox_9.setFont(font)
        self.checkBox_9.setAutoExclusive(False)

        self.gridLayout_2.addWidget(self.checkBox_9, 1, 1, 1, 1)

        self.checkBox_10 = QCheckBox(self.groupBox_7)
        self.checkBox_10.setObjectName(u"checkBox_10")
        sizePolicy7.setHeightForWidth(self.checkBox_10.sizePolicy().hasHeightForWidth())
        self.checkBox_10.setSizePolicy(sizePolicy7)
        self.checkBox_10.setMinimumSize(QSize(75, 0))
        self.checkBox_10.setFont(font)
        self.checkBox_10.setAutoExclusive(False)

        self.gridLayout_2.addWidget(self.checkBox_10, 1, 2, 1, 1)


        self.verticalLayout_26.addLayout(self.gridLayout_2)

        self.groupBox_5 = QGroupBox(self.page4_ModelTraining)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(50, 330, 299, 88))
        sizePolicy6.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy6)
        self.groupBox_5.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_5.setStyleSheet(u"QGroupBox{\n"
"    border: 2px solid rgb(17, 17, 17);\n"
"    border-radius: 10px;\n"
"    margin-top: 0.5em;\n"
"	font-family: \"\u9ed1\u4f53\";\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.verticalLayout_27 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_8)

        self.spinBox_3 = QSpinBox(self.groupBox_5)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setStyleSheet(u"QSpinBox {\n"
"    border: none;\n"
"    border-radius: 2px;\n"
"    background-color: white;\n"
"}\n"
"")
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setValue(1)

        self.horizontalLayout_11.addWidget(self.spinBox_3)


        self.verticalLayout_27.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(15)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_2 = QPushButton(self.groupBox_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)

        self.horizontalLayout_12.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.groupBox_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)

        self.horizontalLayout_12.addWidget(self.pushButton_3)


        self.verticalLayout_27.addLayout(self.horizontalLayout_12)

        self.groupBox_6 = QGroupBox(self.page4_ModelTraining)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(480, 330, 299, 139))
        sizePolicy6.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy6)
        self.groupBox_6.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_6.setStyleSheet(u"QGroupBox{\n"
"    border: 2px solid rgb(17, 17, 17);\n"
"    border-radius: 10px;\n"
"    margin-top: 0.5em;\n"
"	font-family: \"\u9ed1\u4f53\";\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.gridLayout_4 = QGridLayout(self.groupBox_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(10)
        self.gridLayout_4.setContentsMargins(15, 15, 15, -1)
        self.label_11 = QLabel(self.groupBox_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_11, 0, 2, 1, 1)

        self.lineEdit_10 = QLineEdit(self.groupBox_6)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setFont(font)

        self.gridLayout_4.addWidget(self.lineEdit_10, 2, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.groupBox_6)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setFont(font)

        self.gridLayout_4.addWidget(self.lineEdit_7, 1, 1, 1, 1)

        self.lineEdit_15 = QLineEdit(self.groupBox_6)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setFont(font)

        self.gridLayout_4.addWidget(self.lineEdit_15, 3, 3, 1, 1)

        self.lineEdit_12 = QLineEdit(self.groupBox_6)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setFont(font)

        self.gridLayout_4.addWidget(self.lineEdit_12, 2, 3, 1, 1)

        self.label_9 = QLabel(self.groupBox_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_9, 3, 0, 1, 1)

        self.lineEdit_14 = QLineEdit(self.groupBox_6)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setFont(font)

        self.gridLayout_4.addWidget(self.lineEdit_14, 3, 2, 1, 1)

        self.lineEdit_9 = QLineEdit(self.groupBox_6)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setFont(font)

        self.gridLayout_4.addWidget(self.lineEdit_9, 1, 3, 1, 1)

        self.label_10 = QLabel(self.groupBox_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setTextFormat(Qt.RichText)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_10, 0, 1, 1, 1)

        self.label_12 = QLabel(self.groupBox_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(self.groupBox_6)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setFont(font)

        self.gridLayout_4.addWidget(self.lineEdit_11, 2, 2, 1, 1)

        self.lineEdit_13 = QLineEdit(self.groupBox_6)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setFont(font)

        self.gridLayout_4.addWidget(self.lineEdit_13, 3, 1, 1, 1)

        self.label_13 = QLabel(self.groupBox_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_13, 2, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_14, 0, 3, 1, 1)

        self.lineEdit_8 = QLineEdit(self.groupBox_6)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setFont(font)

        self.gridLayout_4.addWidget(self.lineEdit_8, 1, 2, 1, 1)

        self.label_15 = QLabel(self.groupBox_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_15, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.page4_ModelTraining)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(570, 20, 299, 150))
        self.groupBox_3.setMinimumSize(QSize(0, 150))
        self.groupBox_3.setMaximumSize(QSize(16777215, 200))
        self.groupBox_3.setStyleSheet(u"QGroupBox{\n"
"    border: 2px solid rgb(17, 17, 17);\n"
"    border-radius: 10px;\n"
"    margin-top: 0.5em;\n"
"	font-family: \"\u9ed1\u4f53\";\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.verticalLayout_28 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_28.setSpacing(6)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(9, 15, -1, 9)
        self.plainTextEdit = QPlainTextEdit(self.groupBox_3)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit {\n"
"    border-radius: 10px;\n"
"	border: none;\n"
"	background-color: #ffffff;\n"
"}\n"
"")

        self.verticalLayout_28.addWidget(self.plainTextEdit)

        self.stackedWidget.addWidget(self.page4_ModelTraining)
        self.page5_ResultAnalysis = QWidget()
        self.page5_ResultAnalysis.setObjectName(u"page5_ResultAnalysis")
        self.stackedWidget.addWidget(self.page5_ResultAnalysis)
        self.page6_FeatureGeneration = QWidget()
        self.page6_FeatureGeneration.setObjectName(u"page6_FeatureGeneration")
        self.stackedWidget.addWidget(self.page6_FeatureGeneration)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(False)
        font4.setItalic(False)
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout_18.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidgetMLRawData.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"DataPilot", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"ML GUI / Data Deep Explore", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_FeatureProcessing.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u5904\u7406", None))
        self.btn_FeatureSelection.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u9009\u62e9", None))
        self.btn_ModelTraining.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u8bad\u7ec3", None))
        self.btn_ResultAnalysis.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u679c\u5206\u6790", None))
        self.btn_FeatureGeneration.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u751f\u6210", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zen"
                        "o Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"DataPilot", None))
        self.btn_theme.setText("")
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.btn_downloadDatabase.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u70b9\u51fb\u4e0b\u8f7d\u6570\u636e</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_downloadDatabase.setText(QCoreApplication.translate("MainWindow", u"\u6676\u4f53\u7ed3\u6784", None))
#if QT_CONFIG(tooltip)
        self.btn_videoTutorial.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u70b9\u51fb\u64ad\u653e\u89c6\u9891\u6559\u7a0b</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_videoTutorial.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u6559\u7a0b", None))
        self.lineedit_imported_filename.setText("")
        self.lineedit_imported_filename.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.btn_open_local_file.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.btn_FeatureProcessing_2.setText(QCoreApplication.translate("MainWindow", u"FeatureProcessing", None))
        self.label_missing_values_handling.setText(QCoreApplication.translate("MainWindow", u"\u7f3a\u5931\u503c\u5904\u7406\uff1a", None))
        self.combobox_missing_values_handling.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5e73\u5747\u503c\u586b\u5145", None))
        self.combobox_missing_values_handling.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e2d\u4f4d\u6570\u586b\u5145", None))
        self.combobox_missing_values_handling.setItemText(2, QCoreApplication.translate("MainWindow", u"\u4f17\u6570\u586b\u5145", None))
        self.combobox_missing_values_handling.setItemText(3, QCoreApplication.translate("MainWindow", u"\u56fa\u5b9a\u503c\u586b\u5145", None))
        self.combobox_missing_values_handling.setItemText(4, QCoreApplication.translate("MainWindow", u"\u6700\u8fd1\u90bb\u586b\u5145", None))
        self.combobox_missing_values_handling.setItemText(5, QCoreApplication.translate("MainWindow", u"\u5220\u9664\u6574\u884c", None))
        self.combobox_missing_values_handling.setItemText(6, QCoreApplication.translate("MainWindow", u"\u5220\u9664\u6574\u5217", None))
        self.combobox_missing_values_handling.setItemText(7, QCoreApplication.translate("MainWindow", u"\u4e0d\u5904\u7406", None))

        self.label_outlier_handling.setText(QCoreApplication.translate("MainWindow", u"\u5f02\u5e38\u503c\u5904\u7406\uff1a", None))
        self.combobox_outlier_handling.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5e73\u5747\u503c\u586b\u5145", None))
        self.combobox_outlier_handling.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e2d\u4f4d\u6570\u586b\u5145", None))
        self.combobox_outlier_handling.setItemText(2, QCoreApplication.translate("MainWindow", u"\u4f17\u6570\u586b\u5145", None))
        self.combobox_outlier_handling.setItemText(3, QCoreApplication.translate("MainWindow", u"\u5220\u9664\u6574\u884c", None))
        self.combobox_outlier_handling.setItemText(4, QCoreApplication.translate("MainWindow", u"\u5220\u9664\u6574\u5217", None))
        self.combobox_outlier_handling.setItemText(5, QCoreApplication.translate("MainWindow", u"\u4e0d\u5904\u7406", None))

        self.label_categorical_handling.setText(QCoreApplication.translate("MainWindow", u"\u79bb\u6563\u503c\u5904\u7406\uff1a", None))
        self.combobox_categorical_handling.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6807\u7b7e\u7f16\u7801\uff08Label Encoding\uff09", None))
        self.combobox_categorical_handling.setItemText(1, QCoreApplication.translate("MainWindow", u"\u72ec\u70ed\u7f16\u7801\uff08One-Hot Encoding\uff09", None))
        self.combobox_categorical_handling.setItemText(2, QCoreApplication.translate("MainWindow", u"\u4e8c\u8fdb\u5236\u7f16\u7801\uff08Binary Encoding\uff09", None))
        self.combobox_categorical_handling.setItemText(3, QCoreApplication.translate("MainWindow", u"\u79bb\u6563\u54c8\u5e0c\uff08Feature Hashing\uff09", None))
        self.combobox_categorical_handling.setItemText(4, QCoreApplication.translate("MainWindow", u"\u5d4c\u5165\u65b9\u6cd5\uff08Embeddings\uff09", None))
        self.combobox_categorical_handling.setItemText(5, QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u7f16\u7801\uff08Target Encoding\uff09", None))
        self.combobox_categorical_handling.setItemText(6, QCoreApplication.translate("MainWindow", u"\u4e0d\u5904\u7406", None))

        self.label_data_normalization_handling.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5f52\u4e00\u5316\uff1a", None))
        self.combobox_data_normalization_handling.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6700\u5c0f\u6700\u5927\u5f52\u4e00\u5316", None))
        self.combobox_data_normalization_handling.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5747\u503c\u5f52\u4e00\u5316", None))
        self.combobox_data_normalization_handling.setItemText(2, QCoreApplication.translate("MainWindow", u"\u6807\u51c6\u5316", None))
        self.combobox_data_normalization_handling.setItemText(3, QCoreApplication.translate("MainWindow", u"\u6700\u5927\u7edd\u5bf9\u503c\u5f52\u4e00\u5316", None))
        self.combobox_data_normalization_handling.setItemText(4, QCoreApplication.translate("MainWindow", u"\u9c81\u68d2\u5f52\u4e00\u5316", None))
        self.combobox_data_normalization_handling.setItemText(5, QCoreApplication.translate("MainWindow", u"\u4e0d\u5904\u7406", None))

        self.tabWidgetMLRawData.setTabText(self.tabWidgetMLRawData.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"\u539f\u59cb\u6570\u636e", None))
        self.tabWidgetMLRawData.setTabText(self.tabWidgetMLRawData.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u7f3a\u5931\u503c\u5904\u7406\u540e", None))
        self.tabWidgetMLRawData.setTabText(self.tabWidgetMLRawData.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u5f02\u5e38\u503c\u5904\u7406\u540e", None))
        self.tabWidgetMLRawData.setTabText(self.tabWidgetMLRawData.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u79bb\u6563\u503c\u5904\u7406\u540e", None))
        self.tabWidgetMLRawData.setTabText(self.tabWidgetMLRawData.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5f52\u4e00\u5316\u540e", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u8fc7\u6ee4\u6cd5\uff08Filter methods\uff09", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u5305\u88f9\u6cd5\uff08Wrapper methods\uff09", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"\u5d4c\u5165\u6cd5\uff08Embedded methods\uff09", None))
        ___qtreewidgetitem = self.treeWidget_featureSelection.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u9009\u62e9", None));

        __sortingEnabled = self.treeWidget_featureSelection.isSortingEnabled()
        self.treeWidget_featureSelection.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget_featureSelection.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Filter\u8fc7\u6ee4\u6cd5", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"\u65b9\u5dee\u8fc7\u6ee4", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"\u76f8\u5173\u6027\u8fc7\u6ee4", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem3.child(0)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"\u5361\u65b9\u8fc7\u6ee4", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem3.child(1)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"F\u68c0\u9a8c", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem3.child(2)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"\u4e92\u4fe1\u606f\u6cd5", None));
        ___qtreewidgetitem7 = self.treeWidget_featureSelection.topLevelItem(1)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"Embedded\u5d4c\u5165\u6cd5", None));
        ___qtreewidgetitem8 = self.treeWidget_featureSelection.topLevelItem(2)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"Wrapper\u5305\u88c5\u6cd5", None));
        self.treeWidget_featureSelection.setSortingEnabled(__sortingEnabled)

        self.btn_eatureSelection.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u7b5b\u9009", None))
        self.tabWidget_FeatureSelectionData.setTabText(self.tabWidget_FeatureSelectionData.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget_FeatureSelectionData.setTabText(self.tabWidget_FeatureSelectionData.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        ___qtreewidgetitem9 = self.treeWidget.headerItem()
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"\u7b97\u6cd5\u9009\u62e9", None));

        __sortingEnabled1 = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem10 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"\u56de\u5f52", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem10.child(0)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"\u7ebf\u6027\u56de\u5f52 (Linear Regression)", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem10.child(1)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"\u5cad\u56de\u5f52 (Ridge Regression)", None));
        ___qtreewidgetitem13 = ___qtreewidgetitem10.child(2)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MainWindow", u"\u5957\u7d22\u56de\u5f52 (Lasso Regression)", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem10.child(3)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MainWindow", u"\u5f39\u6027\u7f51\u7edc (Elastic Net)", None));
        ___qtreewidgetitem15 = ___qtreewidgetitem10.child(4)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MainWindow", u"\u51b3\u7b56\u6811\u56de\u5f52 (Decision Tree Regression)", None));
        ___qtreewidgetitem16 = ___qtreewidgetitem10.child(5)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MainWindow", u"\u968f\u673a\u68ee\u6797\u56de\u5f52 (Random Forest Regression)", None));
        ___qtreewidgetitem17 = ___qtreewidgetitem10.child(6)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MainWindow", u"\u68af\u5ea6\u63d0\u5347\u56de\u5f52\u6811 (Gradient Boosting Regression Trees\uff0cGBRT)", None));
        ___qtreewidgetitem18 = ___qtreewidgetitem10.child(7)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("MainWindow", u"\u652f\u6301\u5411\u91cf\u673a\u56de\u5f52 (Support Vector Machine Regression\uff0cSVMR)", None));
        ___qtreewidgetitem19 = ___qtreewidgetitem10.child(8)
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("MainWindow", u"\u795e\u7ecf\u7f51\u7edc\u56de\u5f52 (Neural Networks Regression)", None));
        ___qtreewidgetitem20 = ___qtreewidgetitem10.child(9)
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("MainWindow", u"K\u8fd1\u90bb\u56de\u5f52 (K-Nearest Neighbors Regression\uff0cKNN)", None));
        ___qtreewidgetitem21 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("MainWindow", u"\u5206\u7c7b", None));
        ___qtreewidgetitem22 = ___qtreewidgetitem21.child(0)
        ___qtreewidgetitem22.setText(0, QCoreApplication.translate("MainWindow", u"\u903b\u8f91\u56de\u5f52 (Logistic Regression)", None));
        ___qtreewidgetitem23 = ___qtreewidgetitem21.child(1)
        ___qtreewidgetitem23.setText(0, QCoreApplication.translate("MainWindow", u"K\u8fd1\u90bb\u5206\u7c7b (K-Nearest Neighbors\uff0cKNN)", None));
        ___qtreewidgetitem24 = ___qtreewidgetitem21.child(2)
        ___qtreewidgetitem24.setText(0, QCoreApplication.translate("MainWindow", u"\u652f\u6301\u5411\u91cf\u673a (Support Vector Machine\uff0cSVM)", None));
        ___qtreewidgetitem25 = ___qtreewidgetitem21.child(3)
        ___qtreewidgetitem25.setText(0, QCoreApplication.translate("MainWindow", u"\u51b3\u7b56\u6811 (Decision Tree)", None));
        ___qtreewidgetitem26 = ___qtreewidgetitem21.child(4)
        ___qtreewidgetitem26.setText(0, QCoreApplication.translate("MainWindow", u"\u968f\u673a\u68ee\u6797 (Random Forest)", None));
        ___qtreewidgetitem27 = ___qtreewidgetitem21.child(5)
        ___qtreewidgetitem27.setText(0, QCoreApplication.translate("MainWindow", u"\u68af\u5ea6\u63d0\u5347\u6811 (Gradient Boosting Trees)", None));
        ___qtreewidgetitem28 = ___qtreewidgetitem21.child(6)
        ___qtreewidgetitem28.setText(0, QCoreApplication.translate("MainWindow", u"\u6734\u7d20\u8d1d\u53f6\u65af (Naive Bayes)", None));
        ___qtreewidgetitem29 = ___qtreewidgetitem21.child(7)
        ___qtreewidgetitem29.setText(0, QCoreApplication.translate("MainWindow", u"\u795e\u7ecf\u7f51\u7edc (Neural Networks)", None));
        ___qtreewidgetitem30 = ___qtreewidgetitem21.child(8)
        ___qtreewidgetitem30.setText(0, QCoreApplication.translate("MainWindow", u"AdaBoost", None));
        ___qtreewidgetitem31 = ___qtreewidgetitem21.child(9)
        ___qtreewidgetitem31.setText(0, QCoreApplication.translate("MainWindow", u"XGBoost", None));
        ___qtreewidgetitem32 = ___qtreewidgetitem21.child(10)
        ___qtreewidgetitem32.setText(0, QCoreApplication.translate("MainWindow", u"LightGBM", None));
        ___qtreewidgetitem33 = ___qtreewidgetitem21.child(11)
        ___qtreewidgetitem33.setText(0, QCoreApplication.translate("MainWindow", u"CatBoost", None));
        ___qtreewidgetitem34 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem34.setText(0, QCoreApplication.translate("MainWindow", u"\u964d\u7ef4", None));
        ___qtreewidgetitem35 = ___qtreewidgetitem34.child(0)
        ___qtreewidgetitem35.setText(0, QCoreApplication.translate("MainWindow", u"\u4e3b\u6210\u5206\u5206\u6790 (Principal Component Analysis\uff0cPCA)", None));
        ___qtreewidgetitem36 = ___qtreewidgetitem34.child(1)
        ___qtreewidgetitem36.setText(0, QCoreApplication.translate("MainWindow", u"\u7ebf\u6027\u5224\u522b\u5206\u6790 (Linear Discriminant Analysis\uff0cLDA)", None));
        ___qtreewidgetitem37 = ___qtreewidgetitem34.child(2)
        ___qtreewidgetitem37.setText(0, QCoreApplication.translate("MainWindow", u"t-\u5206\u5e03\u968f\u673a\u90bb\u57df\u5d4c\u5165 (t-Distributed Stochastic Neighbor Embedding\uff0ct-SNE)", None));
        ___qtreewidgetitem38 = ___qtreewidgetitem34.child(3)
        ___qtreewidgetitem38.setText(0, QCoreApplication.translate("MainWindow", u"\u56e0\u5b50\u5206\u6790 (Factor Analysis)", None));
        ___qtreewidgetitem39 = ___qtreewidgetitem34.child(4)
        ___qtreewidgetitem39.setText(0, QCoreApplication.translate("MainWindow", u"\u72ec\u7acb\u6210\u5206\u5206\u6790 (Independent Component Analysis\uff0cICA)", None));
        ___qtreewidgetitem40 = ___qtreewidgetitem34.child(5)
        ___qtreewidgetitem40.setText(0, QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u7f16\u7801\u5668 (Autoencoders)", None));
        ___qtreewidgetitem41 = ___qtreewidgetitem34.child(6)
        ___qtreewidgetitem41.setText(0, QCoreApplication.translate("MainWindow", u"\u591a\u7ef4\u5c3a\u5ea6\u7f29\u51cf (Multidimensional Scaling\uff0cMDS)", None));
        ___qtreewidgetitem42 = ___qtreewidgetitem34.child(7)
        ___qtreewidgetitem42.setText(0, QCoreApplication.translate("MainWindow", u"UMAP (Uniform Manifold Approximation and Projection)", None));
        ___qtreewidgetitem43 = self.treeWidget.topLevelItem(3)
        ___qtreewidgetitem43.setText(0, QCoreApplication.translate("MainWindow", u"\u805a\u7c7b", None));
        ___qtreewidgetitem44 = ___qtreewidgetitem43.child(0)
        ___qtreewidgetitem44.setText(0, QCoreApplication.translate("MainWindow", u"K\u5747\u503c\u805a\u7c7b (K-Means Clustering)", None));
        ___qtreewidgetitem45 = ___qtreewidgetitem43.child(1)
        ___qtreewidgetitem45.setText(0, QCoreApplication.translate("MainWindow", u"\u5c42\u6b21\u805a\u7c7b (HierarchicalClustering)", None));
        ___qtreewidgetitem46 = ___qtreewidgetitem43.child(2)
        ___qtreewidgetitem46.setText(0, QCoreApplication.translate("MainWindow", u"DBSCAN (Density-Based Spatial Clustering of Applications with Noise)", None));
        ___qtreewidgetitem47 = ___qtreewidgetitem43.child(3)
        ___qtreewidgetitem47.setText(0, QCoreApplication.translate("MainWindow", u"\u9ad8\u65af\u6df7\u5408\u6a21\u578b (Gaussian Mixture Models\uff0cGMM)", None));
        ___qtreewidgetitem48 = ___qtreewidgetitem43.child(4)
        ___qtreewidgetitem48.setText(0, QCoreApplication.translate("MainWindow", u"\u5149\u8c31\u805a\u7c7b (SpectralClustering)", None));
        ___qtreewidgetitem49 = ___qtreewidgetitem43.child(5)
        ___qtreewidgetitem49.setText(0, QCoreApplication.translate("MainWindow", u"\u5747\u503c\u6f02\u79fb\u805a\u7c7b (Mean Shift Clustering)", None));
        ___qtreewidgetitem50 = ___qtreewidgetitem43.child(6)
        ___qtreewidgetitem50.setText(0, QCoreApplication.translate("MainWindow", u"\u5bc6\u5ea6\u5cf0\u503c\u805a\u7c7b (Density Peak Clustering)", None));
        ___qtreewidgetitem51 = ___qtreewidgetitem43.child(7)
        ___qtreewidgetitem51.setText(0, QCoreApplication.translate("MainWindow", u"\u81ea\u7ec4\u7ec7\u6620\u5c04 (Self-Organizing Maps\uff0cSOM)", None));
        ___qtreewidgetitem52 = ___qtreewidgetitem43.child(8)
        ___qtreewidgetitem52.setText(0, QCoreApplication.translate("MainWindow", u"OPTICS (Ordering Points To ldentify the Clustering Structure)", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled1)

        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u4ea4\u53c9\u9a8c\u8bc1", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u7559\u51fa\u4ea4\u53c9\u9a8c\u8bc1", None))
#if QT_CONFIG(tooltip)
        self.radioButton_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u8bbe\u4e3a</span><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">1</span><span style=\" font-size:12pt;\">\u5c06\u8fdb\u884c\u7559\u4e00\u6cd5\u4ea4\u53c9\u9a8c\u8bc1\uff0c\u5927\u4e8e1\u5c06\u8fdb\u884c\u7559P\u6cd5\u4ea4\u53c9\u9a8c\u8bc1\u3002</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u75591/P\u6cd5\u4ea4\u53c9\u9a8c\u8bc1", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"K\u6298\u4ea4\u53c9\u9a8c\u8bc1", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"\u5206\u5c42\u4ea4\u53c9\u9a8c\u8bc1", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5212\u5206", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u72ec\u7acb\u6d4b\u8bd5\u96c6\u5927\u5c0f:", None))
#if QT_CONFIG(tooltip)
        self.checkBox_5.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">shuffle\u53c2\u6570\u53ef\u4ee5\u7528\u6765\u63a7\u5236\u8bad\u7ec3\u6570\u636e\u7684\u987a\u5e8f\u662f\u5426\u6253\u4e71\u3002\u5728\u673a\u5668\u5b66\u4e60\u4e2d\uff0c\u6253\u4e71\u8bad\u7ec3\u6570\u636e\u7684\u987a\u5e8f\u53ef\u4ee5\u5e2e\u52a9\u6a21\u578b\u66f4\u597d\u5730\u5b66\u4e60\u7279\u5f81\u548c\u907f\u514d\u51fa\u73b0\u8fc7\u62df\u5408\u7684\u95ee\u9898.\u5f53shuffle\u53c2\u6570\u8bbe\u7f6e\u4e3aTrue\u65f6\uff0c\u8bad\u7ec3\u6570\u636e\u4f1a\u88ab\u968f\u673a\u6253\u4e71\uff0c\u5426\u5219\u8bad\u7ec3\u6570\u636e\u4f1a\u6309\u7167\u539f\u59cb\u987a\u5e8f\u4f7f\u7528\u3002</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Shuffle", None))
#if QT_CONFIG(tooltip)
        self.checkBox_6.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">random_seed\u662f\u4e3arandom_state\u53c2\u6570\u63d0\u4f9b\u4e00\u4e2a\u968f\u673a\u79cd\u5b50\uff0c\u4e3a\u4e86\u63a7\u5236\u6bcf\u6b21\u751f\u6210\u7684\u968f\u673a\u6570\u76f8\u540c\uff0c\u4fdd\u8bc1\u7ed3\u679c\u7684\u53ef\u91cd\u590d\u6027\u3002\u5728\u67d0\u4e9b\u60c5\u51b5\u4e0b\uff0c\u6211\u4eec\u9700\u8981\u591a\u6b21\u8fd0\u884c\u76f8\u540c\u7684\u4ee3\u7801\uff0c\u4ee5\u5f97\u5230\u5e73\u5747\u7ed3\u679c\u6216\u5bf9\u7ed3\u679c\u8fdb\u884c\u6bd4\u8f83\u3002\u5982\u679c\u4e0d\u8bbe\u7f6erandom_state\u53c2\u6570\uff0c\u6bcf\u6b21\u751f\u6210\u7684\u968f\u673a\u6570\u5c06\u4e0d\u540c\uff0c\u8fd9\u6837\u5c31\u65e0\u6cd5\u4fdd\u8bc1\u7ed3\u679c\u7684\u4e00\u81f4\u6027\u3002</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"Random_seed", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"Save model", None))
#if QT_CONFIG(tooltip)
        self.checkBox_8.setToolTip(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Z-score\u6807\u51c6\u5316(Standardization)\uff1a\u5c06\u6570\u636e\u7f29\u653e\u5230\u5747\u503c\u4e3a0\uff0c\u6807\u51c6\u5dee\u4e3a1\u7684\u6b63\u6001\u5206\u5e03\u3002\u5bf9\u4e8e\u6bcf\u4e2a\u7279\u5f81\uff0c\u5c06\u539f\u59cb\u503c\u51cf\u53bb\u5747\u503c\uff0c\u7136\u540e\u9664\u4ee5\u6807\u51c6\u5dee\u3002</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"Z-score", None))
#if QT_CONFIG(tooltip)
        self.checkBox_9.setToolTip(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u6700\u5c0f-\u6700\u5927\u89c4\u8303\u5316(Min-Max Scaling)\uff1a\u5c06\u6570\u636e\u7f29\u653e\u5230[0,1]\u7684\u8303\u56f4\u5185\u3002\u5bf9\u4e8e\u6bcf\u4e2a\u7279\u5f81\uff0c\u5c06\u539f\u59cb\u503c\u51cf\u53bb\u6700\u5c0f\u503c\uff0c\u7136\u540e\u9664\u4ee5\u6700\u5927\u503c\u548c\u6700\u5c0f\u503c\u4e4b\u5dee\u3002</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"MinMax", None))
#if QT_CONFIG(tooltip)
        self.checkBox_10.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">MaxAbsScaler\uff1a\u9996\u5148\u8ba1\u7b97\u6bcf\u4e2a\u7279\u5f81\u7684\u6700\u5927\u7edd\u5bf9\u503c\uff0c\u518d\u5c06\u6bcf\u4e2a\u7279\u5f81\u9664\u4ee5\u5176\u6700\u5927\u503c\u7edd\u5bf9\u503c\uff0c\u4ece\u800c\u5c06\u7279\u5f81\u7f29\u653e\u5230[-1,1]\u4e4b\u95f4\u3002\u8fd9\u79cd\u7f29\u653e\u65b9\u5f0f\u4fdd\u7559\u4e86\u7279\u5f81\u7684\u7b26\u53f7\u4fe1\u606f\uff0c\u4e14\u4e0d\u4f1a\u7834\u574f\u6570\u636e\u7684\u7a00\u758f\u6027\u3002</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"MaxAbs", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u9884\u6d4b\u63a7\u5236", None))
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">\u9700\u8981\u6ce8\u610f\u7684\u662f\uff0c\u8fd9\u4e2a\u53c2\u6570\u53ea\u5728\u6570\u636e\u91cf\u5f88\u5927\u65f6\u624d\u4f1a\u6709\u6548\u679c\uff0c\u5bf9\u4e8e\u8f83\u5c0f\u7684\u6570\u636e\u96c6\uff0c\u4f7f\u7528\u591a\u6838\u53cd\u800c\u4f1a\u5bfc\u81f4\u7a0b\u5e8f\u8fd0\u884c\u53d8\u6162\u3002\u53e6\u5916\uff0c\u6709\u4e9b\u7b97\u6cd5\u672c\u8eab\u5e76\u4e0d\u652f\u6301\u5e76\u884c\u8ba1\u7b97\uff0c\u6b64\u65f6\u8bbe\u7f6en_jobs\u4e5f\u4e0d\u4f1a\u8d77\u5230\u52a0\u901f\u7684\u4f5c\u7528\u3002<br/></span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"CV\u542f\u52a8\u7684CPU\u6838\u5fc3\u6570:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u9884\u6d4b\u5f97\u5206", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"MAE", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"R2", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Metric", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Validation", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"RMSE", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Training", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u8bbe\u7f6e", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: liyihang", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

