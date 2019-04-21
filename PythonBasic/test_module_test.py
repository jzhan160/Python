import test_module as test

print(test.a)
print(test.b)
print(test._c)
test.add()
t1 = test.Test()
t1.test()

from test_module import *
print(a)
print(b)
# print(_c) illegal
add()
t2 = Test()
t2.test()


from test_module import add as extern_add
# partially import
# use alias name to avoid the condition that there are functions with the same name
extern_add()