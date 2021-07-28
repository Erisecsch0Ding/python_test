#filename : 012_Parity_check.py
#author by : erisecsch

#奇偶校验
# 偶数除以2的余数是0
# 奇数除以2的余数是1

num = int(input('请输入要校验的数字：'))
if (num%2) == 0:
    print('{}是偶数'.format(num))
else:
    print('{}是奇数'.format(num))
