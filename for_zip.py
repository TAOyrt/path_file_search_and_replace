import zipfile
from tools import remove_text_before_char

def create_zip_files_dict_with_size(zip_file_path):
    files_dict = {}

    with zipfile.ZipFile(zip_file_path, 'r') as zip:
        for file_info in zip.infolist():
            # print(f"File: {file_info.filename}, Size: {file_info.file_size} bytes")
            # 将文件名中每个键中的斜杠 / 替换为反斜杠 \\
            file_name = file_info.filename.replace('/', '\\')
            files_dict[file_name] = file_info.file_size

        return files_dict
# # 指定要解析的ZIP文件路径
# zip_file_path = r"D:\Software\Games\Game\最后生还者重制版 豪华中文 v1.1.2+全DLC+学习补丁合集+全解锁存档+修改器+赠品 支持手柄 解压即玩\The Last of Us Part I v1.1.2.zip"
#
# # 调用函数创建字典
# files_dict = create_zip_files_dict_with_size(zip_file_path)
#
# # 调用函数列出zip文件结构
# create_zip_files_dict_with_size(zip_file_path)
#
# # 打印字典
# for file, size in files_dict.items():
#     print(f"File: {file}, Size: {size} bytes")