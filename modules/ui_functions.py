# ///////////////////////////////////////////////////////////////
#
# 作者: liyihang
# 项目使用: Qt Designer 和 PySide6 制作
# 版本: 1.0.0
#
# ///////////////////////////////////////////////////////////////

# 主文件
# ///////////////////////////////////////////////////////////////
from main import *

# 全局变量
# ///////////////////////////////////////////////////////////////
GLOBAL_STATE = False  # 初始状态为非最大化
GLOBAL_TITLE_BAR = True  # 使用自定义标题栏

# 定义UI功能的类，继承自主窗口类
class UIFunctions(MainWindow):
    # 最大化/还原窗口
    # ///////////////////////////////////////////////////////////////
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        # 如果窗口未最大化，则最大化窗口
        if status == False:
            self.showMaximized()
            GLOBAL_STATE = True
            self.ui.bgApp.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip("Restore")  # 更改提示
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))  # 更改图标
            # 隐藏窗口大小调整把手
            self.ui.frame_size_grip.hide()
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            # 如果窗口已最大化，则还原窗口
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)  # 触发窗口更新
            self.ui.bgApp.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
            # 显示窗口大小调整把手
            self.ui.frame_size_grip.show()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()

    # 返回当前窗口状态（最大化或非最大化）
    def returStatus(self):
        return GLOBAL_STATE

    # 设置当前窗口状态
    def setStatus(self, status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    # 切换菜单显示/隐藏
    def toggleMenu(self, enable):
        if enable:
            # 获取当前宽度
            width = self.ui.leftMenuBg.width()
            maxExtend = Settings.MENU_WIDTH
            standard = 60

            # 设置最大宽度
            if width == 60:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # 开始动画
            self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    # 切换左侧额外盒子的显示/隐藏
    def toggleLeftBox(self, enable):
        if enable:
            # 获取当前宽度
            width = self.ui.extraLeftBox.width()
            widthRightBox = self.ui.extraRightBox.width()
            maxExtend = Settings.LEFT_BOX_WIDTH
            color = Settings.BTN_LEFT_BOX_COLOR
            standard = 0

            # 获取当前按钮样式
            style = self.ui.toggleLeftBox.styleSheet()

            # 设置最大宽度
            if width == 0:
                widthExtended = maxExtend
                # 选择按钮
                self.ui.toggleLeftBox.setStyleSheet(style + color)
                # 如果右侧盒子也打开，重置其样式
                if widthRightBox != 0:
                    style = self.ui.settingsTopBtn.styleSheet()
                    self.ui.settingsTopBtn.setStyleSheet(style.replace(Settings.BTN_RIGHT_BOX_COLOR, ''))
            else:
                widthExtended = standard
                # 重置按钮样式
                self.ui.toggleLeftBox.setStyleSheet(style.replace(color, ''))
                
        # 开始动画
        UIFunctions.start_box_animation(self, width, widthRightBox, "left")

    # 切换右侧额外盒子的显示/隐藏
    def toggleRightBox(self, enable):
        if enable:
            # 获取当前宽度
            width = self.ui.extraRightBox.width()
            widthLeftBox = self.ui.extraLeftBox.width()
            maxExtend = Settings.RIGHT_BOX_WIDTH
            color = Settings.BTN_RIGHT_BOX_COLOR
            standard = 0

            # 获取当前按钮样式
            style = self.ui.settingsTopBtn.styleSheet()

            # 设置最大宽度
            if width == 0:
                widthExtended = maxExtend
                # 选择按钮
                self.ui.settingsTopBtn.setStyleSheet(style + color)
                # 如果左侧盒子也打开，重置其样式
                if widthLeftBox != 0:
                    style = self.ui.toggleLeftBox.styleSheet()
                    self.ui.toggleLeftBox.setStyleSheet(style.replace(Settings.BTN_LEFT_BOX_COLOR, ''))
            else:
                widthExtended = standard
                # 重置按钮样式
                self.ui.settingsTopBtn.setStyleSheet(style.replace(color, ''))

            # 开始动画
            UIFunctions.start_box_animation(self, widthLeftBox, width, "right")

    # 开始左右盒子动画
    def start_box_animation(self, left_box_width, right_box_width, direction):
        # 初始化左右盒子宽度
        right_width = 0
        left_width = 0 

        # 根据方向和当前宽度确定左侧盒子的目标宽度
        if left_box_width == 0 and direction == "left":
            left_width = 240  # 如果当前宽度为0且方向为左，则设置为240
        else:
            left_width = 0    # 否则设置为0

        # 根据方向和当前宽度确定右侧盒子的目标宽度
        if right_box_width == 0 and direction == "right":
            right_width = 240 # 如果当前宽度为0且方向为右，则设置为240
        else:
            right_width = 0   # 否则设置为0       

        # 左侧盒子动画        
        self.left_box = QPropertyAnimation(self.ui.extraLeftBox, b"minimumWidth")  # 创建动画对象
        self.left_box.setDuration(Settings.TIME_ANIMATION)  # 设置动画持续时间
        self.left_box.setStartValue(left_box_width)  # 设置动画起始值
        self.left_box.setEndValue(left_width)  # 设置动画结束值
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)  # 设置动画曲线

        # 右侧盒子动画        
        self.right_box = QPropertyAnimation(self.ui.extraRightBox, b"minimumWidth")  # 创建动画对象
        self.right_box.setDuration(Settings.TIME_ANIMATION)  # 设置动画持续时间
        self.right_box.setStartValue(right_box_width)  # 设置动画起始值
        self.right_box.setEndValue(right_width)  # 设置动画结束值
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)  # 设置动画曲线

        # 组合动画
        self.group = QParallelAnimationGroup()  # 创建动画组
        self.group.addAnimation(self.left_box)  # 添加左侧盒子动画
        self.group.addAnimation(self.right_box)  # 添加右侧盒子动画
        self.group.start()  # 开始动画

    # 选择/取消选择菜单项
    # 选择
    def selectMenu(getStyle):
        # 添加选中样式到当前样式
        select = getStyle + Settings.MENU_SELECTED_STYLESHEET
        return select

    # 取消选择
    def deselectMenu(getStyle):
        # 从当前样式移除选中样式
        deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, "")
        return deselect

    # 开始选择
    def selectStandardMenu(self, widget):
        # 遍历顶部菜单中的所有QPushButton
        for w in self.ui.topMenu.findChildren(QPushButton):
            # 如果找到了指定的widget，则应用选中样式
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    # 重置选择
    def resetStyle(self, widget):
        # 遍历顶部菜单中的所有QPushButton
        for w in self.ui.topMenu.findChildren(QPushButton):
            # 如果widget的名称不是指定的widget，则取消选中样式
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    # 导入主题文件QSS/CSS
    def theme(self, file, useCustomTheme):
        # 如果使用自定义主题
        if useCustomTheme:
            # 读取文件内容
            str = open(file, 'r', encoding='utf-8').read()
            # 应用样式表
            self.ui.styleSheet.setStyleSheet(str)

    # 定义界面UI
    def uiDefinitions(self):
        # 定义双击最大化还原事件
        def dobleClickMaximizeRestore(event):
            # 如果是双击事件，则最大化或还原窗口
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))
        # 设置双击事件
        self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

        # 如果启用了自定义标题栏
        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            # 设置窗口为无边框
            self.setWindowFlags(Qt.FramelessWindowHint)
            # 设置窗口背景为透明
            self.setAttribute(Qt.WA_TranslucentBackground)

            # 定义移动窗口函数
            def moveWindow(event):
                # 如果窗口最大化，则还原
                if UIFunctions.returStatus(self):
                    UIFunctions.maximize_restore(self)
                # 如果是左键按下，则移动窗口
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()
            # 设置鼠标移动事件
            self.ui.titleRightInfo.mouseMoveEvent = moveWindow

            # 自定义窗口大小调整把手
            self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
            self.right_grip = CustomGrip(self, Qt.RightEdge, True)
            self.top_grip = CustomGrip(self, Qt.TopEdge, True)
            self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

        else:
            # 设置窗口边距
            self.ui.bgApp.setContentsMargins(0, 0, 0, 0)
            # 隐藏最小化、最大化和关闭按钮
            self.ui.minimizeAppBtn.hide()
            self.ui.maximizeRestoreAppBtn.hide()
            self.ui.closeAppBtn.hide()
            # 隐藏大小调整把手
            self.ui.frame_size_grip.hide()

        # 设置窗口阴影效果
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)  # 阴影模糊半径
        self.shadow.setXOffset(0)  # x偏移
        self.shadow.setYOffset(0)  # y偏移
        self.shadow.setColor(QColor(0, 0, 0, 150))  # 阴影颜色
        self.ui.bgApp.setGraphicsEffect(self.shadow)  # 应用到背景

        # 设置窗口大小调整把手样式
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # 设置最小化按钮点击事件
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # 设置最大化还原按钮点击事件
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # 设置关闭应用按钮点击事件
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())

    # 调整大小把手位置
    def resize_grips(self):
        # 如果启用了自定义标题栏
        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            # 设置左右上下把手位置和大小
            self.left_grip.setGeometry(0, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
            self.top_grip.setGeometry(0, 0, self.width(), 10)
            self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    # ///////////////////////////////////////////////////////////////
    # 结束 - GUI 定义
