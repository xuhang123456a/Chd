import tkinter as tk
from tkinter import filedialog
import chardet
import json

class FileContentViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("文件内容查看器")
        # 设置窗口初始大小
        self.root.geometry("1000x800")
        # 允许窗口在水平和垂直方向上调整大小
        self.root.resizable(True, True)

        # 创建按钮
        self.open_button = tk.Button(self.root, text="打开文件", command=self.open_file)
        self.open_button.pack(pady=10)

        # 创建文本区域和滚动条
        self.text_area = tk.Text(self.root, wrap=tk.WORD)
        self.scrollbar = tk.Scrollbar(self.root, command=self.text_area.yview)
        self.text_area.config(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # 创建用于放置按钮的 Canvas 和滚动条
        self.button_canvas = tk.Canvas(self.root)
        self.button_scrollbar = tk.Scrollbar(self.root, command=self.button_canvas.yview)
        self.button_canvas.config(yscrollcommand=self.button_scrollbar.set)
        self.button_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.button_canvas.pack(pady=10, fill=tk.BOTH, expand=True)

        # 创建一个 Frame 用于存放按钮
        self.json_buttons_frame = tk.Frame(self.button_canvas)
        self.button_canvas.create_window((0, 0), window=self.json_buttons_frame, anchor='nw')

        # 绑定 Canvas 内容变化时的事件
        self.json_buttons_frame.bind("<Configure>", lambda e: self.button_canvas.configure(
            scrollregion=self.button_canvas.bbox("all")))

        # 绑定鼠标滚轮事件，关键改动
        self.button_canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def open_file(self):
        # 限定文件类型
        filetypes = (
            ('json文件', '*.json'),
            ('所有文件', '*.*')
        )
        file_path = filedialog.askopenfilename(filetypes=filetypes)
        if file_path:
            try:
                # 读取文件的一部分内容用于检测编码
                with open(file_path, 'rb') as raw_file:
                    raw_data = raw_file.read(20000)
                    result = chardet.detect(raw_data)
                    encoding = result['encoding']
                    confidence = result['confidence']
                    print(f"检测到的编码: {encoding}，置信度: {confidence}")

                # 使用检测到的编码读取文件
                with open(file_path, 'r', encoding=encoding, errors='ignore') as file:
                    content = file.read()
                    self.text_area.delete('1.0', tk.END)
                    self.text_area.insert(tk.END, content)
                    # 解析 JSON 数据
                    try:
                        json_data = json.loads(content)
                        # 清除之前的按钮
                        for widget in self.json_buttons_frame.winfo_children():
                            widget.destroy()
                        # 为每个 key 创建按钮，使用 grid 布局
                        col_num = 0
                        row_num = 0
                        max_cols = 5  # 每行最多显示 5 个按钮，可根据需要调整
                        for key in json_data.keys():
                            button = tk.Button(self.json_buttons_frame, text=key,
                                               command=lambda k=key: self.show_key_value(k, json_data))
                            button.grid(row=row_num, column=col_num, padx=5, pady=5)
                            col_num += 1
                            if col_num >= max_cols:
                                col_num = 0
                                row_num += 1
                    except json.JSONDecodeError:
                        self.text_area.insert(tk.END, "\n文件内容不是有效的 JSON 格式。")
            except Exception as e:
                self.text_area.delete('1.0', tk.END)
                self.text_area.insert(tk.END, f"读取文件时出错: {e}")

    def show_key_value(self, key, json_data):
        value = json_data[key]
        self.text_area.delete('1.0', tk.END)
        self.text_area.insert(tk.END, value)
        
    # 鼠标滚轮事件处理函数，关键改动
    def _on_mousewheel(self, event):
        self.button_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileContentViewer(root)
    root.mainloop()