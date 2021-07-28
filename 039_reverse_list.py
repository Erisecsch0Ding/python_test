#filename : 039_reverse_list.py
#author by : erisecsch

#翻转列表

#方法一
def reverse1(newlist):
    newlist_one = [i for i in reversed(newlist)]
    return newlist_one

newlist = [1,2,3,4,5]
a = reverse1(newlist)
print(a)

#方法二
def reverse2(newlist):
    newlist_two = newlist[::-1]
    return newlist_two

newlist = [1,2,3,4,5]
b = reverse2(newlist)
print(b)
