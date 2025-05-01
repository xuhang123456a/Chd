import chardet
import json

def open_file(file_path):
    if file_path:
        try:
            # 读取文件的一部分内容用于检测编码
            with open(file_path, 'rb') as raw_file:
                raw_data = raw_file.read(20000)
                result = chardet.detect(raw_data)
                encoding = result['encoding']
                confidence = result['confidence']
                print(f"检测到的编码: {encoding}，置信度: {confidence}")

            # 使用检测到的编码读取文件
            with open(file_path, 'r', encoding=encoding, errors='ignore') as file:
                content = file.read()
                # 解析 JSON 数据
                try:
                    json_data = json.loads(content)
                except json.JSONDecodeError:
                    print("\n文件内容不是有效的 JSON 格式。")
        except Exception as e:
            print("\n读取文件出错。")

file_path = f'E:\Game\Chd\小草\data\Config\1536622268\A96DC7EFCBAED2C1C8CBA967\Config.save'

open_file(file_path)