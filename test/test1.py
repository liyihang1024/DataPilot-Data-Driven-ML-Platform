import sys
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from PySide6.QtGui import QAction, QIcon, QCursor

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox, QTableWidget, QTabWidget, QMenu
from PySide6.QtCore import Qt, QThread, Signal, QFile, QPoint
from Ui_test1 import Ui_MainWindow  # 从你的UI模块导入Ui_MainWindow

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QFileDialog
# 假设你已经有了上面的 Ui_MainWindow 类定义

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # 填充数据到第一个表格
        self.tableWidget.setRowCount(2)  # 仅作为示例，实际行数依据数据而定
        self.tableWidget.setColumnCount(3)  # 仅作为示例，实际列数依据数据而定
        for i in range(2):
            for j in range(3):
                item = QTableWidgetItem(f"Item {i},{j}")
                self.tableWidget.setItem(i, j, item)

        # 右键点击事件
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.show_context_menu)

    def show_context_menu(self, pos):
        # 检查当前表是否为空
        if self.tableWidget.rowCount() > 0:
            context_menu = QMenu(self)
            export_action = context_menu.addAction("Export Data")
            action = context_menu.exec(self.tableWidget.mapToGlobal(pos))
            if action == export_action:
                self.export_data()

    def export_data(self):
        # 选择保存文件的位置
        path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "CSV Files (*.csv)")
        if path:
            with open(path, 'w') as file:
                for row in range(self.tableWidget.rowCount()):
                    row_data = []
                    for column in range(self.tableWidget.columnCount()):
                        item = self.tableWidget.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                    file.write(','.join(row_data) + '\n')
            print(f"Data exported successfully to {path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
