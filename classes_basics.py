import numpy as np

class Person(object):
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def full_name(self):
        return self.first + ' ' + self.last

    def display(self):
        print("First Name::" + self.first)
        print("Last Name::" + self.last)
        print("Age::", self.age)
        print("Pets::", self.pets)

    
per = Person('Rayan', 'Shabbir', 20)

print(per.full_name())
print(per.age)
print(per.first)
print(per.last)

# Changing value of data member of class
per.first = 'Shahmeer'
print(per.full_name())

# Defining a data member of class at run time
pets = {'cat':10, 'dog':12}

per.pets = pets
print(per.pets)

print("\n")

print(per.display())