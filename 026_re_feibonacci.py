#filename : 026_re_feibonacci.py
#author by : erisecsch

#递归函数输出斐波那契数列

#构建递归函数体
def re_feibonacci(n):
    if n <= 1:
        return n
    else:
        return (re_feibonacci(n-1)+re_feibonacci(n-2))

nterms = int(input('你要输出几项：'))

if nterms <= 0:
    print("输入正数")
else:
    print("feibonacci")
    for i in range(nterms):
        print(re_feibonacci(i))
