import os
import glob
import chardet
from pathlib import Path
from src.utils.tools import get_game_dungeon_name,get_game_character_name
from src.utils.log import colored_bg_log

# 获取脚本所在目录
script_dir = Path(__file__).parent.resolve()
# 指定目录路径
# specified_directory = script_dir.parent.parent / "心月狐" / "data" / "Config" / "3476670590"
specified_directory = script_dir.parent.parent / "心月狐" / "data" / "Config" 

# 要替换的字符串和替换后的字符串
needReplace = True
old_strings = ['拾取开关判断=不检测']  # 替换为你要查找的字符串
new_strings = ['拾取开关判断=全程开启拾取']  # 替换为你想要的新字符串
find_strings = [
    # '副本难度=简单',
    # '副本难度=普通',
    # '副本难度=困难',
    # '是否采集=开启',
    # '是否挖矿=开启',
    # '开门就走=关闭',
    # '任务领取=关闭',
    '拾取开关判断=不检测',
    # '拾取开关判断=默认',
    # '拾取开关判断=队伍有人关拾取没人开启',
    # '不打苏尔特=开启',
    # '不打苏尔特=关闭',
    # '退组进队长组=开启',
    # '送死流=关闭',
    # '送死流=全程送死',
    # '组队模式=关闭'
    # '组队模式=[打手]组队一起打'
    # '自动吃减伤晚餐=开启'
    # '带经验本=大号',
]

game_name_strings = get_game_dungeon_name()
name_strings = get_game_character_name()

# needReplace:是否需要替换
def checkFile(dir, needReplace):
    # 计数
    index = 0
    # 使用 glob 模块获取所有文件
    files = glob.glob(os.path.join(dir, '*'))

    # 读取每个文件的内容
    for file in files:
        if os.path.isdir(file):
            checkFile(file, needReplace)
        if os.path.isfile(file):  # 确保是文件而不是文件夹
            with open(file, 'rb') as f:
                raw_data = f.read(10000)
                result = chardet.detect(raw_data)
                encoding = result['encoding']

            try:
                # 读取文件内容
                with open(file, 'r', encoding='gbk', errors='surrogateescape') as f:
                    content = f.read()
            except Exception as e:
                print(f"读取文件 {file} 时发生错误: {e}")
                continue  # 跳过此文件

            # 检测是否存在字符串
            for find_string in find_strings:
                if find_string in content:
                    str1 = ''
                    str2 = '？？？？？'
                    str3 = file
                    for name_string in name_strings:
                        if name_string[1] in file:
                            str1 = name_string[0]
                    for game_name_string in game_name_strings:
                        if game_name_string[1] in file:
                            str2 = game_name_string[0]
                            str3 = game_name_string[1]

                    # print(f"文件 {file} 副本 {str2} 角色 {str1} 中有 {find_string} 字符串")
                    index = index + 1
                    if str2 == '丽西泰亚之门' or str2 == '蘑菇树沼泽':
                        colored_bg_log(f"{index:<5}{str2:<20} {str3:<16} {str1:<10} |||---{find_string}")
                    else:
                        print(f"{index:<5}{str2:<20} {str3:<16} {str1:<10} |||---{find_string}")

                    if needReplace:
                        # 替换字符串
                        for old_str, new_str in zip(old_strings, new_strings):
                            content = content.replace(old_str, new_str)

                        # 将替换后的内容写回文件
                        try:
                            with open(file, 'w', encoding='gbk', errors='surrogateescape') as f:
                                f.write(content)
                        except Exception as e:
                            print(f"写入文件 {file} 时发生错误: {e}")


checkFile(specified_directory, needReplace)
