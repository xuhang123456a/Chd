from pathlib import Path
import json
import re

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

def read_json_file(file_path):
    try:
        # 使用gbk编码读取文件
        with open(file_path, 'r', encoding='gbk', errors='surrogateescape') as file:
            content = file.read()
            return content
    except Exception as e:
        print(f"读取文件时出现错误: {e}")
        return None
    
def save_json_file(file_path, content, encoding):
    try:
        with open(file_path, 'w', encoding=encoding, errors='surrogateescape') as file:
            file.write(content)
        print(f"文件保存成功。 {file_path}")
    except Exception as e:
        print(f"保存文件时出现错误: {e}")

def modify_json_data(content, key, new_value):
    # 准备目标键的正则表达式模式（使用原始字符串）
    key_pattern = rf'"{key}"\s*:'
    
    # 查找键的位置
    import re
    match = re.search(key_pattern, content)
    if not match:
        print(f"未找到键: {key}")
        return False
    
    # 定位值的起始位置（跳过键和冒号）
    key_start, key_end = match.span()
    value_start = key_end
    
    # 跳过冒号后的空白字符
    while value_start < len(content) and content[value_start].isspace():
        value_start += 1
    
    # 判断值的类型并找到结束位置
    value_type = content[value_start]
    value_end = None
    
    if value_type == '"':
        # 字符串值：找到匹配的引号（处理转义引号）
        i = value_start + 1
        in_quote = True
        while i < len(content):
            if content[i] == '"' and content[i-1] != '\\':
                value_end = i + 1
                break
            i += 1
    elif value_type in {'{', '['}:
        # 对象或数组：找到匹配的闭合符号
        stack = [value_type]
        i = value_start + 1
        while i < len(content) and stack:
            char = content[i]
            if char in {'{', '['}:
                stack.append(char)
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            i += 1
        if not stack:
            value_end = i
    else:
        # 简单值（数字、布尔、null）：找到下一个逗号或闭合符号
        i = value_start
        while i < len(content):
            char = content[i]
            if char in {',', '}', ']'}:
                value_end = i
                break
            i += 1
    
    if value_end is None:
        print("无法确定值的结束位置")
        return False
    
    # 获取原始值的字符串
    original_value_str = content[value_start:value_end]

    # 将新值转换为 JSON 字符串表示
    if isinstance(new_value, str):
        # 手动处理字符串转义
        escaped_value = new_value.replace('\\', '\\\\').replace('"', '\\"')
        new_value_str = f'"{escaped_value}"'
    else:
        # 其他类型使用 json.dumps
        import json
        new_value_str = json.dumps(new_value, ensure_ascii=False)
    
    # 比较新旧值是否相同
    if original_value_str == new_value_str:
        print(f"新值与旧值相同，不进行修改")
        return False

    # 替换值部分，保留其他内容不变
    modified_content = (
        content[:value_start] +
        new_value_str +
        content[value_end:]
    )
    print(f"将键 '{key}' 的值修改为: {original_value_str} =====> {new_value}")
    return modified_content