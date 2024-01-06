class Settings():
    # 应用程序设置部分
    # ///////////////////////////////////////////////////////////////

    # 是否启用自定义标题栏
    ENABLE_CUSTOM_TITLE_BAR = True

    # 菜单宽度设置
    MENU_WIDTH = 240  # 菜单的宽度

    # 左侧盒子的宽度（通常用于左侧导航或工具栏）
    LEFT_BOX_WIDTH = 240

    # 右侧盒子的宽度（通常用于附加信息或控制）
    RIGHT_BOX_WIDTH = 240

    # 动画持续时间（毫秒），用于过渡效果等
    TIME_ANIMATION = 500

    # 左侧和右侧盒子按钮颜色设置
    # ///////////////////////////////////////////////////////////////

    # 左侧盒子按钮的背景颜色，RGB格式
    BTN_LEFT_BOX_COLOR = "background-color: rgb(44, 49, 58);"

    # 右侧盒子按钮的背景颜色，这里使用了hex颜色代码
    BTN_RIGHT_BOX_COLOR = "background-color: #ff79c6;"

    # 菜单选中项的样式表设置
    # ///////////////////////////////////////////////////////////////

    # 当菜单项被选中时，用于样式展示的CSS样式表字符串
    # 包含了边框设置、渐变背景等CSS属性
    MENU_SELECTED_STYLESHEET = """
    border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
    background-color: rgb(40, 44, 52);
    """
