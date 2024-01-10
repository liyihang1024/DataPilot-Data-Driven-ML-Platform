import sys
import math
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QPainter, QPolygon, QPen, QColor, QBrush
from PySide6.QtCore import QPoint, QSize, Qt

class HexagonButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setMinimumSize(120, 104)
        self.pressed = False

    def sizeHint(self):
        return QSize(120, 104)

    def paintEvent(self, event):
        painter = QPainter(self)
        hexagon = self.create_hexagon(self.width() / 2, self.height() / 2, min(self.width(), self.height()) / 3)
        
        # Change the button color based on whether it is pressed
        if not self.pressed:
            painter.setPen(QPen(QColor(0, 0, 0), 2))
            painter.setBrush(QBrush(QColor(255, 255, 255)))  # Normal background
        else:
            painter.setPen(QPen(QColor(0, 0, 0), 2))
            painter.setBrush(QBrush(QColor(200, 200, 200)))  # Pressed background

        painter.drawPolygon(hexagon)
        painter.setPen(QPen(QColor(0, 0, 0)))
        painter.drawText(hexagon.boundingRect(), Qt.AlignCenter, self.text())

    def create_hexagon(self, x, y, size):
        hexagon = QPolygon()
        for i in range(6):
            angle_deg = 60 * i - 30
            angle_rad = math.pi / 180 * angle_deg
            hexagon.append(QPoint(
                x + size * math.cos(angle_rad),
                y + size * math.sin(angle_rad)
            ))
        return hexagon

    def mousePressEvent(self, event):
        self.pressed = True
        self.update()  # Trigger a repaint

    def mouseReleaseEvent(self, event):
        self.pressed = False
        self.update()  # Trigger a repaint
        self.clicked.emit()  # Emit the clicked signal

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 创建主窗口的中心小部件和布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # 创建按钮并添加到布局中
        btn_get_data = HexagonButton("Get Data")
        btn_clean_data = HexagonButton("Clean, Prepare &\nManipulate Data")
        btn_train_model = HexagonButton("Train Model")
        btn_test_data = HexagonButton("Test Data")
        btn_improve = HexagonButton("Improve")

        # 创建水平布局以包含步骤按钮
        steps_layout = QVBoxLayout()
        steps_layout.addWidget(btn_get_data)
        steps_layout.addWidget(btn_clean_data)
        steps_layout.addWidget(btn_train_model)
        steps_layout.addWidget(btn_test_data)
        steps_layout.addWidget(btn_improve)

        # 将步骤布局添加到主布局中
        main_layout.addLayout(steps_layout)

        # 设置窗口属性
        self.setWindowTitle("Machine Learning Workflow")
        self.resize(800, 600)

# 创建应用实例和窗口，然后运行应用
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
