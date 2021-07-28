#filename : 31_get_yesterday_date.py
#author by : erisecsch

#获取昨天的日期

import datetime
def getyesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days = 1)
    yesterday = today - oneday
    return yesterday

print(getyesterday())