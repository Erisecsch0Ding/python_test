#filename : 032_list_common_operations.py
#author by : erisecsch

#list的常规操作

#list的定义
print('list的定义')
li = [1,2,3,'a','b','c']
print(li)
print('----------')

#list的索引、切片
print('list的索引、切片')
print(li[1]) #输出第二个元素
print(li[-1]) #输出倒数第一个元素
print(li[1:3]) #切片，输出第2个元素到第3个元素的list
print(li[1:-1]) #切片，输出第2个元素到最后一个元素的list
print('----------')

#list的增加元素
print('list的增加元素')
li.append('d') #增加单个元素
print(li)
li.insert(0,'first') #增加元素到指定位置
print(li)
li.extend(['e','f','g']) #添加list
print(li)
print('---------')

#list的搜索
print('list的搜索')
print(li.index('first')) #根据元素查询其索引
print('----------')

#list的删除
print('list的删除')
li.remove('first') #如果有两个‘first',则删除首个
print(li)
print(li.pop()) #pop()会删除list最后一个元素，并返回删除元素的值
print(li)
print('----------')

#list的运算符
print('list的运算符')
li = li + ['one','two','three']
print(li)
li += ['four']
print(li)
li = li * 3
print(li)
print('----------')

#使用join链接list,成为字符串
print('使用join链接list,成为字符串')
d1 = {'name':'annie','age':'six','location':'hangzhou'}
l1 = ['%s=%s'%(k,v) for k,v in d1.items()]
l2 = ['{0}={1}'.format(k,v) for k,v in d1.items()]
print(l1)
print(l2)
l1_j = ';'.join(l1)
l2_j = '/'.join(l2)
print(l1_j)
print(l2_j)
print('----------')

#用split将一个字符串分割成多元素 list
print('用split将一个字符串分割成多元素 list')
l1_j_s = l1_j.split(';') #全部分割
l2_j_s = l2_j.split('/',1) #只分割一次
print(l1_j_s)
print(l2_j_s)
print('----------')

#list 的映射解析
print('list 的映射解析')
l1 = [1,2,5,9]
l2 = [i * 2 for i in l1]
print(l1)
print('----------')

#dictionary 中的解析
print('dictionary 中的解析')
d1 = {'name':'annie','age':'six','location':'hangzhou'}

list_k1 = d1.keys()
list_k2 = [k for k,v in d1.items()]
print(list_k1,'\n',list_k2)

list_v1 = d1.values()
list_v2 = [v for k,v in d1.items()]
print(list_v1,'\n',list_v2)
list_items1 = d1.items()
list_items2 = ['%s=%s'%(k,v) for k,v in d1.items()]
print(list_items1,'\n',list_items2)
print('----------')

#list的过滤
print('list的过滤')
list_test = ['a','b','cc','dd','eee','fff','eee','fff']
list_filter1 = [i for i in list_test if len(i) == 2] #筛选所有含有2个字符的元素
print(list_filter1)
list_filter2 = [i for i in list_test if list_test.count(i) == 2] #筛选list中有两个相同值的元素
print(list_filter2)
print('----------')
