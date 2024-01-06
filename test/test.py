import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QTabWidget, QTableWidget, QTableWidgetItem, 
                               QMenu, QFileDialog, QHBoxLayout, QWidget)
import pandas as pd

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个TabWidget
        self.tab_widget = QTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        # 第一个TableWidget的水平布局
        horizontal_layout1 = QHBoxLayout()
        self.empty_table = QTableWidget(0, 3)  # 0行3列
        self.empty_table.setObjectName("empty_table")  # 设置对象名称
        horizontal_layout1.addWidget(self.empty_table)
        empty_tab = QWidget()
        empty_tab.setLayout(horizontal_layout1)
        self.tab_widget.addTab(empty_tab, "水平布局的空TableWidget")

        # 第二个TableWidget的水平布局
        horizontal_layout2 = QHBoxLayout()
        self.filled_table = QTableWidget(3, 3)  # 3行3列
        self.filled_table.setObjectName("filled_table")  # 设置对象名称
        self.fill_data(self.filled_table)  # 填充数据
        horizontal_layout2.addWidget(self.filled_table)
        filled_tab = QWidget()
        filled_tab.setLayout(horizontal_layout2)
        self.tab_widget.addTab(filled_tab, "水平布局填充了数据的TableWidget")

    def fill_data(self, table_widget):
        """填充数据到TableWidget"""
        for row in range(3):
            for col in range(3):
                item = QTableWidgetItem(f"Item {row},{col}")
                table_widget.setItem(row, col, item)

    def contextMenuEvent(self, event):
        """重写contextMenuEvent来提供自定义的右键菜单。"""
        tab = self.tab_widget.currentWidget()
        # 查找嵌入在QWidget中的QTableWidget
        table_widget = tab.findChild(QTableWidget)
        if table_widget and not self.is_table_empty(table_widget):
            menu = QMenu(self)
            export_action = menu.addAction("导出数据")
            export_action.triggered.connect(lambda: self.export_data(table_widget))
            menu.exec(event.globalPos())

    def is_table_empty(self, table_widget):
        """检查指定的QTableWidget是否为空。"""
        return table_widget.rowCount() == 0 or table_widget.columnCount() == 0

    def export_data(self, table_widget):
        """从table_widget中导出数据到指定的文件。"""
        file_name, _ = QFileDialog.getSaveFileName(self, "保存文件", "", "Excel Files (*.xlsx);;CSV Files (*.csv)")
        if file_name:
            data = []
            for row in range(table_widget.rowCount()):
                row_data = []
                for col in range(table_widget.columnCount()):
                    item = table_widget.item(row, col)
                    row_data.append(item.text() if item else "")
                data.append(row_data)
            df = pd.DataFrame(data)
            if file_name.endswith('.xlsx'):
                df.to_excel(file_name, index=False)
            elif file_name.endswith('.csv'):
                df.to_csv(file_name, index=False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
