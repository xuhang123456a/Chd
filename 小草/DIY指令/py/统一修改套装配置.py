import os
import glob
import chardet

# 指定目录路径
xc_string = '心月狐'
specified_directory = 'E:\Game\Chd\小草\\' + xc_string + \
    '\data\Config\\' + 'D7FCD7FCD7D4C8BBC3C8A4B4D7FC'

# 要替换的字符串和替换后的字符串
old_strings = ['经验套',]  # 替换为你要查找的字符串
new_strings = ['经验套装']  # 替换为你想要的新字符串
find_strings = ['流水','格挡套','珊瑚手枪','珊瑚套']

# 使用 glob 模块获取所有文件
files = glob.glob(os.path.join(specified_directory, '*'))

# 读取每个文件的内容
for file in files:
    if os.path.isfile(file):  # 确保是文件而不是文件夹
        with open(file, 'rb') as f:
            raw_data = f.read()
            result = chardet.detect(raw_data)
            encoding = result['encoding']
        
        try:
            # 读取文件内容
            with open(file, 'r', encoding=encoding, errors='replace') as f:
                content = f.read()
        except Exception as e:
            print(f"读取文件 {file} 时发生错误: {e}")
            continue  # 跳过此文件
        
        # 进行替换
        modified_content = content
        replacements_made = False

        # 检测是否存在字符串
        for find_string in find_strings:
            if find_string in content:
                print(f"文件 {file} 中有 {find_string} 字符串")

        for old_string, new_string in zip(old_strings, new_strings):
            if old_string in modified_content:
                modified_content = modified_content.replace(old_string, new_string)
                replacements_made = True

        if replacements_made:
            # 写入修改后的内容回原文件
            # with open(file, 'w', encoding = encoding) as f:
            #     f.write(modified_content)
            print(f"文件 {file} 中的内容已成功替换。\n")
        # else:
        #     print(f"文件 {file} 中未找到要替换的字符串，无需修改。\n")