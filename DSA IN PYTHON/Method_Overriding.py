class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    pass

dog = Dog()
cat = Cat()
cow = Cow()

print("Dog says:", dog.speak())
print("Cat says:", cat.speak())
print("Cow says:", cow.speak())
