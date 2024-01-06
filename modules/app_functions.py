# ///////////////////////////////////////////////////////////////
#
# 作者: liyihang
# 项目使用: Qt Designer 和 PySide6 制作
# 版本: 1.0.0
#
# 所有功能的多线程类都可以在这里定义
#
# ///////////////////////////////////////////////////////////////

# 主文件
# ///////////////////////////////////////////////////////////////
from main import *  # 从main.py文件导入所有内容
import numpy as np
import pandas as pd
from PySide6.QtCore import QThread, Signal  # 导入QThread和Signal类
from sklearn.preprocessing import MinMaxScaler, StandardScaler, MaxAbsScaler, RobustScaler

# 访问主窗口小部件
# ///////////////////////////////////////////////////////////////
class AppFunctions(MainWindow):  # 定义AppFunctions类，继承自MainWindow类
    # 设置主题样式的函数
    def setThemeHack(self):
        # 设置左侧菜单按钮的背景颜色
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #495474;"
        # 设置右侧额外区域按钮的背景颜色
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #495474;"
        # 设置选中菜单项的样式
        Settings.MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: #566388;
        """


        # SET MANUAL STYLES
        # self.ui.lineEdit.setStyleSheet("background-color: #6272a4;")
        # self.ui.pushButton.setStyleSheet("background-color: #6272a4;")
        # self.ui.plainTextEdit.setStyleSheet("background-color: #6272a4;")
        # self.ui.tableWidget.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        # self.ui.scrollArea.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        # self.ui.comboBox.setStyleSheet("background-color: #6272a4;")
        # self.ui.horizontalScrollBar.setStyleSheet("background-color: #6272a4;")
        # self.ui.verticalScrollBar.setStyleSheet("background-color: #6272a4;")
        # self.ui.commandLinkButton.setStyleSheet("color: #ff79c6;")

# ============ 代码块#1：导入本地数据并显示在表格中 ============
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
# ======================== 代码快#1：结束 ========================


# ============ 代码块#2：特征处理 ============
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
        """
        处理异常值的函数。
        
        参数:
        data - pandas DataFrame，包含可能存在异常值的数据。
        operation_method - 字符串，指定处理异常值的方法。
        
        支持的操作方法:
        "平均值填充" - 用各列的平均值填充对应列的异常值。
        "中位数填充" - 用各列的中位数填充对应列的异常值。
        "众数填充" - 用各列的众数填充对应列的异常值。
        "删除整行" - 删除包含异常值的行。
        "删除整列" - 删除包含异常值的列。
        "不处理" - 不进行任何处理，返回原始数据。
        
        返回:
        处理后的pandas DataFrame。
        """
        if operation_method in ["平均值填充", "中位数填充", "众数填充"]:
            for col in data.select_dtypes(include=[np.number]).columns:
                column_data = data[col].dropna()
                mean = np.mean(column_data)
                std = np.std(column_data)
                z_score = np.abs((column_data - mean) / std)  # 计算Z-score
                outlier_indexes = data[z_score > 3].index  # 通常Z-score大于3认为是异常值
                
                if operation_method == "平均值填充":
                    data.loc[outlier_indexes, col] = mean
                elif operation_method == "中位数填充":
                    data.loc[outlier_indexes, col] = np.median(column_data)
                elif operation_method == "众数填充":
                    data.loc[outlier_indexes, col] = column_data.mode()[0]

        elif operation_method == "删除整行":
            for col in data.select_dtypes(include=[np.number]).columns:
                column_data = data[col].dropna()
                mean = np.mean(column_data)
                std = np.std(column_data)
                z_score = np.abs((column_data - mean) / std)
                data = data[z_score <= 3]  # 保留非异常值

        elif operation_method == "删除整列":
            for col in data.select_dtypes(include=[np.number]).columns:
                column_data = data[col].dropna()
                mean = np.mean(column_data)
                std = np.std(column_data)
                z_score = np.abs((column_data - mean) / std)
                if any(z_score > 3):
                    data.drop(columns=col, inplace=True)

        elif operation_method == "不处理":
            return data  # 不进行任何操作，返回原始数据

        return data

    def handle_categorical(self, data, operation_method):
        # 实现离散值处理逻辑
        return data

    def handle_normalization(self, data, operation_method):
        """
        处理数据归一化的函数。
        
        参数:
        data - pandas DataFrame，包含需要归一化处理的数据。
        operation_method - 字符串，指定归一化处理的方法。
        
        支持的操作方法:
        "最小最大归一化" - 将所有特征缩放到[0, 1]区间内。
        "均值归一化" - 将所有特征值缩放到均值为0，方差为1的分布。
        "标准化" - 将数据按比例缩放，使得数据的总体标准偏差为1，均值为0。
        "最大绝对值归一化" - 缩放每个特征到[-1,1]区间内，通过除以最大绝对值。
        "鲁棒归一化" - 使用中位数和四分位数范围来缩放特征，对异常值有更好的鲁棒性。
        "不处理" - 不进行任何归一化处理。
        
        返回:
        归一化处理后的pandas DataFrame。
        """
        if operation_method == "最小最大归一化":
            scaler = MinMaxScaler()
            return pd.DataFrame(scaler.fit_transform(data), columns=data.columns, index=data.index)

        elif operation_method == "均值归一化":
            return (data - data.mean()) / (data.max() - data.min())

        elif operation_method == "标准化":
            scaler = StandardScaler()
            return pd.DataFrame(scaler.fit_transform(data), columns=data.columns, index=data.index)

        elif operation_method == "最大绝对值归一化":
            scaler = MaxAbsScaler()
            return pd.DataFrame(scaler.fit_transform(data), columns=data.columns, index=data.index)

        elif operation_method == "鲁棒归一化":
            scaler = RobustScaler()
            return pd.DataFrame(scaler.fit_transform(data), columns=data.columns, index=data.index)

        elif operation_method == "不处理":
            return data  # 不进行任何操作，返回原始数据

        else:
            return data  # 如果没有匹配的处理方法，返回原始数据

    # 在此处定义其他数据处理方法...
# ======================== 代码块#2：结束 ========================


# ======================== 代码块#3：特征选择 ========================
class FeatureSelectionThread(QThread):
    # 定义一个信号，传递处理后的数据和对应的项目名称
    data_processed = Signal(pd.DataFrame, str)

    def __init__(self, data, selected_items):
        super().__init__()
        self.data = data
        self.selected_items = selected_items
        # print("特征选择线程...")
        # print(data.iloc[0:3, 0:5])
        # print(selected_items)

    def run(self):
        for item in self.selected_items:
            processed_data = self.process_data(self.data, item)
            self.data_processed.emit(processed_data, item)

    def process_data(self, data, method):
        # 在这里根据method处理数据
        # 这里只是返回原始数据作为示例
        return data

# ======================== 代码块#3：结束 ========================


# 参数设置窗口类
class FeatureSelectionParamsDialog(QDialog):
    def __init__(self, feature_selection_method, parent=None):
        super().__init__(parent)
        # self.setWindowTitle(f"{feature_selection_methods.__name__} Parameters")
        # self.algorithm = algorithm_class()  # 实例化算法
        self.params = feature_selection_method  # 获取参数
        self.init_ui()  # 初始化界面

    # 初始化用户界面
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(10)  # 设置元素间的间距

        # 获取最长参数名称的长度
        max_param_length = max(len(param) for param in self.params)

        # 用于跟踪每个参数的LineEdit的字典
        self.param_line_edits = {}

        # 计算标签的统一宽度
        label_width = max_param_length * 10  # 修改点：设置了一个基于最长参数名称的固定宽度

        # 为每个参数创建一个水平布局的标签和LineEdit
        for param, value in self.params.items():
            param_layout = QHBoxLayout()
            param_label = QLabel(f"{param}:")
            param_label.setFixedWidth(label_width)  # 修改点：设置固定宽度
            param_label.setAlignment(Qt.AlignRight)  # 右对齐
            line_edit = QLineEdit(str(value))
            line_edit.setFixedWidth(100)  # 设置统一的LineEdit长度
            param_layout.addWidget(param_label)
            param_layout.addWidget(line_edit)
            self.param_line_edits[param] = line_edit
            layout.addLayout(param_layout)

        # 创建确定和取消按钮，并连接它们的点击信号到槽函数
        self.ok_button = QPushButton("确定", self)
        self.cancel_button = QPushButton("取消", self)
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        
        # 添加按钮到界面底部，并设置合理的间距
        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addWidget(self.ok_button)
        buttons_layout.addWidget(self.cancel_button)
        buttons_layout.setSpacing(10)  # 设置按钮之间的间距
        layout.addLayout(buttons_layout)

        self.setLayout(layout)
        self.setStyleSheet("QWidget { font-size: 14px; } QPushButton { width: 80px; }")  # 设置字体大小和按钮宽度

    # 接受修改，关闭对话框并打印修改后的参数
    def accept(self):
        # modified_params = {param: line_edit.text() for param, line_edit in self.param_line_edits.items()}
        # print("修改后的参数：", modified_params)
        feature_selection_method = list(self.params.keys())[0]
        self.params[feature_selection_method] = self.param_line_edits[feature_selection_method].text()
        super().accept()

        # return modified_params

    # 拒绝修改，关闭对话框但不打印参数
    def reject(self):
        # 由于是取消操作，这里不需要打印任何参数
        super().reject()
