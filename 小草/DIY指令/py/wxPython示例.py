import wx
import wx.adv
import wx.grid
import wx.html
import wx.lib.agw.aui as aui
import wx.lib.scrolledpanel as scrolled
import os
import sys
import time
import webbrowser

class WxPythonControlsDemo(wx.Frame):
    def __init__(self, parent, title):
        super(WxPythonControlsDemo, self).__init__(parent, title=title, size=(1000, 700))
        
        # 创建状态栏
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText("就绪")
        
        # 创建菜单栏
        self.create_menu_bar()
        
        # 创建工具栏
        self.create_tool_bar()
        
        # 创建主面板
        self.notebook = wx.Notebook(self)
        
        # 创建各个标签页
        self.create_basic_controls_panel()
        self.create_layout_panel()
        self.create_advanced_controls_panel()
        self.create_dialog_panel()
        self.create_grid_panel()
        self.create_custom_panel()
        
        # 设置图标
        # self.SetIcon(wx.Icon("icon.ico"))
        
        # 居中显示
        self.Centre()
        self.Show(True)
    
    def create_menu_bar(self):
        """创建菜单栏"""
        menubar = wx.MenuBar()
        
        # 文件菜单
        file_menu = wx.Menu()
        new_item = file_menu.Append(wx.ID_NEW, "新建(&N)", "创建新文件")
        open_item = file_menu.Append(wx.ID_OPEN, "打开(&O)", "打开文件")
        file_menu.AppendSeparator()
        exit_item = file_menu.Append(wx.ID_EXIT, "退出(&Q)", "退出程序")
        
        # 编辑菜单
        edit_menu = wx.Menu()
        cut_item = edit_menu.Append(wx.ID_CUT, "剪切(&T)", "剪切选中内容")
        copy_item = edit_menu.Append(wx.ID_COPY, "复制(&C)", "复制选中内容")
        paste_item = edit_menu.Append(wx.ID_PASTE, "粘贴(&P)", "粘贴内容")
        edit_menu.AppendSeparator()
        
        # 子菜单示例
        pref_menu = wx.Menu()
        pref_menu.Append(wx.ID_ANY, "选项1", "选项1描述")
        pref_menu.Append(wx.ID_ANY, "选项2", "选项2描述")
        edit_menu.AppendSubMenu(pref_menu, "首选项(&P)")
        
        # 视图菜单
        view_menu = wx.Menu()
        self.show_statusbar = view_menu.Append(wx.ID_ANY, "显示状态栏(&S)", "显示或隐藏状态栏", kind=wx.ITEM_CHECK)
        view_menu.Check(self.show_statusbar.GetId(), True)
        
        # 帮助菜单
        help_menu = wx.Menu()
        about_item = help_menu.Append(wx.ID_ABOUT, "关于(&A)", "关于本程序")
        
        # 添加菜单到菜单栏
        menubar.Append(file_menu, "文件(&F)")
        menubar.Append(edit_menu, "编辑(&E)")
        menubar.Append(view_menu, "视图(&V)")
        menubar.Append(help_menu, "帮助(&H)")
        
        # 设置菜单栏
        self.SetMenuBar(menubar)
        
        # 绑定事件
        self.Bind(wx.EVT_MENU, self.on_exit, exit_item)
        self.Bind(wx.EVT_MENU, self.on_about, about_item)
        self.Bind(wx.EVT_MENU, self.on_toggle_statusbar, self.show_statusbar)
    
    def create_tool_bar(self):
        """创建工具栏"""
        toolbar = self.CreateToolBar()
        
        # 添加工具按钮
        new_tool = toolbar.AddTool(wx.ID_NEW, "新建", wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR), "新建文件")
        open_tool = toolbar.AddTool(wx.ID_OPEN, "打开", wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR), "打开文件")
        save_tool = toolbar.AddTool(wx.ID_SAVE, "保存", wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR), "保存文件")
        
        toolbar.AddSeparator()
        
        cut_tool = toolbar.AddTool(wx.ID_CUT, "剪切", wx.ArtProvider.GetBitmap(wx.ART_CUT, wx.ART_TOOLBAR), "剪切")
        copy_tool = toolbar.AddTool(wx.ID_COPY, "复制", wx.ArtProvider.GetBitmap(wx.ART_COPY, wx.ART_TOOLBAR), "复制")
        paste_tool = toolbar.AddTool(wx.ID_PASTE, "粘贴", wx.ArtProvider.GetBitmap(wx.ART_PASTE, wx.ART_TOOLBAR), "粘贴")
        
        # 实现工具栏
        toolbar.Realize()
    
    def create_basic_controls_panel(self):
        """创建基础控件面板"""
        panel = wx.Panel(self.notebook)
        self.notebook.AddPage(panel, "基础控件")
        
        # 使用垂直布局
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        # 标签控件
        label_section = wx.StaticBox(panel, label="标签(StaticText)")
        label_sizer = wx.StaticBoxSizer(label_section, wx.VERTICAL)
        label1 = wx.StaticText(panel, label="这是一个普通标签")
        label2 = wx.StaticText(panel, label="这是一个带样式的标签")
        label2.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD))
        label2.SetForegroundColour(wx.RED)
        label_sizer.Add(label1, 0, wx.ALL, 5)
        label_sizer.Add(label2, 0, wx.ALL, 5)
        vbox.Add(label_sizer, 0, wx.ALL | wx.EXPAND, 5)
        
        # 按钮控件
        button_section = wx.StaticBox(panel, label="按钮(Button)")
        button_sizer = wx.StaticBoxSizer(button_section, wx.VERTICAL)
        
        btn1 = wx.Button(panel, label="普通按钮")
        btn2 = wx.ToggleButton(panel, label="切换按钮")
        btn3 = wx.BitmapButton(panel, bitmap=wx.ArtProvider.GetBitmap(wx.ART_INFORMATION, wx.ART_BUTTON))
        
        button_sizer.Add(btn1, 0, wx.ALL, 5)
        button_sizer.Add(btn2, 0, wx.ALL, 5)
        button_sizer.Add(btn3, 0, wx.ALL, 5)
        vbox.Add(button_sizer, 0, wx.ALL | wx.EXPAND, 5)
        
        # 文本输入控件
        text_section = wx.StaticBox(panel, label="文本输入(TextCtrl)")
        text_sizer = wx.StaticBoxSizer(text_section, wx.VERTICAL)
        
        text1 = wx.TextCtrl(panel, value="单行文本输入")
        text2 = wx.TextCtrl(panel, value="多行文本输入\n第二行\n第三行", style=wx.TE_MULTILINE | wx.TE_RICH2)
        text3 = wx.TextCtrl(panel, value="密码输入", style=wx.TE_PASSWORD)
        
        text_sizer.Add(text1, 0, wx.ALL | wx.EXPAND, 5)
        text_sizer.Add(text2, 0, wx.ALL | wx.EXPAND, 5)
        text_sizer.Add(text3, 0, wx.ALL | wx.EXPAND, 5)
        vbox.Add(text_sizer, 0, wx.ALL | wx.EXPAND, 5)
        
        # 选择控件
        choice_section = wx.StaticBox(panel, label="选择控件")
        choice_sizer = wx.StaticBoxSizer(choice_section, wx.VERTICAL)
        
        # 复选框
        cb1 = wx.CheckBox(panel, label="复选框1")
        cb2 = wx.CheckBox(panel, label="复选框2")
        cb2.SetValue(True)
        
        # 单选按钮
        rb_sizer = wx.BoxSizer(wx.HORIZONTAL)
        rb1 = wx.RadioButton(panel, label="单选1", style=wx.RB_GROUP)
        rb2 = wx.RadioButton(panel, label="单选2")
        rb3 = wx.RadioButton(panel, label="单选3")
        rb_sizer.Add(rb1, 0, wx.RIGHT, 10)
        rb_sizer.Add(rb2, 0, wx.RIGHT, 10)
        rb_sizer.Add(rb3, 0, wx.RIGHT, 10)
        
        # 下拉列表
        choices = ["选项1", "选项2", "选项3", "选项4"]
        choice = wx.Choice(panel, choices=choices)
        choice.SetSelection(0)
        
        # 组合框
        combo = wx.ComboBox(panel, value="可编辑选项", choices=choices)
        
        choice_sizer.Add(cb1, 0, wx.ALL, 5)
        choice_sizer.Add(cb2, 0, wx.ALL, 5)
        choice_sizer.Add(rb_sizer, 0, wx.ALL, 5)
        choice_sizer.Add(choice, 0, wx.ALL | wx.EXPAND, 5)
        choice_sizer.Add(combo, 0, wx.ALL | wx.EXPAND, 5)
        vbox.Add(choice_sizer, 0, wx.ALL | wx.EXPAND, 5)
        
        # 设置面板的布局
        panel.SetSizer(vbox)
        
        # 绑定事件
        btn1.Bind(wx.EVT_BUTTON, self.on_button_click)
        btn2.Bind(wx.EVT_TOGGLEBUTTON, self.on_toggle_button)
        btn3.Bind(wx.EVT_BUTTON, self.on_bitmap_button)
        choice.Bind(wx.EVT_CHOICE, self.on_choice)
        combo.Bind(wx.EVT_COMBOBOX, self.on_combo)
        
    def create_layout_panel(self):
        """创建布局面板"""
        panel = wx.Panel(self.notebook)
        self.notebook.AddPage(panel, "布局管理")
        
        # 主布局
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # BoxSizer示例
        box_section = wx.StaticBox(panel, label="BoxSizer布局")
        box_sizer = wx.StaticBoxSizer(box_section, wx.VERTICAL)
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        for i in range(3):
            btn = wx.Button(panel, label=f"按钮 {i+1}")
            hbox.Add(btn, 1, wx.EXPAND | wx.ALL, 5)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        for i in range(3):
            btn = wx.Button(panel, label=f"按钮 {i+4}")
            vbox.Add(btn, 0, wx.EXPAND | wx.ALL, 5)
        
        box_sizer.Add(wx.StaticText(panel, label="水平BoxSizer:"), 0, wx.ALL, 5)
        box_sizer.Add(hbox, 0, wx.ALL | wx.EXPAND, 5)
        box_sizer.Add(wx.StaticText(panel, label="垂直BoxSizer:"), 0, wx.ALL, 5)
        box_sizer.Add(vbox, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(box_sizer, 0, wx.ALL | wx.EXPAND, 5)
        
        # GridSizer示例
        grid_section = wx.StaticBox(panel, label="GridSizer布局")
        grid_sizer = wx.StaticBoxSizer(grid_section, wx.VERTICAL)
        
        gs = wx.GridSizer(2, 3, 5, 5)  # 2行3列，行间距5，列间距5
        for i in range(6):
            btn = wx.Button(panel, label=f"按钮 {i+1}")
            gs.Add(btn, 0, wx.EXPAND)
        
        grid_sizer.Add(wx.StaticText(panel, label="GridSizer (2x3):"), 0, wx.ALL, 5)
        grid_sizer.Add(gs, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(grid_sizer, 0, wx.ALL | wx.EXPAND, 5)
        
        # FlexGridSizer示例
        flex_section = wx.StaticBox(panel, label="FlexGridSizer布局")
        flex_sizer = wx.StaticBoxSizer(flex_section, wx.VERTICAL)
        
        fgs = wx.FlexGridSizer(3, 2, 5, 5)  # 3行2列，行间距5，列间距5
        fgs.AddGrowableCol(1, 1)  # 第2列可增长
        
        labels = ["姓名:", "年龄:", "地址:"]
        for label in labels:
            fgs.Add(wx.StaticText(panel, label=label), 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
            fgs.Add(wx.TextCtrl(panel), 0, wx.EXPAND)
        
        flex_sizer.Add(wx.StaticText(panel, label="FlexGridSizer (3x2):"), 0, wx.ALL, 5)
        flex_sizer.Add(wx.StaticText(panel, label="FlexGridSizer (3x2):"), 0, wx.ALL, 5)
        flex_sizer.Add(fgs, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(flex_sizer, 0, wx.ALL | wx.EXPAND, 5)
        
        # 设置面板的布局
        panel.SetSizer(main_sizer)
    
    def create_advanced_controls_panel(self):
        """创建高级控件面板"""
        panel = wx.Panel(self.notebook)
        self.notebook.AddPage(panel, "高级控件")
        
        # 主布局
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # 列表控件
        list_section = wx.StaticBox(panel, label="列表控件")
        list_sizer = wx.StaticBoxSizer(list_section, wx.VERTICAL)
        
        # 列表框
        list_box = wx.ListBox(panel, choices=["项目1", "项目2", "项目3", "项目4", "项目5"])
        
        # 列表控件
        list_ctrl = wx.ListCtrl(panel, style=wx.LC_REPORT)
        list_ctrl.InsertColumn(0, "名称", width=100)
        list_ctrl.InsertColumn(1, "大小", width=80)
        list_ctrl.InsertColumn(2, "修改日期", width=120)
        
        for i in range(5):
            list_ctrl.InsertItem(i, f"文件{i+1}")
            list_ctrl.SetItem(i, 1, f"{i*10+5} KB")
            list_ctrl.SetItem(i, 2, "2023-01-01")
        
        list_sizer.Add(wx.StaticText(panel, label="列表框(ListBox):"), 0, wx.ALL, 5)
        list_sizer.Add(list_box, 0, wx.ALL | wx.EXPAND, 5)
        list_sizer.Add(wx.StaticText(panel, label="列表控件(ListCtrl):"), 0, wx.ALL, 5)
        list_sizer.Add(list_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(list_sizer, 0, wx.ALL | wx.EXPAND, 5)
        
        # 树控件
        tree_section = wx.StaticBox(panel, label="树控件(TreeCtrl)")
        tree_sizer = wx.StaticBoxSizer(tree_section, wx.VERTICAL)
        
        tree = wx.TreeCtrl(panel, style=wx.TR_DEFAULT_STYLE | wx.TR_HAS_BUTTONS)
        root = tree.AddRoot("根节点")
        
        for i in range(3):
            parent = tree.AppendItem(root, f"父节点 {i+1}")
            for j in range(3):
                child = tree.AppendItem(parent, f"子节点 {i+1}-{j+1}")
                for k in range(2):
                    tree.AppendItem(child, f"叶节点 {i+1}-{j+1}-{k+1}")
        
        tree.Expand(root)
        
        tree_sizer.Add(tree, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(tree_sizer, 0, wx.ALL | wx.EXPAND, 5)
        
        # 滑块和进度条
        slider_section = wx.StaticBox(panel, label="滑块和进度条")
        slider_sizer = wx.StaticBoxSizer(slider_section, wx.VERTICAL)
        
        # 滑块
        slider_label = wx.StaticText(panel, label="滑块(Slider):")
        slider = wx.Slider(panel, value=50, minValue=0, maxValue=100, style=wx.SL_HORIZONTAL | wx.SL_LABELS)
        
        # 进度条
        gauge_label = wx.StaticText(panel, label="进度条(Gauge):")
        gauge = wx.Gauge(panel, range=100, style=wx.GA_HORIZONTAL)
        gauge.SetValue(75)
        
        slider_sizer.Add(slider_label, 0, wx.ALL, 5)
        slider_sizer.Add(slider, 0, wx.ALL | wx.EXPAND, 5)
        slider_sizer.Add(gauge_label, 0, wx.ALL, 5)
        slider_sizer.Add(gauge, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(slider_sizer, 0, wx.ALL | wx.EXPAND, 5)
        
        # 设置面板的布局
        panel.SetSizer(main_sizer)
        
        # 绑定事件
        list_box.Bind(wx.EVT_LISTBOX, self.on_list_box)
        list_ctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_list_ctrl)
        tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_tree_sel_changed)
        slider.Bind(wx.EVT_SLIDER, self.on_slider)
    
    def create_dialog_panel(self):
        """创建对话框面板"""
        panel = wx.Panel(self.notebook)
        self.notebook.AddPage(panel, "对话框")
        
        # 主布局
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # 消息对话框
        msg_section = wx.StaticBox(panel, label="消息对话框")
        msg_sizer = wx.StaticBoxSizer(msg_section, wx.VERTICAL)
        
        btn_info = wx.Button(panel, label="信息对话框")
        btn_warn = wx.Button(panel, label="警告对话框")
        btn_error = wx.Button(panel, label="错误对话框")
        btn_question = wx.Button(panel, label="问题对话框")
        
        msg_sizer.Add(btn_info, 0, wx.ALL, 5)
        msg_sizer.Add(btn_warn, 0, wx.ALL, 5)
        msg_sizer.Add(btn_error, 0, wx.ALL, 5)
        msg_sizer.Add(btn_question, 0, wx.ALL, 5)
        main_sizer.Add(msg_sizer, 0, wx.ALL | wx.EXPAND, 5)
        
        # 文件对话框
        file_section = wx.StaticBox(panel, label="文件对话框")
        file_sizer = wx.StaticBoxSizer(file_section, wx.VERTICAL)
        
        btn_open = wx.Button(panel, label="打开文件对话框")
        btn_save = wx.Button(panel, label="保存文件对话框")
        btn_dir = wx.Button(panel, label="选择目录对话框")
        
        file_sizer.Add(btn_open, 0, wx.ALL, 5)
        file_sizer.Add(btn_save, 0, wx.ALL, 5)
        file_sizer.Add(btn_dir, 0, wx.ALL, 5)
        main_sizer.Add(file_sizer, 0, wx.ALL | wx.EXPAND, 5)
        
        # 颜色和字体对话框
        style_section = wx.StaticBox(panel, label="颜色和字体对话框")
        style_sizer = wx.StaticBoxSizer(style_section, wx.VERTICAL)
        
        btn_color = wx.Button(panel, label="颜色对话框")
        btn_font = wx.Button(panel, label="字体对话框")
        
        style_sizer.Add(btn_color, 0, wx.ALL, 5)
        style_sizer.Add(btn_font, 0, wx.ALL, 5)
        main_sizer.Add(style_sizer, 0, wx.ALL | wx.EXPAND, 5)
        
        # 自定义对话框
        custom_section = wx.StaticBox(panel, label="自定义对话框")
        custom_sizer = wx.StaticBoxSizer(custom_section, wx.VERTICAL)
        
        btn_custom = wx.Button(panel, label="显示自定义对话框")
        
        custom_sizer.Add(btn_custom, 0, wx.ALL, 5)
        main_sizer.Add(custom_sizer, 0, wx.ALL | wx.EXPAND, 5)
        
        # 设置面板的布局
        panel.SetSizer(main_sizer)
        
        # 绑定事件
        btn_info.Bind(wx.EVT_BUTTON, self.on_info_dialog)
        btn_warn.Bind(wx.EVT_BUTTON, self.on_warn_dialog)
        btn_error.Bind(wx.EVT_BUTTON, self.on_error_dialog)
        btn_question.Bind(wx.EVT_BUTTON, self.on_question_dialog)
        btn_open.Bind(wx.EVT_BUTTON, self.on_open_file_dialog)
        btn_save.Bind(wx.EVT_BUTTON, self.on_save_file_dialog)
        btn_dir.Bind(wx.EVT_BUTTON, self.on_dir_dialog)
        btn_color.Bind(wx.EVT_BUTTON, self.on_color_dialog)
        btn_font.Bind(wx.EVT_BUTTON, self.on_font_dialog)
        btn_custom.Bind(wx.EVT_BUTTON, self.on_custom_dialog)
    
    def create_grid_panel(self):
        """创建网格面板"""
        panel = wx.Panel(self.notebook)
        self.notebook.AddPage(panel, "网格控件")
        
        # 主布局
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # 网格控件
        grid = wx.grid.Grid(panel)
        grid.CreateGrid(10, 5)
        
        # 设置列标题
        for col in range(5):
            grid.SetColLabelValue(col, f"列 {col+1}")
        
        # 设置行标题
        for row in range(10):
            grid.SetRowLabelValue(row, f"行 {row+1}")
        
        # 填充数据
        for row in range(10):
            for col in range(5):
                grid.SetCellValue(row, col, f"单元格 ({row+1},{col+1})")
        
        # 设置单元格属性
        grid.SetCellTextColour(1, 1, wx.RED)
        grid.SetCellBackgroundColour(2, 2, wx.LIGHT_GREY)
        grid.SetCellFont(3, 3, wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD))
        
        # 合并单元格
        grid.SetCellSize(5, 0, 2, 2)
        grid.SetCellValue(5, 0, "合并单元格")
        grid.SetCellAlignment(5, 0, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        
        main_sizer.Add(grid, 1, wx.ALL | wx.EXPAND, 10)
        
        # 设置面板的布局
        panel.SetSizer(main_sizer)
    
    def create_custom_panel(self):
        """创建自定义控件面板"""
        panel = wx.Panel(self.notebook)
        self.notebook.AddPage(panel, "自定义控件")
        
        # 主布局
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # HTML窗口
        html_section = wx.StaticBox(panel, label="HTML窗口")
        html_sizer = wx.StaticBoxSizer(html_section, wx.VERTICAL)
        
        html_win = wx.html.HtmlWindow(panel, size=(400, 200))
        html_content = """
        <html>
        <body>
            <h2>HTML窗口示例</h2>
            <p>这是一个<b>HTML</b>窗口，可以显示<font color="red">格式化</font>文本。</p>
            <ul>
                <li>项目1</li>
                <li>项目2</li>
                <li>项目3</li>
            </ul>
            <p><a href="https://www.wxpython.org">wxPython官网</a></p>
        </body>
        </html>
        """
        html_win.SetPage(html_content)
        
        html_sizer.Add(html_win, 1, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(html_sizer, 1, wx.ALL | wx.EXPAND, 5)
        
        # 日期时间选择器
        date_section = wx.StaticBox(panel, label="日期时间选择器")
        date_sizer = wx.StaticBoxSizer(date_section, wx.VERTICAL)
        
        date_picker = wx.adv.DatePickerCtrl(panel, style=wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
        time_picker = wx.adv.TimePickerCtrl(panel)
        
        date_sizer.Add(wx.StaticText(panel, label="日期选择器:"), 0, wx.ALL, 5)
        date_sizer.Add(date_picker, 0, wx.ALL | wx.EXPAND, 5)
        date_sizer.Add(wx.StaticText(panel, label="时间选择器:"), 0, wx.ALL, 5)
        date_sizer.Add(time_picker, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(date_sizer, 0, wx.ALL | wx.EXPAND, 5)
        
        # 设置面板的布局
        panel.SetSizer(main_sizer)
        
        # 绑定事件
        html_win.Bind(wx.html.EVT_HTML_LINK_CLICKED, self.on_html_link)
        date_picker.Bind(wx.adv.EVT_DATE_CHANGED, self.on_date_changed)
        time_picker.Bind(wx.adv.EVT_TIME_CHANGED, self.on_time_changed)
    
    # 事件处理函数
    def on_exit(self, event):
        """退出程序"""
        self.Close()
    
    def on_about(self, event):
        """显示关于对话框"""
        info = wx.adv.AboutDialogInfo()
        info.SetName("wxPython控件示例")
        info.SetVersion("1.0")
        info.SetDescription("这是一个wxPython控件示例程序，展示了各种常用控件的用法。")
        info.SetCopyright("(C) 2023")
        info.SetWebSite("https://www.wxpython.org/")
        wx.adv.AboutBox(info)
    
    def on_toggle_statusbar(self, event):
        """切换状态栏显示/隐藏"""
        if self.statusbar.IsShown():
            self.statusbar.Hide()
        else:
            self.statusbar.Show()
        self.Layout()
    
    def on_button_click(self, event):
        """按钮点击事件"""
        self.statusbar.SetStatusText("普通按钮被点击")
    
    def on_toggle_button(self, event):
        """切换按钮事件"""
        btn = event.GetEventObject()
        if btn.GetValue():
            self.statusbar.SetStatusText("切换按钮: 开")
        else:
            self.statusbar.SetStatusText("切换按钮: 关")
    
    def on_bitmap_button(self, event):
        """位图按钮点击事件"""
        self.statusbar.SetStatusText("位图按钮被点击")
    
    def on_choice(self, event):
        """选择控件事件"""
        choice = event.GetEventObject()
        selection = choice.GetSelection()
        text = choice.GetString(selection)
        self.statusbar.SetStatusText(f"选择: {text}")
    
    def on_combo(self, event):
        """组合框事件"""
        combo = event.GetEventObject()
        text = combo.GetValue()
        self.statusbar.SetStatusText(f"组合框: {text}")
    
    def on_list_box(self, event):
        """列表框事件"""
        list_box = event.GetEventObject()
        selection = list_box.GetSelection()
        text = list_box.GetString(selection)
        self.statusbar.SetStatusText(f"列表框选择: {text}")
    
    def on_list_ctrl(self, event):
        """列表控件事件"""
        list_ctrl = event.GetEventObject()
        item = event.GetItem()
        text = item.GetText()
        self.statusbar.SetStatusText(f"列表控件选择: {text}")
    
    def on_tree_sel_changed(self, event):
        """树控件选择变更事件"""
        tree = event.GetEventObject()
        item = event.GetItem()
        text = tree.GetItemText(item)
        self.statusbar.SetStatusText(f"树控件选择: {text}")
    
    def on_slider(self, event):
        """滑块事件"""
        slider = event.GetEventObject()
        value = slider.GetValue()
        self.statusbar.SetStatusText(f"滑块值: {value}")
    
    def on_info_dialog(self, event):
        """信息对话框"""
        wx.MessageBox("这是一条信息消息", "信息", wx.OK | wx.ICON_INFORMATION)
    
    def on_warn_dialog(self, event):
        """警告对话框"""
        wx.MessageBox("这是一条警告消息", "警告", wx.OK | wx.ICON_WARNING)
    
    def on_error_dialog(self, event):
        """错误对话框"""
        wx.MessageBox("这是一条错误消息", "错误", wx.OK | wx.ICON_ERROR)
    
    def on_question_dialog(self, event):
        """问题对话框"""
        result = wx.MessageBox("您确定要执行此操作吗？", "确认", 
                              wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION)
        if result == wx.YES:
            self.statusbar.SetStatusText("用户选择: 是")
        elif result == wx.NO:
            self.statusbar.SetStatusText("用户选择: 否")
        else:
            self.statusbar.SetStatusText("用户选择: 取消")
    
    def on_open_file_dialog(self, event):
        """打开文件对话框"""
        with wx.FileDialog(self, "打开文件", wildcard="文本文件 (*.txt)|*.txt|所有文件 (*.*)|*.*",
                          style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            
            pathname = fileDialog.GetPath()
            self.statusbar.SetStatusText(f"选择的文件: {pathname}")
    
    def on_save_file_dialog(self, event):
        """保存文件对话框"""
        with wx.FileDialog(self, "保存文件", wildcard="文本文件 (*.txt)|*.txt|所有文件 (*.*)|*.*",
                          style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            
            pathname = fileDialog.GetPath()
            self.statusbar.SetStatusText(f"保存的文件: {pathname}")
    
    def on_dir_dialog(self, event):
        """选择目录对话框"""
        with wx.DirDialog(self, "选择目录", style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST) as dirDialog:
            if dirDialog.ShowModal() == wx.ID_CANCEL:
                return
            
            pathname = dirDialog.GetPath()
            self.statusbar.SetStatusText(f"选择的目录: {pathname}")
    
    def on_color_dialog(self, event):
        """颜色对话框"""
        with wx.ColourDialog(self) as colorDialog:
            if colorDialog.ShowModal() == wx.ID_CANCEL:
                return
            
            color = colorDialog.GetColourData().GetColour()
            self.statusbar.SetStatusText(f"选择的颜色: {color.GetAsString(wx.C2S_HTML_SYNTAX)}")
    
    def on_font_dialog(self, event):
        """字体对话框"""
        data = wx.FontData()
        data.EnableEffects(True)
        data.SetInitialFont(wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT))
        
        with wx.FontDialog(self, data) as fontDialog:
            if fontDialog.ShowModal() == wx.ID_CANCEL:
                return
            
            font = fontDialog.GetFontData().GetChosenFont()
            self.statusbar.SetStatusText(f"选择的字体: {font.GetFaceName()}, 大小: {font.GetPointSize()}")
    
    def on_custom_dialog(self, event):
        """自定义对话框"""
        dialog = CustomDialog(self, "自定义对话框")
        if dialog.ShowModal() == wx.ID_OK:
            name = dialog.name_ctrl.GetValue()
            age = dialog.age_ctrl.GetValue()
            self.statusbar.SetStatusText(f"自定义对话框结果: 姓名={name}, 年龄={age}")
        dialog.Destroy()
    
    def on_html_link(self, event):
        """HTML链接点击事件"""
        href = event.GetLinkInfo().GetHref()
        webbrowser.open(href)
    
    def on_date_changed(self, event):
        """日期变更事件"""
        date_picker = event.GetEventObject()
        date = date_picker.GetValue()
        date_str = date.FormatISODate()
        self.statusbar.SetStatusText(f"选择的日期: {date_str}")
    
    def on_time_changed(self, event):
        """时间变更事件"""
        time_picker = event.GetEventObject()
        time = time_picker.GetValue()
        time_str = time.FormatISOTime()
        self.statusbar.SetStatusText(f"选择的时间: {time_str}")


class CustomDialog(wx.Dialog):
    """自定义对话框示例"""
    def __init__(self, parent, title):
        super(CustomDialog, self).__init__(parent, title=title, size=(300, 200))
        
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        # 创建表单
        form_sizer = wx.FlexGridSizer(2, 2, 10, 10)
        form_sizer.AddGrowableCol(1, 1)
        
        name_label = wx.StaticText(panel, label="姓名:")
        self.name_ctrl = wx.TextCtrl(panel)
        age_label = wx.StaticText(panel, label="年龄:")
        self.age_ctrl = wx.TextCtrl(panel)
        
        form_sizer.Add(name_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.name_ctrl, 0, wx.EXPAND)
        form_sizer.Add(age_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.age_ctrl, 0, wx.EXPAND)
        
        vbox.Add(form_sizer, 0, wx.ALL | wx.EXPAND, 10)
        
        # 创建按钮
        button_sizer = wx.StdDialogButtonSizer()
        ok_button = wx.Button(panel, wx.ID_OK)
        cancel_button = wx.Button(panel, wx.ID_CANCEL)
        button_sizer.AddButton(ok_button)
        button_sizer.AddButton(cancel_button)
        button_sizer.Realize()
        
        vbox.Add(button_sizer, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        
        panel.SetSizer(vbox)
        self.Centre()


def main():
    app = wx.App()
    frame = WxPythonControlsDemo(None, "wxPython控件示例")
    app.MainLoop()


if __name__ == "__main__":
    main()