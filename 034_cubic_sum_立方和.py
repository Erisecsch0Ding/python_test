#filename : 034_cubic_sum_立方和.py
#author by : erisecsch

#立方和

def cubic_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**3
    return sum

n = 10
print('0到{0}的立方和是{1}'.format(n,cubic_sum(n)))
