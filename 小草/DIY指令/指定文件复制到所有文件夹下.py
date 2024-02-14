import os
import shutil

def copy_file_to_subfolders(source_file, target_folder):
    for root, dirs, files in os.walk(target_folder):
        for dir in dirs:
            target_dir = os.path.join(root, dir)
            os.makedirs(target_dir, exist_ok=True)
            try:
                shutil.copy(source_file, target_dir)
            except:
                pass

# Call the function to perform the copy operation
copy_file_to_subfolders('D:\Program Files (x86)\Chd\Chd\小草\SNXC\data\Config\A1E6A5D9A8FDA8FDC2E3D7B0\家族本.sc', 'D:\Program Files (x86)\Chd\Chd\小草\SNXC\data\Config')