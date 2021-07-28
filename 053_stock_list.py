import baostock as bs
import pandas as pd

lg = bs.login()
print('login responderror_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)
rs =bs.query_stock_basic(code="sh.600000")
print('query_stock_basic responderror_code:'+rs.error_code)
print('query_stock_basicrespond  error_msg:'+rs.error_msg)
data_list = []
while (rs.error_code == '0') &rs.next():
   data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list,columns=rs.fields)
result.to_csv("C:/dgqpy/stock_basic.csv",encoding="gbk", index=False)
print(result)
bs.logout()
