#filename : 037_swaplist.py
#author by : erisecsch

#将列表中的头尾两个元素对调

def swaplist(newlist):
    size = len(newlist)

    temp = newlist[0]
    newlist[0] = newlist[-1]
    newlist[-1] = temp

    return newlist

newlist = [1,2,3,4,5]
print(swaplist(newlist))
