#filename : 10_judging_num
#author by : erisecsch

#输入一个数字后，判断是正数、负数或零

a = float(input("输入数字："))

#判断
if a > 0:
  print("{}是正数".format(a))
elif a == 0:
  print("{}是零".format(a))
else:
  print("{}是负数".format(a))
