import os
import myfunction
import glob
from pathlib import Path

# 用于存储角色名的列表
character_names = []
# 用于存储角色编码的列表
character_gbk_names = []

# 写入新的文件中
def write_to_file(lines, output_file_path):
    try:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for line in lines:
                output_file.write(line + '\n')  # 每行末尾添加换行符
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def checkFile(dir):
    # 使用 glob 模块获取所有文件
    files = glob.glob(os.path.join(dir, '*'))

    # 读取每个文件的内容
    for file in files:
        if os.path.isdir(file):
            checkFile(file)
        if os.path.isfile(file):  # 确保是文件而不是文件夹
            _, extension = os.path.splitext(file)
            if extension == '':#这是角色名字
                # 获取当前文件的 Path 对象
                current_path = Path(file).resolve()
                # 获取当前文件名（包含扩展名）
                file_name = current_path.name
                # 获取父文件夹名
                parent_folder = current_path.parent.name
                character_names.append(file_name)
                character_gbk_names.append(parent_folder)


script_dir = myfunction.script_dir
配置路径 = script_dir.parent.parent / "心月狐" / "data" / "Config" 
角色名字保存路径 = script_dir / "name_dic" / "角色名字.lua"
角色编码名字保存路径 = script_dir / "name_dic" / "角色编码名字.lua"
checkFile(配置路径)
write_to_file(character_names, 角色名字保存路径)
write_to_file(character_gbk_names, 角色编码名字保存路径)