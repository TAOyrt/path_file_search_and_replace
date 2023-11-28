import shutil

# 指定源文件和目标文件路径
source_file_path = "path/to/source/file.txt"
destination_file_path = "path/to/destination/file.txt"

# 使用 copy2 函数复制文件
shutil.copy2(source_file_path, destination_file_path)

print(f"文件复制成功：{destination_file_path}")

