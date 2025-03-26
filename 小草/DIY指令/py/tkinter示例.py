import tkinter as tk
from tkinter import ttk, messagebox, colorchooser, filedialog, font, scrolledtext
import webbrowser
from PIL import Image, ImageTk
import os

class GUIControlsDemo:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI控件示例")
        self.root.geometry("1000x700")
        
        # 创建一个笔记本控件作为主容器
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 创建各个标签页
        self.create_basic_controls_tab()
        self.create_container_tab()
        self.create_advanced_controls_tab()
        self.create_menu_toolbar_tab()
        self.create_dialog_tab()
        self.create_styling_tab()
        
        # 状态栏
        self.status_bar = tk.Label(root, text="状态栏: 就绪", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def create_basic_controls_tab(self):
        """基础控件标签页"""
        basic_frame = ttk.Frame(self.notebook)
        self.notebook.add(basic_frame, text="基础控件")
        
        # 使用网格布局
        basic_frame.columnconfigure(0, weight=1)
        basic_frame.columnconfigure(1, weight=1)
        
        # 标签控件
        ttk.Label(basic_frame, text="标签(Label)控件:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        ttk.Label(basic_frame, text="这是一个简单的标签").grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)
        
        # 按钮控件
        ttk.Label(basic_frame, text="按钮(Button)控件:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        ttk.Button(basic_frame, text="点击我", command=lambda: messagebox.showinfo("按钮点击", "按钮被点击了！")).grid(row=1, column=1, sticky=tk.W, padx=10, pady=5)
        
        # 输入框控件
        ttk.Label(basic_frame, text="输入框(Entry)控件:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        entry = ttk.Entry(basic_frame)
        entry.insert(0, "在此输入文本")
        entry.grid(row=2, column=1, sticky=tk.W+tk.E, padx=10, pady=5)
        
        # 复选框控件
        ttk.Label(basic_frame, text="复选框(Checkbutton)控件:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        check_var = tk.BooleanVar()
        ttk.Checkbutton(basic_frame, text="选择我", variable=check_var).grid(row=3, column=1, sticky=tk.W, padx=10, pady=5)
        
        # 单选按钮控件
        ttk.Label(basic_frame, text="单选按钮(Radiobutton)控件:").grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
        radio_frame = ttk.Frame(basic_frame)
        radio_frame.grid(row=4, column=1, sticky=tk.W, padx=10, pady=5)
        radio_var = tk.StringVar()
        radio_var.set("选项1")
        ttk.Radiobutton(radio_frame, text="选项1", variable=radio_var, value="选项1").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(radio_frame, text="选项2", variable=radio_var, value="选项2").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(radio_frame, text="选项3", variable=radio_var, value="选项3").pack(side=tk.LEFT, padx=5)
        
        # 组合框控件
        ttk.Label(basic_frame, text="组合框(Combobox)控件:").grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)
        combo = ttk.Combobox(basic_frame, values=["选项1", "选项2", "选项3", "选项4"])
        combo.current(0)
        combo.grid(row=5, column=1, sticky=tk.W+tk.E, padx=10, pady=5)
        
        # 滑块控件
        ttk.Label(basic_frame, text="滑块(Scale)控件:").grid(row=6, column=0, sticky=tk.W, padx=10, pady=5)
        scale_var = tk.DoubleVar()
        scale = ttk.Scale(basic_frame, from_=0, to=100, orient=tk.HORIZONTAL, variable=scale_var, length=200)
        scale.grid(row=6, column=1, sticky=tk.W, padx=10, pady=5)
        scale.set(50)
        
        # 进度条控件
        ttk.Label(basic_frame, text="进度条(Progressbar)控件:").grid(row=7, column=0, sticky=tk.W, padx=10, pady=5)
        progress = ttk.Progressbar(basic_frame, orient=tk.HORIZONTAL, length=200, mode='determinate')
        progress.grid(row=7, column=1, sticky=tk.W, padx=10, pady=5)
        progress['value'] = 75
        
        # 分隔线
        ttk.Separator(basic_frame, orient=tk.HORIZONTAL).grid(row=8, column=0, columnspan=2, sticky=tk.EW, padx=10, pady=10)
        
        # 控件使用说明
        text = """控件使用示例:
        
1. 标签(Label): 用于显示文本或图像
   label = ttk.Label(parent, text="文本内容")
   
2. 按钮(Button): 用户可点击的按钮
   button = ttk.Button(parent, text="按钮文本", command=callback_function)
   
3. 输入框(Entry): 单行文本输入
   entry = ttk.Entry(parent)
   text = entry.get()  # 获取输入内容
   entry.insert(0, "默认文本")  # 设置默认文本
   
4. 复选框(Checkbutton): 可选择的框
   var = tk.BooleanVar()
   check = ttk.Checkbutton(parent, text="选项", variable=var)
   
5. 单选按钮(Radiobutton): 多选一按钮
   var = tk.StringVar()
   radio1 = ttk.Radiobutton(parent, text="选项1", variable=var, value="1")
   radio2 = ttk.Radiobutton(parent, text="选项2", variable=var, value="2")
   
6. 组合框(Combobox): 下拉选择框
   combo = ttk.Combobox(parent, values=["选项1", "选项2"])
   combo.current(0)  # 设置默认选中项
   
7. 滑块(Scale): 滑动选择数值
   var = tk.DoubleVar()
   scale = ttk.Scale(parent, from_=0, to=100, variable=var)
   
8. 进度条(Progressbar): 显示进度
   progress = ttk.Progressbar(parent, length=200, mode='determinate')
   progress['value'] = 75  # 设置进度值
        """
        text_widget = scrolledtext.ScrolledText(basic_frame, wrap=tk.WORD, width=40, height=15)
        text_widget.grid(row=9, column=0, columnspan=2, sticky=tk.EW, padx=10, pady=5)
        text_widget.insert(tk.END, text)
        text_widget.config(state=tk.DISABLED)
        
    def create_container_tab(self):
        """容器控件标签页"""
        container_frame = ttk.Frame(self.notebook)
        self.notebook.add(container_frame, text="容器控件")
        
        # 使用网格布局
        container_frame.columnconfigure(0, weight=1)
        container_frame.columnconfigure(1, weight=1)
        
        # 框架控件
        ttk.Label(container_frame, text="框架(Frame)控件:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        frame_demo = ttk.LabelFrame(container_frame, text="这是一个框架")
        frame_demo.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)
        ttk.Button(frame_demo, text="框架中的按钮").pack(padx=10, pady=10)
        
        # 标签页控件
        ttk.Label(container_frame, text="标签页(Notebook)控件:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        notebook_demo = ttk.Notebook(container_frame, width=200, height=100)
        notebook_demo.grid(row=1, column=1, sticky=tk.W, padx=10, pady=5)
        tab1 = ttk.Frame(notebook_demo)
        tab2 = ttk.Frame(notebook_demo)
        notebook_demo.add(tab1, text="标签页1")
        notebook_demo.add(tab2, text="标签页2")
        ttk.Label(tab1, text="这是标签页1的内容").pack(padx=10, pady=10)
        ttk.Label(tab2, text="这是标签页2的内容").pack(padx=10, pady=10)
        
        # 面板窗口控件
        ttk.Label(container_frame, text="面板窗口(PanedWindow)控件:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        paned = ttk.PanedWindow(container_frame, orient=tk.HORIZONTAL)
        paned.grid(row=2, column=1, sticky=tk.W, padx=10, pady=5)
        left = ttk.Frame(paned, width=100, height=75)
        right = ttk.Frame(paned, width=100, height=75)
        paned.add(left)
        paned.add(right)
        ttk.Label(left, text="左侧面板").pack(padx=10, pady=10)
        ttk.Label(right, text="右侧面板").pack(padx=10, pady=10)
        
        # 分隔线
        ttk.Separator(container_frame, orient=tk.HORIZONTAL).grid(row=3, column=0, columnspan=2, sticky=tk.EW, padx=10, pady=10)
        
        # 控件使用说明
        text = """容器控件使用示例:
        
1. 框架(Frame/LabelFrame): 用于组织和容纳其他控件
   frame = ttk.Frame(parent)
   label_frame = ttk.LabelFrame(parent, text="带标题的框架")
   
2. 标签页(Notebook): 创建多个标签页
   notebook = ttk.Notebook(parent)
   tab1 = ttk.Frame(notebook)
   tab2 = ttk.Frame(notebook)
   notebook.add(tab1, text="标签页1")
   notebook.add(tab2, text="标签页2")
   
3. 面板窗口(PanedWindow): 可调整大小的分隔面板
   paned = ttk.PanedWindow(parent, orient=tk.HORIZONTAL)
   left_frame = ttk.Frame(paned)
   right_frame = ttk.Frame(paned)
   paned.add(left_frame)
   paned.add(right_frame)
   
4. 布局管理器:
   - pack(): 简单的块级布局
     widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
   
   - grid(): 网格布局
     widget.grid(row=0, column=0, sticky=tk.W+tk.E)
   
   - place(): 绝对定位
     widget.place(x=10, y=10, width=100, height=30)
        """
        text_widget = scrolledtext.ScrolledText(container_frame, wrap=tk.WORD, width=40, height=15)
        text_widget.grid(row=4, column=0, columnspan=2, sticky=tk.EW, padx=10, pady=5)
        text_widget.insert(tk.END, text)
        text_widget.config(state=tk.DISABLED)
        
    def create_advanced_controls_tab(self):
        """高级控件标签页"""
        advanced_frame = ttk.Frame(self.notebook)
        self.notebook.add(advanced_frame, text="高级控件")
        
        # 使用网格布局
        advanced_frame.columnconfigure(0, weight=1)
        advanced_frame.columnconfigure(1, weight=1)
        
        # 文本编辑器控件
        ttk.Label(advanced_frame, text="文本编辑器(Text)控件:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        text_editor = tk.Text(advanced_frame, width=30, height=5)
        text_editor.grid(row=0, column=1, sticky=tk.W+tk.E, padx=10, pady=5)
        text_editor.insert(tk.END, "这是一个多行文本编辑器\n可以输入多行文本\n支持富文本格式")
        
        # 滚动文本控件
        ttk.Label(advanced_frame, text="滚动文本(ScrolledText)控件:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        scrolled_text = scrolledtext.ScrolledText(advanced_frame, width=30, height=5, wrap=tk.WORD)
        scrolled_text.grid(row=1, column=1, sticky=tk.W+tk.E, padx=10, pady=5)
        scrolled_text.insert(tk.END, "这是一个带滚动条的文本控件\n" * 5)
        
        # 列表框控件
        ttk.Label(advanced_frame, text="列表框(Listbox)控件:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        listbox_frame = ttk.Frame(advanced_frame)
        listbox_frame.grid(row=2, column=1, sticky=tk.W+tk.E, padx=10, pady=5)
        listbox = tk.Listbox(listbox_frame, height=5)
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox.config(yscrollcommand=scrollbar.set)
        for i in range(1, 21):
            listbox.insert(tk.END, f"列表项 {i}")
        
        # 树状视图控件
        ttk.Label(advanced_frame, text="树状视图(Treeview)控件:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        tree_frame = ttk.Frame(advanced_frame)
        tree_frame.grid(row=3, column=1, sticky=tk.W+tk.E, padx=10, pady=5)
        tree = ttk.Treeview(tree_frame, height=5)
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tree_scroll = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        tree.configure(yscrollcommand=tree_scroll.set)
        
        # 添加列
        tree['columns'] = ('size', 'modified')
        tree.column('#0', width=120, minwidth=25)
        tree.column('size', width=80, minwidth=25)
        tree.column('modified', width=120, minwidth=25)
        
        # 添加表头
        tree.heading('#0', text='名称', anchor=tk.W)
        tree.heading('size', text='大小', anchor=tk.W)
        tree.heading('modified', text='修改日期', anchor=tk.W)
        
        # 添加数据
        folder1 = tree.insert('', 'end', text='文件夹1', values=('--', '2023-01-01'))
        tree.insert(folder1, 'end', text='文件1.txt', values=('2 KB', '2023-01-02'))
        tree.insert(folder1, 'end', text='文件2.txt', values=('1 KB', '2023-01-03'))
        folder2 = tree.insert('', 'end', text='文件夹2', values=('--', '2023-01-04'))
        tree.insert(folder2, 'end', text='文件3.txt', values=('4 KB', '2023-01-05'))
        
        # 画布控件
        ttk.Label(advanced_frame, text="画布(Canvas)控件:").grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
        canvas = tk.Canvas(advanced_frame, width=200, height=100, bg='white')
        canvas.grid(row=4, column=1, sticky=tk.W, padx=10, pady=5)
        # 在画布上绘制图形
        canvas.create_line(10, 10, 190, 10, fill='blue', width=2)
        canvas.create_rectangle(10, 20, 90, 80, fill='green')
        canvas.create_oval(110, 20, 190, 80, fill='red')
        canvas.create_text(100, 90, text='画布示例', fill='black')
        
        # 分隔线
        ttk.Separator(advanced_frame, orient=tk.HORIZONTAL).grid(row=5, column=0, columnspan=2, sticky=tk.EW, padx=10, pady=10)
        
        # 控件使用说明
        text = """高级控件使用示例:
        
1. 文本编辑器(Text): 多行文本编辑
   text = tk.Text(parent, width=30, height=5)
   text.insert(tk.END, "文本内容")
   content = text.get("1.0", tk.END)  # 获取所有文本
   
2. 滚动文本(ScrolledText): 带滚动条的文本编辑器
   from tkinter import scrolledtext
   st = scrolledtext.ScrolledText(parent, width=30, height=5)
   
3. 列表框(Listbox): 显示选项列表
   listbox = tk.Listbox(parent)
   for item in ["选项1", "选项2", "选项3"]:
       listbox.insert(tk.END, item)
   selected = listbox.curselection()  # 获取选中项索引
   
4. 树状视图(Treeview): 显示层次化数据
   tree = ttk.Treeview(parent)
   tree['columns'] = ('col1', 'col2')
   tree.heading('#0', text='名称')
   tree.heading('col1', text='列1')
   parent_item = tree.insert('', 'end', text='父项', values=('值1', '值2'))
   child_item = tree.insert(parent_item, 'end', text='子项', values=('值3', '值4'))
   
5. 画布(Canvas): 绘制图形和图像
   canvas = tk.Canvas(parent, width=200, height=100)
   line = canvas.create_line(0, 0, 100, 100, fill='red')
   rect = canvas.create_rectangle(50, 25, 150, 75, fill='blue')
   oval = canvas.create_oval(10, 10, 80, 80, fill='green')
   text = canvas.create_text(100, 50, text='文本', fill='black')
        """
        text_widget = scrolledtext.ScrolledText(advanced_frame, wrap=tk.WORD, width=40, height=15)
        text_widget.grid(row=6, column=0, columnspan=2, sticky=tk.EW, padx=10, pady=5)
        text_widget.insert(tk.END, text)
        text_widget.config(state=tk.DISABLED)
        
    def create_menu_toolbar_tab(self):
        """菜单和工具栏标签页"""
        menu_frame = ttk.Frame(self.notebook)
        self.notebook.add(menu_frame, text="菜单和工具栏")
        
        # 使用网格布局
        menu_frame.columnconfigure(0, weight=1)
        
        # 菜单示例
        ttk.Label(menu_frame, text="菜单(Menu)示例:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        
        menu_demo_frame = ttk.LabelFrame(menu_frame, text="菜单演示")
        menu_demo_frame.grid(row=1, column=0, sticky=tk.EW, padx=10, pady=5)
        
        # 创建一个临时的顶级窗口来展示菜单
        menu_demo = ttk.Label(menu_demo_frame, text="点击下面的按钮查看菜单示例")
        menu_demo.pack(padx=10, pady=10)
        
        def show_menu_demo():
            menu_window = tk.Toplevel(self.root)
            menu_window.title("菜单示例")
            menu_window.geometry("400x300")
            
            # 创建菜单栏
            menubar = tk.Menu(menu_window)
            menu_window.config(menu=menubar)
            
            # 创建文件菜单
            file_menu = tk.Menu(menubar, tearoff=0)
            menubar.add_cascade(label="文件", menu=file_menu)
            file_menu.add_command(label="新建", command=lambda: messagebox.showinfo("菜单", "新建文件"))
            file_menu.add_command(label="打开", command=lambda: messagebox.showinfo("菜单", "打开文件"))
            file_menu.add_separator()
            file_menu.add_command(label="保存", command=lambda: messagebox.showinfo("菜单", "保存文件"))
            file_menu.add_command(label="另存为", command=lambda: messagebox.showinfo("菜单", "文件另存为"))
            file_menu.add_separator()
            file_menu.add_command(label="退出", command=menu_window.destroy)
            
            # 创建编辑菜单
            edit_menu = tk.Menu(menubar, tearoff=0)
            menubar.add_cascade(label="编辑", menu=edit_menu)
            edit_menu.add_command(label="剪切", command=lambda: messagebox.showinfo("菜单", "剪切"))
            edit_menu.add_command(label="复制", command=lambda: messagebox.showinfo("菜单", "复制"))
            edit_menu.add_command(label="粘贴", command=lambda: messagebox.showinfo("菜单", "粘贴"))
            
            # 创建带有子菜单的菜单
            view_menu = tk.Menu(menubar, tearoff=0)
            menubar.add_cascade(label="视图", menu=view_menu)
            
            # 子菜单
            zoom_menu = tk.Menu(view_menu, tearoff=0)
            view_menu.add_cascade(label="缩放", menu=zoom_menu)
            zoom_menu.add_command(label="放大", command=lambda: messagebox.showinfo("菜单", "放大"))
            zoom_menu.add_command(label="缩小", command=lambda: messagebox.showinfo("菜单", "缩小"))
            zoom_menu.add_command(label="重置", command=lambda: messagebox.showinfo("菜单", "重置缩放"))
            
            # 单选菜单项
            view_menu.add_separator()
            view_var = tk.StringVar()
            view_var.set("normal")
            view_menu.add_radiobutton(label="普通视图", variable=view_var, value="normal")
            view_menu.add_radiobutton(label="紧凑视图", variable=view_var, value="compact")
            view_menu.add_radiobutton(label="扩展视图", variable=view_var, value="expanded")
            
            # 复选菜单项
            view_menu.add_separator()
            statusbar_var = tk.BooleanVar()
            statusbar_var.set(True)
            view_menu.add_checkbutton(label="显示状态栏", variable=statusbar_var)
            
            # 帮助菜单
            help_menu = tk.Menu(menubar, tearoff=0)
            menubar.add_cascade(label="帮助", menu=help_menu)
            help_menu.add_command(label="关于", command=lambda: messagebox.showinfo("关于", "菜单示例程序 v1.0"))
            
            # 添加一些内容到窗口
            ttk.Label(menu_window, text="这是一个菜单示例窗口\n请查看顶部的菜单栏").pack(expand=True)
        
        ttk.Button(menu_demo_frame, text="显示菜单示例", command=show_menu_demo).pack(padx=10, pady=10)
        
        # 工具栏示例
        ttk.Label(menu_frame, text="工具栏示例:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        
        toolbar_frame = ttk.LabelFrame(menu_frame, text="工具栏演示")
        toolbar_frame.grid(row=3, column=0, sticky=tk.EW, padx=10, pady=5)
        
        # 创建一个简单的工具栏
        toolbar = ttk.Frame(toolbar_frame)
        toolbar.pack(fill=tk.X, padx=5, pady=5)
        
        # 工具栏按钮
        btn_new = ttk.Button(toolbar, text="新建", width=8, command=lambda: self.status_bar.config(text="状态栏: 新建文件"))
        btn_new.pack(side=tk.LEFT, padx=2)
        
        btn_open = ttk.Button(toolbar, text="打开", width=8, command=lambda: self.status_bar.config(text="状态栏: 打开文件"))
        btn_open.pack(side=tk.LEFT, padx=2)
        
        btn_save = ttk.Button(toolbar, text="保存", width=8, command=lambda: self.status_bar.config(text="状态栏: 保存文件"))
        btn_save.pack(side=tk.LEFT, padx=2)
        
        # 分隔符
        ttk.Separator(toolbar, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=2)
        
        btn_cut = ttk.Button(toolbar, text="剪切", width=8, command=lambda: self.status_bar.config(text="状态栏: 剪切"))
        btn_cut.pack(side=tk.LEFT, padx=2)
        
        btn_copy = ttk.Button(toolbar, text="复制", width=8, command=lambda: self.status_bar.config(text="状态栏: 复制"))
        btn_copy.pack(side=tk.LEFT, padx=2)
        
        btn_paste = ttk.Button(toolbar, text="粘贴", width=8, command=lambda: self.status_bar.config(text="状态栏: 粘贴"))
        btn_paste.pack(side=tk.LEFT, padx=2)
        
        # 工具栏下方的内容区域
        content_area = ttk.Frame(toolbar_frame)
        content_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        ttk.Label(content_area, text="这是工具栏下方的内容区域").pack(pady=20)
        
        # 分隔线
        ttk.Separator(menu_frame, orient=tk.HORIZONTAL).grid(row=4, column=0, sticky=tk.EW, padx=10, pady=10)
        
        # 控件使用说明
        text = """菜单和工具栏使用示例:
        
1. 菜单(Menu): 创建应用程序菜单
   # 创建菜单栏
   menubar = tk.Menu(root)
   root.config(menu=menubar)
   
   # 创建菜单
   file_menu = tk.Menu(menubar, tearoff=0)
   menubar.add_cascade(label="文件", menu=file_menu)
      # 添加菜单项
   file_menu.add_command(label="新建", command=callback_function)
   file_menu.add_command(label="打开", command=callback_function)
   file_menu.add_separator()  # 添加分隔线
   file_menu.add_command(label="退出", command=root.destroy)
   
   # 创建子菜单
   sub_menu = tk.Menu(parent_menu, tearoff=0)
   parent_menu.add_cascade(label="子菜单", menu=sub_menu)
   
   # 创建单选菜单项
   view_var = tk.StringVar()
   view_menu.add_radiobutton(label="选项1", variable=view_var, value="1")
   
   # 创建复选菜单项
   show_var = tk.BooleanVar()
   view_menu.add_checkbutton(label="显示", variable=show_var)
   
2. 工具栏: 通常使用Frame控件创建
   toolbar = ttk.Frame(root)
   toolbar.pack(side=tk.TOP, fill=tk.X)
   
   # 添加工具栏按钮
   btn_new = ttk.Button(toolbar, text="新建", command=callback)
   btn_new.pack(side=tk.LEFT, padx=2, pady=2)
   
   # 添加分隔符
   ttk.Separator(toolbar, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=5)
        """
        text_widget = scrolledtext.ScrolledText(menu_frame, wrap=tk.WORD, width=40, height=15)
        text_widget.grid(row=5, column=0, sticky=tk.EW, padx=10, pady=5)
        text_widget.insert(tk.END, text)
        text_widget.config(state=tk.DISABLED)
        
    def create_dialog_tab(self):
        """对话框标签页"""
        dialog_frame = ttk.Frame(self.notebook)
        self.notebook.add(dialog_frame, text="对话框")
        
        # 使用网格布局
        dialog_frame.columnconfigure(0, weight=1)
        dialog_frame.columnconfigure(1, weight=1)
        
        # 消息框
        ttk.Label(dialog_frame, text="消息框(messagebox):").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        message_frame = ttk.Frame(dialog_frame)
        message_frame.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)
        
        ttk.Button(message_frame, text="信息", 
                  command=lambda: messagebox.showinfo("信息", "这是一个信息消息框")).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(message_frame, text="警告", 
                  command=lambda: messagebox.showwarning("警告", "这是一个警告消息框")).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(message_frame, text="错误", 
                  command=lambda: messagebox.showerror("错误", "这是一个错误消息框")).pack(side=tk.LEFT, padx=5)
        
        # 询问对话框
        ttk.Label(dialog_frame, text="询问对话框:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        question_frame = ttk.Frame(dialog_frame)
        question_frame.grid(row=1, column=1, sticky=tk.W, padx=10, pady=5)
        
        ttk.Button(question_frame, text="是/否", 
                  command=lambda: messagebox.askyesno("问题", "你喜欢Python吗?")).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(question_frame, text="确定/取消", 
                  command=lambda: messagebox.askokcancel("确认", "确定要执行此操作吗?")).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(question_frame, text="重试/取消", 
                  command=lambda: messagebox.askretrycancel("重试", "操作失败，是否重试?")).pack(side=tk.LEFT, padx=5)
        
        # 文件对话框
        ttk.Label(dialog_frame, text="文件对话框:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        file_frame = ttk.Frame(dialog_frame)
        file_frame.grid(row=2, column=1, sticky=tk.W, padx=10, pady=5)
        
        ttk.Button(file_frame, text="打开文件", 
                  command=lambda: filedialog.askopenfilename(
                      title="选择文件",
                      filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]
                  )).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(file_frame, text="保存文件", 
                  command=lambda: filedialog.asksaveasfilename(
                      title="保存文件",
                      defaultextension=".txt",
                      filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]
                  )).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(file_frame, text="选择目录", 
                  command=lambda: filedialog.askdirectory(title="选择目录")).pack(side=tk.LEFT, padx=5)
        
        # 颜色选择器
        ttk.Label(dialog_frame, text="颜色选择器:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        color_frame = ttk.Frame(dialog_frame)
        color_frame.grid(row=3, column=1, sticky=tk.W, padx=10, pady=5)
        
        color_display = tk.Canvas(color_frame, width=30, height=30, bg="red")
        color_display.pack(side=tk.LEFT, padx=5)
        
        def choose_color():
            color = colorchooser.askcolor(title="选择颜色", initialcolor="red")
            if color[1]:  # 如果用户选择了颜色而不是取消
                color_display.config(bg=color[1])
        
        ttk.Button(color_frame, text="选择颜色", command=choose_color).pack(side=tk.LEFT, padx=5)
        
        # 自定义对话框
        ttk.Label(dialog_frame, text="自定义对话框:").grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
        
        def show_custom_dialog():
            dialog = tk.Toplevel(self.root)
            dialog.title("自定义对话框")
            dialog.geometry("300x200")
            dialog.transient(self.root)  # 设置为主窗口的临时窗口
            dialog.grab_set()  # 模态对话框
            
            ttk.Label(dialog, text="请输入您的信息:").pack(pady=10)
            
            form_frame = ttk.Frame(dialog)
            form_frame.pack(pady=10)
            
            ttk.Label(form_frame, text="姓名:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
            name_entry = ttk.Entry(form_frame)
            name_entry.grid(row=0, column=1, padx=5, pady=5)
            
            ttk.Label(form_frame, text="年龄:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
            age_entry = ttk.Entry(form_frame)
            age_entry.grid(row=1, column=1, padx=5, pady=5)
            
            def on_submit():
                name = name_entry.get()
                age = age_entry.get()
                messagebox.showinfo("提交的信息", f"姓名: {name}\n年龄: {age}")
                dialog.destroy()
            
            button_frame = ttk.Frame(dialog)
            button_frame.pack(pady=10)
            
            ttk.Button(button_frame, text="提交", command=on_submit).pack(side=tk.LEFT, padx=5)
            ttk.Button(button_frame, text="取消", command=dialog.destroy).pack(side=tk.LEFT, padx=5)
            
            # 等待窗口关闭
            self.root.wait_window(dialog)
        
        ttk.Button(dialog_frame, text="显示自定义对话框", 
                  command=show_custom_dialog).grid(row=4, column=1, sticky=tk.W, padx=10, pady=5)
        
        # 分隔线
        ttk.Separator(dialog_frame, orient=tk.HORIZONTAL).grid(row=5, column=0, columnspan=2, sticky=tk.EW, padx=10, pady=10)
        
        # 控件使用说明
        text = """对话框使用示例:
        
1. 消息框(messagebox): 显示消息给用户
   from tkinter import messagebox
   messagebox.showinfo("标题", "信息内容")
   messagebox.showwarning("标题", "警告内容")
   messagebox.showerror("标题", "错误内容")
   
2. 询问对话框: 获取用户的选择
   result = messagebox.askyesno("标题", "问题内容")
   if result:  # 用户点击了"是"
       # 执行操作
   
   result = messagebox.askokcancel("标题", "确认内容")
   result = messagebox.askretrycancel("标题", "重试内容")
   
3. 文件对话框: 选择文件或目录
   from tkinter import filedialog
   
   # 打开文件
   file_path = filedialog.askopenfilename(
       title="选择文件",
       filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]
   )
   
   # 保存文件
   file_path = filedialog.asksaveasfilename(
       title="保存文件",
       defaultextension=".txt",
       filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]
   )
   
   # 选择目录
   dir_path = filedialog.askdirectory(title="选择目录")
   
4. 颜色选择器: 选择颜色
   from tkinter import colorchooser
   color = colorchooser.askcolor(title="选择颜色", initialcolor="red")
   # color[0]是RGB元组，color[1]是十六进制颜色值
   
5. 自定义对话框: 创建自定义的对话框窗口
   dialog = tk.Toplevel(root)
   dialog.title("自定义对话框")
   dialog.transient(root)  # 设置为主窗口的临时窗口
   dialog.grab_set()  # 模态对话框
   
   # 添加控件到对话框
   
   # 等待对话框关闭
   root.wait_window(dialog)
        """
        text_widget = scrolledtext.ScrolledText(dialog_frame, wrap=tk.WORD, width=40, height=15)
        text_widget.grid(row=6, column=0, columnspan=2, sticky=tk.EW, padx=10, pady=5)
        text_widget.insert(tk.END, text)
        text_widget.config(state=tk.DISABLED)
        
    def create_styling_tab(self):
        """样式和主题标签页"""
        style_frame = ttk.Frame(self.notebook)
        self.notebook.add(style_frame, text="样式和主题")
        
        # 使用网格布局
        style_frame.columnconfigure(0, weight=1)
        style_frame.columnconfigure(1, weight=1)
        
        # 主题选择
        ttk.Label(style_frame, text="ttk主题:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        
        themes_frame = ttk.Frame(style_frame)
        themes_frame.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)
        
        # 获取可用的ttk主题
        style = ttk.Style()
        available_themes = style.theme_names()
        
        theme_var = tk.StringVar()
        theme_var.set(style.theme_use())  # 设置当前主题为默认值
        
        def change_theme():
            selected_theme = theme_var.get()
            style.theme_use(selected_theme)
        
        for theme in available_themes:
            ttk.Radiobutton(themes_frame, text=theme, value=theme, 
                           variable=theme_var, command=change_theme).pack(anchor=tk.W)
        
        # 自定义样式
        ttk.Label(style_frame, text="自定义样式:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        
        custom_style_frame = ttk.Frame(style_frame)
        custom_style_frame.grid(row=1, column=1, sticky=tk.W, padx=10, pady=5)
        
        # 创建自定义样式的按钮
        style.configure("TButton", padding=6, relief="flat", background="#ccc")
        style.configure("Red.TButton", foreground="red", font=("Arial", 10, "bold"))
        style.configure("Green.TButton", foreground="green", font=("Arial", 10, "bold"))
        style.configure("Blue.TButton", foreground="blue", font=("Arial", 10, "bold"))
        
        ttk.Button(custom_style_frame, text="默认样式按钮").pack(anchor=tk.W, pady=5)
        ttk.Button(custom_style_frame, text="红色样式按钮", style="Red.TButton").pack(anchor=tk.W, pady=5)
        ttk.Button(custom_style_frame, text="绿色样式按钮", style="Green.TButton").pack(anchor=tk.W, pady=5)
        ttk.Button(custom_style_frame, text="蓝色样式按钮", style="Blue.TButton").pack(anchor=tk.W, pady=5)
        
        # 字体设置
        ttk.Label(style_frame, text="字体设置:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        
        font_frame = ttk.Frame(style_frame)
        font_frame.grid(row=2, column=1, sticky=tk.W, padx=10, pady=5) 
        font_frame = ttk.Frame(style_frame)
        font_frame.grid(row=2, column=1, sticky=tk.W, padx=10, pady=5)
        
        # 创建不同字体的标签
        default_font = tk.Label(font_frame, text="默认字体")
        default_font.pack(anchor=tk.W, pady=2)
        
        arial_font = tk.Label(font_frame, text="Arial字体", font=("Arial", 12))
        arial_font.pack(anchor=tk.W, pady=2)
        
        times_font = tk.Label(font_frame, text="Times New Roman字体", font=("Times New Roman", 12))
        times_font.pack(anchor=tk.W, pady=2)
        
        bold_font = tk.Label(font_frame, text="粗体", font=("Arial", 12, "bold"))
        bold_font.pack(anchor=tk.W, pady=2)
        
        italic_font = tk.Label(font_frame, text="斜体", font=("Arial", 12, "italic"))
        italic_font.pack(anchor=tk.W, pady=2)
        
        underline_font = tk.Label(font_frame, text="下划线", font=("Arial", 12, "underline"))
        underline_font.pack(anchor=tk.W, pady=2)
        
        # 颜色设置
        ttk.Label(style_frame, text="颜色设置:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        
        color_frame = ttk.Frame(style_frame)
        color_frame.grid(row=3, column=1, sticky=tk.W, padx=10, pady=5)
        
        # 创建不同颜色的标签
        black_label = tk.Label(color_frame, text="黑色文本", fg="black", bg="white")
        black_label.pack(anchor=tk.W, pady=2, fill=tk.X)
        
        red_label = tk.Label(color_frame, text="红色文本", fg="red", bg="white")
        red_label.pack(anchor=tk.W, pady=2, fill=tk.X)
        
        blue_label = tk.Label(color_frame, text="蓝色文本", fg="blue", bg="white")
        blue_label.pack(anchor=tk.W, pady=2, fill=tk.X)
        
        green_label = tk.Label(color_frame, text="绿色文本", fg="green", bg="white")
        green_label.pack(anchor=tk.W, pady=2, fill=tk.X)
        
        white_on_black = tk.Label(color_frame, text="白色文本，黑色背景", fg="white", bg="black")
        white_on_black.pack(anchor=tk.W, pady=2, fill=tk.X)
        
        # 分隔线
        ttk.Separator(style_frame, orient=tk.HORIZONTAL).grid(row=4, column=0, columnspan=2, sticky=tk.EW, padx=10, pady=10)
        
        # 控件使用说明
        text = """样式和主题使用示例:
        
1. ttk主题: 更改应用程序的整体外观
   style = ttk.Style()
   available_themes = style.theme_names()  # 获取可用主题
   current_theme = style.theme_use()  # 获取当前主题
   style.theme_use("clam")  # 设置主题
   
2. 自定义样式: 自定义控件的外观
   style = ttk.Style()
   
   # 配置所有按钮的样式
   style.configure("TButton", padding=6, relief="flat", background="#ccc")
   
   # 创建自定义样式
   style.configure("Red.TButton", foreground="red", font=("Arial", 10, "bold"))
   
   # 使用自定义样式
   button = ttk.Button(parent, text="按钮", style="Red.TButton")
   
3. 字体设置: 设置文本的字体
   label = tk.Label(parent, text="文本", font=("字体名称", 大小, "样式"))
   
   # 字体样式可以是: "bold"(粗体), "italic"(斜体), "underline"(下划线)
   # 也可以组合使用: font=("Arial", 12, "bold italic")
   
4. 颜色设置: 设置前景色和背景色
   label = tk.Label(parent, text="文本", fg="前景色", bg="背景色")
   
   # 颜色可以使用颜色名称: "red", "blue", "green", "black", "white"等
   # 也可以使用十六进制颜色值: fg="#FF0000", bg="#00FF00"
        """
        text_widget = scrolledtext.ScrolledText(style_frame, wrap=tk.WORD, width=40, height=15)
        text_widget.grid(row=5, column=0, columnspan=2, sticky=tk.EW, padx=10, pady=5)
        text_widget.insert(tk.END, text)
        text_widget.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    root.title("Python GUI 控件示例")
    root.geometry("800x600")
    
    # 设置应用程序图标
    # root.iconbitmap("icon.ico")  # 如果有图标文件，可以取消注释
    
    app = GUIControlsDemo(root)
    
    # 启动主循环
    root.mainloop()

if __name__ == "__main__":
    main()