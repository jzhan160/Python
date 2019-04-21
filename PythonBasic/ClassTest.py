# class

class MyClass:
    pass

instance1 = MyClass()
print(isinstance(instance1,MyClass))



# Each class is on object in the memory and it has id , type and value.
# The value may contains public variables and functions.
# Each instance of this class is also an object and has its own values of
# varaibles. Functions of instances are all the same because they are from
# the class object. However, variables in instances can come from its class
# or itself.
class Person:
    name = 'jc'  # public static, can be used by Person.name
                # p.name is not a class property

    def __init__(self,name):
        self.name = name

    # the class method can be invoked by class or instance
    # its first arg is cls
    @classmethod
    def cls_fn(cls):
        print('class method')

    # the static method can be invoked by class or instance
    #it has no default args
    @staticmethod
    def static_fn():
        print('static method')

    def sayHi(self): # self is the instance that invokes the function
        print('Hi',self.name)

    def get_age(self):  # age belongs to each instance and is encapsulated
        return self._age

    def set_age(self,age):
        self._age = age

    def get_gender(self):
        return self.__gender  # cannot be access by p.__gender
                              # but can also be visited by _Person__gender

    def set_gender(self,gender):
        self.__gender = gender

    # using property decorator: function name has to be the same as variables
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

p1 = Person('zhang')
p2 = Person('wang')

p1.sayHi()
p2.sayHi()

p1.set_age(20)
print(p1.get_age())
print(p1._age)

p1.set_gender('male')
print(p1.get_gender())
# print(p1.__gender) cannot visit in this way
print(p1._Person__gender) # accessible

p1.address = 'syr'
print(p1.address)

p1.cls_fn()
Person.cls_fn()
p1.static_fn()
Person.static_fn()