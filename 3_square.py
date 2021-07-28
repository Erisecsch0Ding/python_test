#filename : 3_square_root.py
#author by : erisecsch

#输入一个数字后，求平方根

num = float(input("请输入一个数字："))
num_square_root = num ** 0.5 #实数开平方根
print("%.3f 的平方根是 %.3f"%(num,num_square_root))

#"%"即后者的替身引用
#例如：print("%.2f"%a),则代表先传递a到前面的表达式（"%.2f"）中(取2位小数点)，再输出该表达式的值
#如果a = 2.3897,运行结果是 a = 2.39
