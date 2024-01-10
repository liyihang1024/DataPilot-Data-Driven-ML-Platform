import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                               QTreeWidget, QTreeWidgetItem, QVBoxLayout, 
                               QWidget, QTableWidget, QTableWidgetItem, QLabel,
                               QMdiArea, QMdiSubWindow)
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和初始大小
        self.setWindowTitle("特征选择与相关性分析")
        self.setGeometry(100, 100, 800, 600)

        # 创建MDI区域
        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)

        # 添加控件面板
        control_panel = QWidget()
        layout = QVBoxLayout(control_panel)

        # 添加树状列表
        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderLabel("特征列表")
        self.populate_tree()  # 填充树状列表
        layout.addWidget(self.tree_widget)

        # 添加按钮
        self.btn_feature_selection = QPushButton("特征选择")
        self.btn_feature_selection.clicked.connect(self.feature_selection)
        layout.addWidget(self.btn_feature_selection)

        self.btn_correlation_analysis = QPushButton("相关性分析")
        self.btn_correlation_analysis.clicked.connect(self.correlation_analysis)
        layout.addWidget(self.btn_correlation_analysis)

        # 将控件面板作为子窗口添加到MDI区域
        control_subwindow = QMdiSubWindow()
        control_subwindow.setWidget(control_panel)
        control_subwindow.setWindowTitle("控制面板")
        self.mdi_area.addSubWindow(control_subwindow)
        control_subwindow.show()

    def populate_tree(self):
        for i in range(5):
            item = QTreeWidgetItem(self.tree_widget)
            item.setText(0, f"Feature {i+1}")
            item.setCheckState(0, Qt.CheckState.Unchecked)

    def feature_selection(self):
        selected_features = []
        for index in range(self.tree_widget.topLevelItemCount()):
            if self.tree_widget.topLevelItem(index).checkState(0):
                selected_features.append(self.tree_widget.topLevelItem(index).text(0))
        processed_data = [[f"{feature} data" for feature in selected_features]]
        self.show_data(processed_data)

    def correlation_analysis(self):
        self.show_plot("这里是相关性分析的图形占位符")

    def show_data(self, data):
        data_window = QWidget()
        layout = QVBoxLayout()
        table = QTableWidget(len(data), len(data[0]))
        for i, row in enumerate(data):
            for j, val in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(val))
        layout.addWidget(table)
        data_window.setLayout(layout)

        # 将数据窗口作为子窗口添加到MDI区域
        data_subwindow = QMdiSubWindow()
        data_subwindow.setWidget(data_window)
        data_subwindow.setWindowTitle("处理后的数据")
        self.mdi_area.addSubWindow(data_subwindow)
        data_subwindow.show()

    def show_plot(self, plot_content):
        plot_window = QWidget()
        layout = QVBoxLayout()
        label = QLabel(plot_content)
        layout.addWidget(label)
        plot_window.setLayout(layout)

        # 将绘图窗口作为子窗口添加到MDI区域
        plot_subwindow = QMdiSubWindow()
        plot_subwindow.setWidget(plot_window)
        plot_subwindow.setWindowTitle("相关性分析")
        self.mdi_area.addSubWindow(plot_subwindow)
        plot_subwindow.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
