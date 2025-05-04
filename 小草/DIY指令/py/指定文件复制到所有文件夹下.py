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
            # 检查文件大小是否为 0 字节
            file_path = os.path.join(root, file)
            # 分割文件路径，获取扩展名
            root, extension = os.path.splitext(file_name)
            if extension == '.lua' and os.path.isfile(file_path):
                if os.path.getsize(file_path) == 0:
                    os.remove(file_path)
                    print(f"空文件 {file_path} 已删除。")
                if file == file_name:
                    try:
                        os.remove(file_path)
                        print(f"文件 {file_path} 已删除。")
                    except Exception as e:
                        print(f"删除文件 {file_path} 时出错: {e}")


# 删除所有角色的执行脚本
target_folder = r'E:\Game\Chd\小草\心月狐\data\Config\3387891881'
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
]
for file_name in files_name:
    delete_file_from_subfolders(file_name, target_folder)

print("执行完毕")

# 复制执行脚本到所有角色
files_name = [
    #补给脚本设置 begin
    '9d9b1392b8dbef0b.lua',
    '44cbeb42cd4b1694.lua',
    '44d490f43fe985aa.lua',
    '45c1f04cedd8f18e.lua',
    '846e21921f47d44a.lua',
    'a5a29df1c82c5b20.lua',
    'ee919f8838a9262c.lua',
    #补给脚本设置 end
]
# source_file = r'E:\Game\Chd\小草\心月狐\data\Config\A96DC7EFCBAED2C1C8CBA967\a所有本.sc'
# source_dir = 'E:\\Game\\Chd\\小草\\心月狐\\data\\Config\\1536622268\\CDEDC0B4CCECD3FBD1A96F\\'
# target_folder = r'E:\Game\Chd\小草\心月狐\data\Config\1536622268'
# for file_name in files_name:
#     source_file = os.path.join(source_dir, file_name)
#     copy_file_to_subfolders(source_file, target_folder)
# print("执行完毕")