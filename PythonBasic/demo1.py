#Python 的数据类型

#一条语句分行执行,用\
print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
aaaaaaaaaaaaaaaaaaaaaa')

#python中整型数据大小没有限制，如果数字长度过大，用_分割
num = 123_4245_53456464_545425
print(num)
binary_num = 0b11
oct_num = 0o10
hex_num = 0x10
print(binary_num)
print(oct_num)
print(hex_num)

#对浮点数进行运算可能会得到不精确的结果,因为py无法表示1/10
res = 0.1+0.2;
print(res) #0.30000000000000004

#三个单引号或者双引号可以实现换行
print('''this is 
a
test
sentence.''')

#字符串只能和字符串进行+拼接
concat1 = "a"+"b"
print(concat1)
#concat2 = "a"+ 1 TypeError: can only concatenate str (not "int") to str
print('a','b') #a b
print('a',1) #a 1

# 定义字符串时使用占位符,%s表示任意字符串,后面可以加限定长度e.g. %3s表示至少三个，%3.5s表示3到5个
# %f可是填充浮点数，%.2f保留两位小数
# %d是整数占位符，只保留整数位
str1 = 'Hello %s，I am %s'%('A','B')
print(str1)

#格式化字符串 嵌入变量
str2 = f'hello {concat1}'
print(str2)

# 字符串复制
str3 = str1 * 3
print(str3)

#布尔值 bool : True /  False 实际是整型
#空值 None

#类型检查
print(type(1))
print(type("1"))
print(type(1.3))
print(type(True))
