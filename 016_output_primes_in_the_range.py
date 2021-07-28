#filename : 016_output_primes_in_the_range.py
#author by : erisecsch

#输出指定范围内的素数

lower = int(input('范围最小值：'))
upper = int(input('范围最大值：'))

for num in range(lower,upper+1): #遍历范围内每个数，并赋值给num
    if num > 1:
        for i in range(2,num): #遍历（2-num），并赋值给i
            if (num % i) == 0: #校验 num 是否能被 i 整除（即检查num是否是素数）
                break
        else: #输入2时，直接跳入else；输入大于2时，经过if检验后，再进入else
            print(num)
