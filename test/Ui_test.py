# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1031, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.row_1 = QFrame(self.centralwidget)
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
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.btn_open_local_file.setFont(font)
        self.btn_open_local_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open_local_file.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open_local_file.setIcon(icon)

        self.gridLayout.addWidget(self.btn_open_local_file, 0, 0, 1, 1)

        self.btn_FeatureProcessing = QPushButton(self.frame_content_wid_1)
        self.btn_FeatureProcessing.setObjectName(u"btn_FeatureProcessing")
        self.btn_FeatureProcessing.setMinimumSize(QSize(150, 30))
        self.btn_FeatureProcessing.setFont(font)
        self.btn_FeatureProcessing.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_FeatureProcessing.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-data-process.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_FeatureProcessing.setIcon(icon1)

        self.gridLayout.addWidget(self.btn_FeatureProcessing, 0, 2, 1, 1)


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

        self.horizontalLayout_7.addWidget(self.label_data_normalization_handling)

        self.combobox_data_normalization_handling = QComboBox(self.frame_title_wid_1)
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
"    background: lightgray;\n"
"    border: 2px solid gray;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: white;\n"
"    border-color: #9B9B9B;\n"
"	font-weight: bold;\n"
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

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1031, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidgetMLRawData.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineedit_imported_filename.setText("")
        self.lineedit_imported_filename.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.btn_open_local_file.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.btn_FeatureProcessing.setText(QCoreApplication.translate("MainWindow", u"FeatureProcessing", None))
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
        self.combobox_outlier_handling.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5747\u503c\u586b\u5145", None))
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
        self.combobox_data_normalization_handling.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6700\u5c0f-\u6700\u5927\u5f52\u4e00\u5316\uff08Min-Max Normalization\uff09", None))
        self.combobox_data_normalization_handling.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6807\u51c6\u5316\uff08Z-score Normalization\uff09", None))
        self.combobox_data_normalization_handling.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5747\u503c\u5f52\u4e00\u5316\uff08Mean Normalization\uff09", None))
        self.combobox_data_normalization_handling.setItemText(3, QCoreApplication.translate("MainWindow", u"\u4e0d\u5904\u7406", None))

        self.tabWidgetMLRawData.setTabText(self.tabWidgetMLRawData.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"\u539f\u59cb\u6570\u636e", None))
        self.tabWidgetMLRawData.setTabText(self.tabWidgetMLRawData.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u7f3a\u5931\u503c\u5904\u7406\u540e", None))
        self.tabWidgetMLRawData.setTabText(self.tabWidgetMLRawData.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u5f02\u5e38\u503c\u5904\u7406\u540e", None))
        self.tabWidgetMLRawData.setTabText(self.tabWidgetMLRawData.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u79bb\u6563\u503c\u5904\u7406\u540e", None))
        self.tabWidgetMLRawData.setTabText(self.tabWidgetMLRawData.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5f52\u4e00\u5316\u540e", None))
    # retranslateUi

