#filename : 036_array_change_position.py
#author by : erisecsch

#数组翻转到指定的位置

def leftRotate(arr, d, n): #定义函数1：调用d次函数2
    for i in range(d):
        leftRotatebyOne(arr, n)


def leftRotatebyOne(arr, n): #定义函数2：将第一个元素移至最后
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp


def printArray(arr, size): #定义函数3：将数组元素以数字形式输出
    for i in range(size):
        print("%d" % arr[i], end=" ")


arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2, 7)
printArray(arr, 7)
