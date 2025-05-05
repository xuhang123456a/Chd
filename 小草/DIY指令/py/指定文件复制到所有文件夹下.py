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
        # print(f"当前正在遍历的目录: {root}")
        # print(f"该目录下的子目录: {dirs}")
        # print(f"该目录下的文件: {files}")
        # print("-" * 50)
        for file in files:
            # 检查文件大小是否为 0 字节
            # 分割文件路径，获取扩展名
            _, extension = os.path.splitext(file)
            #删除空文件
            # if extension == '.lua':
            #     file_path = os.path.join(root, file)
            #     if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
            #         os.remove(file_path)
            #         print(f"空文件 {file_path} 已删除。")
            #删除指定文件
            if file == file_name:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"文件 {file_path} 已删除。")
                except Exception as e:
                    print(f"删除文件 {file_path} 时出错: {e}")


# 删除所有角色的执行脚本
target_folder = r'E:\Game\Chd\小草\心月狐\data\Config\1536622268'
files_name = [
    '98f1b7e516ec6a9a.lua',
    'ad8b2233fe127818.lua',
    '2c38eeecd310a461.lua',
    '6817b81e81d9dd09.lua',
    '7c52c35a1e9a2478.lua',
    'abe1b5494f70eb41.lua',
    '72136dda73cbbb55.lua',
    '997d65f152167b05.lua',
    '84c3f59472b1198a.lua',
    '149fd72a2c9d6dca.lua',
    '21c2b37326c6c16e.lua',
    '0bac2c53fd03a193.lua',
    'a1b48ddb31437933.lua',
    '539623a721c5a1bf.lua',
    '9c07de0cd157fa84.lua',
    'ad5ca3610bcd40ca.lua',
    '7bf7d0bcaf88c40a.lua',
    'f1c87ceee2180828.lua',
    '1a8d682a22d4f1fb.lua',
    'd2419586736b1169.lua',
    '81fdab1ef3eab3af.lua',
    '55bd9ba6bcd62afb.lua',
    'ec2f3ffd0aa8bc41.lua',
    'd7fab05005f7f667.lua',
    '77f0318eca3011b3.lua',
    'd71ff61274354c69.lua',
    'fa682fc33781a2f7.lua',
]
# for file_name in files_name:
#     delete_file_from_subfolders(file_name, target_folder)
# print("执行完毕")

# 复制执行脚本到所有角色
files_name = [
    #补给脚本设置 begin
    # '9d9b1392b8dbef0b.lua',
    # '44cbeb42cd4b1694.lua',
    # '44d490f43fe985aa.lua',
    # '45c1f04cedd8f18e.lua',
    # '846e21921f47d44a.lua',
    # 'a5a29df1c82c5b20.lua',
    # 'ee919f8838a9262c.lua',
    #补给脚本设置 end

    '14bcb0915711d136.lua',#遗迹
    '4f686063e7f76556.lua',#神树
    '74b04b62710052ab.lua',#尼夫
    '54cbda403ac1e8ef.lua',#庭院
    '3884d4a499b541a9.lua',#神笔
    'b24d2a7bcca5b4a6.lua',#忘却
    '98fdd49c1dc42339.lua',#奈落之屋
    'e2baaba053baf0cd.lua',#龙之峡谷
]
filter_name = [

]
source_dir = 'E:\\Game\\Chd\\小草\\心月狐\\data\\Config\\1536622268\\C4DCD2FBD2BBB1ADCEDE6F\\'
target_folder = r'E:\Game\Chd\小草\心月狐\data\Config\1536622268'
for file_name in files_name:
    source_file = os.path.join(source_dir, file_name)
    copy_file_to_subfolders(source_file, target_folder)
print("执行完毕")