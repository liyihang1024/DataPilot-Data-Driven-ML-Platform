import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QHBoxLayout,
                               QPushButton, QLabel, QLineEdit, QDialog)
from PySide6.QtCore import Qt

class CustomDialog(QDialog):
    def __init__(self, parent=None, title=""):
        super(CustomDialog, self).__init__(parent)
        self.setWindowTitle(title)

        # 主垂直布局
        main_layout = QVBoxLayout(self)

        # 添加标签和文本编辑框
        self.label = QLabel(title)
        self.text_edit = QLineEdit()

        # 添加确定和取消按钮
        self.ok_button = QPushButton('确定')
        self.cancel_button = QPushButton('取消')

        # 水平布局来容纳按钮
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)

        main_layout.addWidget(self.label)
        main_layout.addWidget(self.text_edit)
        main_layout.addLayout(button_layout)

        # 连接按钮信号
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建TreeWidget
        self.tree = QTreeWidget()
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(["方法", "备注"])
        items = [
            ("Mutual Information", "互信息"),
            ("F-test", "F检验"),
            ("Variance Threshold", "方差过滤"),
            ("Chi-Square", "卡方过滤")
        ]
        for method, note in items:
            item = QTreeWidgetItem([method, note])
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(0, Qt.Unchecked)
            self.tree.addTopLevelItem(item)

        # 调整第一列宽度以适应内容
        self.tree.resizeColumnToContents(0)

        # 展开所有项
        self.tree.expandAll()

        # 存储参数的字典
        self.parameters = {}

        # 设置窗口的主部件
        self.setCentralWidget(self.tree)

        # 连接信号
        self.tree.itemClicked.connect(self.on_item_clicked)

    def on_item_clicked(self, item, column):
        # 只处理第一列的点击事件
        if column == 0:
            method = item.text(0)
            note = item.text(1)
            key = f"{method}-{note}"
            # 检查项目的勾选状态
            if item.checkState(column) == Qt.Checked:
                # 如果项目被勾选，弹出对话框
                dialog = CustomDialog(self, title=note)
                if dialog.exec():
                    # 如果点击确定，保存参数
                    self.parameters[method] = dialog.text_edit.text()
                else:
                    # 如果点击取消，取消勾选
                    item.setCheckState(column, Qt.Unchecked)
            else:
                # 如果取消勾选，从字典中删除对应的键值对
                if method in self.parameters:
                    del self.parameters[method]
            
            print('刚点击的参数：', method)
            print('所有选中的参数：\n', self.parameters)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
