import os
import shutil

# 使用示例
def copy_file_to_folder(source_file, destination_folder):
    """
    将指定的源文件复制到目标文件夹中。
    如果目标文件夹不存在,则会自动创建。
    如果目标文件夹中已存在同名文件,则会覆盖它。
    """
    # 检查目标文件夹是否存在,如果不存在则创建
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    # 获取源文件的文件名
    filename = os.path.basename(source_file)
    # 构建目标文件的完整路径
    destination_file = os.path.join(destination_folder, filename)
    # 将源文件复制到目标文件夹
    shutil.copy2(source_file, destination_file)
    print(f"文件 '{destination_file}' 已被复制到 '{destination_file}'.")
    


def copy_file_to_subfolders(source_file, target_folder):
    for root, dirs, files in os.walk(target_folder):
        for dir in dirs:
            target_dir = os.path.join(root, dir)
            os.makedirs(target_dir, exist_ok=True)
            try:
                shutil.copy(source_file, target_dir)
            except:
                pass

def delete_file_from_subfolders(file_name, target_folder):
    for root, dirs, files in os.walk(target_folder):
        for file in files:
            if file == file_name:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"文件 {file_path} 已删除。")
                except Exception as e:
                    print(f"删除文件 {file_path} 时出错: {e}")


source_file = r'E:\Game\Chd\小草\心月狐\data\Config\A96DC7EFCBAED2C1C8CBA967\a所有本.sc'
target_folder = r'E:\Game\Chd\小草\心月狐\data\Config'
# 复制单个执行脚本到所有角色
copy_file_to_subfolders(source_file, target_folder)
# 删除所有角色的单个执行脚本
file_name = '连体困难.sc'
# delete_file_from_subfolders(file_name, target_folder)
print("执行完毕")

# 复制单个执行脚本到所有角色
# copy_file_to_subfolders('E:\Game\Chd\小草\心月狐\data\Config\D7FAD7FAD7FAD7FAD7FAD0A1BDE3BDE3\连体打泡泡.sc', 'E:\Game\Chd\小草\心月狐\data\Config')
# print("执行完毕")

# 复制某个脚本的配置（是否开门就走。。。）到所有角色
# copy_file_to_subfolders('E:\Game\Chd\小草\心月狐\data\Config\A1E6A5D9A8FDA8FDC2E3D7B0\cda10ab13c9eff4c.lua', 'E:\Game\Chd\小草\心月狐\data\Config')

# 秋水伊人搭配_装备搭配 = "E:\Game\Chd\小草\SNXC\data\Config\A96DC7EFCBAED2C1C8CBA967\diy.suit"
# 裸装 = "E:\Game\Chd\小草\SNXC\data\Config\A1E6A5D9A8FDA8FDC2E3D7B0"
# 酷我音乐 = "E:\Game\Chd\小草\SNXC\data\Config\A1FABFE1CED2D2F4C0D6A1FA"
# 酷狗音乐 = "E:\Game\Chd\小草\SNXC\data\Config\BFE1B9B7D2F4C0D6A8A1"
# 满船清梦压星河 = "E:\Game\Chd\小草\SNXC\data\Config\C2FAB4ACC7E5C3CED1B9D0C7BAD351"
# 能饮一杯无o = "E:\Game\Chd\小草\SNXC\data\Config\C4DCD2FBD2BBB1ADCEDE6F"
# 水澹澹兮生烟 = "E:\Game\Chd\小草\SNXC\data\Config\CBAEE5A3E5A3D9E2C9FAD1CCFE5D"
# 晚来天欲雪o = "E:\Game\Chd\小草\SNXC\data\Config\CDEDC0B4CCECD3FBD1A96F"
# copy_file_to_folder(秋水伊人搭配_装备搭配, 裸装)
# copy_file_to_folder(秋水伊人搭配_装备搭配, 酷我音乐)
# copy_file_to_folder(秋水伊人搭配_装备搭配, 酷狗音乐)
# copy_file_to_folder(秋水伊人搭配_装备搭配, 满船清梦压星河)
# copy_file_to_folder(秋水伊人搭配_装备搭配, 能饮一杯无o)
# copy_file_to_folder(秋水伊人搭配_装备搭配, 水澹澹兮生烟)
# copy_file_to_folder(秋水伊人搭配_装备搭配, 晚来天欲雪o)
