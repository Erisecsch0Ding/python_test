#filename : factorial.py
#author by erisecsch

#乘阶运算，即n!=1*2*...*n

num = int(input('请输入数字：'))
factorial = 1

if num < 0:
    print('负数没有乘阶')
elif num == 0:
    print('零的乘阶是1')
else:
    for i in range(1,num+1):
        factorial = factorial * i
    print('{}的乘阶是{}'.format(num,factorial))



