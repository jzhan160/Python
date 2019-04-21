# Base class
class Animal:
    def __init__(self,name):
        self._name = name
        print('the name is', self._name)
        
    def run(self):
        print('Animals can run.')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

        
# Derived class
class Dog(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        #Animal.__init__(self,name)
        self._age = age
        print('the age is', self._age)

    # override
    def run(self):
        print('Dogs can run.')

    def bark(self):
        print('Dogs can bark.')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

dog = Dog('guoguo',1)
dog.run()
dog.bark()
print(dog.age)
print(dog.name) # derived from parent class


class Base1:
    def test(self):
        print('test in base1 class')
class Base2:
    def test(self):
        print('test in base2 class')

# multiple inheritance
# if there are same functions in parents classes and the child class do
# not define such functions, the child will use the function in the base
# class which is in the front of the ()
class Child(Base1,Base2):
    def Ctest(self):
        print('test in child class')

child = Child()
child.test()
