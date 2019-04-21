
def test_div(a,b):
    try:
        res = a/b
    except ZeroDivisionError as ze:
        print(ze)
    except Exception as e:
        print(e)
    else:  # no exception
        print(res)
    finally:
        print('end')


test_div(1,2)
test_div(1,0)


class MyException(Exception):
    pass


def test_add(a,b):
    if a<0 or b<0:
        raise MyException('MyException')
    print('a + b = ', a+b)


test_add(1,1)
test_add(1,-1)




