
#装饰器其实就是一个以函数作为参数并返回一个替换函数的可执行函数。

def decorate(fun): #定义装饰函数,名为“decorate"，作用是：关联fun函数跟inner函数【即传入fun方法名，返回inner方法】

    def inner(a, b): # 定义要装饰（改装）fun函数的具体方法，并命名为”inner“，作用是：将”inner方法“新增到”fun方法“中，使其成为新的fun方法，
                     # 即先把fun的返回值作为inner方法的参数，再根据inner方法计算，得到一个新的返回值，最后把新的返回值赋值给新的fun函数。

        ret = fun(a, b)

        return abs(ret)

    return inner

@decorate  #等同于 sub = decorate(sub) ，即将decorate方法中的(求绝对值)功能，新增给fun函数(求和)，使其成为新的fun函数(求和后再求绝对值）
def sub(a, b):
    return a - b

y = sub(3,4)
print(y)
