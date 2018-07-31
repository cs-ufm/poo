"""
Dog class

"""
# own modules
from Animal import Animal,hey
import sys


class Dog():
    # class attribute
    animal_group="mammal"
    breed="Street Dog"

    # Constructor
    def __init__(self, name=None, age=0):
        # Instance attributes
        self.name = name
        # Public Instance variables
        self.age = age
        # "non-public" instance vars [Encapsulation]
        self._owner = None

    # instance methods
    def tag(self):
        return "{} is {} years old".format(self.name, self.age)

    def noise(self,sound):
        return "{} says: {}".format(self.name,sound)

    def sleep(self):
        pass


# inheritance
class Corgi(Dog):
    breed="Corgi"
    def sleep(self):
        return '{} is sleeping zZZZz'.format(self.name)


# own modules
a=Animal()
hey()

# Code
x=Dog()
y=Dog()
print(x==y)

doggy=Dog("Gino",12)
doge=Dog("Blacky",1)

print(doggy.name)
print(doggy.age)

print(doge.name)
print(doge.age)


print("{} is {} and {} is {}.".format(
    doggy.name, doggy.age, doge.name, doge.age))


print("{} is a {}".format(doggy.name,doggy.animal_group))

# inheritance
terry=Corgi("Terry",2)
print(terry.sleep())

print(isinstance(terry,Corgi))

# DIR
print(dir(doggy))

random_var=""
print(dir())
del random_var
print(dir())