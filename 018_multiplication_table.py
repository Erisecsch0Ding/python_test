#filename : 018_multiplication_table.py
#author by : erisecsch

#九九乘法表

for i in range(1,10):
    for j in range(1,i+1):
        print('{0}*{1}={2}\t'.format(i,j,i*j),end = '')
    print()
