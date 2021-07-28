#filename : 040_element_judge_isin.py
#author by : erisecsch

#判断元素是否在列表中存在

root_list = [1,2,3,4,5,6,7,8,9]

#方法一：使用for循环
for i in root_list:
    if i == 4:
        print('存在')

print('----------')

#方法二：使用in
if (4 in root_list):
    print('存在')
else:
    print('不存在')
print('----------')



