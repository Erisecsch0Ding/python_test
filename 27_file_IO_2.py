#filename : 27_file_IO_2.py
#author erisecsch

#文件IO

with open('c:/dgqpy/27_file_IO_2','w+') as f:
    f.write('这是第二个文件')

with open('c:/dgqpy/27_file_IO_2','r') as f:
    str = f.readline()

print(str)