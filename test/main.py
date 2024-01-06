import sys
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from PySide6.QtGui import QAction, QIcon, QCursor

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox, QTableWidget, QTabWidget, QMenu
from PySide6.QtCore import Qt, QThread, Signal, QFile, QPoint

# 导入你的ui文件
# from your_ui_file import Ui_MainWindow
from Ui_test import Ui_MainWindow  # 导入从Qt Designer转换的UI

class DataLoaderThread(QThread):
    """
    用于在后台线程中加载数据的类。
    继承自QThread，专门用于读取Excel或者csv文件并在完成后发出信号。
    
    Attributes:
        data_loaded: 一个自定义的Signal，用于在数据加载完成后发出信号。携带加载的pd.DataFrame数据。
        file_name: 用于存储待加载文件的文件名。
    
    Methods:
        __init__(self, file_name): 构造函数，接收一个表示Excel或者csv文件路径的字符串。
        run(self): 重写的QThread方法，用于执行数据加载操作。
    """

    data_loaded = Signal(pd.DataFrame)  # 定义一个信号，用于在数据加载完成时发出

    def __init__(self, file_name):
        """
        DataLoaderThread类的初始化方法。
        
        Parameters:
            file_name: 一个字符串，表示要加载的Excel或者csv文件的路径。
        """
        super().__init__()
        self.file_name = file_name  # 存储文件路径

    def run(self):
        """
        重写QThread的run方法。这是线程开始执行时调用的方法。
        该方法会加载指定的Excel或者csv文件，读取数据，并通过data_loaded信号发送数据。
        """
        try:
            if self.file_name.endswith(('.xlsx', '.xls')):
                # 用pandas读取Excel文件
                data = pd.read_excel(self.file_name, header=0, index_col=0)
            elif self.file_name.endswith('.csv'):
                # 用pandas读取CSV文件
                data = pd.read_csv(self.file_name, header=0, index_col=0)
            else:
                QMessageBox.warning(self, "文件类型错误", "不支持的文件类型！")
                return
        except Exception as e:
            QMessageBox.critical(self, "加载失败", f"加载数据失败：{e}")

        self.data_loaded.emit(data)  # 数据加载完成后，发出信号并附带加载的数据


class DataProcessingThread(QThread):
    data_processed = Signal(pd.DataFrame, str, bool)

    def __init__(self, data, process_sequence):
        super().__init__()
        self.data = data
        self.process_sequence = process_sequence

    def run(self):
        """线程的运行入口，按顺序执行定义的数据处理序列。"""
        current_data = self.data
        for process_func, operation_method, table_widget in self.process_sequence:
            processed = True  # 假设每步默认进行处理
            if operation_method != "不处理":
                # 动态调用处理方法
                current_data = getattr(self, process_func)(current_data, operation_method)
            else:
                # 如果当前步骤选择“不处理”，设置标志为False
                processed = False

            # 发送每步处理后的数据、操作名称和是否显示处理的标志
            self.data_processed.emit(current_data, table_widget, processed)

    def handle_missing_values(self, data, operation_method):
        """
        处理缺失值的函数。
        
        参数:
        data - pandas DataFrame，包含可能存在缺失值的数据。
        operation_method - 字符串，指定处理缺失值的方法。
        
        支持的操作方法:
        "平均值处理" - 用各列的平均值填充对应列的缺失值。
        "中位数填充" - 用各列的中位数填充对应列的缺失值。
        "众数填充" - 用各列的众数填充对应列的缺失值。
        "固定值填充" - 用一个固定值填充所有缺失值，这里假设为0。
        "最近邻填充" - 用K-最近邻算法填充缺失值。
        "删除整行" - 删除包含缺失值的行。
        "删除整列" - 删除包含缺失值的列。
        
        返回:
        处理后的pandas DataFrame。
        """
        if operation_method == "平均值填充":
            return data.fillna(data.mean())
        elif operation_method == "中位数填充":
            return data.fillna(data.median())
        elif operation_method == "众数填充":
            return data.fillna(data.mode().iloc[0])
        elif operation_method == "固定值填充":
            return data.fillna(0)  # 这里假设用0作为填充值，可以根据需要修改
        elif operation_method == "最近邻填充":
            imputer = KNNImputer(n_neighbors=2)  # K-最近邻算法，这里假设用2个最近邻
            return pd.DataFrame(imputer.fit_transform(data), columns=data.columns)
        elif operation_method == "删除整行":
            return data.dropna(axis=0)  # 删除包含缺失值的行
        elif operation_method == "删除整列":
            return data.dropna(axis=1)  # 删除包含缺失值的列
        else:
            return data  # 如果没有匹配的处理方法，返回原始数据

    def handle_outliers(self, data, operation_method):
        # 实现异常值处理逻辑
        return data

    def handle_categorical(self, data, operation_method):
        # 实现离散值处理逻辑
        return data

    def handle_normalization(self, data, operation_method):
        # 实现数据归一化逻辑
        return data

    # 在此处定义其他数据处理方法...


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.ui = Ui_MainWindow()  # 创建UI对象
#         self.ui.setupUi(self)  # 设置UI

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data = None

        # 为主窗口添加一个右键菜单事件
        # self.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.customContextMenuRequested.connect(self.show_context_menu)

        # 绑定按钮事件
        self.btn_open_local_file.clicked.connect(self.load_data)
        self.btn_FeatureProcessing.clicked.connect(self.data_processing)
        
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
            self.lineedit_imported_filename.setText(file_name)
            
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
        self.show_data(data, self.tablewidget_raw_data)  # 在界面上显示数据
        self.check_data()  # 检查数据并进行后续处理


    def data_processing(self):
        """初始化并启动数据处理线程。"""
        if self.data is not None:
            # 定义数据处理顺序和对应的方法、选项和表格名称
            process_sequence = [
                ('handle_missing_values', self.combobox_missing_values_handling.currentText(), 'tablewidget_data_missing_handled'),
                ('handle_outliers', self.combobox_outlier_handling.currentText(), 'tablewidget_data_outlier_handled'),
                ('handle_categorical', self.combobox_categorical_handling.currentText(), 'tablewidget_data_categorical_handled'),
                ('handle_normalization', self.combobox_data_normalization_handling.currentText(), 'tablewidget_data_normalization_handled'),
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
        table_widget = getattr(self, operation_name)

        if processed:
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
            self.progressBar.setValue(int(row_index / total_rows * 100))

        # widgets.tablewidget_raw_data.resizeColumnsToContents()   # 调整列宽以适应内容
        self.progressBar.setValue(100)  # 最后确保进度条到达100%
        
        # 数据显示完成，弹出消息框通知用户
        # QMessageBox.information(self, "显示数据", "数据导入成功！")

    def check_data(self):
        """
        检查导入的数据中是否存在缺失值和异常值，根据实际情况更新UI。
        如果存在缺失值，禁用combobox_missing_values_handling。
        如果存在异常值，禁用combobox_outlier_handling。
        """
        # 检查缺失值
        if self.data.isnull().any().any():
            self.combobox_missing_values_handling.setEnabled(True)
        else:
            self.combobox_missing_values_handling.setDisabled(True)
        
        # 检查异常值，这里使用简单的统计方法作为示例
        if self.has_outliers(self.data):
            self.combobox_outlier_handling.setEnabled(True)
        else:
            self.combobox_outlier_handling.setDisabled(True)

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
        self.tabWidgetMLRawData.setCurrentWidget(parent_widget)

        # parent_widget1 = parent_widget.parentWidget()
        # parent_widget1.setCurrentWidget(parent_widget)


 ################### 右键导出数据 ###########################
    def contextMenuEvent(self, event):
        """重写contextMenuEvent来提供自定义的右键菜单。"""
        tab = self.tabWidgetMLRawData.currentWidget()
        # 查找嵌入在QWidget中的QTableWidget
        table_widget = tab.findChild(QTableWidget)
        if table_widget and not self.is_table_empty(table_widget):
            menu = QMenu(self)
            export_action = menu.addAction("导出数据")
            export_action.triggered.connect(lambda: self.export_data(table_widget))
            menu.exec(event.globalPos())

    def is_table_empty(self, table_widget):
        """检查指定的QTableWidget是否为空。"""
        return table_widget.rowCount() == 0 or table_widget.columnCount() == 0

    def export_data(self, table_widget):
        """从table_widget中导出数据到指定的文件，并包括表头。"""
        file_name, _ = QFileDialog.getSaveFileName(self, "保存文件", "", "Excel Files (*.xlsx);;CSV Files (*.csv)")
        if file_name:
            # 收集数据
            data = []
            for row in range(table_widget.rowCount()):
                row_data = []
                for col in range(table_widget.columnCount()):
                    item = table_widget.item(row, col)
                    row_data.append(item.text() if item else "")
                data.append(row_data)
            
            # 获取列标题
            column_headers = [table_widget.horizontalHeaderItem(i).text() for i in range(table_widget.columnCount())]
            
            # 获取行标题
            # row_headers = [table_widget.verticalHeaderItem(i).text() for i in range(table_widget.rowCount())]

            # 创建DataFrame
            df = pd.DataFrame(data, columns=column_headers)

            # 将第一列设置为索引
            df.set_index(df.columns[0], inplace=True)

            # 将所有的文本浮点数转换为真正的浮点数
            for column in df.columns:
                df[column] = pd.to_numeric(df[column], errors='coerce')

            # 导出文件
            if file_name.endswith('.xlsx'):
                df.to_excel(file_name, index=True)
            elif file_name.endswith('.csv'):
                df.to_csv(file_name, index=True)
##############################################


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建应用程序实例
    window = MainWindow()  # 创建主窗口实例
    window.show()  # 显示窗口
    sys.exit(app.exec())  # 运行应用程序