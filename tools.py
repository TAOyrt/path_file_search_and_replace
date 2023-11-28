import os
import shutil
import json
import sys

# 替换文件路径
def remove_text_before_char(input_string, target_char):
    # 使用 find 方法找到目标字符的位置
    char_position = input_string.find(target_char)

    # 如果找到目标字符，返回该位置之后的部分；否则返回原始字符串
    return input_string[char_position:] if char_position != -1 else input_string

# 示例
# input_string = "some_text_to_remove:remaining_text"
# target_char = "me"
#
# result = remove_text_before_char(input_string, target_char)
# print(result)


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

# 复制文件
def file_copy(dict, folder_path, game_name):
    for file, size in dict.items():
        source_file_path = folder_path+ file.removeprefix(game_name) # .removeprefix删除前缀
        destination_file_path = folder_path + "_bk" + file.removeprefix(game_name)
        #print(f"{source_file_path}\n{destination_file_path}")
        # 创建目标目录的上层目录
        os.makedirs(os.path.dirname(destination_file_path), exist_ok=True)
        # 使用 shutil 模块的 copy2 函数复制文件
        try:
            shutil.copy2(source_file_path, destination_file_path)
            print(f"文件复制成功：{destination_file_path}")
        except Exception as e:
            print(f"文件复制失败：{str(e)}")

# 写log
def log_writting(log_file_path, log_name, dict_for_log):
    # Create the log folder if it doesn't exist
    os.makedirs(log_file_path, exist_ok=True)

    # # Configure logging to write to the log file
    # log_file_name = log_file_path + "\\" + log_name + ".log"
    # print(log_file_name)
    # logging.basicConfig(filename=log_file_name , level=logging.INFO)

    # 将字典转换为JSON格式的字符串
    json_data = json.dumps(dict_for_log, indent=4)

    # Write the JSON data to a text file
    txt_file_name = os.path.join(f"{log_file_path}\\{log_name}.txt")
    with open(txt_file_name, 'w') as txt_file:
        txt_file.write(json_data)

    # Change the file extension to .log
    log_file_name = os.path.join(log_file_path, f"{log_name}.log")
    os.rename(txt_file_name, log_file_name)

    print(f"Dictionary logged to '{log_file_name}'.")

# log_file_path = r"D:\Software\Games\Game\The Last of Us Part I v1.1.2_bk"
# dict1 = {"key1": "value1", "key2": "value2"}
# log_writting(log_file_path,"888",dict1)
