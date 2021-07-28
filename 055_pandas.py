import pandas as pd
import data

# test 1 用‘list’列表创建一维数组的内容和index
x = [11,22,33,44,55,66,77,88,99]
datas = [20200101,20200102,20200103,20200104,20200105,20200106,20200107,20200108,20200109]
s1 = pd.Series(x,index=datas)
s1.name = '数组'
print(s1)

# test 2 用‘dict’字典创建一维数组的内容和index
text_dict = {'BABA':11,'PDD':22,'JD':33,'BIDU':44}
s2 = pd.Series(text_dict,name='中概股')
print(s2)
