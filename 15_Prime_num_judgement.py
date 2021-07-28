#filename : 15_Prime_num_judgement.py
#author : erisecsch

#质数判断


i = 0

while True:
    i += 1

    if i < 5: #循环5次
        num = int(input('请输入一个数字'))
        if num > 1:
            for i in range(2, num):  # 遍历因子
                if (num % i) == 0:
                    print('{}不是质数'.format(num))
                    print(i, '乘以', num // i, '是', num)
                    break
            else:
                print('{}是质数'.format(num))
        elif num == 1:
            print('不是质数')
    else:
        break


