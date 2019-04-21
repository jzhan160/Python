
# scope: global and local
a = 0
b = 0
def test1():
    global a #change the global var
    a = 1
    b = 1

test1()
print(a,b)

# namespace


def test2():
    cur = locals()
    print('current namespace is ', cur)
    global_ = globals()
    print('global namespace is ',global_)



scope = locals()
print(scope['a'])
print('current namespace is ', scope)
test2()