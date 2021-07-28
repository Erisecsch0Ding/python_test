#filename : 042_copy_list.py
#author by : erisecsch

#复制列表

#方法一：直接复制
def copy_list_1(nowlist):
    nowlist_copy = nowlist[:]
    return nowlist_copy

li1 = [1,2,3,4,5]
li2 = copy_list_1(li1)
print('原始列表：',li1)
print('复制后的列表:',li2)
print('----------')

#方法二：创建空的list，然后扩展
def copy_list_2(list):
    list_two = []
    list_two.extend(list)
    return list_two

li1 = [1,2,3,4,5]
li2 = copy_list_2(li2)
print('原始列表：',li1)
print('复制后的列表：',li2)
print('----------')
