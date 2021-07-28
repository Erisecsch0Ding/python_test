#filename : 38_list_change_position.py
#author by : erisecsch

#将列表中的指定位置的两个元素相互调换

def swappositions(newlist,pos1,pos2):

    newlist[pos1],newlist[pos2] = newlist[pos2],newlist[pos1]

    return newlist

newlist = [1,2,3,4,5]
pos1 = 1
pos2 = 3
print(swappositions(newlist,pos1,pos2))