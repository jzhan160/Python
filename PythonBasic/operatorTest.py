#对象： 一切皆是对象
#对象包含： id(immutable), type(immutable), value(mul/imul)

#类型转换： int(), float(), str(), bool()

#运算符
a = 10 / 3
print(a)
b = 10 // 3 #整除
print(b)
c = 10 % 3
print(c)

d = 2 ** 2 #指数
print(d)

#关系运算符： == ！=比较的是值  is / is not 比较的是地址
str1 = "hi"
str2 = "hi"
print(str1==str2) #true
print(str1 is str2) #true

#逻辑运算符： not, and , or
#非bool值的and / or 运算，将两边的值转换成bool进行运行 然后返回原值
#and 时如果第一个值是false，直接返回第一个值，否则返回第二个
#or 时如果第一个值是true，直接返回第一个值，否则返回第二个
res1 = 1 and 2 # 2
res2 = 0 and 2 # 0
res3 = 1 or 2 #1
res4 = 0 or None # None

print(res1)
print(res2)
print(res3)
print(res4)

#三元运算: stat1 if true else stat2
num1 = 1
num2 = 2

print('num1 > num2') if num1>num2 else print('num2 > num1') # num1>num2?print():print
