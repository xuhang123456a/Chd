import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkinter import scrolledtext

class TkinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter 控件示例")
        self.root.geometry("800x600")
        
        # 创建主框架
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 创建标题标签
        title_label = ttk.Label(self.main_frame, text="Tkinter 控件示例程序", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # 创建文件夹下拉框框架
        folder_frame = ttk.Frame(self.main_frame)
        folder_frame.pack(fill=tk.X, pady=5)
        
        folder_label = ttk.Label(folder_frame, text="选择子文件夹中的文件:")
        folder_label.pack(side=tk.LEFT, padx=5)
        
        self.folder_combo = ttk.Combobox(folder_frame, width=50)
        self.folder_combo.pack(side=tk.LEFT, padx=5)
        
        refresh_button = ttk.Button(folder_frame, text="刷新", command=self.load_files)
        refresh_button.pack(side=tk.LEFT, padx=5)
        
        # 创建选项卡控件
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # 创建基本控件选项卡
        self.basic_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.basic_tab, text="基本控件")
        self.setup_basic_tab()
        
        # 创建高级控件选项卡
        self.advanced_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.advanced_tab, text="高级控件")
        self.setup_advanced_tab()
        
        # 加载文件
        self.load_files()
    
    def load_files(self):
        self.folder_combo['values'] = []
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        files_list = []
        for root, dirs, files in os.walk(current_dir):
            # 跳过当前目录
            if root == current_dir:
                continue
            # 跳过非Config目录
            if os.path.basename(root) != "Config":
                continue
                
            # 获取相对路径
            rel_path = os.path.relpath(root, current_dir)
            
            # 添加子文件夹中的文件
            for file in files:
                file_path = os.path.join(rel_path, file)
                files_list.append(file_path)
        
        if not files_list:
            self.folder_combo['values'] = ["未找到子文件夹中的文件"]
        else:
            self.folder_combo['values'] = files_list
            
        self.folder_combo.current(0)
    
    def setup_basic_tab(self):
        # 使用网格布局
        self.basic_tab.columnconfigure(0, weight=1)
        self.basic_tab.columnconfigure(1, weight=1)
        
        # 按钮组
        button_group = ttk.LabelFrame(self.basic_tab, text="按钮控件")
        button_group.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        
        normal_button = ttk.Button(button_group, text="普通按钮", 
                                  command=lambda: messagebox.showinfo("消息", "你点击了普通按钮"))
        normal_button.pack(padx=10, pady=5, fill=tk.X)
        
        self.toggle_var = tk.BooleanVar()
        toggle_button = ttk.Checkbutton(button_group, text="切换按钮", 
                                       variable=self.toggle_var,
                                       command=self.toggle_button_state)
        toggle_button.pack(padx=10, pady=5, fill=tk.X)
        
        # 文本输入组
        input_group = ttk.LabelFrame(self.basic_tab, text="文本输入")
        input_group.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
        
        ttk.Label(input_group, text="单行文本:").pack(anchor=tk.W, padx=10, pady=2)
        self.line_edit = ttk.Entry(input_group)
        self.line_edit.pack(padx=10, pady=2, fill=tk.X)
        
        ttk.Label(input_group, text="多行文本:").pack(anchor=tk.W, padx=10, pady=2)
        self.text_edit = scrolledtext.ScrolledText(input_group, height=5)
        self.text_edit.pack(padx=10, pady=2, fill=tk.BOTH, expand=True)
        
        # 选择控件组
        selection_group = ttk.LabelFrame(self.basic_tab, text="选择控件")
        selection_group.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
        
        # 复选框
        check_frame = ttk.Frame(selection_group)
        check_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.check_var1 = tk.BooleanVar()
        self.check_var2 = tk.BooleanVar()
        self.check_var3 = tk.BooleanVar()
        
        check1 = ttk.Checkbutton(check_frame, text="选项1", variable=self.check_var1)
        check2 = ttk.Checkbutton(check_frame, text="选项2", variable=self.check_var2)
        check3 = ttk.Checkbutton(check_frame, text="选项3", variable=self.check_var3)
        
        check1.pack(side=tk.LEFT, padx=5)
        check2.pack(side=tk.LEFT, padx=5)
        check3.pack(side=tk.LEFT, padx=5)
        
        # 单选框
        radio_frame = ttk.Frame(selection_group)
        radio_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.radio_var = tk.StringVar()
        radio1 = ttk.Radiobutton(radio_frame, text="单选1", variable=self.radio_var, value="1")
        radio2 = ttk.Radiobutton(radio_frame, text="单选2", variable=self.radio_var, value="2")
        radio3 = ttk.Radiobutton(radio_frame, text="单选3", variable=self.radio_var, value="3")
        
        radio1.pack(side=tk.LEFT, padx=5)
        radio2.pack(side=tk.LEFT, padx=5)
        radio3.pack(side=tk.LEFT, padx=5)
        
        # 下拉框
        combo_frame = ttk.Frame(selection_group)
        combo_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(combo_frame, text="下拉框:").pack(side=tk.LEFT, padx=5)
        self.combo = ttk.Combobox(combo_frame, values=["选项A", "选项B", "选项C", "选项D"])
        self.combo.current(0)
        self.combo.pack(side=tk.LEFT, padx=5)
    
    def setup_advanced_tab(self):
        # 使用网格布局
        self.advanced_tab.columnconfigure(0, weight=1)
        self.advanced_tab.columnconfigure(1, weight=1)
        
        # 数值控件组
        numeric_group = ttk.LabelFrame(self.advanced_tab, text="数值控件")
        numeric_group.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        
        # 滑块
        slider_frame = ttk.Frame(numeric_group)
        slider_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(slider_frame, text="滑块:").pack(side=tk.LEFT, padx=5)
        self.slider_var = tk.IntVar(value=50)
        self.slider = ttk.Scale(slider_frame, from_=0, to=100, orient=tk.HORIZONTAL, 
                               variable=self.slider_var, command=self.update_progress)
        self.slider.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # 进度条
        progress_frame = ttk.Frame(numeric_group)
        progress_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(progress_frame, text="进度条:").pack(side=tk.LEFT, padx=5)
        self.progress = ttk.Progressbar(progress_frame, orient=tk.HORIZONTAL, length=200, mode='determinate')
        self.progress.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.progress['value'] = 50
        
        # 数字输入
        spin_frame = ttk.Frame(numeric_group)
        spin_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(spin_frame, text="数字输入:").pack(side=tk.LEFT, padx=5)
        self.spin_var = tk.IntVar(value=50)
        self.spin = ttk.Spinbox(spin_frame, from_=0, to=100, textvariable=self.spin_var)
        self.spin.pack(side=tk.LEFT, padx=5)
        
        # 日期时间组
        datetime_group = ttk.LabelFrame(self.advanced_tab, text="日期时间控件")
        datetime_group.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
        
        # 日期选择
        date_frame = ttk.Frame(datetime_group)
        date_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(date_frame, text="日期选择:").pack(side=tk.LEFT, padx=5)
        # self.date_entry = DateEntry(date_frame)
        # self.date_entry.pack(side=tk.LEFT, padx=5)
        
        # 日历
        # self.calendar = Calendar(datetime_group, selectmode='day')
        # self.calendar.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        # 列表和表格组
        list_group = ttk.LabelFrame(self.advanced_tab, text="列表和表格")
        list_group.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
        
        # 列表框
        list_frame = ttk.Frame(list_group)
        list_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        ttk.Label(list_frame, text="列表框:").pack(anchor=tk.W)
        self.listbox = tk.Listbox(list_frame)
        self.listbox.pack(fill=tk.BOTH, expand=True)
        
        for item in ["项目1", "项目2", "项目3", "项目4", "项目5"]:
            self.listbox.insert(tk.END, item)
        
        # 树状视图（代替表格）
        tree_frame = ttk.Frame(list_group)
        tree_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        ttk.Label(tree_frame, text="树状视图:").pack(anchor=tk.W)
        
        columns = ("列1", "列2", "列3")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show='headings')
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=80)
        
        for i in range(4):
            self.tree.insert('', tk.END, values=(f"单元格 {i+1},1", f"单元格 {i+1},2", f"单元格 {i+1},3"))
        
        self.tree.pack(fill=tk.BOTH, expand=True)
    
    def toggle_button_state(self):
        state = "开启" if self.toggle_var.get() else "关闭"
        messagebox.showinfo("切换按钮", f"按钮状态: {state}")
    
    def update_progress(self, value):
        # 将字符串转换为整数
        value = int(float(value))
        self.progress['value'] = value

if __name__ == "__main__":
    root = tk.Tk()
    app = TkinterApp(root)
    root.mainloop()