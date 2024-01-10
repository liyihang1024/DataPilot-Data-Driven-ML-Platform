import sys
from PySide6.QtGui import QAction, QIcon, QCursor
from PySide6.QtCore import QPropertyAnimation, QRect, QEasingCurve, QPoint, Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget
# 假设这两个是从 Qt Designer 生成的 UI 类
from ui_loginwidget import Ui_LoginWidget
from ui_registerwidget import Ui_RegisterWidget

class LoginWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoginWidget()
        self.ui.setupUi(self)
        # 隐藏登录页面窗口边框
        # self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # 设置适当的窗口大小
        self.resize(656, 534)
        # 设置任务栏图标
        self.setWindowIcon(QIcon("images/images/DataPilot_icon.png"))
        
        # 初始化用于窗口拖动的变量
        self.oldPos = None

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.oldPos:
            delta = QPoint(event.globalPosition().toPoint() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPosition().toPoint()

        # 这里添加登录逻辑
        # ...

class RegisterWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_RegisterWidget()
        self.ui.setupUi(self)
        # 隐藏登录页面窗口边框
        # self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # 设置适当的窗口大小
        self.resize(656, 534)
        # 设置任务栏图标
        self.setWindowIcon(QIcon("images/images/DataPilot_icon.png"))

        # 初始化用于窗口拖动的变量
        self.oldPos = None

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.oldPos:
            delta = QPoint(event.globalPosition().toPoint() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPosition().toPoint()

        # 这里添加注册逻辑
        # ...

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.stacked_widget = QStackedWidget()
        self.login_widget = LoginWidget()
        self.register_widget = RegisterWidget()

        self.stacked_widget.addWidget(self.login_widget)
        self.stacked_widget.addWidget(self.register_widget)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

        self.login_widget.ui.btn_register.clicked.connect(self.flip_to_register)
        self.register_widget.ui.btn_back.clicked.connect(self.flip_to_login)

        # 设置 MainWindow 的初始大小
        self.resize(800, 600)

    def flip_to_register(self):
        self.animate_flip(0, 1)

    def flip_to_login(self):
        self.animate_flip(1, 0)

    def animate_flip(self, start_index, end_index):
        animation = QPropertyAnimation(self.stacked_widget, b"geometry")
        animation.setDuration(500)
        animation.setEasingCurve(QEasingCurve.InOutCubic)

        start_rect = self.stacked_widget.currentWidget().geometry()
        mid_rect = QRect(start_rect)
        end_rect = QRect(start_rect)

        mid_rect.setWidth(280)  # 中间状态宽度为0
        animation.setStartValue(start_rect)
        animation.setEndValue(mid_rect)

        def on_animation_finished():
            # 当第一次动画完成时，切换页面并开始第二次动画
            self.stacked_widget.setCurrentIndex(end_index)
            animation.setStartValue(mid_rect)
            animation.setEndValue(end_rect)
            animation.finished.disconnect()  # 断开之前的连接
            animation.start()

        animation.finished.connect(on_animation_finished)
        animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
