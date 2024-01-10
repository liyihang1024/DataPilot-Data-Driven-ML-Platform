# ///////////////////////////////////////////////////////////////
#
# __init__.py 文件功能说明
# __init__.py 是一个特殊的Python文件，它的存在告诉Python解释器这个目录可以被视为一个Python包。
# 这样，你就可以导入包和包内的模块。当你导入包时，__init__.py 决定了哪些模块或对象会被暴露给外部。
# 在这个 __init__.py 文件中，我们导入了必要的PySide6模块和项目特定的模块，组织了应用程序的主要部分，
# 包括UI界面、设置、功能和应用程序逻辑。这样做使得代码结构更清晰，模块化，便于维护和扩展。
#
# 作者: WANDERSON M.PIMENTA
# 项目使用: Qt Designer 和 PySide6 制作
# 版本: 1.0.0
#
# 本项目可以自由用于所有用途，只要在Python脚本中保留相应的信用标记，
# GUI中的任何信息都可以修改，不会有任何后果。
#
# 如果你想将产品商业化使用，Qt 许可证有一些限制，
# 我推荐在官方网站上阅读它们：https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# 从PySide6.QtCore导入所有内容，包括核心工具和功能，如事件循环、信号和槽等
from PySide6.QtCore import *

# 从PySide6.QtGui导入所有内容，包含了用于窗口系统交互的界面元素，如图标、字体和颜色
from PySide6.QtGui import *

# 从PySide6.QtWidgets导入所有内容，提供了一套UI组件用于创建经典的桌面风格的用户界面
from PySide6.QtWidgets import *

# GUI FILE
# 导入从Qt Designer设计的UI主窗口
from . ui_main import Ui_MainWindow

# APP SETTINGS
# 导入应用程序设置模块，这里包含配置和偏好设置
from . app_settings import Settings

# IMPORT FUNCTIONS
# 导入UI功能模块，这里可能包含窗口行为和逻辑功能
from . ui_functions import *

# APP FUNCTIONS
# 导入应用程序功能模块，这里包含应用程序的核心功能和业务逻辑
from . app_functions import *

# 从自定特义征选择模块导入其他UI窗口
from . Ui_widget_FeatureSelection import *

# 从自定特义模型训练块导入其他UI窗口
from . Ui_widget_ModelTrain import *