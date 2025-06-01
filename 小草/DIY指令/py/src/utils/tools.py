from pathlib import Path

# 获取脚本所在目录
script_dir = Path(__file__).parent.resolve()
script_dir = script_dir.parent.parent

# 同时读取两个文件，并将第一个文件的每一行与第二个文件的每一行配对作为元素的两个值，然后打包返回这些值
def read_files_in_parallel(file1_path, file2_path):
    # 初始化两个空列表来存储文件内容
    lines_file1 = []
    lines_file2 = []

    # 读取第一个文件的所有行
    with open(file1_path, 'r', encoding='utf-8') as file1:
        lines_file1 = file1.readlines()

    # 读取第二个文件的所有行
    with open(file2_path, 'r', encoding='utf-8') as file2:
        lines_file2 = file2.readlines()

    # 使用 zip 函数将两个文件的行配对，并去除每行末尾的换行符
    paired_lines = [(line1.strip(), line2.strip())
                    for line1, line2 in zip(lines_file1, lines_file2)]

    # 如果两个文件行数不同，这里会丢失多余行的信息
    # 如果需要处理这种情况，可以添加额外的逻辑

    return paired_lines

def get_game_dungeon_name():
    副本名字路径 = script_dir / "name_dic" / "副本名字.lua"
    副本编码名字路径 = script_dir / "name_dic" / "副本编码名字.lua"
    game_name_strings = read_files_in_parallel(副本名字路径, 副本编码名字路径)
    return game_name_strings

def get_game_character_name():
    角色名字路径 = script_dir / "name_dic" / "角色名字.lua"
    角色编码名字路径 = script_dir / "name_dic" / "角色编码名字.lua"
    game_name_strings = read_files_in_parallel(角色名字路径, 角色编码名字路径)
    return game_name_strings