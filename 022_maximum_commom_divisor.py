#filename : 022_masimum_common_divisor.py
#author by : erisecsch

#最大公约数算法

def hcf(x,y):
    if x > y :
        smaller = y
    else:
        smaller = x

    for i in range (1,smaller+1) :
        if (x % i == 0) and (y % i == 0) :
            hcf = i
    return hcf

num1 = int(input('请输入第一个数字：'))
num2 = int(input('请输入第二个数字：'))

print('{0}和{1}的最大公约数是{2}'.format(num1,num2,hcf(num1,num2)))
