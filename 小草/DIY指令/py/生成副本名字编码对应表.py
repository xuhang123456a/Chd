import os
import chardet
import re # 正则表达式
from datetime import datetime

# 读取文本文件然后将[]包裹起来的部分解析为中文
def extract_bracketed_content(file_path):
    bracketed_lines = []

    try:
        # 首先读取文件的一小部分来检测编码
        with open(file_path, 'rb') as f:
            raw_data = f.read(10000)  # 读取前10000个字节
        encoding = chardet.detect(raw_data)['encoding']
        
        # 然后用检测到的编码打开整个文件
        with open(file_path, 'r', encoding=encoding, errors='ignore') as file:
            for line in file:
                # 去除所有空白字符
                stripped_line = re.sub(r'\s+', '', line)
                # 检查是否以 [ 开头并以 ] 结尾
                if stripped_line.startswith('"script":"') and stripped_line.endswith('",'):
                    # 输出被包裹的内容（不包括方括号）
                    bracketed_content = stripped_line[10:-2]
                    bracketed_lines.append(bracketed_content)
                # 检查是否以 [ 开头并以 ] 结尾
                # if stripped_line.startswith('I'):
                #     print("---------------------" + stripped_line)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return bracketed_lines

# 读取目录下所有lua文件的文件名
def list_lua_files_in_directory(directory_path):
    try:
        # 确保目录存在
        if not os.path.isdir(directory_path):
            print(f"Error: The directory {directory_path} does not exist.")
            return
        
        # 用于存储 .lua 文件名的列表
        lua_files = []
        
        # 遍历目录及其子目录
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.lua'):
                    full_path = os.path.join(root, file)
                    mtime = os.path.getmtime(full_path)
                    # 将时间戳转换为 datetime 对象
                    # mod_time = datetime.fromtimestamp(mtime)
                    # 格式化日期为 年-月-日 字符串
                    # formatted_date = mod_time.strftime('%Y-%m-%d %H:%M:%S')
                    # 构建文件的完整路径（可选，这里只存储文件名）
                    # full_path = os.path.join(root, file)
                    # 只存储文件名
                    file_name = file[0:-4]
                    lua_files.append((mtime,file_name))

        # 按修改时间从低到高排序
        lua_files.sort()
        # 提取排序后的文件名列表
        sorted_lua_files = [file for mtime, file in lua_files]
        return sorted_lua_files
    
    except Exception as e:
        print(f"An error occurred: {e}")


# 写入新的文件中
def write_to_file(lines, output_file_path):
    try:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for line in lines:
                output_file.write(line + '\n')  # 每行末尾添加换行符
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

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
    paired_lines = [(line1.strip(), line2.strip()) for line1, line2 in zip(lines_file1, lines_file2)]
    
    # 如果两个文件行数不同，这里会丢失多余行的信息
    # 如果需要处理这种情况，可以添加额外的逻辑
    
    return paired_lines

副本名字获取路径 = r"E:\Game\Chd\小草\心月狐\data\Config\3476670590\D7FCD7FCD1A9C8DEC0B6DDAEA4B4\autoscrpt.save"
副本名字路径 = r"E:\Game\Chd\小草\DIY指令\py\副本名字.lua"
副本名字 = extract_bracketed_content(副本名字获取路径)
write_to_file(副本名字, 副本名字路径)

副本编码名字获取路径 = r'E:\Game\Chd\小草\心月狐\data\Config\3476670590\D7FCD7FCD1A9C8DEC0B6DDAEA4B4'
副本编码名字路径 = r"E:\Game\Chd\小草\DIY指令\py\副本编码名字.lua"
副本编码名字 =  list_lua_files_in_directory(副本编码名字获取路径)
write_to_file(副本编码名字, 副本编码名字路径)

paired_data = read_files_in_parallel(副本名字路径, 副本编码名字路径)