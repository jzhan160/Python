


def CalDecorator(operation):
    def decorator(*args, **kwargs):
        print("Start:")
        res = operation(*args, **kwargs)
        print("End.")
        return res
    return decorator

@CalDecorator
def add(a,b):
    return a+b

@CalDecorator
def mul(a,b):
    return a*b

@CalDecorator
def polymerization(a,b,c,x):
    return a*(x**2)+b*x+c

print(add(1,2))
print(mul(2,2))
print(polymerization(1,1,1,2))

# new_add = CalDecorator(add)
# print(new_add(1,2))
#
# new_mul = CalDecorator(mul)
# print(new_mul(2,3))
#
# new_poly = CalDecorator(polymerization)
# print(new_poly(1,1,1,2))

