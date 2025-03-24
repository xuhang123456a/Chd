import chardet

# 从十六进制字符串到中文字符串
def exchange_str_to_word(hex_str):
    try:
        gbk_bytes = bytes.fromhex(hex_str)
        decoded_str = gbk_bytes.decode('gbk')
        return decoded_str
        print("解码结果:", decoded_str)
    except UnicodeDecodeError:
        print("解码失败：存在非 GBK 编码字符！")

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
                # 去除前后空白字符
                stripped_line = line.strip()
                # 检查是否以 [ 开头并以 ] 结尾
                if stripped_line.startswith('[') and stripped_line.endswith(']'):
                    # 输出被包裹的内容（不包括方括号）
                    bracketed_content = stripped_line[1:-1]
                    bracketed_lines.append(bracketed_content)
                    print(exchange_str_to_word(bracketed_content))
                # 检查是否以 [ 开头并以 ] 结尾
                if stripped_line.startswith('I'):
                    print("---------------------" + stripped_line)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return bracketed_lines

# 示例使用
file_path = r"E:\Game\Chd\小草\心月狐\data\Config\D7FCD7FCD7D4C8BBC3C8A4B4D7FC\AutoDIY.DAT"  # 替换为你的文本文件路径
extracted_content = extract_bracketed_content(file_path)