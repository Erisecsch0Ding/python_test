#filename : 44_regular_expression_tese.py
# author by : erisecsch

#正则表达式

#1-re.match(): 尝试从字符串的起始位置开始匹配一个模式，如果不是起始位置匹配成功的话，返回none
#2-re.search(): 扫描整个字符串，然后返回第一个成功的匹配
#实例对比
import re

line = 'cats are more smarter than dogs'

matchobj = re.match(r'dogs',line,re.M|re.I)
if matchobj:
    print('match-->matchobj.group():',matchobj.group())
else:
    print('no match!')

searchobj = re.search(r'dogs',line,re.M|re.I)
if searchobj:
    print('search-->searchobj.group():',searchobj.group())
else:
    print('no search')

print('----------')

#3-re.sub(): 检索与替换[s = re.sub('表达式','repl','要检查匹配的字符串'，'标志位')
import re

#repl是非函数
phonenum = '2004-666-999 # 这是一个电话号码'
phonenum1 = re.sub(r'#.*$','',phonenum) #删除注释
print(phonenum1)
phonenum2 = re.sub(r'\D','',phonenum1) #删除非数字符号
print(phonenum2)
print('----------')

#repl是函数
s = 'A242HH230242KK'

def double(matched):
    value = int(matched.group('value'))
    return str(value*2)

print(re.sub('(?P<value>\d+)', double, s))

#4-compile():编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用


