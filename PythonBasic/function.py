# function is also an object

def f1():
    print('f1()')

def sum(a, b=0): # set default val
    print(a+b)

def change(arr):
    arr[0] = 10



print(type(f1))
f1()
sum(1,2)   # pass params by positions
sum(1)     # use a default val
sum(b = 1, a = 2)  # pass params by keyword

arr = [1,2]
change(arr)
print(arr) #changed
arr = [1,2]
change(arr.copy())
print(arr)
change(arr[:])
print(arr)

# changable params
def f2(*a, b, c): # equal to receiving a tuple
    print(a,b,c)

f2(1,2,3,b = 4,c = 5) # params after * must be passed by keywords

def f3(**a): # equal to receiving a dict
    print(a)

f3(a = 1, b = 2)


# doc


def f():
   '''
    test
   '''
   return 1

help(print)
help(f)


# advanced function: pass a function as a param

def isOdd(num):
    return num % 2 != 0

def isEven(num):
    return num % 2 == 0

def filter(rule, list):
    res = []
    for i in list:
        if rule(i):
            res.append(i)
    return  res

my_list = [1,2,3,4,5,6,7,8,9]
print(filter(isEven, my_list))  #get even nums from the list
print(filter(isOdd, my_list))  #get odd nums from the list


# lambda
res = (lambda a,b : a+b)(1,2)
print(res)

# map
my_list = [1,2,3]
res = map(lambda i: i+1,my_list)
print(list(res))

#sort

l = ['aa','b','ccc']
l.sort(key=len) #sorted by length
print(l)

l = [1,'2','3',4]
l.sort(key=int) #sorted by int val
print(l)

l = [2,1,4]
print(sorted(l))
print(l)