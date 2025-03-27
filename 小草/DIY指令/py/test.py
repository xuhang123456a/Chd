import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtCore import pyqtSignal, QObject


class ProgressSignal(QObject):
    result = pyqtSignal(str)


class SkillAllocationGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.signal = ProgressSignal()
        self.signal.result.connect(self.show_result)

    def initUI(self):
        layout = QVBoxLayout()

        self.points_label = QLabel('请输入技能点数:')
        self.points_input = QLineEdit()
        layout.addWidget(self.points_label)
        layout.addWidget(self.points_input)

        self.calculate_button = QPushButton('计算最佳分配')
        self.calculate_button.clicked.connect(self.start_calculation)
        layout.addWidget(self.calculate_button)

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        self.setLayout(layout)
        self.setWindowTitle('技能点数分配计算器')
        self.setGeometry(300, 300, 900, 900)
        self.show()

    def start_calculation(self):
        try:
            total_points = int(self.points_input.text())
            self.calculate_button.setEnabled(False)
            self.result_text.clear()
            import threading
            thread = threading.Thread(target=self.calculate_allocation, args=(total_points,))
            thread.start()
        except ValueError:
            self.result_text.setText('请输入有效的技能点数！')

    def calculate_allocation(self, total_points):
        def calculate_cost(attr_points, first_cost, step_cost):
            total_cost = 0
            for i in range(attr_points):
                total_cost += first_cost + i * step_cost
            return total_cost

        def calculate_damage(attrs):
            attr1, attr2, attr3, attr4, attr5, attr6, attr7, attr8, attr9 = attrs
            min_damage = 100
            max_damage = 200
            crit_damage = 100
            weapon_attr_force = 0
            super_weapon_attr_force = 0
            new_min_damage = min_damage * (1 + 0.01 * attr2) * (1 - 0.05 * attr5) * (1 + 1.69 * attr7)
            new_max_damage = max_damage * (1 + 0.01 * attr1) * (1 + 0.1 * attr5) * (1 + 1.66 * attr8)
            new_crit_damage = crit_damage * (1 + 0.01 * attr3) * (1 + 2.38 * attr6)
            new_weapon_attr_force = weapon_attr_force + attr4
            new_super_weapon_attr_force = super_weapon_attr_force + 764 * attr9
            total_attr_force = new_weapon_attr_force + new_super_weapon_attr_force
            final_damage = total_attr_force * new_crit_damage * (new_max_damage + new_min_damage) / 2
            return final_damage

        # 各属性的最大点数
        max_points = [
            min(total_points // 3, 1000),
            min(total_points // 3, 1000),
            min(total_points // 3, 1000),
            min(total_points // 3, 1000),
            min(total_points // 3, 250),
            40,
            40,
            40,
            20
        ]
        # 初始化动态规划数组
        dp = {}
        best_allocation = None
        max_damage = 0

        def dfs(attrs, remaining_points):
            nonlocal max_damage, best_allocation
            key = tuple(attrs)
            if key in dp:
                return dp[key]
            if remaining_points < 0:
                return 0
            damage = calculate_damage(attrs)
            if damage > max_damage:
                max_damage = damage
                best_allocation = attrs[:]
            for i in range(len(attrs)):
                if attrs[i] < max_points[i]:
                    new_attrs = attrs[:]
                    new_attrs[i] += 1
                    if i < 5:
                        new_remaining_points = remaining_points - 3
                    elif i == 5:
                        new_remaining_points = remaining_points - calculate_cost(new_attrs[i], 2, 5)
                    elif i == 6:
                        new_remaining_points = remaining_points - calculate_cost(new_attrs[i], 2, 5)
                    elif i == 7:
                        new_remaining_points = remaining_points - calculate_cost(new_attrs[i], 2, 5)
                    else:
                        new_remaining_points = remaining_points - calculate_cost(new_attrs[i], 10, 10)
                    dfs(new_attrs, new_remaining_points)
            dp[key] = damage
            return damage

        initial_attrs = [0] * 9
        dfs(initial_attrs, total_points)

        result_str = f"最佳分配方式:\n"
        result_str += f"最大伤害: {best_allocation[0]} 点\n"
        result_str += f"最小伤害: {best_allocation[1]} 点\n"
        result_str += f"暴击伤害: {best_allocation[2]} 点\n"
        result_str += f"武器属性力: {best_allocation[3]} 点\n"
        result_str += f"最小伤害换最大伤害: {best_allocation[4]} 点\n"
        result_str += f"最终暴击伤害: {best_allocation[5]} 点\n"
        result_str += f"最终最小伤害: {best_allocation[6]} 点\n"
        result_str += f"最终最大伤害: {best_allocation[7]} 点\n"
        result_str += f"超级武器属性力: {best_allocation[8]} 点\n"
        result_str += f"最终造成的最大伤害: {max_damage}\n"

        # 发送信号，将结果传递给主线程
        self.signal.result.emit(result_str)
        self.calculate_button.setEnabled(True)

    def show_result(self, result):
        self.result_text.setText(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SkillAllocationGUI()
    sys.exit(app.exec_())
    