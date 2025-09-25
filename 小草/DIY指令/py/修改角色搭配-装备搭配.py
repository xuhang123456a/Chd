import os
import json
import os
from pathlib import Path
from src.utils.tools import read_json_file, save_json_file

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


# 示例修改函数，将 "name" 字段的值修改为 "New Name"
def diysuit_modification(data, target_data):
    if 'diysuit_item' in target_data:
        target_data['diysuit_item'] = data
    return target_data

# 获取脚本所在目录
script_dir = Path(__file__).parent.resolve()
file_path = script_dir / "搭配-装备搭配.txt"
json_content = read_json_file(file_path)
target_path = script_dir.parent.parent / "心月狐" / "data" / "Config" 
target_files_path = [
    # ["﹎秋水伊人ゞ", "1536622268\\A96DC7EFCBAED2C1C8CBA967"],
    # ["晚来天欲雪o", "1536622268\\CDEDC0B4CCECD3FBD1A96F"],
    # ["小姐姐", "1536622268\\D7FAD7FAD7FAD7FAD7FAD0A1BDE3BDE3"],
    # ["云青青兮欲雨", "1536622268\\D4C6C7E0C7E0D9E2D3FBD3EAFE5D"],
    # ["满船清梦压星河Q", "1536622268\\C2FAB4ACC7E5C3CED1B9D0C7BAD351"],
    # ["能饮一杯无o", "1536622268\\C4DCD2FBD2BBB1ADCEDE6F"],
    # ["醉后不知天在水o", "1536622268\\D7EDBAF3B2BBD6AACCECD4DACBAE6F"],
    # ["→酷我音乐→", "1536622268\\A1FABFE1CED2D2F4C0D6A1FA"],
    # ["酷狗音乐ā", "1536622268\\BFE1B9B7D2F4C0D6A8A1"],
    # ["℃ベ裸装", "1536622268\\A1E6A5D9A8FDA8FDC2E3D7B0"],
    # ["终不似o", '1536622268\\D6D5B2BBCBC66F'],
    # ["最是人间留不住o", "1536622268\\D7EECAC7C8CBBCE4C1F4B2BBD7A16F"],
    # ["水澹澹兮生烟", "1536622268\\CBAEE5A3E5A3D9E2C9FAD1CCFE5D"],
    # ["少年游o", "1536622268\\C9D9C4EAD3CE6F"],

    # ["你到底吻不吻我o", "3387891881\\C4E3B5BDB5D7CEC7B2BBCEC7CED26F"],
    # ["来去荒芜", "3387891881\\C0B4C8A5BBC4CEDF"],
    # ["不要碰我肩膀", "3387891881\\B2BBD2AAC5F6CED2BCE7B0F2"],
    # ["逾白","3387891881\\D3E2B0D7FE5D"],
    # ["陌辰","3387891881\\C4B0B3BD"],
    # ["我有药", "3387891881\\CED2D3D0D2A9"],
    # ["惊觉","3387891881\\BEAABEF5FE5D"],
    # ["乙骨犹太","3387891881\\D2D2B9C7D3CCCCAB"],
    # ["心缩","3387891881\\D0C4CBF5"],
    # ["鸦九","3387891881\\D1BBBEC5"],
    # ["烟雨情相思","3387891881\\D7FAD1CCD3EAC7E9CFE0CBBCD7FA"],
    # ["荼茶","3387891881\\DDB1B2E8"],
    # ["莫吵","3387891881\\C4AAB3B3"],
    # ["无心梦","3387891881\\CEDED0C4C3CE"],

    # ["自然萌ご", "3476670590\\D7FCD7FCD7D4C8BBC3C8A4B4D7FC"],
    ["十八岁青春男高", "3476670590\\CAAEB0CBCBEAC7E0B4BAC4D0B8DF"],
    ["雪绒薄荷ご", "3476670590\\D7FCD7FCD1A9C8DEB1A1BAC9A4B4"],
    ["傻海我们走~", "3476670590\\C9B5BAA3CED2C3C7D7DF7E"],
    ["BaLl,", "3476670590\\42614C6C2C"],
    ["蓝莓ご", "3476670590\\D7FCD7FCC0B6DDAEA4B4"],
    ["萌萌仓库-格挡","3476670590\\C3C8C3C8B2D6BFE22DB8F1B5B2"],
    ["萌萌仓库-爆率","3476670590\\C3C8C3C8B2D6BFE22DB1ACC2CA"],
    ["芝士羊绒ご","3476670590\\D7FCD7FCD6A5CABFD1F2C8DEA4B4"],
    ["雪绒蓝莓ご","3476670590\\D7FCD7FCD1A9C8DEC0B6DDAEA4B4"],

    # ["山有木兮卿有意", "1578659491\\C9BDD3D0C4BED9E2D7FCC7E4D3D0D2E2"],
    # ["糯米Nomi", "1578659491\\D7FCC5B4C3D7D7FC4E6F6D69D7FC"],
    # ["秋意也泛舟", "1578659491\\C7EFD2E2D2B2B7BAD6DB"],
    # ["若惊鸿一梦", "1578659491\\C8F4BEAABAE8D2BBC3CE"],
    # ["弥猫深巷離人心", "1578659491\\C3D6C3A8C9EECFEFD7FCEB78C8CBD0C4"],
    # ["玫瑰花的梦", "1578659491\\C3B5B9E5BBA8B5C4C3CE"],
    # ["诉萌", "1578659491\\CBDFC3C8"],
    # ["龙卷风摧毁停車场", "1578659491\\C1FABEEDB7E7B4DDBBD9CDA3DC87B3A1"],
]
for target_file_path in target_files_path:
    target_file_path = os.path.join(target_path, target_file_path[1])
    target_file_path = os.path.join(target_file_path, 'Config.save')
    target_json_content = read_json_file(target_file_path)
    if json_content:
        # 修改 JSON 数据
        modified_json = modify_json_data(json_content,target_json_content, diysuit_modification)
        if modified_json:
            # 保存修改后的 JSON 文件
            save_json_file(target_file_path, modified_json, 'gbk')