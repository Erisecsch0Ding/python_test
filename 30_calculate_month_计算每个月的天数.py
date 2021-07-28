#filename : 30_calculate_month_计算每个月的天数.py
#author by : erisecsch

#计算每个月的天数

import calendar

yy = int(input('年份：'))
mm = int(input('月份：'))

monthrange = calendar.monthrange(yy,mm)

print(monthrange) #输出一个元祖（tulpe），第一个元素是所查月份的第一天对应的星期几（0-6），第二个对应的是这个月的天数。
