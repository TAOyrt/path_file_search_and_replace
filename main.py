import os
import shutil
from for_file import create_files_dict_with_size
from for_rar import create_rar_files_dict_with_size
from for_zip import create_zip_files_dict_with_size
from tools import compare_dicts
from tools import file_copy
from tools import log_writting

game_name = "The Last of Us Part I v1.1.2"
# 指定要遍历的文件夹路径
folder_path = r"D:\Software\Games\Game\The Last of Us Part I v1.1.2"
# 指定要解析的RAR文件路径
compressed_file_path = r"D:\Software\Games\Game\最后生还者重制版 豪华中文 v1.1.2+全DLC+学习补丁合集+全解锁存档+修改器+赠品 支持手柄 解压即玩\The Last of Us Part I v1.1.2.zip"

# 判断压缩文件格式
compressed_type = compressed_file_path.rsplit(".",1)[1]
if compressed_type == "rar":
    create_compressed_files_dict_with_size = create_rar_files_dict_with_size
elif compressed_type == "zip":
    create_compressed_files_dict_with_size = create_zip_files_dict_with_size
# 调用函数创建字典
files_dict = create_files_dict_with_size(folder_path, game_name)
compressed_files_dict = create_compressed_files_dict_with_size(compressed_file_path)
file_diff_dict, file_missing_dict, file_adding_dict = compare_dicts(compressed_files_dict, files_dict)
info_dict = {"files":len(files_dict),
             "compressed_files":len(compressed_files_dict),
             "file_diff":len(file_diff_dict),
             "file_missing":len(file_missing_dict),
             "file_adding":len(file_adding_dict)}

print(f"files_dict:              {len(files_dict):<}\n"
      f"compressed_files_dict:   {len(compressed_files_dict):<}\n"
      f"file_diff_dict:          {len(file_diff_dict):<}\n"
      f"file_missing_dict:       {len(file_missing_dict):<}\n"
      f"file_adding_dict:        {len(file_adding_dict):<}")

# 使用 copy2 函数复制文件
# if file_diff_dict:
#     file_copy(file_diff_dict,folder_path,game_name)
# if file_adding_dict:
#     file_copy(file_adding_dict,folder_path,game_name)

# 写log
log_file_path = folder_path + "_bk"
log_writting(log_file_path,"0.info",info_dict)
log_writting(log_file_path,"1.files",files_dict)
log_writting(log_file_path,"2.compressed_files",compressed_files_dict)
log_writting(log_file_path,"3.file_diff",file_diff_dict)
log_writting(log_file_path,"4.file_missing",file_missing_dict)
log_writting(log_file_path,"5.file_adding",file_adding_dict)

