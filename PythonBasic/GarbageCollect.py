class A:
    def __init__(self):
        print('An instance of A is created.')
    def __del__(self):
        print('An instance of A is destroyed.')
      

a = A()
b = a
a = None
del b

# when ther is no reference to the object A(), the garbage collector
# in Python will remove the object automatically


