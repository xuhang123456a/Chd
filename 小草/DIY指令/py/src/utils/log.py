from colorama import init, Fore, Back, Style

# 初始化 colorama，确保在 Windows 上也能正常显示颜色
init(autoreset=True)  # 自动重置颜色

def colored_log(message, color=Fore.RESET):
    """带颜色的日志打印函数"""
    print(f"{color}{message}")

def colored_bg_log(message, color=Back.RED):
    print(color + f"{message}")

print(Style.RESET_ALL)  # 手动重置所有样式