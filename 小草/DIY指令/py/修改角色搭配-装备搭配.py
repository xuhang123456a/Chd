import os
import chardet
import json

def read_json_file(file_path):
    try:
        # 以二进制模式打开文件，读取部分内容用于检测编码
        with open(file_path, 'rb') as file:
            raw_data = file.read(20000)  # 读取前 1024 字节的数据，可根据文件大小调整
            result = chardet.detect(raw_data)
            encoding = result['encoding']
            confidence = result['confidence']

            print(f"检测到的编码: {encoding}，置信度: {confidence}")

        # 使用检测到的编码读取文件
        with open(file_path, 'r', encoding=encoding, errors='ignore') as file:
            content = file.read()
            return content, encoding
    except Exception as e:
        print(f"读取文件时出现错误: {e}")
        return None, None

def modify_json_data(json_content, target_json_content, modification_func):
    try:
        # 解析 JSON 数据
        data = json.loads(json_content)
        target_data = json.loads(target_json_content)
        # 调用修改函数
        modified_data = modification_func(data,target_data)
        # 生成修改后的 JSON 字符串，保留缩进
        modified_json = json.dumps(modified_data, indent='\t', ensure_ascii=False)
        return modified_json
    except json.JSONDecodeError as e:
        print(f"解析 JSON 数据时出现错误: {e}")
        return None

def save_json_file(file_path, content, encoding):
    try:
        with open(file_path, 'w', encoding=encoding, errors='ignore') as file:
            file.write(content)
        print("文件保存成功。")
    except Exception as e:
        print(f"保存文件时出现错误: {e}")


# 示例修改函数，将 "name" 字段的值修改为 "New Name"
def example_modification(data, target_data):
    if 'diysuit_item' in target_data:
        target_data['diysuit_item'] = data
    return target_data

file_path = r'E:\Game\Chd\小草\DIY指令\吉他号\搭配-装备搭配 魔法主职连体.txt'
json_content,encoding = read_json_file(file_path)
target_path = r'E:\Game\Chd\小草\心月狐\data\Config\3476670590'
target_files_path = [
    ["自然萌ご", "D7FCD7FCD7D4C8BBC3C8A4B4D7FC"],
    ["傻海我们走~", "C9B5BAA3CED2C3C7D7DF7E"],
    ["十八岁青春男高", "CAAEB0CBCBEAC7E0B4BAC4D0B8DF"],
    ["雪绒薄荷ご", "D7FCD7FCD1A9C8DEB1A1BAC9A4B4"],
    ["傻海我们走~", "C9B5BAA3CED2C3C7D7DF7E"],
    ["BaLl,", "42614C6C2C"],
]
for target_file_path in target_files_path:
    target_file_path = os.path.join(target_path, target_file_path[1])
    target_file_path = os.path.join(target_file_path, 'Config.save')
    target_json_content, encoding = read_json_file(target_file_path)
    if json_content and encoding:
        # 修改 JSON 数据
        modified_json = modify_json_data(json_content,target_json_content, example_modification)
        if modified_json:
            # 保存修改后的 JSON 文件
            save_json_file(target_file_path, modified_json, 'gbk')