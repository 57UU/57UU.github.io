import os
import argparse

def replace_html_content(directory, source_file):
    # 验证目标目录是否存在
    if not os.path.isdir(directory):
        print(f"错误：目录 '{directory}' 不存在")
        return False

    # 验证源文件是否存在
    if not os.path.isfile(source_file):
        print(f"错误：源文件 '{source_file}' 不存在")
        return False

    path=source_file
    # 读取源文件内容（二进制模式）
    try:
        with open(source_file, 'rb') as f:
            source_content = f.read()
    except Exception as e:
        print(f"读取源文件失败：{e}")
        return False

    # 计数器
    processed_files = 0

    # 递归遍历目录
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # 检查文件扩展名（不区分大小写）
            if filename.lower().endswith(('.html', '.htm')):
                file_path = os.path.join(root, filename)
                try:
                    # 写入新内容（二进制模式）
                    with open(file_path, 'wb') as f:
                        f.write(source_content)
                    processed_files += 1
                    print(f"已更新：{file_path}")
                except Exception as e:
                    print(f"更新失败 [{file_path}]: {e}")

    print(f"\n操作完成！共处理了 {processed_files} 个文件")
    return True

if __name__ == "__main__":
    # 设置命令行参数
    parser = argparse.ArgumentParser(
        description='递归替换目录中所有HTML文件内容',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        'directory',
        help='要处理的根目录路径'
    )
    parser.add_argument(
        'source_file',
        help='用作替换内容的HTML文件路径'
    )

    # 解析参数
    args = parser.parse_args()

    # 执行替换操作
    replace_html_content(args.directory, args.source_file)