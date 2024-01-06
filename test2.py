from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QMessageBox
import sys
import pandas as pd
import os
import subprocess

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个按钮用于导出数据
        self.export_button = QPushButton("导出数据", self)
        self.export_button.clicked.connect(self.download_data)  # 将按钮的点击信号连接到导出数据的函数
        self.export_button.move(10, 10)  # 移动按钮到合适的位置

        # 创建一个按钮用于播放视频教程
        self.tutorial_button = QPushButton("视频教程", self)
        self.tutorial_button.clicked.connect(self.play_tutorial)  # 将按钮的点击信号连接到播放视频的函数
        self.tutorial_button.move(10, 50)  # 移动按钮到合适的位置

    def download_data(self):
        """下载数据并保存为Excel或CSV文件。
        
        此函数将弹出一个文件保存对话框，让用户选择保存文件的位置和格式。
        用户可以选择保存为Excel格式或CSV格式。
        """
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog

        # 弹出文件保存对话框，让用户选择保存为Excel或CSV
        fileName, selectedFilter = QFileDialog.getSaveFileName(self, "保存数据",
                                                               "", "Excel Files (*.xlsx);;CSV Files (*.csv)",
                                                               options=options)
        
        if fileName:
            # 假设你要导出的数据
            data = pd.read_excel("databases/test-data.xlsx")

            # 根据用户选择的文件类型保存数据
            if selectedFilter == "Excel Files (*.xlsx)":
                data.to_excel(fileName, index=False)
            elif selectedFilter == "CSV Files (*.csv)":
                data.to_csv(fileName, index=False)

            # 这里可以添加反馈给用户的代码，例如弹出一个对话框告诉用户数据下载成功
            QMessageBox.information(self, "数据下载", "数据下载成功！")

    def play_tutorial(self):
        """用默认播放器打开项目中的mp4视频教程。"""
        video_path = os.path.join(os.getcwd(), "databases/tutorial.mp4")  # 替换为视频文件的实际路径
        print("当前工作目录:", os.getcwd())
        print("视频教程目录:", video_path)
        if os.path.exists(video_path):
            if sys.platform == 'win32':
                os.startfile(video_path)  # Windows下使用startfile打开
            else:
                opener = "open" if sys.platform == "darwin" else "xdg-open"  # MacOS使用open，Linux使用xdg-open
                subprocess.call([opener, video_path])
        else:
            QMessageBox.warning(self, "视频教程", "找不到视频文件！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
