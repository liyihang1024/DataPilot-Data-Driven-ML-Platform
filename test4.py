import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem,
                               QTabWidget, QPushButton, QVBoxLayout, QWidget)
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QHBoxLayout
from PySide6.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建主布局
        layout = QVBoxLayout()

        # 创建TreeWidget
        self.tree = QTreeWidget()
        self.tree.setHeaderLabel('特征选择')

        # 创建树形结构的顶级项目
        filter_method = QTreeWidgetItem(self.tree)
        filter_method.setText(0, 'Filter过滤法')
        filter_method.setFlags(filter_method.flags() | Qt.ItemIsUserCheckable)
        filter_method.setCheckState(0, Qt.Unchecked)

        embedded_method = QTreeWidgetItem(self.tree)
        embedded_method.setText(0, 'Embedded嵌入法')
        embedded_method.setFlags(embedded_method.flags() | Qt.ItemIsUserCheckable)
        embedded_method.setCheckState(0, Qt.Unchecked)

        wrapper_method = QTreeWidgetItem(self.tree)
        wrapper_method.setText(0, 'Wrapper包装法')
        wrapper_method.setFlags(wrapper_method.flags() | Qt.ItemIsUserCheckable)
        wrapper_method.setCheckState(0, Qt.Unchecked)

        # 创建子项目
        corr_filter = QTreeWidgetItem(filter_method)
        corr_filter.setText(0, '相关性过滤')
        corr_filter.setFlags(corr_filter.flags() | Qt.ItemIsUserCheckable)
        corr_filter.setCheckState(0, Qt.Unchecked)

        # 创建相关性过滤的子项目
        chi_squared = QTreeWidgetItem(corr_filter)
        chi_squared.setText(0, '卡方过滤')
        chi_squared.setFlags(chi_squared.flags() | Qt.ItemIsUserCheckable)
        chi_squared.setCheckState(0, Qt.Unchecked)

        f_test = QTreeWidgetItem(corr_filter)
        f_test.setText(0, 'F检验')
        f_test.setFlags(f_test.flags() | Qt.ItemIsUserCheckable)
        f_test.setCheckState(0, Qt.Unchecked)

        mutual_info = QTreeWidgetItem(corr_filter)
        mutual_info.setText(0, '互信息法')
        mutual_info.setFlags(mutual_info.flags() | Qt.ItemIsUserCheckable)
        mutual_info.setCheckState(0, Qt.Unchecked)

        # 创建TabWidget
        self.tabs = QTabWidget()

        # 创建按钮
        self.button = QPushButton('Add Tabs')
        self.button.clicked.connect(self.add_tabs)

        # 将组件添加到布局中
        layout.addWidget(self.tree)
        layout.addWidget(self.tabs)
        layout.addWidget(self.button)

        # 设置主窗口的中心部件
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.selected_items = []  # 用于存储所有被选中的项目

    def add_tabs(self):
        self.tabs.clear()
        self.selected_items.clear()  # 清空之前的选中项目
        a = self.add_tabs_recursive(self.tree.invisibleRootItem())
        print(a)
        # 可以在这里调用新线程处理selected_items
        # self.process_selected_items()

    def add_tabs_recursive(self, tree_item):
        for i in range(tree_item.childCount()):
            child = tree_item.child(i)
            if child.checkState(0) == Qt.Checked:
                self.selected_items.append(child.text(0))  # 添加到选中项目列表中
                self.create_tab(child)  # 使用封装的函数创建标签页
            self.add_tabs_recursive(child)  # 递归检查所有子项目
        
        return self.selected_items

    def create_tab(self, tree_item):
        # 创建一个新的标签页
        tab = QWidget()
        self.tabs.addTab(tab, tree_item.text(0))

        # 创建表格并设置行列数
        table = QTableWidget(10, 3)  # 示例：10行3列
        table.setHorizontalHeaderLabels(['Header 1', 'Header 2', 'Header 3'])  # 设置列头标签

        # 填充数据到表格中（这里使用示例数据）
        for row in range(10):
            for column in range(3):
                item = QTableWidgetItem(f"Item {row},{column}")
                table.setItem(row, column, item)

        # 创建一个水平布局
        layout = QHBoxLayout()
        layout.addWidget(table)  # 将表格添加到布局中

        # 将布局设置为标签页的布局
        tab.setLayout(layout)

    def process_selected_items(self):
        # 在这里编写你的数据处理逻辑
        # 可以在新线程中处理self.selected_items
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
