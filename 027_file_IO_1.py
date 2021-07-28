#filename : 027_file_IO_1.py
#author by : erisecsch

#文件IO

f = open('c:/dgqpy/27_file_IO_1','w+') #打开文件
f.write('这是第一个文件') #写文件

f = open('c:/dgqpy/27_file_IO_1','r') #打开文件
str = f.readline() #读文件

print(str)

f.close()

