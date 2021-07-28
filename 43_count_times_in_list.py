#filename : 43_count_times_in_list.py
#author by : erisecsch

#统计某元素出现的次数

#方法一
def countx_1(list,x):
    count_num = 0
    for i in list:
        if (i == x):
            count_num += 1
    return count_num

li = [1,1,2,2,3,4,4,4,4,55,6,7,8,99]
a = 4
print(countx_1(li,a))
print('----------')

#方法二
def countx_2(list,x):
    return list.count(x)

li = [1,1,2,2,3,4,4,4,4,55,6,7,8,99]
a = 4
print(countx_1(li,a))
print('----------')