# 导入必要的模块
from PySide6.QtWidgets import QApplication, QWidget, QTextBrowser, QPushButton
from PySide6.QtCore import QRect
import sys


"""
这个简单的程序创建了一个窗体，包含一个文本框和一个按钮，用于模拟播放和暂停音乐的功能。
"""

# 定义UI界面类
class Ui_Form(object):
    def setupUi(self, Form):
        # 设置窗体属性
        Form.setObjectName("Form")
        Form.resize(551, 427)
        
        # 初始化标记
        self.is_switching = False  # 正在切换歌曲的标记
        self.is_pause = True  # 暂停状态的标记

        # 创建并设置文本框
        self.textEdit = QTextBrowser(Form)
        self.textEdit.setGeometry(QRect(60, 210, 161, 131))
        self.textEdit.setStyleSheet("border-radius:19px;\n"
                                    "border: 2px solid DarkGray;\n"
                                    "background:#ffffff;\n"
                                    "")
        self.textEdit.setObjectName("textEdit")

        # 创建并设置按钮
        self.pushButton = QPushButton(Form)
        self.pushButton.setGeometry(QRect(110, 130, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.playMusic)  # 绑定按钮点击事件

        # 设置窗体的其他属性
        self.retranslateUi(Form)
        Form.show()

    # 播放音乐的方法
    def playMusic(self):
        if self.is_pause or self.is_switching:
            self.textEdit.append("运行中...")  # 在文本框中显示状态
            self.is_pause = False  # 更新暂停状态标记
            self.pushButton.setText('暂停')  # 更新按钮文本
        elif (not self.is_pause) and (not self.is_switching):
            self.textEdit.append("暂停中...")  # 在文本框中显示状态
            self.is_pause = True  # 更新暂停状态标记
            self.pushButton.setText('运行')  # 更新按钮文本

    # 设置窗体的文本
    def retranslateUi(self, Form):
        Form.setWindowTitle("音乐播放器")  # 设置窗体标题
        self.pushButton.setText("运行")  # 设置按钮的初始文本

# 主程序入口
if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建应用程序
    Form = QWidget()  # 创建窗体
    ui = Ui_Form()  # 实例化UI界面
    ui.setupUi(Form)  # 设置UI界面
    sys.exit(app.exec())  # 启动应用程序并等待退出
