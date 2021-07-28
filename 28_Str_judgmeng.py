#filename : 28_a_judgment.py
#author by : erisecsch

#字符串判断

#测试实例一

print('测试实例一')
a = 'python.org'
print(a.isalnum()) #判断字符串是否都是数字或者字母
print(a.isalpha()) #判断字符串是否都是字母
print(a.isdigit()) #判断字符串是否都是数字
print(a.islower()) #判断字符串是否都是小写
print(a.isupper()) #判断字符串是否都是大写
print(a.istitle()) #判断字符串是否都是首字母大写，像标题
print(a.isspace()) #判断字符串是否都是空白字符，\t,\n,\r

#测试实例二

print('测试实例二')
a = 'python'
print(a.isalnum())
print(a.isalpha())
print(a.isdigit())
print(a.islower())
print(a.isupper())
print(a.isspace())
print(a.istitle())