import sys
import time
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QLabel, QPushButton, QLineEdit, QProgressBar, QTextEdit, 
                            QGroupBox, QGridLayout, QSpinBox, QDoubleSpinBox)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QMutex
from PyQt5.QtGui import QFont

class CalculationThread(QThread):
    progress_updated = pyqtSignal(int)
    result_updated = pyqtSignal(str)
    calculation_finished = pyqtSignal(list)
    combinations_updated = pyqtSignal(str)  # 使用字符串传递组合数，避免整数溢出
    
    def __init__(self, total_points, attr_values):
        super().__init__()
        self.total_points = total_points
        self.attr_values = attr_values  # 存储各属性的效果值
        self.mutex = QMutex()
        self.is_running = True
        self.combinations_checked = 0
        
    def run(self):
        self.calculate_optimal_distribution()
    
    def stop(self):
        self.mutex.lock()
        self.is_running = False
        self.mutex.unlock()
    
    def calculate_optimal_distribution(self):
        best_damage = 0
        best_distribution = None
        
        # 最大伤害、最小伤害、暴击伤害、武器属性力的最大值
        max_regular_attr = 1000
        # 最小伤害换最大伤害的最大值
        max_min_to_max = 250
        # 最终属性的最大值
        max_final_attr = 40
        # 超级武器属性力的最大值
        max_super_attr = 20
        
        # 预先计算最终属性和超级属性的成本
        final_attr_costs = [self.calculate_final_attr_cost(i) for i in range(max_final_attr + 1)]
        super_attr_costs = [self.calculate_super_attr_cost(i) for i in range(max_super_attr + 1)]
        
        # 获取属性效果值
        final_crit_effect = self.attr_values['final_crit']
        final_min_effect = self.attr_values['final_min']
        final_max_effect = self.attr_values['final_max']
        super_attr_effect = self.attr_values['super_attr']
        
        # 优化策略：先分配最终属性和超级属性，再分配普通属性
        # 先遍历最终暴击伤害、最终最小伤害、最终最大伤害和超级武器属性力
        for final_crit in range(max_final_attr, -1, -1):  # 从最大值开始，优先分配最终属性
            crit_cost = final_attr_costs[final_crit]
            if crit_cost > self.total_points:
                continue
            
            remaining_points1 = self.total_points - crit_cost
            
            for final_min in range(max_final_attr, -1, -1):
                min_cost = final_attr_costs[final_min]
                if min_cost > remaining_points1:
                    continue
                
                remaining_points2 = remaining_points1 - min_cost
                
                for final_max in range(max_final_attr, -1, -1):
                    max_cost = final_attr_costs[final_max]
                    if max_cost > remaining_points2:
                        continue
                    
                    remaining_points3 = remaining_points2 - max_cost
                    
                    for super_attr in range(max_super_attr, -1, -1):
                        super_cost = super_attr_costs[super_attr]
                        if super_cost > remaining_points3:
                            continue
                        
                        remaining_points4 = remaining_points3 - super_cost
                        
                        # 计算最终属性的实际效果
                        final_crit_value = final_crit * final_crit_effect
                        final_min_value = final_min * final_min_effect
                        final_max_value = final_max * final_max_effect
                        super_attr_value = super_attr * super_attr_effect
                        
                        # 然后分配剩余点数到普通属性
                        # 最小伤害换最大伤害的最大可用点数
                        max_possible_min_to_max = min(max_min_to_max, remaining_points4 // 3)
                        
                        for min_to_max in range(0, max_possible_min_to_max + 1):
                            remaining_points5 = remaining_points4 - min_to_max * 3
                            
                            # 计算剩余点数可以分配的最大普通属性点数
                            max_possible_regular = remaining_points5 // 3
                            
                            # 尝试不同的普通属性分配方案
                            for max_dmg_percent in range(0, 101, 5):  # 最大伤害占比0%-100%，步长5%提高效率
                                max_dmg = int(max_possible_regular * max_dmg_percent / 100)
                                remaining_after_max = remaining_points5 - max_dmg * 3
                                
                                for min_dmg_percent in range(0, 101, 5):  # 最小伤害占比0%-100%，步长5%提高效率
                                    if max_dmg_percent + min_dmg_percent > 100:
                                        continue
                                        
                                    min_dmg = int(max_possible_regular * min_dmg_percent / 100)
                                    remaining_after_min = remaining_after_max - min_dmg * 3
                                    
                                    for crit_dmg_percent in range(0, 101, 5):  # 暴击伤害占比0%-100%，步长5%提高效率
                                        if max_dmg_percent + min_dmg_percent + crit_dmg_percent > 100:
                                            continue
                                            
                                        crit_dmg = int(max_possible_regular * crit_dmg_percent / 100)
                                        remaining_after_crit = remaining_after_min - crit_dmg * 3
                                        
                                        # 剩余全部分配给属性力
                                        attr_power = remaining_after_crit // 3
                                        
                                        # 计算实际属性值
                                        actual_max_dmg = max_dmg * 1 + min_to_max * 10 + final_max_value
                                        actual_min_dmg = min_dmg * 1 - min_to_max * 5 + final_min_value
                                        
                                        # 跳过最小伤害超过最大伤害的无效组合
                                        if actual_min_dmg > actual_max_dmg:
                                            continue
                                        
                                        actual_crit_dmg = crit_dmg * 1 + final_crit_value
                                        actual_attr_power = attr_power * 1 + super_attr_value
                                        
                                        # 计算伤害
                                        damage = actual_attr_power * actual_crit_dmg * (actual_max_dmg + actual_min_dmg) / 2
                                        
                                        self.combinations_checked += 1
                                        if self.combinations_checked % 50000000 == 0:  # 降低更新频率，减少对性能的影响
                                            self.combinations_updated.emit(f"{self.combinations_checked:,}")
                                        
                                        if damage > best_damage:
                                            best_damage = damage
                                            best_distribution = [max_dmg, min_dmg, crit_dmg, attr_power, min_to_max, 
                                                                final_crit, final_min, final_max, super_attr, 
                                                                actual_max_dmg, actual_min_dmg, actual_crit_dmg, 
                                                                actual_attr_power, damage, 
                                                                self.total_points - (remaining_after_crit - attr_power * 3)]
                                            
                                            # 只在找到更好的解时更新UI，减少UI更新频率
                                            self.result_updated.emit(f"当前最佳伤害: {best_damage:.2f}\n" + 
                                                                    f"最大伤害: {max_dmg}, 最小伤害: {min_dmg}, 暴击伤害: {crit_dmg}\n" +
                                                                    f"武器属性力: {attr_power}, 最小换最大: {min_to_max}\n" +
                                                                    f"最终暴击: {final_crit}, 最终最小: {final_min}, 最终最大: {final_max}\n" +
                                                                    f"超级属性力: {super_attr}\n" +
                                                                    f"实际最大伤害: {actual_max_dmg:.2f}%, 实际最小伤害: {actual_min_dmg:.2f}%\n" +
                                                                    f"实际暴击伤害: {actual_crit_dmg:.2f}%, 实际属性力: {actual_attr_power:.2f}\n" +
                                                                    f"已使用点数: {self.total_points - (remaining_after_crit - attr_power * 3)}/{self.total_points}")
                            
                            # 在找到一个较好的解后，进行局部精细搜索
                            if best_distribution and min_to_max == best_distribution[4]:
                                best_max_dmg = best_distribution[0]
                                best_min_dmg = best_distribution[1]
                                best_crit_dmg = best_distribution[2]
                                
                                # 在最佳解附近进行精细搜索
                                for max_dmg in range(max(0, best_max_dmg - 10), min(max_possible_regular, best_max_dmg + 10) + 1):
                                    remaining_after_max = remaining_points5 - max_dmg * 3
                                    
                                    for min_dmg in range(max(0, best_min_dmg - 10), min(max_possible_regular, best_min_dmg + 10) + 1):
                                        if max_dmg * 3 + min_dmg * 3 > remaining_points5:
                                            continue
                                            
                                        remaining_after_min = remaining_after_max - min_dmg * 3
                                        
                                        for crit_dmg in range(max(0, best_crit_dmg - 10), min(max_possible_regular, best_crit_dmg + 10) + 1):
                                            if max_dmg * 3 + min_dmg * 3 + crit_dmg * 3 > remaining_points5:
                                                continue
                                                
                                            remaining_after_crit = remaining_after_min - crit_dmg * 3
                                            
                                            # 剩余全部分配给属性力
                                            attr_power = remaining_after_crit // 3
                                            
                                            # 计算实际属性值
                                            actual_max_dmg = max_dmg * 1 + min_to_max * 10 + final_max_value
                                            actual_min_dmg = min_dmg * 1 - min_to_max * 5 + final_min_value
                                            
                                            # 跳过最小伤害超过最大伤害的无效组合
                                            if actual_min_dmg > actual_max_dmg:
                                                continue
                                            
                                            actual_crit_dmg = crit_dmg * 1 + final_crit_value
                                            actual_attr_power = attr_power * 1 + super_attr_value
                                            
                                            # 计算伤害
                                            damage = actual_attr_power * actual_crit_dmg * (actual_max_dmg + actual_min_dmg) / 2
                                            
                                            self.combinations_checked += 1
                                            
                                            if damage > best_damage:
                                                best_damage = damage
                                                best_distribution = [max_dmg, min_dmg, crit_dmg, attr_power, min_to_max, 
                                                                    final_crit, final_min, final_max, super_attr, 
                                                                    actual_max_dmg, actual_min_dmg, actual_crit_dmg, 
                                                                    actual_attr_power, damage, 
                                                                    self.total_points - (remaining_after_crit - attr_power * 3)]
                                                
                                                self.result_updated.emit(f"当前最佳伤害: {best_damage:.2f}\n" + 
                                                                        f"最大伤害: {max_dmg}, 最小伤害: {min_dmg}, 暴击伤害: {crit_dmg}\n" +
                                                                        f"武器属性力: {attr_power}, 最小换最大: {min_to_max}\n" +
                                                                        f"最终暴击: {final_crit}, 最终最小: {final_min}, 最终最大: {final_max}\n" +
                                                                        f"超级属性力: {super_attr}\n" +
                                                                        f"实际最大伤害: {actual_max_dmg:.2f}%, 实际最小伤害: {actual_min_dmg:.2f}%\n" +
                                                                        f"实际暴击伤害: {actual_crit_dmg:.2f}%, 实际属性力: {actual_attr_power:.2f}\n" +
                                                                        f"已使用点数: {self.total_points - (remaining_after_crit - attr_power * 3)}/{self.total_points}")
                        
                        # 更新进度
                        progress = int((1 - final_crit / max_final_attr) * 100)
                        self.progress_updated.emit(progress)
                        
                        # 检查是否应该停止计算
                        self.mutex.lock()
                        should_stop = not self.is_running
                        self.mutex.unlock()
                        
                        if should_stop:
                            self.calculation_finished.emit(best_distribution)
                            return
        
        self.progress_updated.emit(100)
        self.calculation_finished.emit(best_distribution)
    
    def calculate_final_attr_cost(self, points):
        if points == 0:
            return 0
        
        total_cost = 2  # 第一点的成本
        for i in range(1, points):
            total_cost += 2 + i * 5
        
        return total_cost
    
    def calculate_super_attr_cost(self, points):
        if points == 0:
            return 0
        
        total_cost = 10  # 第一点的成本
        for i in range(1, points):
            total_cost += 10 + i * 10
        
        return total_cost

class AttributeCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.calculation_thread = None
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('属性点数分配计算器')
        self.setGeometry(100, 100, 900, 1300)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建主布局
        main_layout = QVBoxLayout(central_widget)
        
        # 创建输入区域
        input_group = QGroupBox("输入参数")
        input_layout = QGridLayout()
        
        # 总点数输入
        points_label = QLabel("总点数:")
        self.points_input = QSpinBox()
        self.points_input.setRange(1, 1000000)
        self.points_input.setValue(10000)
        input_layout.addWidget(points_label, 0, 0)
        input_layout.addWidget(self.points_input, 0, 1)
        
        # 属性效果值输入
        effect_label = QLabel("属性效果值设置:")
        input_layout.addWidget(effect_label, 1, 0, 1, 2)
        
        # 最终暴击伤害效果
        final_crit_label = QLabel("最终暴击伤害效果(%):")
        self.final_crit_input = QDoubleSpinBox()
        self.final_crit_input.setRange(1, 1000)
        self.final_crit_input.setValue(238)
        input_layout.addWidget(final_crit_label, 2, 0)
        input_layout.addWidget(self.final_crit_input, 2, 1)
        
        # 最终最小伤害效果
        final_min_label = QLabel("最终最小伤害效果(%):")
        self.final_min_input = QDoubleSpinBox()
        self.final_min_input.setRange(1, 1000)
        self.final_min_input.setValue(169)
        input_layout.addWidget(final_min_label, 3, 0)
        input_layout.addWidget(self.final_min_input, 3, 1)
        
        # 最终最大伤害效果
        final_max_label = QLabel("最终最大伤害效果(%):")
        self.final_max_input = QDoubleSpinBox()
        self.final_max_input.setRange(1, 1000)
        self.final_max_input.setValue(166)
        input_layout.addWidget(final_max_label, 4, 0)
        input_layout.addWidget(self.final_max_input, 4, 1)
        
        # 超级武器属性力效果
        super_attr_label = QLabel("超级武器属性力效果:")
        self.super_attr_input = QDoubleSpinBox()
        self.super_attr_input.setRange(1, 2000)
        self.super_attr_input.setValue(764)
        input_layout.addWidget(super_attr_label, 5, 0)
        input_layout.addWidget(self.super_attr_input, 5, 1)
        
        # 计算按钮
        button_layout = QHBoxLayout()
        self.calculate_button = QPushButton("开始计算")
        self.calculate_button.clicked.connect(self.start_calculation)
        self.stop_button = QPushButton("停止计算")
        self.stop_button.clicked.connect(self.stop_calculation)
        self.stop_button.setEnabled(False)
        button_layout.addWidget(self.calculate_button)
        button_layout.addWidget(self.stop_button)
        input_layout.addLayout(button_layout, 6, 0, 1, 2)
        
        input_group.setLayout(input_layout)
        main_layout.addWidget(input_group)
        
        # 创建进度和计数区域
        status_group = QGroupBox("计算状态")
        status_layout = QVBoxLayout()
        
        # 进度条
        progress_label = QLabel("计算进度:")
        self.progress_bar = QProgressBar()
        status_layout.addWidget(progress_label)
        status_layout.addWidget(self.progress_bar)
        
        # 方案计数
        count_layout = QHBoxLayout()
        count_label = QLabel("已检查方案数:")
        self.count_display = QLabel("0")
        count_layout.addWidget(count_label)
        count_layout.addWidget(self.count_display)
        status_layout.addLayout(count_layout)
        
        status_group.setLayout(status_layout)
        main_layout.addWidget(status_group)
        
        # 创建结果显示区域
        result_group = QGroupBox("计算结果")
        result_layout = QVBoxLayout()
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        result_layout.addWidget(self.result_text)
        result_group.setLayout(result_layout)
        main_layout.addWidget(result_group)
        
        # 创建属性说明区域
        info_group = QGroupBox("属性说明")
        info_layout = QVBoxLayout()
        info_text = QTextEdit()
        info_text.setReadOnly(True)
        info_text.setHtml("""
        <p><b>最大伤害</b>: 每点增加1%最大伤害，最多1000点，每点需要3点数</p>
        <p><b>最小伤害</b>: 每点增加1%最小伤害，最多1000点，每点需要3点数</p>
        <p><b>暴击伤害</b>: 每点增加1%暴击伤害，最多1000点，每点需要3点数</p>
        <p><b>武器属性力</b>: 每点增加1属性力，最多1000点，每点需要3点数</p>
        <p><b>最小伤害换最大伤害</b>: 每点最小伤害减少5%，最大伤害增加10%，最多250点，每点需要3点数</p>
        <p><b>最终暴击伤害</b>: 每点增加设定百分比暴击伤害，最多40点，点数递增</p>
        <p><b>最终最小伤害</b>: 每点增加设定百分比最小伤害，最多40点，点数递增</p>
        <p><b>最终最大伤害</b>: 每点增加设定百分比最大伤害，最多40点，点数递增</p>
        <p><b>超级武器属性力</b>: 每点增加设定属性力，最多20点，点数递增</p>
        <p><b>伤害计算公式</b>: 属性力 * 暴击伤害 * (最大伤害 + 最小伤害) / 2</p>
        <p><b>限制条件</b>: 实际最小伤害不能超过实际最大伤害</p>
        """)
        info_layout.addWidget(info_text)
        info_group.setLayout(info_layout)
        main_layout.addWidget(info_group)
        
    def start_calculation(self):
        total_points = self.points_input.value()
        
        # 获取属性效果值
        attr_values = {
            'final_crit': self.final_crit_input.value(),
            'final_min': self.final_min_input.value(),
            'final_max': self.final_max_input.value(),
            'super_attr': self.super_attr_input.value()
        }
        
        self.result_text.clear()
        self.result_text.append(f"开始计算最佳分配方式，总点数: {total_points}...")
        self.result_text.append(f"属性效果值设置:")
        self.result_text.append(f"- 最终暴击伤害: {attr_values['final_crit']}%")
        self.result_text.append(f"- 最终最小伤害: {attr_values['final_min']}%")
        self.result_text.append(f"- 最终最大伤害: {attr_values['final_max']}%")
        self.result_text.append(f"- 超级武器属性力: {attr_values['super_attr']}")
        self.progress_bar.setValue(0)
        self.count_display.setText("0")
        
        self.calculate_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        
        # 创建并启动计算线程
        self.calculation_thread = CalculationThread(total_points, attr_values)
        self.calculation_thread.progress_updated.connect(self.update_progress)
        self.calculation_thread.result_updated.connect(self.update_result)
        self.calculation_thread.calculation_finished.connect(self.calculation_complete)
        self.calculation_thread.combinations_updated.connect(self.update_combinations_count)
        self.calculation_thread.start()
    
    def stop_calculation(self):
        if self.calculation_thread and self.calculation_thread.isRunning():
            self.calculation_thread.stop()
            self.result_text.append("正在停止计算...")
    
    def update_progress(self, value):
        self.progress_bar.setValue(value)
    
    def update_result(self, result):
        self.result_text.setText(result)
    
    def update_combinations_count(self, count_str):
        self.count_display.setText(count_str)
    
    def calculation_complete(self, best_distribution):
        if best_distribution:
            self.result_text.append("\n计算完成！\n")
            self.result_text.append(f"最佳伤害值: {best_distribution[13]:,.2f}")
            self.result_text.append(f"最大伤害点数: {best_distribution[0]}")
            self.result_text.append(f"最小伤害点数: {best_distribution[1]}")
            self.result_text.append(f"暴击伤害点数: {best_distribution[2]}")
            self.result_text.append(f"武器属性力点数: {best_distribution[3]}")
            self.result_text.append(f"最小换最大点数: {best_distribution[4]}")
            self.result_text.append(f"最终暴击伤害点数: {best_distribution[5]}")
            self.result_text.append(f"最终最小伤害点数: {best_distribution[6]}")
            self.result_text.append(f"最终最大伤害点数: {best_distribution[7]}")
            self.result_text.append(f"超级武器属性力点数: {best_distribution[8]}")
            self.result_text.append(f"实际最大伤害: {best_distribution[9]:.2f}%")
            self.result_text.append(f"实际最小伤害: {best_distribution[10]:.2f}%")
            self.result_text.append(f"实际暴击伤害: {best_distribution[11]:.2f}%")
            self.result_text.append(f"实际属性力: {best_distribution[12]:.2f}")
            self.result_text.append(f"已使用点数: {best_distribution[14]}")
            
            # 显示总检查方案数
            self.result_text.append(f"\n总计检查方案数: {self.count_display.text()}")
        else:
            self.result_text.append("计算完成，但未找到有效的分配方式。")
        
        self.calculate_button.setEnabled(True)
        self.stop_button.setEnabled(False)

def main():
    app = QApplication(sys.argv)
    calculator = AttributeCalculator()
    calculator.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()