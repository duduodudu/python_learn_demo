import os
import re


# 去除 AV 号
def rename():
    path = '.'
    dirs = os.listdir(path)
    for file in dirs:
        # 匹配(AV P)
        ad = re.search(r'[(]Av.*,P.*[)]', file)
        if ad:
            print('匹配的内容:', ad.group())
            old_file_path = os.path.join(path, file)
            new_file_path = os.path.join(path, file.replace(ad.group(), ''))
            print('old', old_file_path)
            print('new', new_file_path)
            # 重命名
            # os.rename(old_file_path,new_file_path)
        #
        # 去除重复的数字
        no = re.search(r'^\d{1,3}[.]', file)
        if no:
            print('匹配的内容', no.group())
            old_file_path = os.path.join(path, file)
            new_file_path = os.path.join(path, file.replace(no.group(), ''))
            print('old', old_file_path)
            print('new', new_file_path)
            # os.rename(old_file_path,new_file_path)
        pass


if __name__ == '__main__':
    rename()
