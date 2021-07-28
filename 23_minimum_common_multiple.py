#filename : 23_minimum_common_multiple.py
#author by : erisecsch

#最小公倍数算法

def lcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    return lcm

num1 = int(input('请输入第一个数字：'))
num2 = int(input('请输入第二个数字：'))
print('{0}跟{1}的最小公约数是{2}'.format(num1,num2,lcm(num1,num2)))