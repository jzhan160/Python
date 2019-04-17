#流程控制语句

#if语句
user = input("please enter a username: ") #input()接收的是str，可以组织程序向下运行
if user == 'admin':
    print('admin')
else:
    print('not admin')

#循环语句
i = 0
while i<5:
    i+=1
    if i==4:
        pass #占位
    print(i)
else:
    print('end')