#tuple 不可变

tuple = (1,2,3)
#当tuple不为空时可以省略（）
tuple = 1,2,3
print(tuple[0])

#解包
a,b,c = tuple;
print(a,b,c)

#利用解包交换变量值
a = 100
b = 200
a,b = b,a
print(a,b)

my_tuple = (1,2,3,4,5)
*a, b, c = my_tuple   #解包时变量数和元素数不一致 使用* 但是不能出现两个以上
print(a)
print(b)
print(c)