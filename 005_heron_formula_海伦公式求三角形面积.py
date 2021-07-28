#filename : 005_heron_formula_海伦公式求三角形面积.py
#author by : erisecsch

#海伦公式求三角形面积

a = float(input("第一条边长"))
b = float(input("第二条边长"))
c = float(input("第三条边长"))

s = （a+b+c）/2

area = (s*(s-a)*(s-b)*(s-c))**0.5
print("三角形的面积是%.2f"%area)
