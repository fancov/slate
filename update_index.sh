#! /bin/bash

# 遍历目录，生成目录与文件名的组合字符串如 dir_a/file_b
# shellcheck disable=SC2006
path=`pwd`/includes
file_list=`ls "$path"`

declare -a file_str_list
for file_name in $file_list:
do
  sub_path=$path/$file_name

    if [ -d "$sub_path" ]
    then
      sub_file_list=`ls "$sub_path"`
      for sub_file in $sub_file_list:
      do
        echo "$sub_file"
        filename=${sub_file%.*}
        file_str_list[0]="  -includes/$filename"
      done

    fi
done


for file_str in ${file_str_list[*]}
do
        echo "$file_str"
done


sed -i '' "1 a ${file_str_list[0]}" index.html.md


# 寻找字符串，如果dir_a/file 在index.html.md中，那么就不用做多余动作

# 如果dir_a/file 不在index.html.md中
  # 如果dir_a 在index.html.md中，就添加到最后一个含有dir_a行的下面
  # 如果dir_a 不在 index.html.md中，就添加到error行的前面


## 问题1，如果想把某个md文件插入到特定位置，要怎么配置。目前只能做到新文件往旧文件后面添加，
# 如果要指定顺序，需要增加配置
