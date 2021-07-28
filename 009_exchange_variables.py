#filename : 009_exchange_variables.py
#author by : erisecsch

#交换变量

x = input("请输入x的值：")
y = input("请输入y的值：")

#创建临时变量temp
temp = x

temp = x
x = y
y = temp

print("交换变量后的x值是：{}".format(x))
print("交换变量后的y值是：{}".format(y))
