import rarfile
from tools import remove_text_before_char

def create_rar_files_dict_with_size(rar_file_path):
    files_dict = {}

    with rarfile.RarFile(rar_file_path, 'r') as rar:
        for file_info in rar.infolist():
            # print(f"File: {file_info.filename}, Size: {file_info.file_size} bytes")
            # 将文件名中每个键中的斜杠 / 替换为反斜杠 \\
            file_name = file_info.filename.replace('/', '\\')
            files_dict[file_name] = file_info.file_size

        return files_dict
# # 指定要解析的RAR文件路径
# rar_file_path = "D:\For_PT\Red Dead Redemption 2.rar"
#
# # 调用函数创建字典
# files_dict = create_rar_files_dict_with_size(rar_file_path)
#
# # 调用函数列出RAR文件结构
# create_rar_files_dict_with_size(rar_file_path)
#
# # 打印字典
# for file, size in files_dict.items():
#     print(f"File: {file}, Size: {size} bytes")