import sys
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtGui import QPainter, QPolygon, QPen
from PySide6.QtCore import QPoint, QSize, Qt

class HexagonButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(120, 104)  # Ensure enough space for the hexagon

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5))

        # Predefined hexagon coordinates
        hexagon = QPolygon([
            QPoint(60, 2),    # Top
            QPoint(110, 26),  # Top right
            QPoint(110, 78),  # Bottom right
            QPoint(60, 102),  # Bottom
            QPoint(10, 78),   # Bottom left
            QPoint(10, 26),   # Top left
        ])

        painter.drawPolygon(hexagon)
        super().paintEvent(event)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建自定义的HexagonButton（假设在其他地方定义）
        self.hexButton = HexagonButton(self)

        # 设置HexagonButton作为中央窗口
        # self.setCentralWidget(self.hexButton)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
