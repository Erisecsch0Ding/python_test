#filename : 24_simple_calculate.py
#author by : erisecsch

#简易计算器

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multipliy(x,y):
    return x*y

def divide(x,y):
    return x/y

print('选择功能：')
print('1:加法；\n2:减法；\n3:乘法；\n4:除法；\n')

choice = int(input('请输入你的选择（1/2/3/4）:'))

num1 = float(input('请输入第一个数字：'))
num2 = float(input('请输入第二个数字：'))

if choice == 1:
    print(num1,'+',num2,'=',add(num1,num2))
elif choice == 2:
    print(num1,'-',num2,'=',subtract(num1,num2))
elif choice == 3:
    print(num1,'*',num2,'=',multipliy(num1,num2))
elif choice == 4:
    print(num1,'/',num2,'=',divide(num1,num2))
else:
    print('输入不合法')