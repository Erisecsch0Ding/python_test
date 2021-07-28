#filename : 011_judging_str.py
#author by : erisecsch

#判断字符串是否为数字

def is_number(s):
  
  try:
    float(s)
    return True
  except ValueError:
    pass
  
  try:
    import unicodedata
    unicodedata.numeric(s)
    return True
  except (TyprError,ValueError):
    pass
  
  return False

#测试字符串和数字
print(is_number('foo'))           #结果是 Flase
print(is_number('1'))             #结果是True
print(is_number('1.2'))           #结果是True
print(is_number('-1.37'))         #结果是True
print(is_number('1+1e'))          #结果是Fales

#测试Unicode
print(is_number('٥')) #阿拉伯语的5  结果是True
print(is_number('๒')) #泰语的2     结果是True
print(is_number('四')) #中文的4    结果是True
print(is_number('©')) #版权号      结果是False
