import sys
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
        # 设置窗口标题和大小
        self.setWindowTitle('PyQt 控件示例')
        self.setGeometry(100, 100, 1000, 800)
        
        # 创建状态栏
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('准备就绪')
        
        # 创建工具栏
        self.toolbar = QToolBar('主工具栏')
        self.addToolBar(self.toolbar)
        
        # 添加工具栏按钮
        newAction = QAction(QIcon(), '新建', self)
        newAction.setStatusTip('创建新文件')
        newAction.triggered.connect(self.showMessage)
        self.toolbar.addAction(newAction)
        
        # 创建菜单栏
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件')
        
        # 添加菜单项
        newAct = QAction('新建', self)
        newAct.setShortcut('Ctrl+N')
        newAct.triggered.connect(self.showMessage)
        fileMenu.addAction(newAct)
        
        # 创建中央部件
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        
        # 创建主布局
        mainLayout = QVBoxLayout(self.centralWidget)
        
        # 创建选项卡部件
        tabWidget = QTabWidget()
        mainLayout.addWidget(tabWidget)
        
        # 创建基本控件选项卡
        basicTab = QWidget()
        tabWidget.addTab(basicTab, "基本控件")
        
        # 创建高级控件选项卡
        advancedTab = QWidget()
        tabWidget.addTab(advancedTab, "高级控件")
        
        # 创建对话框选项卡
        dialogTab = QWidget()
        tabWidget.addTab(dialogTab, "对话框")
        
        # 设置基本控件选项卡的布局
        basicLayout = QVBoxLayout(basicTab)
        
        # 标签和文本输入
        textGroup = QGroupBox("文本和输入控件")
        textLayout = QVBoxLayout()
        
        # 标签
        label = QLabel("这是一个标签 (QLabel)")
        label.setAlignment(Qt.AlignCenter)
        textLayout.addWidget(label)
        
        # 单行文本框
        lineEdit = QLineEdit()
        lineEdit.setPlaceholderText("这是一个单行文本框 (QLineEdit)")
        lineEdit.textChanged.connect(lambda text: self.statusBar.showMessage(f"文本已更改: {text}"))
        textLayout.addWidget(lineEdit)
        
        # 多行文本框
        textEdit = QTextEdit()
        textEdit.setPlaceholderText("这是一个多行文本框 (QTextEdit)")
        textLayout.addWidget(textEdit)
        
        textGroup.setLayout(textLayout)
        basicLayout.addWidget(textGroup)
        
        # 按钮控件
        buttonGroup = QGroupBox("按钮控件")
        buttonLayout = QVBoxLayout()
        
        # 普通按钮
        button = QPushButton("点击我 (QPushButton)")
        button.clicked.connect(lambda: self.statusBar.showMessage("按钮被点击"))
        buttonLayout.addWidget(button)
        
        # 复选框
        checkbox = QCheckBox("复选框 (QCheckBox)")
        checkbox.stateChanged.connect(lambda state: self.statusBar.showMessage(f"复选框状态: {'选中' if state == Qt.Checked else '未选中'}"))
        buttonLayout.addWidget(checkbox)
        
        # 单选按钮组
        radioLayout = QHBoxLayout()
        radio1 = QRadioButton("选项1 (QRadioButton)")
        radio2 = QRadioButton("选项2")
        radio1.toggled.connect(lambda checked: checked and self.statusBar.showMessage("选项1被选中"))
        radio2.toggled.connect(lambda checked: checked and self.statusBar.showMessage("选项2被选中"))
        radioLayout.addWidget(radio1)
        radioLayout.addWidget(radio2)
        buttonLayout.addLayout(radioLayout)
        
        buttonGroup.setLayout(buttonLayout)
        basicLayout.addWidget(buttonGroup)
        
        # 选择控件
        selectionGroup = QGroupBox("选择控件")
        selectionLayout = QVBoxLayout()
        
        # 下拉框
        comboBox = QComboBox()
        comboBox.addItems(["选项1", "选项2", "选项3"])
        comboBox.currentIndexChanged.connect(lambda index: self.statusBar.showMessage(f"选择了: {comboBox.currentText()}"))
        selectionLayout.addWidget(QLabel("下拉框 (QComboBox):"))
        selectionLayout.addWidget(comboBox)
        
        # 滑块
        slider = QSlider(Qt.Horizontal)
        slider.setRange(0, 100)
        slider.setValue(50)
        slider.valueChanged.connect(lambda value: self.statusBar.showMessage(f"滑块值: {value}"))
        selectionLayout.addWidget(QLabel("滑块 (QSlider):"))
        selectionLayout.addWidget(slider)
        
        # 进度条
        progressBar = QProgressBar()
        progressBar.setRange(0, 100)
        progressBar.setValue(50)
        slider.valueChanged.connect(progressBar.setValue)  # 将滑块与进度条连接
        selectionLayout.addWidget(QLabel("进度条 (QProgressBar):"))
        selectionLayout.addWidget(progressBar)
        
        # 数字输入框
        spinBox = QSpinBox()
        spinBox.setRange(0, 100)
        spinBox.setValue(50)
        spinBox.valueChanged.connect(lambda value: self.statusBar.showMessage(f"整数值: {value}"))
        selectionLayout.addWidget(QLabel("整数输入框 (QSpinBox):"))
        selectionLayout.addWidget(spinBox)
        
        # 浮点数输入框
        doubleSpinBox = QDoubleSpinBox()
        doubleSpinBox.setRange(0.0, 100.0)
        doubleSpinBox.setValue(50.0)
        doubleSpinBox.setSingleStep(0.1)
        doubleSpinBox.valueChanged.connect(lambda value: self.statusBar.showMessage(f"浮点值: {value}"))
        selectionLayout.addWidget(QLabel("浮点数输入框 (QDoubleSpinBox):"))
        selectionLayout.addWidget(doubleSpinBox)
        
        selectionGroup.setLayout(selectionLayout)
        basicLayout.addWidget(selectionGroup)
        
        # 设置高级控件选项卡的布局
        advancedLayout = QVBoxLayout(advancedTab)
        
        # 列表和表格
        listTableGroup = QGroupBox("列表和表格控件")
        listTableLayout = QVBoxLayout()
        
        # 列表部件
        listWidget = QListWidget()
        listWidget.addItems(["项目1", "项目2", "项目3", "项目4", "项目5"])
        listWidget.currentItemChanged.connect(lambda current, previous: 
                                            self.statusBar.showMessage(f"选择了列表项: {current.text() if current else ''}"))
        listTableLayout.addWidget(QLabel("列表部件 (QListWidget):"))
        listTableLayout.addWidget(listWidget)
        
        # 表格部件
        tableWidget = QTableWidget(4, 3)  # 4行3列
        tableWidget.setHorizontalHeaderLabels(["列1", "列2", "列3"])
        for row in range(4):
            for col in range(3):
                tableWidget.setItem(row, col, QTableWidgetItem(f"单元格 ({row},{col})"))
        tableWidget.cellClicked.connect(lambda row, col: 
                                    self.statusBar.showMessage(f"点击了单元格: ({row},{col})"))
        listTableLayout.addWidget(QLabel("表格部件 (QTableWidget):"))
        listTableLayout.addWidget(tableWidget)
        
        listTableGroup.setLayout(listTableLayout)
        advancedLayout.addWidget(listTableGroup)
        
        # 日期和时间控件
        dateTimeGroup = QGroupBox("日期和时间控件")
        dateTimeLayout = QVBoxLayout()
        
        # 日历部件
        calendar = QCalendarWidget()
        calendar.clicked.connect(lambda date: self.statusBar.showMessage(f"选择的日期: {date.toString()}"))
        dateTimeLayout.addWidget(QLabel("日历部件 (QCalendarWidget):"))
        dateTimeLayout.addWidget(calendar)
        
        # 日期编辑器
        dateEdit = QDateEdit()
        dateEdit.setDate(QDate.currentDate())
        dateEdit.dateChanged.connect(lambda date: self.statusBar.showMessage(f"日期已更改: {date.toString()}"))
        dateTimeLayout.addWidget(QLabel("日期编辑器 (QDateEdit):"))
        dateTimeLayout.addWidget(dateEdit)
        
        # 时间编辑器
        timeEdit = QTimeEdit()
        timeEdit.setTime(QTime.currentTime())
        timeEdit.timeChanged.connect(lambda time: self.statusBar.showMessage(f"时间已更改: {time.toString()}"))
        dateTimeLayout.addWidget(QLabel("时间编辑器 (QTimeEdit):"))
        dateTimeLayout.addWidget(timeEdit)
        
        # 日期时间编辑器
        dateTimeEdit = QDateTimeEdit()
        dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        dateTimeEdit.dateTimeChanged.connect(lambda dateTime: self.statusBar.showMessage(f"日期时间已更改: {dateTime.toString()}"))
        dateTimeLayout.addWidget(QLabel("日期时间编辑器 (QDateTimeEdit):"))
        dateTimeLayout.addWidget(dateTimeEdit)
        
        dateTimeGroup.setLayout(dateTimeLayout)
        advancedLayout.addWidget(dateTimeGroup)
        
        # 其他高级控件
        otherGroup = QGroupBox("其他高级控件")
        otherLayout = QVBoxLayout()
        
        # 刻度盘
        dial = QDial()
        dial.setRange(0, 100)
        dial.setValue(30)
        dial.valueChanged.connect(lambda value: self.statusBar.showMessage(f"刻度盘值: {value}"))
        otherLayout.addWidget(QLabel("刻度盘 (QDial):"))
        otherLayout.addWidget(dial)
        
        otherGroup.setLayout(otherLayout)
        advancedLayout.addWidget(otherGroup)
        
        # 设置对话框选项卡的布局
        dialogLayout = QVBoxLayout(dialogTab)
        
        # 文件对话框
        fileDialogBtn = QPushButton("打开文件对话框 (QFileDialog)")
        fileDialogBtn.clicked.connect(self.showFileDialog)
        dialogLayout.addWidget(fileDialogBtn)
        
        # 颜色对话框
        colorDialogBtn = QPushButton("打开颜色对话框 (QColorDialog)")
        colorDialogBtn.clicked.connect(self.showColorDialog)
        dialogLayout.addWidget(colorDialogBtn)
        
        # 字体对话框
        fontDialogBtn = QPushButton("打开字体对话框 (QFontDialog)")
        fontDialogBtn.clicked.connect(self.showFontDialog)
        dialogLayout.addWidget(fontDialogBtn)
        
        # 消息对话框
        messageBoxBtn = QPushButton("打开消息对话框 (QMessageBox)")
        messageBoxBtn.clicked.connect(self.showMessageBox)
        dialogLayout.addWidget(messageBoxBtn)
        
        # 输入对话框
        inputDialogBtn = QPushButton("打开输入对话框 (QInputDialog)")
        inputDialogBtn.clicked.connect(self.showInputDialog)
        dialogLayout.addWidget(inputDialogBtn)
        
    def showMessage(self):
        self.statusBar.showMessage('操作已执行', 2000)
        
    def showFileDialog(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "所有文件 (*);;文本文件 (*.txt)")
        if fileName:
            self.statusBar.showMessage(f"选择的文件: {fileName}")
            
    def showColorDialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.statusBar.showMessage(f"选择的颜色: RGB({color.red()},{color.green()},{color.blue()})")
            
    def showFontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.statusBar.showMessage(f"选择的字体: {font.family()}, {font.pointSize()}pt")
            
    def showMessageBox(self):
        reply = QMessageBox.question(self, '消息对话框', 
                                    "这是一个问题对话框。\n您想继续吗?",
                                    QMessageBox.Yes | QMessageBox.No, 
                                    QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            self.statusBar.showMessage('您选择了"是"')
        else:
            self.statusBar.showMessage('您选择了"否"')
            
    def showInputDialog(self):
        text, ok  = QInputDialog.getText(self, '输入对话框', '请输入您的姓名:')
        if ok and text:
            self.statusBar.showMessage(f"您的姓名是: {text}")
    def showInputDialog(self):
        text, ok = QInputDialog.getText(self, '输入对话框', '请输入文本:')
        if ok:
            self.statusBar.showMessage(f'您输入的文本: {text}')

def main():
    app = QApplication(sys.argv)
    demo = PyQtControlsDemo()
    demo.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()