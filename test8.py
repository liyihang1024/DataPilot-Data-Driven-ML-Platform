import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMdiArea, QMdiSubWindow
from modules.Ui_widget_featureSelection import Ui_MdiSubW_featureSelection  # 确保这里的路径正确
from PySide6.QtCore import Qt

class FeatureSelectionWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MdiSubW_featureSelection()
        self.ui.setupUi(self)

class NonClosableMdiSubWindow(QMdiSubWindow):
    def closeEvent(self, event):
        # 重写closeEvent，阻止窗口关闭
        event.ignore()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和初始大小
        self.setWindowTitle("特征选择与相关性分析")
        self.setGeometry(100, 100, 800, 600)

        # 创建MDI区域并设置为中央小部件
        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)

        # 创建并显示特征选择窗口
        self.show_feature_selection_window()

    def show_feature_selection_window(self):
        feature_selection_window = FeatureSelectionWindow()
        sub_window = NonClosableMdiSubWindow()  # 使用自定义的NonClosableMdiSubWindow
        sub_window.setWidget(feature_selection_window)
        sub_window.setWindowTitle("特征选择")

        self.mdi_area.addSubWindow(sub_window)
        sub_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
