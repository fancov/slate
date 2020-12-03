#! /usr/bin/python3

# 寻找字符串，如果dir_a/file 在index.html.md中，那么就不用做多余动作

# 如果dir_a/file 不在index.html.md中
  # 如果dir_a 在index.html.md中，就添加到最后一个含有dir_a行的下面
  # 如果dir_a 不在 index.html.md中，就添加到error行的前面


## 问题1，如果想把某个md文件插入到特定位置，要怎么配置。目前只能做到新文件往旧文件后面添加，
# 如果要指定顺序，需要增加配置

import os

include_path = "includes"

include_str_l = []

# 目前只支持目录，根据需求可增加文件
for file_name in os.listdir(include_path):
    if os.path.isdir(os.path.join(include_path, file_name)):
        dir_name = file_name
        dir_path = os.path.join(include_path, file_name)
        for sub_file_name in os.listdir(dir_path):
            file_basename = os.path.splitext(sub_file_name)[0].strip('_')
            include_str_l.append(f'{dir_name}/{file_basename}')

main_file_name = 'index.html.md'

with open(main_file_name, encoding='utf-8') as f:
    file_content = f.read()
    f.seek(0)
    lines = f.readlines()


def find_match_index_num(match_str, pos=0):
    match_index = -1
    for index, line in enumerate(lines):
        if match_str in line:
            match_index = index

    return match_index + pos


for include_str in include_str_l:
    if include_str in file_content:
        continue

    dir_name = include_str.split('/')[0]
    if dir_name + '/' in file_content:
        match_index = find_match_index_num(dir_name+'/', pos=1)
        lines.insert(match_index, f'  - {include_str}\n')
    else:
        match_index = find_match_index_num('errors')
        lines.insert(match_index, f'  - {include_str}\n')

with open('index.html.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)
