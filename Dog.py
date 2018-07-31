class Dog():
    # class attribute
    breed="chihuahua"
    # Constructor
    def __init__(self, name=None, age=0):
        # Instance attributes
        self.name = name
        self.age = age






# Code
x=Dog()
y=Dog()
print(x==y)

doggy=Dog("Gino",12)
doge=Dog("Blacky",1)

print(doggy.name)
print(doggy.breed)

print(doge.name)
print(doge.breed)


print("{} is {} and {} is {}.".format(
    doggy.name, doggy.age, doge.name, doge.age))