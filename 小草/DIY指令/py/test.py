import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QLabel, QPushButton, QLineEdit, QTextEdit, QCheckBox, QRadioButton,
                            QComboBox, QSlider, QProgressBar, QSpinBox, QDoubleSpinBox, 
                            QTabWidget, QGroupBox, QListWidget, QTableWidget, QTableWidgetItem,
                            QCalendarWidget, QDateEdit, QTimeEdit, QDateTimeEdit, QDial,
                            QScrollArea, QSplitter, QFileDialog, QColorDialog, QFontDialog,
                            QMessageBox, QInputDialog, QMenu, QAction, QToolBar, QStatusBar)
from PyQt5.QtCore import Qt, QDate, QTime, QDateTime
from PyQt5.QtGui import QIcon, QPixmap, QFont, QColor

class PyQtControlsDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()

        # 创建选择文件夹按钮
        self.select_folder_button = QPushButton('选择文件夹', self)
        self.select_folder_button.clicked.connect(self.select_folder)
        layout.addWidget(self.select_folder_button)

        # 创建下拉框
        self.combo_box = QComboBox(self)
        layout.addWidget(self.combo_box)

        self.setLayout(layout)

        self.setWindowTitle('文件选择下拉框')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, '选择文件夹')
        if folder_path:
            # 清空下拉框原有选项
            self.combo_box.clear()
            # 要查找的文件名
            target_file_name = 'your_target_file.txt'  # 请替换为你要查找的文件名
            file_names = []
            # 遍历文件夹及其子文件夹
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    if file == target_file_name:
                        file_names.append(os.path.join(root, file))
            # 将找到的文件名添加到下拉框
            self.combo_box.addItems(file_names)
        

def main():
    app = QApplication(sys.argv)
    demo = PyQtControlsDemo()
    demo.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()