# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_featureSelectionEmHXTT.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MdiSubW_featureSelection(object):
    def setupUi(self, MdiSubW_featureSelection):
        if not MdiSubW_featureSelection.objectName():
            MdiSubW_featureSelection.setObjectName(u"MdiSubW_featureSelection")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MdiSubW_featureSelection.sizePolicy().hasHeightForWidth())
        MdiSubW_featureSelection.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(MdiSubW_featureSelection)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.treeWidget_featureSelection = QTreeWidget(MdiSubW_featureSelection)
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
        self.treeWidget_featureSelection.setMinimumSize(QSize(0, 0))

        self.verticalLayout_30.addWidget(self.treeWidget_featureSelection)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_featureSelection = QPushButton(MdiSubW_featureSelection)
        self.btn_featureSelection.setObjectName(u"btn_featureSelection")

        self.horizontalLayout_8.addWidget(self.btn_featureSelection)

        self.btn_correlationAnalysis = QPushButton(MdiSubW_featureSelection)
        self.btn_correlationAnalysis.setObjectName(u"btn_correlationAnalysis")

        self.horizontalLayout_8.addWidget(self.btn_correlationAnalysis)

        self.btn_importanceRanking = QPushButton(MdiSubW_featureSelection)
        self.btn_importanceRanking.setObjectName(u"btn_importanceRanking")

        self.horizontalLayout_8.addWidget(self.btn_importanceRanking)


        self.verticalLayout_30.addLayout(self.horizontalLayout_8)


        self.verticalLayout.addLayout(self.verticalLayout_30)


        self.retranslateUi(MdiSubW_featureSelection)

        QMetaObject.connectSlotsByName(MdiSubW_featureSelection)
    # setupUi

    def retranslateUi(self, MdiSubW_featureSelection):
        MdiSubW_featureSelection.setWindowTitle(QCoreApplication.translate("MdiSubW_featureSelection", u"Form", None))
        ___qtreewidgetitem = self.treeWidget_featureSelection.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MdiSubW_featureSelection", u"\u7279\u5f81\u9009\u62e9", None));

        __sortingEnabled = self.treeWidget_featureSelection.isSortingEnabled()
        self.treeWidget_featureSelection.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget_featureSelection.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MdiSubW_featureSelection", u"Filter\u8fc7\u6ee4\u6cd5", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MdiSubW_featureSelection", u"\u65b9\u5dee\u8fc7\u6ee4", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MdiSubW_featureSelection", u"\u76f8\u5173\u6027\u8fc7\u6ee4", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem3.child(0)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MdiSubW_featureSelection", u"\u5361\u65b9\u8fc7\u6ee4", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem3.child(1)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MdiSubW_featureSelection", u"F\u68c0\u9a8c", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem3.child(2)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MdiSubW_featureSelection", u"\u4e92\u4fe1\u606f\u6cd5", None));
        ___qtreewidgetitem7 = self.treeWidget_featureSelection.topLevelItem(1)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MdiSubW_featureSelection", u"Embedded\u5d4c\u5165\u6cd5", None));
        ___qtreewidgetitem8 = self.treeWidget_featureSelection.topLevelItem(2)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MdiSubW_featureSelection", u"Wrapper\u5305\u88c5\u6cd5", None));
        self.treeWidget_featureSelection.setSortingEnabled(__sortingEnabled)

        self.btn_featureSelection.setText(QCoreApplication.translate("MdiSubW_featureSelection", u"\u7279\u5f81\u7b5b\u9009", None))
        self.btn_correlationAnalysis.setText(QCoreApplication.translate("MdiSubW_featureSelection", u"\u76f8\u5173\u6027\u5206\u6790", None))
        self.btn_importanceRanking.setText(QCoreApplication.translate("MdiSubW_featureSelection", u"\u91cd\u8981\u6027\u6392\u5e8f", None))
    # retranslateUi

