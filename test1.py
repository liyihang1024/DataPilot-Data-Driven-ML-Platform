import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建树形控件，并设置两列
        self.tree = QTreeWidget()
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(["算法英文名", "算法中文名"])

        # 创建“回归”主项
        regression_item = QTreeWidgetItem(self.tree, ["回归"])
        
        # 添加几个回归算法作为子项，包括它们的英文和中文名
        algorithms = {
            "Linear Regression": "线性回归",
            "Random Forest Regressor": "随机森林回归",
            "Support Vector Regressor": "支持向量回归"
        }
        for eng_name, cn_name in algorithms.items():
            QTreeWidgetItem(regression_item, [eng_name, cn_name])  # 创建子项并分别设置两列的文本

        # 设置中心控件为树形控件
        self.setCentralWidget(self.tree)

app = QApplication(sys.argv)
window = MainWindow()
window.resize(400, 300)
window.show()
sys.exit(app.exec())
