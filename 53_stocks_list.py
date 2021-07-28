import baostock as bs
import pandas as pd
import csv

lg = bs.login()
print('login responderror_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)
data_list = []
csv_file = csv.reader(open('code.csv'))
for stock_list in csv_file:
    print(stock_list)
    for item in stock_list:
        print(item)
        rs =bs.query_stock_basic(code=str(item))
        print('query_stock_basic responderror_code:'+rs.error_code)
        print('query_stock_basicrespond  error_msg:'+rs.error_msg)
        while (rs.error_code == '0') &rs.next():
            data_list.append(rs.get_row_data())
            result = pd.DataFrame(data_list,columns=rs.fields)
            result.to_csv("C:/dgqpy/stock_basic.csv",encoding="gbk", index=False)
            print(result)
bs.logout()

# import baostock as bs
# import pandas as pd
# import csv
#
# lg = bs.login()
# data_list = []
# print('login responderror_code:'+lg.error_code)
# print('login respond  error_msg:'+lg.error_msg)
# with open('code.csv') as cvsvfile:
#     stock_list = csv.reader(cvsvfile)
#     for line in cvsvfile:
#         item = line.strip()
#         rs = bs.query_stock_basic(code=item)
#         print('query_stock_basic responderror_code:'+rs.error_code)
#         print('query_stock_basicrespond  error_msg:'+rs.error_msg)
#
#         while (rs.error_code == '0') &rs.next():
#             data_list.append(rs.get_row_data())
#         result = pd.DataFrame(data_list,columns=rs.fields)
#         result.to_csv("stock_basic.csv",encoding="gbk", index=False)
#         print(result)
# bs.logout()