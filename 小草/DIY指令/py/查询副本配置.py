import os
import glob
import chardet

# 指定目录路径
xc_string = '心月狐'
specified_directory = 'E:\Game\Chd\小草\\' + xc_string + \
    '\data\Config\\1536622268'  # + 'A96DC7EFCBAED2C1C8CBA967'

# 要替换的字符串和替换后的字符串
needReplace = False
old_strings = ['自动采集=开启']  # 替换为你要查找的字符串
new_strings = ['自动采集=关闭']  # 替换为你想要的新字符串
find_strings = [
    # '副本难度=简单',
    # '副本难度=普通',
    # '副本难度=困难',
    # '自动采集=开启',
    # '自动挖矿=开启',
    # '开门就走=关闭',
    # '任务领取=关闭',
    '拾取开关判断=不检测',
    '拾取开关判断=默认',
    '拾取开关判断=队伍有人关拾取没人开启',
    # '不打苏尔特=开启',
    # '不打苏尔特=关闭',
    # '退组进队长组=开启',
    # '送死流=全程送死',
    # '组队模式=[打手]组队一起打'
    # '送死流=全程送死'
    # '自动吃减伤晚餐=开启'
    # '带经验本=大号',
]
name_strings = [
    ["﹎秋水伊人ゞ", "A96DC7EFCBAED2C1C8CBA967"],
    ["晚来天欲雪o", "CDEDC0B4CCECD3FBD1A96F"],
    ["小姐姐", "D7FAD7FAD7FAD7FAD7FAD0A1BDE3BDE3"],
    ["云青青兮欲雨", "D4C6C7E0C7E0D9E2D3FBD3EAFE5D"],
    ["℃ベ裸装", "A1E6A5D9A8FDA8FDC2E3D7B0"],
    ["能饮一杯无o", "C4DCD2FBD2BBB1ADCEDE6F"],
    ["→酷我音乐→", "A1FABFE1CED2D2F4C0D6A1FA"],
    ["酷狗音乐ā", "BFE1B9B7D2F4C0D6A8A1"],
    ["醉后不知天在水o", "D7EDBAF3B2BBD6AACCECD4DACBAE6F"],
    ["满船清梦压星河Q", "C2FAB4ACC7E5C3CED1B9D0C7BAD351"],
    ["水澹澹兮生烟", "CBAEE5A3E5A3D9E2C9FAD1CCFE5D"],
    ["终不似o", 'D6D5B2BBCBC66F'],
    ["少年游o", "C9D9C4EAD3CE6F"],
    ["最是人间留不住o", "D7EECAC7C8CBBCE4C1F4B2BBD7A16F"],

    # ["你到底吻不吻我o", "C4E3B5BDB5D7CEC7B2BBCEC7CED26F"],
    # ["来去荒芜", "C0B4C8A5BBC4CEDF"],
    # ["我有药", "CED2D3D0D2A9"],
    # ["不要碰我肩膀", "B2BBD2AAC5F6CED2BCE7B0F2"],

    # ["自然萌ご", "D7FCD7FCD7D4C8BBC3C8A4B4D7FC"],
]


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


副本名字路径 = r"E:\Game\Chd\小草\DIY指令\py\副本名字.lua"
副本编码名字路径 = r"E:\Game\Chd\小草\DIY指令\py\副本编码名字.lua"
game_name_strings = read_files_in_parallel(副本名字路径, 副本编码名字路径)

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
                with open(file, 'r', encoding=encoding, errors='replace') as f:
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
                    print(f"{index:<5}{str2:<20} {str3:<16} {str1:<10} |||---{find_string}")

                    if needReplace:
                        # 替换字符串
                        for old_str, new_str in zip(old_strings, new_strings):
                            content = content.replace(old_str, new_str)

                        # 将替换后的内容写回文件
                        try:
                            with open(file, 'w', encoding=encoding, errors='replace') as f:
                                f.write(content)
                        except Exception as e:
                            print(f"写入文件 {file} 时发生错误: {e}")


checkFile(specified_directory, needReplace)
