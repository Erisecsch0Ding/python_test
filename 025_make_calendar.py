#filename : 025_make_calendar.py
#author : erisecsch

#生成日历

import calendar

yy = int(input('输入年份：'))
mm = int(input('输入月份：'))

print(calendar.month(yy,mm))
