# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# 项目使用：Qt Designer 和 PySide6 制作
# 版本: 1.0.0
#
# 本项目可以自由用于所有用途，只要在Python脚本中保留相应的信用标记，
# GUI中的任何信息都可以修改，而不会有任何影响。
#
# 如果您想将产品商业化使用，Qt 许可证有一些限制，
# 我建议在官方网站上阅读它们：https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# 导入必要的库和模块
import sys
import bcrypt
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer
from sklearn.feature_selection import VarianceThreshold, SelectKBest, chi2, f_classif, mutual_info_classif
from PySide6.QtGui import QAction, QIcon, QCursor
from PySide6.QtCore import QEvent, Qt
import os
import time
import psutil   # 用于获取系统信息，如CPU和内存使用情况
import pandas as pd
from datetime import datetime

# 导入 GUI 模块和小部件
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
from PySide6.QtCharts import QChart, QLineSeries, QValueAxis

# 从转换的ui文件导入登录对话框，每次修改ui文件后都需要将其中类名修改为Ui_LoginMainWindow
from modules.ui_login import Ui_LoginMainWindow  


# 打印当前时间
print("当前时间:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 设置环境变量以修复高DPI和缩放超过100%时的显示问题
os.environ["QT_FONT_DPI"] = "96"

# 将 widgets 设置为全局变量
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # 设置 widgets 为全局变量
        # 详细介绍可见https://www.bilibili.com/read/cv14306314/
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # 使用自定义标题栏，对于Mac或Linux请设为False
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # 应用程序名称
        # ///////////////////////////////////////////////////////////////
        title = "DataPilot - Data Driven ML Platform"
        description = "DataPilot - Data Driven ML Platform"
        self.setWindowTitle(title)  # 设置窗口标题
        widgets.titleRightInfo.setText(description)  # 设置界面左上角信息
        # 设置窗口图标
        self.setWindowIcon(QIcon("images/images/DataPilot_icon.png"))

        # 切换菜单
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # 设置 UI 定义
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        # widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 设置按钮点击事件
        # ///////////////////////////////////////////////////////////////

        # 左侧菜单
        widgets.btn_home.clicked.connect(self.buttonClick)  # 设置"主页"按钮的点击事件
        widgets.btn_FeatureProcessing.clicked.connect(self.buttonClick)
        widgets.btn_FeatureSelection.clicked.connect(self.buttonClick)
        widgets.btn_ModelTraining.clicked.connect(self.buttonClick)
        widgets.btn_ResultAnalysis.clicked.connect(self.buttonClick)
        widgets.btn_FeatureGeneration.clicked.connect(self.buttonClick)

        # 新增切换皮肤功能
        widgets.btn_theme.clicked.connect(self.buttonClick)

        # 新增导入本地数据功能
        widgets.btn_open_local_file.clicked.connect(self.load_data)

        # 新增数据处理功能
        widgets.btn_FeatureProcessing_2.clicked.connect(self.data_processing)

        # 新增下载数据功能
        widgets.btn_downloadDatabase.clicked.connect(self.download_data)

        # 新增视频教程功能
        widgets.btn_videoTutorial.clicked.connect(self.play_tutorial)

        # 打开/关闭左侧额外盒子
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # 打开/关闭右侧额外盒子
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)

        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # 显示应用程序
        # ///////////////////////////////////////////////////////////////
        self.show()

        # 设置自定义主题
        # ///////////////////////////////////////////////////////////////
        # 路径冻结，防止打包成exe后路径错乱
        if getattr(sys, 'frozen', False):
            absPath = os.path.dirname(os.path.abspath(sys.executable))
        elif __file__:
            absPath = os.path.dirname(os.path.abspath(__file__))
        useCustomTheme = True
        self.useCustomTheme = useCustomTheme
        self.absPath = absPath
        themeFile = os.path.abspath(os.path.join(absPath, "themes\py_dracula_dark.qss"))
        # SET THEME AND HACKS
        if useCustomTheme:
            # 加载并应用样式
            UIFunctions.theme(self, themeFile, True)

            # # 设置样式修复
            AppFunctions.setThemeHack(self)

        # 解决Pyqt5 无边框窗口点击window菜单栏弹出与最小化
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowSystemMenuHint|Qt.WindowMinimizeButtonHint|Qt.WindowMaximizeButtonHint)  # 隐藏边框

        # 设置初始页面和选中的菜单
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.page1_Home)  # 设置初始显示的页面
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))  # 设置选中的菜单样式

        # 在特征选择MDI页面创建并显示特征选择子窗口
        self.show_feature_selection_window()
        self.open_subwindows = {}  # 用来跟踪打开的子窗口

        # 在模型训练MDI页面创建并显示模型训练子窗口
        self.show_model_train_window()


    # 按钮点击事件处理
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # 获取点击的按钮
        btn = self.sender()
        btnName = btn.objectName()

        # 如果点击的是"主页"按钮
        if btnName == "btn_home":
            # 切换到主页界面
            widgets.stackedWidget.setCurrentWidget(widgets.page1_Home)
            # 重置所有按钮的样式
            UIFunctions.resetStyle(self, btnName)
            # 为当前点击的按钮应用选中样式
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # 切换到特征处理页面，并更新按钮样式
        if btnName == "btn_FeatureProcessing":
            widgets.stackedWidget.setCurrentWidget(widgets.page2_FeatureProcessing)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # 切换到特征选择页面，并更新按钮样式
        if btnName == "btn_FeatureSelection":
            widgets.stackedWidget.setCurrentWidget(widgets.page3_FeatureSelection)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        # 切换到模型训练页面，并更新按钮样式
        if btnName == "btn_ModelTraining":
            widgets.stackedWidget.setCurrentWidget(widgets.page4_ModelTraining)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            # QMessageBox.information(self, "提示", "该功能暂未实现", QMessageBox.Yes)
        
        # 切换到结果分析页面，并更新按钮样式
        if btnName == "btn_ResultAnalysis":
            widgets.stackedWidget.setCurrentWidget(widgets.page5_ResultAnalysis)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            # QMessageBox.information(self, "提示", "该功能暂未实现", QMessageBox.Yes)
        
        # 切换到特征生成页面，并更新按钮样式
        if btnName == "btn_FeatureGeneration":
            widgets.stackedWidget.setCurrentWidget(widgets.page6_FeatureGeneration)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            # QMessageBox.information(self, "提示", "该功能暂未实现", QMessageBox.Yes)

        # # 如果点击的是"切换皮肤"按钮
        # if btnName == "btn_theme":
        #     # 根据当前主题应用相应的主题文件，并重新应用样式和设置
        #     if self.useCustomTheme:
        #         themeFile = os.path.abspath(os.path.join(self.absPath, "themes\py_dracula_light.qss"))
        #         UIFunctions.theme(self, themeFile, True)
        #         # SET HACKS
        #         AppFunctions.setThemeHack(self)
        #         self.useCustomTheme = False
        #     else:
        #         themeFile = os.path.abspath(os.path.join(self.absPath, "themes\py_dracula_dark.qss"))
        #         UIFunctions.theme(self, themeFile, True)
        #         # SET HACKS
        #         AppFunctions.setThemeHack(self)
        #         self.useCustomTheme = True

        # 如果点击的是"切换皮肤"按钮
        if btnName == "btn_theme":
            # 根据当前主题应用相应的主题文件，并重新应用样式和设置
            if self.useCustomTheme == "default":
                themeFile = os.path.abspath(os.path.join(self.absPath, "themes\my_custom_theme.qss"))
                UIFunctions.theme(self, themeFile, True)
                # SET HACKS
                AppFunctions.setThemeHack(self)
                self.useCustomTheme = "custom"
            elif self.useCustomTheme == "default1":
                themeFile = os.path.abspath(os.path.join(self.absPath, "themes\my_custom_theme-default.qss"))
                UIFunctions.theme(self, themeFile, True)
                # SET HACKS
                AppFunctions.setThemeHack(self)
                self.useCustomTheme = "custom1"
            elif self.useCustomTheme == "custom":
                themeFile = os.path.abspath(os.path.join(self.absPath, "themes\py_dracula_dark.qss"))
                UIFunctions.theme(self, themeFile, True)
                # SET HACKS
                AppFunctions.setThemeHack(self)
                self.useCustomTheme = "dark"
            else:
                themeFile = os.path.abspath(os.path.join(self.absPath, "themes\py_dracula_light.qss"))
                UIFunctions.theme(self, themeFile, True)
                # SET HACKS
                AppFunctions.setThemeHack(self)
                self.useCustomTheme = "default"

        # SHOW NEW PAGE
        if btnName == "btn_computer":
            widgets.stackedWidget.setCurrentWidget(widgets.computer_info)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

            self.seriesS = QLineSeries()
            self.seriesL = QLineSeries()
            self.seriesS.setName("cpu")
            self.seriesL.setName("memory")
        
        # 打印按钮名称，用于调试
        print(f'Button "{btnName}" pressed!')

    # 窗口大小调整事件处理
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        UIFunctions.resize_grips(self)  # 更新大小调整手柄

    # 鼠标点击事件处理
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint() # 设置窗口拖拽位置

        # 打印鼠标事件，用于调试
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')


# ============ 代码块#1：导入本地数据并处理，显示在表格中 ============
    def load_data(self):
        """
        加载数据函数：
        此函数负责通过文件对话框打开并加载Excel文件。它同时初始化并启动一个后台线程来处理数据加载，避免阻塞主界面。

        功能流程：
        1. 使用QFileDialog.getOpenFileName弹出文件选择对话框，让用户选择Excel或者csv文件。
        2. 若用户选择了文件，则：
        - 在界面上显示选定的文件名。
        - 创建DataLoaderThread线程实例，在后台加载数据。
        - 将线程的data_loaded信号连接到on_data_loaded槽函数，以便数据加载完成后进行处理。
        - 启动线程，开始执行数据加载操作。

        Parameters:
        None

        Returns:
        None
        """
        # 弹出文件选择对话框，让用户选择Excel文件
        file_filter = "Excel Files (*.xlsx *.xls);;CSV Files (*.csv)"
        file_name, _ = QFileDialog.getOpenFileName(self, "打开文件", "", file_filter)

        # 如果用户选择了文件
        if file_name:
            # 在界面上显示选定的文件名
            widgets.lineedit_imported_filename.setText(file_name)
            
            # 创建并初始化数据加载线程
            self.loader_thread = DataLoaderThread(file_name)
            
            # 连接线程结束时的信号到相应的槽函数
            self.loader_thread.data_loaded.connect(self.on_data_loaded)
            
            # 启动线程，开始异步数据加载
            self.loader_thread.start()

    def on_data_loaded(self, data):
        """
        数据加载完成后的处理函数：
        当数据成功加载后，此函数将被调用。它负责接收加载的数据，并更新界面显示及进行后续检查。

        功能流程：
        1. 接收从后台线程传来的加载完成的数据。
        2. 将接收到的数据保存到类的成员变量中以便后续使用。
        3. 调用show_data函数在界面上显示加载的数据。
        4. 调用check_data函数进行数据的有效性检查及后续处理。

        Parameters:
        data - 加载完成的数据，通常是一个DataFrame或类似的数据结构。

        Returns:
        None
        """
        self.data = data  # 保存加载的数据
        self.show_data(data, widgets.tablewidget_raw_data)  # 在界面上显示数据
        self.check_data()  # 检查数据并进行后续处理
# ======================== 代码块#1结束 ========================
  

# ============ 代码块#2：特征处理，显示在表格中 ============
    def data_processing(self):
        """初始化并启动数据处理线程。"""
        print("Data processing...\n", self.data)
        if self.data is not None:
            # 定义数据处理顺序和对应的方法、选项和表格名称
            process_sequence = [
                ('handle_missing_values', widgets.combobox_missing_values_handling.currentText(), 'tablewidget_data_missing_handled'),
                ('handle_outliers', widgets.combobox_outlier_handling.currentText(), 'tablewidget_data_outlier_handled'),
                ('handle_categorical', widgets.combobox_categorical_handling.currentText(), 'tablewidget_data_categorical_handled'),
                ('handle_normalization', widgets.combobox_data_normalization_handling.currentText(), 'tablewidget_data_normalization_handled'),
            ]

            # 创建并启动处理线程
            self.processor_thread = DataProcessingThread(self.data, process_sequence)
            self.processor_thread.data_processed.connect(self.on_data_processed)
            self.processor_thread.start()

    def on_data_processed(self, processed_data, operation_name, processed):
        """
        当数据处理线程完成一步处理时调用，更新UI展示数据处理结果。
        
        参数:
        processed_data - pd.DataFrame, 处理后的数据
        operation_name - str, 与表格小部件相关联的操作名称
        processed - bool, 指示当前步骤的数据是否被处理
        
        功能描述:
        1. 如果数据被处理（processed为True），则在对应的表格小部件中显示数据。
        2. 如果数据未被处理（processed为False）：
        a. 检查表格是否为空，如果不为空，则清空表格；
        b. 如果表格已经为空，则不执行任何操作。
        """
        # 根据操作名称找到对应的表格小部件
        table_widget = getattr(widgets, operation_name)

        if processed:
            # 如果数据已处理，使用处理后的数据作为新的输入数据
            self.data = processed_data
            # 数据被处理，显示数据
            self.show_data(processed_data, table_widget)
        else:
            # 数据未被处理，检查表格是否为空
            if table_widget.rowCount() > 0 or table_widget.columnCount() > 0:
                # 表格不为空，清空表格内容
                table_widget.clear()
                table_widget.setRowCount(0)  # 重置行数为0
                table_widget.setColumnCount(0)  # 重置列数为0
            # 如果表格已经为空，则不需要额外操作
            else:
                pass
# ======================== 代码块#2结束 ========================


# ============ 代码块##：点击特征选择树弹出参数设置对话框设置并读取参数 ============
    def on_item_clicked(self, item, column):
        # 只处理第一列的点击事件
        if column == 0:
            method = item.text(0)
            note = item.text(1)
            key = f"{method}-{note}"
            # 检查项目的勾选状态
            if item.checkState(column) == Qt.Checked:
                # 如果项目被勾选，弹出对话框
                dialog = FeatureSelectionParamsDialog(self, title=note)
                if dialog.exec():
                    # 如果点击确定，保存参数
                    self.selected_items[method] = dialog.text_edit.text()
                else:
                    # 如果点击取消，取消勾选
                    item.setCheckState(column, Qt.Unchecked)
            else:
                # 如果取消勾选，从字典中删除对应的键值对
                if method in self.selected_items:
                    del self.selected_items[method]
            
            print('刚点击的参数：', method)
            print('所有选中的参数：\n', self.selected_items)
# ======================== 代码块#2结束 ========================
            

# ============ 代码块##：根据选择的特征处理方法显示处理后的数据 ============
    def show_feature_selection_window(self):
            feature_selection_window = FeatureSelectionWindow()
            sub_window_FeatureSelectParam = NonClosableMdiSubWindow()  # 使用自定义的NonClosableMdiSubWindow
            sub_window_FeatureSelectParam.setWidget(feature_selection_window)
            sub_window_FeatureSelectParam.setWindowTitle("特征选择")

            widgets.mdiArea_FeatureSelection.addSubWindow(sub_window_FeatureSelectParam)
            # 创建一个QBrush，用一个纯色填充
            brush = QBrush(QColor(33, 37, 43))
            # 设置QMdiArea的背景画刷
            widgets.mdiArea_FeatureSelection.setBackground(brush)
            sub_window_FeatureSelectParam.show()

            # 将特征选择树与复选框勾选方法关联
            feature_selection_window.ui.treeWidget_featureSelection.itemClicked.connect(self.on_item_clicked)
            # 用于存储特征选择TreeWidget所有被选中的项目
            self.selected_items = {}

            # 将特征选择按钮与特征选择函数关联
            feature_selection_window.ui.btn_featureSelection.clicked.connect(self.feature_selection)
            
            # 将特征相关性分析按钮与热图函数关联
            feature_selection_window.ui.btn_correlationAnalysis.clicked.connect(self.show_correlation_heatmap)
            
            feature_selection_window.ui.btn_importanceRanking.clicked.connect(self.show_feature_importance_dialog)

    def show_correlation_heatmap(self):
        if hasattr(self, 'processed_data'):
            self.create_correlation_heatmap_subwindow(self.processed_data, "Correlation Heatmap")
        else:
            print("没有可用的数据来显示热图。请先进行特征选择。")

    def feature_selection(self):
        # 创建并启动特征选择线程
        self.FeatureSelection_thread = FeatureSelectionThread(self.data, self.selected_items)
        self.FeatureSelection_thread.data_processed.connect(self.on_feature_selection_finished)
        self.FeatureSelection_thread.start()
    
    def on_feature_selection_finished(self, data, processing_info):
        """
        特征选择完成后的处理函数：
        当特征选择完成后，此函数将被调用。它负责接收特征选择的结果，并更新界面显示及进行后续检查。

        功能流程：
        1. 接收从后台线程传来的特征选择结果。
        2. 将接收到的数据保存到类的成员变量中以便后续使用。
        3. 调用show_data函数在界面上显示加载的数据。
        4. 调用check_data函数进行数据的有效性检查及后续处理。

        Parameters:
        data - 加载完成的数据，通常是一个DataFrame或类似的数据结构。

        Returns:
        None
        """      
        self.processed_data = data  # 保存处理后的数据以供热图使用
        # 显示处理后的数据
        self.create_mdi_subwindow_with_table(data, "Processed Data")

        # 绘制并显示皮尔森相关系数热图
        # self.create_correlation_heatmap_subwindow(data, "Correlation Heatmap")

        # 显示处理信息
        info_text = self.format_processing_info(processing_info)
        self.create_mdi_subwindow_with_text(info_text, "Processing Info")

    def format_processing_info(self, processing_info):
        info_lines = [
            f"Total features: {processing_info['total_features']}",
            "Selected features each step:"
        ]
        for method, features in processing_info['selected_each_step'].items():
            info_lines.append(f"{method}: {features}")
        info_lines.append(f"Final selected features: {processing_info['final_selected_features']}")
        return "\n".join(info_lines)

    def subwindow_closed(self, title):
        """当子窗口关闭时调用，从跟踪字典中移除对应的记录"""
        if title in self.open_subwindows:
            del self.open_subwindows[title]

    def create_mdi_subwindow_with_table(self, data, title):
        """
        根据提供的树项目和数据创建新的标签页和表格。

        参数:
        data - pd.DataFrame，包含要在表格中显示的数据。
        title - 字符串，子窗口的标题。
        """
        # 检查子窗口是否已经存在
        if title in self.open_subwindows:
            # 如果已存在，将其带到前台
            self.open_subwindows[title].setFocus()
        else:
            # 创建一个新的QWidget作为MDI子窗口的内容
            widget = QWidget()
            row_count = data.shape[0]
            column_count = data.shape[1]
            table = QTableWidget(row_count, column_count)
            table.setHorizontalHeaderLabels(data.columns)
            
            # 将数据填充到表格中
            for row in range(row_count):
                for column in range(column_count):
                    item_text = str(data.iloc[row, column])
                    item = QTableWidgetItem(item_text)
                    table.setItem(row, column, item)

            # 创建布局并添加表格
            layout = QHBoxLayout()
            layout.addWidget(table)
            widget.setLayout(layout)

            # 创建MDI子窗口并设置内容
            sub_window = QMdiSubWindow()
            sub_window.setWidget(widget)
            sub_window.setWindowTitle(title)

            sub_window.setAttribute(Qt.WA_DeleteOnClose)  # 确保窗口关闭时释放资源
            sub_window.destroyed.connect(lambda: self.subwindow_closed(title))  # 连接关闭信号

            # 将子窗口添加到MDI区域并显示
            widgets.mdiArea_FeatureSelection.addSubWindow(sub_window)
            sub_window.show()

            # 将子窗口添加到跟踪字典
            self.open_subwindows[title] = sub_window

    def create_correlation_heatmap_subwindow(self, data, title="Correlation Heatmap"):
        if title in self.open_subwindows:
            self.open_subwindows[title].setFocus()
        else:
            # 创建画布和图形
            fig = Figure(figsize=(10, 8))
            canvas = FigureCanvas(fig)
            ax = fig.add_subplot(111)

            # 计算皮尔森相关系数并绘制热图
            correlation_matrix = data.iloc[:-1, :-1].corr(method='pearson')
            heatmap = sns.heatmap(correlation_matrix, ax=ax, cmap='jet', linewidths=0.5, square=True, annot=False)

            # 设置坐标轴标签
            ax.set_xlabel('Features')
            ax.set_ylabel('Features')

            # 设置colorbar的标题
            cbar = ax.collections[0].colorbar
            cbar.set_label('Pearson Correlation Coefficient')

            # 创建QWidget作为MDI子窗口的内容
            widget = QWidget()
            layout = QVBoxLayout()
            layout.addWidget(canvas)  # 将画布添加到布局中
            widget.setLayout(layout)

            # 创建MDI子窗口并设置内容
            sub_window = QMdiSubWindow()
            sub_window.setWidget(widget)
            sub_window.setWindowTitle(title)
            sub_window.setAttribute(Qt.WA_DeleteOnClose)
            sub_window.destroyed.connect(lambda: self.subwindow_closed(title))

            widgets.mdiArea_FeatureSelection.addSubWindow(sub_window)
            sub_window.show()

            self.open_subwindows[title] = sub_window

    def create_mdi_subwindow_with_text(self, text, title):
         # 检查子窗口是否已经存在
        if title in self.open_subwindows:
            # 如果已存在，将其带到前台
            self.open_subwindows[title].setFocus()
        else:
            # 创建一个新的QWidget作为MDI子窗口的内容
            widget = QWidget()
            text_edit = QTextEdit()
            text_edit.setText(text)
            text_edit.setReadOnly(True)  # 设置为只读

            # 设置文本编辑器的样式
            text_edit.setStyleSheet("""
                QTextEdit {
                    background-color: rgb(33, 37, 43);
                    color: balck;  /* 字体颜色 */
                }
            """)

            # 创建布局并添加文本编辑器
            layout = QVBoxLayout()
            layout.addWidget(text_edit)
            widget.setLayout(layout)

            # 创建MDI子窗口并设置内容
            sub_window = QMdiSubWindow()
            sub_window.setWidget(widget)
            sub_window.setWindowTitle(title)
            
            sub_window.setAttribute(Qt.WA_DeleteOnClose)  # 确保窗口关闭时释放资源
            sub_window.destroyed.connect(lambda: self.subwindow_closed(title))  # 连接关闭信号

            widgets.mdiArea_FeatureSelection.addSubWindow(sub_window)
            sub_window.show()

            # 将子窗口添加到跟踪字典
            self.open_subwindows[title] = sub_window
# ======================== 代码块##结束 ========================


# ============ 代码块##：根据选择的特征排序方法进行特征重要性排序 ============
    def show_feature_importance_dialog(self):
        dialog = FeatureImportanceDialog()
        if dialog.exec():
            selected_methods = dialog.get_selected_methods()
            if selected_methods:
                self.start_feature_importance_thread(selected_methods)

    def start_feature_importance_thread(self, methods):
        # 创建并启动特征重要性线程
        self.feature_importance_thread = FeatureImportanceThread(self.processed_data, methods)
        self.feature_importance_thread.result_ready.connect(self.on_feature_importance_ready)
        self.feature_importance_thread.start()

    def on_feature_importance_ready(self, importance_results):
        # 展示所有方法和平均特征重要性的表格
        self.create_mdi_subwindow_with_table(importance_results, "Feature Importance")

        # 展示平均特征重要性的柱状图
        self.create_mdi_subwindow_with_plot(importance_results, "Average Feature Importance")

    def create_mdi_subwindow_with_table(self, data, title):
        # ... 创建表格的代码 ...
        # 检查子窗口是否已经存在
        if title in self.open_subwindows:
            # 如果已存在，将其带到前台
            self.open_subwindows[title].setFocus()
        else:
            # 创建一个新的QWidget作为MDI子窗口的内容
            widget = QWidget()
            row_count = data.shape[0]
            column_count = data.shape[1]
            table = QTableWidget(row_count, column_count)
            table.setHorizontalHeaderLabels(data.columns)
            
            # 将数据填充到表格中
            for row in range(row_count):
                for column in range(column_count):
                    item_text = str(data.iloc[row, column])
                    item = QTableWidgetItem(item_text)
                    table.setItem(row, column, item)

            # 创建布局并添加表格
            layout = QHBoxLayout()
            layout.addWidget(table)
            widget.setLayout(layout)

            # 创建MDI子窗口并设置内容
            sub_window = QMdiSubWindow()
            sub_window.setWidget(widget)
            sub_window.setWindowTitle(title)

            sub_window.setAttribute(Qt.WA_DeleteOnClose)  # 确保窗口关闭时释放资源
            sub_window.destroyed.connect(lambda: self.subwindow_closed(title))  # 连接关闭信号

            # 将子窗口添加到MDI区域并显示
            widgets.mdiArea_FeatureSelection.addSubWindow(sub_window)
            sub_window.show()

            # 将子窗口添加到跟踪字典
            self.open_subwindows[title] = sub_window
        

    def create_mdi_subwindow_with_plot(self, data, title):
        # 创建画布和图形
        fig = Figure()
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)

        # 绘制柱状图
        data.iloc[:, -1].plot(kind='barh', ax=ax)

        # 设置坐标轴标签
        ax.set_ylabel('Features')  # 现在y轴表示特征重要性
        ax.set_xlabel('Average feature importance')  # x轴表示特征

        # 反转y轴的顺序
        ax.invert_yaxis()

        # 创建QWidget作为MDI子窗口的内容
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        widget.setLayout(layout)

        # 创建MDI子窗口并设置内容
        sub_window = QMdiSubWindow()
        sub_window.setWidget(widget)
        sub_window.setWindowTitle(title)
        widgets.mdiArea_FeatureSelection.addSubWindow(sub_window)
        sub_window.show()

# ============ 代码块##：结束 ============


# ============ 代码块##：模型训练 ============
    def show_model_train_window(self):
        # 创建模型训练窗口实例
        model_train_window = ModelTrainWindow()

        # 使用自定义的NonClosableMdiSubWindow
        sub_window_ModelTrain = NonClosableMdiSubWindow()
        sub_window_ModelTrain.setWidget(model_train_window)
        sub_window_ModelTrain.setWindowTitle("模型训练")

        # 这段代码会使treeWidget第一列的宽度自动调整以适应其内容，而第二列则会填充剩余的空间
        header = model_train_window.ui.treeWidget_AlgorithmSelection.header()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)  # 第一列
        header.setSectionResizeMode(1, QHeaderView.Stretch)           # 第二列
        
        # 设置子窗口的最大宽度为450
        sub_window_ModelTrain.setMaximumWidth(450)

        # 如果需要，设置一个合理的最小宽度
        sub_window_ModelTrain.setMinimumWidth(390)  # 这里的200可以根据需要调整
        sub_window_ModelTrain.setMinimumHeight(560)  # 这里的200可以根据需要调整

        # 将子窗口添加到MDI区域
        widgets.mdiArea_ModelTraining.addSubWindow(sub_window_ModelTrain)

        # 创建一个QBrush，用一个纯色填充
        brush = QBrush(QColor(33, 37, 43))

        # 设置QMdiArea的背景画刷
        widgets.mdiArea_ModelTraining.setBackground(brush)
        sub_window_ModelTrain.show()

# ============ 代码块##：结束 ============
                

# ============ 代码块#3：在表格中显示数据 ============
    def show_data(self, data, table_widget):
        """
        在界面上显示数据的函数：
        此函数负责将加载的数据显示在指定的表格小部件中。它会调整表格的行列以匹配数据大小，并填充数据。
        同时，它也会将DataFrame的索引和列名显示在表格中。

        功能流程：
        1. 调用switch_tabs函数切换到目标表格所在的标签页。
        2. 设置表格的行数和列数以匹配数据的维度。
        3. 遍历数据，将每个数据项填充到表格的相应单元格中。
        4. 数据显示完成后，弹出消息框通知用户数据导入成功。

        Parameters:
        data - 要显示的数据，通常是一个DataFrame或类似的数据结构。
        table_widget - 要显示数据的QTableWidget对象。

        Returns:
        None
        """
        # 切换到数据应该显示的标签页
        self.switch_tabs(table_widget)  
        
        # 设置表格的行数和列数
        table_widget.setRowCount(data.shape[0])
        table_widget.setColumnCount(data.shape[1] + 1)  # 加1为索引列

        # 获取索引名
        index_name = data.index.name

        # 设置水平表头（列名）
        table_widget.setHorizontalHeaderLabels([index_name] + list(data.columns))

        # 设置垂直表头（索引）
        # table_widget.setVerticalHeaderLabels(data.index.astype(str))
        
        # 数据总行数，用于更新进度条
        total_rows = data.shape[0]
        # 填充数据
        for row_index, row in enumerate(data.itertuples(index=False), start=0):
            # 设置每行的索引值
            table_widget.setItem(row_index, 0, QTableWidgetItem(str(data.index[row_index])))
            # 填充数据
            for col_index, value in enumerate(row):
                table_widget.setItem(row_index, col_index + 1, QTableWidgetItem(str(value)))

            # 更新进度条：完成的行数 / 总行数 * 100
            # time.sleep(0.1)  # 仅用于演示，实际使用中应去掉
            widgets.progressBar.setValue(int(row_index / total_rows * 100))

        # widgets.tablewidget_raw_data.resizeColumnsToContents()   # 调整列宽以适应内容
        widgets.progressBar.setValue(100)  # 最后确保进度条到达100%
        
        # 数据显示完成，弹出消息框通知用户
        # QMessageBox.information(self, "显示数据", "数据导入成功！")

    def switch_tabs(self, table_widget):
        """
        切换标签页的函数：
        此函数负责将用户界面中的当前显示标签页切换到包含指定表格小部件的标签页。函数会检查表格小部件的父组件是否为QTabWidget，并据此进行切换。

        功能流程：
        1. 获取传入的表格小部件的父组件。
        2. 检查父组件是否为QTabWidget类型。如果是，切换到包含表格小部件的标签页；如果不是，弹出错误提示。

        Parameters:
        table_widget - 需要切换到的表格小部件，它的父组件应该是QTabWidget。

        Returns:
        None
        """
        # 获取表格小部件的父组件
        parent_widget = table_widget.parentWidget()
        widgets.tabWidgetMLRawData.setCurrentWidget(parent_widget)

        # parent_widget1 = parent_widget.parentWidget()
        # parent_widget1.setCurrentWidget(parent_widget)
# ======================== 代码快#3结束 ========================


# ============ 代码块#4：检查数据并更新UI ============
    def check_data(self):
        """
        检查导入的数据中是否存在缺失值和异常值，根据实际情况更新UI。
        如果存在缺失值，禁用combobox_missing_values_handling。
        如果存在异常值，禁用combobox_outlier_handling。
        """
        # 检查缺失值
        if self.data.isnull().any().any():
            widgets.combobox_missing_values_handling.setEnabled(True)
        else:
            widgets.combobox_missing_values_handling.setDisabled(True)
        
        # 检查异常值，这里使用简单的统计方法作为示例
        if self.has_outliers(self.data):
            widgets.combobox_outlier_handling.setEnabled(True)
        else:
            widgets.combobox_outlier_handling.setDisabled(True)

    def has_outliers(self, data):
        """
        检查DataFrame是否含有异常值。
        一个简单的统计方法是检查是否有任何值超过了均值的3个标准差。
        注意：这只是一个示例，你可能需要根据数据的实际分布调整这个方法。
        
        Parameters:
        data - pandas DataFrame, 导入的数据

        Returns:
        bool - 如果数据中存在异常值返回True，否则返回False
        """
        if isinstance(data, pd.DataFrame):
            numeric_data = data.select_dtypes(include=[np.number])  # 仅选择数值列
            z_scores = np.abs((numeric_data - numeric_data.mean()) / numeric_data.std())
            return (z_scores > 3).any().any()  # 超过3个标准差认为是异常值
        return False  # 如果不是DataFrame，直接返回False
# ======================== 代码快#4结束 ========================    


# ============ 代码块#5：鼠标右键导出表格数据 ============
    def contextMenuEvent(self, event):
        """重写contextMenuEvent来提供自定义的右键菜单。
        
        当用户在表格上右键点击时，此方法将被触发。如果当前的表格不为空，
        将显示一个包含导出选项的上下文菜单。
        """
        # 获取当前活动的Tab内的QTableWidget
        active_table_widget = widgets.tabWidgetMLRawData.currentWidget().findChild(QTableWidget)
        
        # 如果找到QTableWidget且不为空，则显示菜单
        if active_table_widget and not self.is_table_empty(active_table_widget):
            menu = QMenu(self)

            # 创建导出数据动作，并设置图标和文本
            export_action = QAction(QIcon('images/images/export_data.png'), "导出数据", self)  # 假设有一个icons/export.png图标
            export_action.triggered.connect(lambda: self.export_data(active_table_widget))

            # 将动作添加到菜单
            menu.addAction(export_action)

            # 在鼠标点击位置显示菜单
            menu.exec(event.globalPosition().toPoint())

    def is_table_empty(self, table_widget):
        """检查指定的QTableWidget是否为空。
        
        参数:
        table_widget: 要检查的QTableWidget实例。

        返回:
        bool: 如果表格为空则返回True，否则返回False。
        """
        return table_widget.rowCount() == 0 or table_widget.columnCount() == 0

    def export_data(self, table_widget):
        """从table_widget中导出数据到指定的文件，并包括表头。

        用户将通过文件对话框选择导出的文件路径和格式。支持导出为Excel (.xlsx) 和 CSV (.csv)。

        参数:
        table_widget: 要导出数据的QTableWidget实例。
        """
        file_name, _ = QFileDialog.getSaveFileName(self, "保存文件", "data", "Excel Files (*.xlsx);;CSV Files (*.csv)")
        if file_name:
            # 收集表格数据
            data = [[table_widget.item(row, col).text() if table_widget.item(row, col) else "" 
                     for col in range(table_widget.columnCount())] 
                    for row in range(table_widget.rowCount())]
            
            # 获取列标题
            column_headers = [table_widget.horizontalHeaderItem(i).text() for i in range(table_widget.columnCount())]

            # 创建DataFrame并设置列标题
            df = pd.DataFrame(data, columns=column_headers)

            # 导出文件
            if file_name.endswith('.xlsx'):
                df.to_excel(file_name, index=False)
            elif file_name.endswith('.csv'):
                df.to_csv(file_name, index=False)
# ======================== 代码快#5结束 ========================


# ============ 代码块#6：下载数据库文件 ============
    def download_data(self):
        """下载数据并保存为Excel或CSV文件。
        
        此函数将弹出一个文件保存对话框，让用户选择保存文件的位置和格式。
        用户可以选择保存为Excel格式或CSV格式。
        """
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog

        # 弹出文件保存对话框，让用户选择保存为Excel或CSV
        fileName, selectedFilter = QFileDialog.getSaveFileName(self, "下载数据",
                                                               "data", "Excel Files (*.xlsx);;CSV Files (*.csv)",
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
# ======================== 代码快#6结束 ========================

    
# ============ 代码块#7：播放视频教程 ============
    def play_tutorial(self):
        """用默认播放器打开项目中的mp4视频教程。"""
        video_path = os.path.join(os.getcwd(), "databases/tutorial.mp4")  # 替换为视频文件的实际路径

        if os.path.exists(video_path):
            if sys.platform == 'win32':
                os.startfile(video_path)  # Windows下使用startfile打开
            else:
                opener = "open" if sys.platform == "darwin" else "xdg-open"  # MacOS使用open，Linux使用xdg-open
                subprocess.call([opener, video_path])
        else:
            QMessageBox.warning(self, "视频教程", "找不到视频文件！")
# ======================== 代码快#7结束 ========================


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_dialog = LoginMainWindow()

    def on_login_success():
        # 登录成功后要执行的操作
        app.setWindowIcon(QIcon("images/images/DataPilot_icon.png"))
        window = MainWindow()
        window.show()

    # 连接登录成功的信号到槽函数
    login_dialog.loggedIn.connect(on_login_success)

    login_dialog.show()  # 显示登录窗口
    sys.exit(app.exec())
