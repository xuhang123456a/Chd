import sys
import os
import json
import chardet
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QLabel, QPushButton, QLineEdit, QTextEdit, QCheckBox, QRadioButton,
                            QComboBox, QSlider, QProgressBar, QSpinBox, QDoubleSpinBox, 
                            QTabWidget, QGroupBox, QListWidget, QTableWidget, QTableWidgetItem,
                            QCalendarWidget, QDateEdit, QTimeEdit, QDateTimeEdit, QDial,
                            QScrollArea, QSplitter, QFileDialog, QColorDialog, QFontDialog,
                            QMessageBox, QInputDialog, QMenu, QAction, QToolBar, QStatusBar,
                            QDialog)  # 添加 QDialog
from PyQt5.QtCore import Qt, QDate, QTime, QDateTime
from PyQt5.QtGui import QIcon, QPixmap, QFont, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QComboBox, QFileDialog, QPushButton, QLabel

class FileComboBoxApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # 获取当前程序所在目录
        current_dir = os.path.dirname(sys.argv[0])
        # 定义相对路径
        relative_path = 'data\\Config'
        # 构建默认文件夹路径
        self.default_folder = os.path.join(current_dir, relative_path)
        # 添加图标
        self.setWindowIcon(QIcon('data/icon.ico'))
        self.current_json_data = None  # 添加存储当前JSON数据的变量
        self.current_file_path = None  # 添加存储当前文件路径的变量
        self.field_mappings = {}
        self.load_field_mappings()
        self.initUI()

    def load_field_mappings(self):
        config_path = os.path.join(self.default_folder, 'field_config.json')
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                self.field_mappings = config.get('mappings', {})
        except:
            self.field_mappings = {}

    def select_folder(self):
        folder_path = self.default_folder
        if not os.path.exists(folder_path):
            QMessageBox.warning(self, '警告', f'默认文件夹不存在：{folder_path}')
            return
            
        self.combo_box.clear()
        file_names = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if '.' not in file:
                    file_names.append(os.path.join(root, file))
        
        if not file_names:
            self.combo_box.addItem('未找到任何目标文件')
            self.text_edit.clear()
            return
            
        self.combo_box.addItems(file_names)

    def show_file_content(self, index):
        if index >= 0:
            selected_file_path = self.combo_box.itemText(index)
            
            if selected_file_path == '未找到任何目标文件':
                return
                
            folder_path = os.path.dirname(selected_file_path)
            target_file_name = 'Default.save'
            self.current_file_path = os.path.join(folder_path, target_file_name)
            
            try:
                with open(self.current_file_path, 'rb') as raw_file:
                    raw_data = raw_file.read()
                    result = chardet.detect(raw_data)
                    encoding = result['encoding'] or 'utf-8'
                    
                    try:
                        content = raw_data.decode(encoding, errors='replace')
                        self.current_json_data = json.loads(content)
                        formatted_json = json.dumps(self.current_json_data, indent=4, ensure_ascii=False)
                        self.text_edit.setText(formatted_json)
                        # 创建字段按钮
                        self.create_field_buttons(self.current_json_data)
                        self.save_button.setEnabled(False)
                    except json.JSONDecodeError:
                        # 使用 errors='replace' 来替换无法解码的字符
                        content = raw_data.decode(encoding, errors='replace')
                        # 尝试清理替换字符后再次解析
                        cleaned_content = ''.join(char for char in content if ord(char) < 65535)
                        try:
                            json_data = json.loads(cleaned_content)
                            formatted_json = json.dumps(json_data, indent=4, ensure_ascii=False)
                            self.text_edit.setText(formatted_json)
                        except json.JSONDecodeError:
                            self.text_edit.setText('文件不是有效的 JSON 格式')
                        
            except FileNotFoundError:
                self.text_edit.setText(f'未找到文件: {selected_file_path}')
            except Exception as e:
                self.text_edit.setText(f'读取文件时出现错误: {str(e)}')

    def initUI(self):
        main_layout = QHBoxLayout()
        left_panel = QVBoxLayout()
        right_panel = QVBoxLayout()

        # 左侧面板
        # 文件选择区域
        file_select_group = QGroupBox('文件选择')
        file_layout = QVBoxLayout()
        
        file_list_label = QLabel('目标文件列表:')
        self.combo_box = QComboBox(self)
        self.combo_box.currentIndexChanged.connect(self.show_file_content)
        
        file_layout.addWidget(file_list_label)
        file_layout.addWidget(self.combo_box)
        file_select_group.setLayout(file_layout)
        
        # JSON预览区域
        preview_group = QGroupBox('JSON预览')
        preview_layout = QVBoxLayout()
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        preview_layout.addWidget(self.text_edit)
        preview_group.setLayout(preview_layout)
        
        left_panel.addWidget(file_select_group)
        left_panel.addWidget(preview_group)

        # 右侧面板
        # 字段操作区域
        field_group = QGroupBox('字段操作')
        field_layout = QVBoxLayout()
        
        # 搜索框
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText('搜索字段...')
        self.search_input.textChanged.connect(self.filter_buttons)
        search_layout.addWidget(self.search_input)
        
        # 配置按钮
        config_btn = QPushButton('配置字段', self)
        config_btn.clicked.connect(self.show_field_config)
        search_layout.addWidget(config_btn)
        
        field_layout.addLayout(search_layout)
        
        # 按钮容器
        self.button_container = QWidget()
        self.button_layout = QVBoxLayout()
        self.button_container.setLayout(self.button_layout)
        
        # 滚动区域
        scroll = QScrollArea()
        scroll.setWidget(self.button_container)
        scroll.setWidgetResizable(True)
        field_layout.addWidget(scroll)
        
        # 保存按钮
        self.save_button = QPushButton('保存修改', self)
        self.save_button.clicked.connect(self.save_changes)
        self.save_button.setEnabled(False)
        field_layout.addWidget(self.save_button)
        
        field_group.setLayout(field_layout)
        right_panel.addWidget(field_group)

        # 设置主布局
        main_widget = QWidget()
        main_layout.addLayout(left_panel, 2)
        main_layout.addLayout(right_panel, 1)
        main_widget.setLayout(main_layout)
        
        # 设置中心窗口部件
        self.setCentralWidget(main_widget)
        self.setWindowTitle('JSON编辑器')
        self.setGeometry(300, 300, 1000, 600)

    def filter_buttons(self, text):
        """过滤显示的按钮"""
        for i in range(self.button_layout.count()):
            button = self.button_layout.itemAt(i).widget()
            if button:
                if text.lower() in button.toolTip().lower() or text.lower() in button.text().lower():
                    button.show()
                else:
                    button.hide()

        # 设置样式
        self.setStyleSheet("""
            QComboBox {
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 3px;
            }
            QTextEdit {
                border: 1px solid #ccc;
                border-radius: 3px;
                padding: 5px;
            }
            QLabel {
                font-size: 12px;
            }
        """)

        self.setLayout(layout)
        self.setWindowTitle('test小程序')
        self.setGeometry(300, 300, 800, 600)
        
        # 初始化时加载默认文件夹内容
        self.select_folder()
        
        self.show()

    def create_field_buttons(self, json_data, parent_key=''):
        # 清除现有按钮
        for i in reversed(range(self.button_layout.count())): 
            self.button_layout.itemAt(i).widget().setParent(None)
        
        buttons = []
        def add_button(key, value):
            mapping = self.field_mappings.get(key, {"label": key, "order": 999})
            btn = QPushButton(f"{mapping['label']}", self)
            btn.setToolTip(key)  # 显示原始字段名作为提示
            btn.clicked.connect(lambda: self.edit_field(key, value))
            buttons.append((btn, mapping['order']))

        # 递归创建按钮
        def process_json(data, prefix=''):
            if isinstance(data, dict):
                for k, v in data.items():
                    full_key = f"{prefix}.{k}" if prefix else k
                    if isinstance(v, (dict, list)):
                        process_json(v, full_key)
                    else:
                        add_button(full_key, v)
            elif isinstance(data, list):
                for i, v in enumerate(data):
                    full_key = f"{prefix}[{i}]"
                    if isinstance(v, (dict, list)):
                        process_json(v, full_key)
                    else:
                        add_button(full_key, v)

        process_json(json_data)
        
        # 按order排序添加按钮
        for btn, _ in sorted(buttons, key=lambda x: x[1]):
            self.button_layout.addWidget(btn)

    def show_field_config(self):
        dialog = FieldConfigDialog(self.field_mappings, self)
        if dialog.exec_():
            self.field_mappings = dialog.get_mappings()
            # 保存配置
            config_path = os.path.join(self.default_folder, 'field_config.json')
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump({'mappings': self.field_mappings}, f, ensure_ascii=False, indent=4)
            # 刷新按钮显示
            if self.current_json_data:
                self.create_field_buttons(self.current_json_data)

    def edit_field(self, key, value):
        text, ok = QInputDialog.getText(self, '编辑字段', f'编辑 {key}:', QLineEdit.Normal, str(value))
        if ok:
            # 更新JSON数据
            keys = key.replace('][', '.').replace('[', '.').replace(']', '').split('.')
            current = self.current_json_data
            for i, k in enumerate(keys[:-1]):
                if k.isdigit():
                    current = current[int(k)]
                else:
                    current = current[k]
            
            if keys[-1].isdigit():
                current[int(keys[-1])] = text
            else:
                current[keys[-1]] = text

            # 更新显示
            self.text_edit.setText(json.dumps(self.current_json_data, indent=4, ensure_ascii=False))
            self.save_button.setEnabled(True)

    def save_changes(self):
        if self.current_file_path and self.current_json_data:
            try:
                # 先读取原文件以保持原有格式
                with open(self.current_file_path, 'rb') as file:
                    original_data = file.read()
                    
                # 保存修改后的内容
                with open(self.current_file_path, 'wb') as file:
                    json_str = json.dumps(self.current_json_data, ensure_ascii=False)
                    file.write(json_str.encode(chardet.detect(original_data)['encoding'] or 'utf-8'))
                
                self.save_button.setEnabled(False)
                QMessageBox.information(self, '成功', '修改已保存')
            except Exception as e:
                QMessageBox.warning(self, '错误', f'保存失败: {str(e)}')
                
# 添加配置对话框类
class FieldConfigDialog(QDialog):
    def __init__(self, current_mappings, parent=None):
        super().__init__(parent)
        self.setWindowTitle('字段配置')
        self.setModal(True)
        self.mappings = current_mappings.copy()
        
        layout = QVBoxLayout()
        
        # 添加字段列表
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['字段名', '显示名称', '排序'])
        layout.addWidget(self.table)
        
        # 添加按钮
        button_layout = QHBoxLayout()
        add_btn = QPushButton('添加字段')
        add_btn.clicked.connect(self.add_field)
        save_btn = QPushButton('保存')
        save_btn.clicked.connect(self.accept)
        cancel_btn = QPushButton('取消')
        cancel_btn.clicked.connect(self.reject)
        
        button_layout.addWidget(add_btn)
        button_layout.addWidget(save_btn)
        button_layout.addWidget(cancel_btn)
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
        self.load_mappings()
        
    def load_mappings(self):
        self.table.setRowCount(len(self.mappings))
        for i, (field, info) in enumerate(self.mappings.items()):
            self.table.setItem(i, 0, QTableWidgetItem(field))
            self.table.setItem(i, 1, QTableWidgetItem(info['label']))
            self.table.setItem(i, 2, QTableWidgetItem(str(info['order'])))
            
    def add_field(self):
        row = self.table.rowCount()
        self.table.insertRow(row)
        
    def get_mappings(self):
        mappings = {}
        for i in range(self.table.rowCount()):
            field = self.table.item(i, 0)
            label = self.table.item(i, 1)
            order = self.table.item(i, 2)
            if field and label and order and field.text():
                mappings[field.text()] = {
                    'label': label.text() or field.text(),
                    'order': int(order.text() or '999')
                }
        return mappings


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileComboBoxApp()
    sys.exit(app.exec_())