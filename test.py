import os
import rarfile
import shutil

def create_files_dict_with_size(startpath):

    files_dict = {}

    for root, dirs, files in os.walk(startpath):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)

            file_path = file_path[23:]
            #print(f"File: {file_path}, Size: {file_size} bytes")
            files_dict[file_path] = file_size
    return files_dict

def create_rar_files_dict_with_size(rar_file_path):
    files_dict = {}

    with rarfile.RarFile(rar_file_path, 'r') as rar:
        for file_info in rar.infolist():
            # 将文件名中每个键中的斜杠 / 替换为反斜杠 \\
            file_name = file_info.filename.replace('/', '\\')
            files_dict[file_name] = file_info.file_size

        return files_dict


# 文件夹改变的放在file_diff_dict，缺失的放在file_missing_dict
def compare_dicts(origin_dict, used_dict):
    file_diff_dict = {}
    file_missing_dict = {}
    file_adding_dict = {}

    # 比较两个字典的键和值
    for key in origin_dict:
        if key in used_dict:
            if used_dict[key] != origin_dict[key]:
                file_diff_dict[key] = used_dict[key]
        else:
            file_missing_dict[key] = origin_dict[key]
    for key in used_dict:
        if key not in origin_dict:
            file_adding_dict[key] = used_dict[key]

    return file_diff_dict, file_missing_dict, file_adding_dict


# 指定要遍历的文件夹路径
folder_path = r"D:\Software\Games\Game\Red Dead Redemption 2"
# 指定要解析的RAR文件路径
rar_file_path = "D:\For_PT\Red Dead Redemption 2.rar"

# 调用函数创建字典
files_dict = create_files_dict_with_size(folder_path)
rar_files_dict = create_rar_files_dict_with_size(rar_file_path)
file_diff_dict, file_missing_dict, file_adding_dict = compare_dicts(rar_files_dict, files_dict)

# print(files_dict)
# print(rar_files_dict)
print("Different Files:")
if file_diff_dict:
    for file, size in file_diff_dict.items():
        print(f"File: {file}, Size: {size} bytes")

print("\nMissing Files:")
if file_missing_dict:
    for file, size in file_missing_dict.items():
        print(f"File: {file}, Size: {size} bytes")

print("\nAdding Files:")
if file_adding_dict:
    for file, size in file_adding_dict.items():
        print(f"File: {file}, Size: {size} bytes")
print(len(files_dict), len(rar_files_dict), len(file_diff_dict), len(file_missing_dict), len(file_adding_dict))


# 使用 copy2 函数复制文件
if file_adding_dict:
    for file, size in file_adding_dict.items():
        source_file_path = folder_path + file[21:]
        destination_file_path = folder_path.replace("Red Dead Redemption 2", "Red Dead Redemption 2_bk") + file[21:]
        # 创建目标目录的上层目录
        os.makedirs(os.path.dirname(destination_file_path), exist_ok=True)
        # 使用 shutil 模块的 copy2 函数复制文件
        try:
            shutil.copy2(source_file_path, destination_file_path)
            print(f"文件复制成功：{destination_file_path}")
        except Exception as e:
            print(f"文件复制失败：{str(e)}")


