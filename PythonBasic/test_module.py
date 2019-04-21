a = 1
b = 2
_c = 3 # cannot be visited if this module is used by  from xxx import *
       # but can be seen when imported by import xxx

def add():
    print('a + b =',a+b)

class Test:
    def test(self):
        print('test')

# run only test_module.py is executed as the main module 
if __name__ == '__main__':
    add()
    t = Test()
    t.test()