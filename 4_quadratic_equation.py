#filename : 4_quadratic_equation.py
#author by : erisecsch

#求解而原方程（ax^2+bx+c=0,a!=0）

import cmath #导入cmath（复杂数学运算）模块

a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))

d = （b**2）-（4*a*c）

sol1 = (-b+cmath.sqrt(d))/(2*a)
sol2 = (-b-cmath.sqrt(d))/(2*a)

print("结果为{0}和{1}".format(sol1,sol2))
