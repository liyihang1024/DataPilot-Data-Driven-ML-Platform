import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem,
    QHBoxLayout, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QDialog
)
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

# 字典映射算法名称到它们相应的sklearn类
ALGORITHMS = {
    "随机森林回归": RandomForestRegressor,
    "支持向量回归": SVR
}

# 参数设置窗口类
class AlgorithmParamsDialog(QDialog):
    def __init__(self, algorithm_class, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"{algorithm_class.__name__} Parameters")
        self.algorithm = algorithm_class()  # 实例化算法
        self.params = self.algorithm.get_params()  # 获取参数
        self.init_ui()  # 初始化界面

    # 初始化用户界面
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(10)  # 设置元素间的间距

        # 获取最长参数名称的长度
        max_param_length = max(len(param) for param in self.params)

        # 用于跟踪每个参数的LineEdit的字典
        self.param_line_edits = {}

        # 计算标签的统一宽度
        label_width = max_param_length * 10  # 修改点：设置了一个基于最长参数名称的固定宽度

        # 为每个参数创建一个水平布局的标签和LineEdit
        for param, value in self.params.items():
            param_layout = QHBoxLayout()
            param_label = QLabel(f"{param}:")
            param_label.setFixedWidth(label_width)  # 修改点：设置固定宽度
            param_label.setAlignment(Qt.AlignRight)  # 右对齐
            line_edit = QLineEdit(str(value))
            line_edit.setFixedWidth(200)  # 设置统一的LineEdit长度
            param_layout.addWidget(param_label)
            param_layout.addWidget(line_edit)
            self.param_line_edits[param] = line_edit
            layout.addLayout(param_layout)

        # 创建确定和取消按钮，并连接它们的点击信号到槽函数
        self.ok_button = QPushButton("确定", self)
        self.cancel_button = QPushButton("取消", self)
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        
        # 添加按钮到界面底部，并设置合理的间距
        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addWidget(self.ok_button)
        buttons_layout.addWidget(self.cancel_button)
        buttons_layout.setSpacing(10)  # 设置按钮之间的间距
        layout.addLayout(buttons_layout)

        self.setLayout(layout)
        self.setStyleSheet("QWidget { font-size: 14px; } QPushButton { width: 80px; }")  # 设置字体大小和按钮宽度

    # 接受修改，关闭对话框并打印修改后的参数
    def accept(self):
        modified_params = {param: line_edit.text() for param, line_edit in self.param_line_edits.items()}
        print("修改后的参数：", modified_params)
        super().accept()

    # 拒绝修改，关闭对话框但不打印参数
    def reject(self):
        # 由于是取消操作，这里不需要打印任何参数
        super().reject()

# 主窗口类
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建树形控件
        self.tree = QTreeWidget()
        self.tree.setColumnCount(1)
        self.tree.setHeaderLabels(["Algorithms"])

        # 创建根项目
        regression_item = QTreeWidgetItem(self.tree, ["回归"])
        classification_item = QTreeWidgetItem(self.tree, ["分类"])

        # 为根项目添加带复选框的子项目
        self.add_child_with_checkbox(regression_item, "随机森林回归")
        self.add_child_with_checkbox(regression_item, "支持向量回归")

        # 连接项目改变信号到槽
        self.tree.itemChanged.connect(self.on_item_changed)

        # 设置中心控件
        self.setCentralWidget(self.tree)
        self.current_item = None  # 当前选中的树形项目

    # 为父项目添加子项目并加上复选框
    def add_child_with_checkbox(self, parent, text):
        child = QTreeWidgetItem(parent, [text])
        child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
        child.setCheckState(0, Qt.Unchecked)

    # 处理项目变化的槽函数
    def on_item_changed(self, item, _):
        # 检查状态是否为选中并且项目不是根项目
        if item.checkState(0) == Qt.Checked and item.parent():
            algorithm_name = item.text(0)
            if algorithm_name in ALGORITHMS:
                # 如果当前已有打开的对话框，先关闭它
                if self.current_item is not None:
                    self.current_item.setCheckState(0, Qt.Unchecked)
                # 打开新的参数设置对话框
                algorithm_class = ALGORITHMS[algorithm_name]
                dialog = AlgorithmParamsDialog(algorithm_class, self)
                self.current_item = item  # 保存当前选中的项目
                accepted = dialog.exec()  # 以模态方式执行对话框
                if not accepted:
                    # 如果用户取消，则清除复选框
                    self.current_item.setCheckState(0, Qt.Unchecked)
                self.current_item = None  # 清除当前选中的项目

app = QApplication(sys.argv)
window = MainWindow()
window.resize(400, 300)
window.show()
sys.exit(app.exec())

