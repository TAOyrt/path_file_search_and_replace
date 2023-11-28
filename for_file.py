import os

# def list_files(startpath):
#     for root, dirs, files in os.walk(startpath):
#         level = root.replace(startpath, '').count(os.sep)
#         indent = ' ' * 4 * (level)
#         print('{}{}/'.format(indent, os.path.basename(root)))
#         subindent = ' ' * 4 * (level + 1)
#         for file in files:
#             print('{}{}'.format(subindent, file))
#
# # 指定要遍历的文件夹路径
# folder_path = r"D:\Software\Games\Game\Red Dead Redemption 2"
#
# # 调用函数列出文件结构
# list_files(folder_path)

def list_files_with_size(startpath):

    files_dict = {}

    for root, dirs, files in os.walk(startpath):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)

            file_path = file_path[23:]
            #print(f"File: {file_path}, Size: {file_size} bytes")
            files_dict[file_path] = file_size
    return files_dict

# 指定要遍历的文件夹路径
folder_path = r"D:\Software\Games\Game\Red Dead Redemption 2"

# 调用函数创建字典
files_dict = list_files_with_size(folder_path)

# 打印字典
for file, size in files_dict.items():
    print(f"File: {file}, Size: {size} bytes")

# 调用函数列出文件结构及大小
#list_files_with_size(folder_path)