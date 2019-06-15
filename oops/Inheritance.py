class Animal:

    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an Animal")

    def eat(self):
        print("I am eating")

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):
        print("I am a Dog")

    def bark(self):
        print("WHOOF")

    def speak(self):
        print('WHOOF')


class NewDog:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " says WHOOF")

class NewCat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " says meow")


myAnimal = Animal()
myAnimal.eat()
myAnimal.who_am_i()
myDog = Dog()
myDog.who_am_i()
myDog.speak()

niko = NewDog("Niko")
felix = NewCat("felix")

for pet in [niko, felix]:
    pet.speak()

def petspeak(pet):
    pet.speak()

petspeak(niko)
petspeak(felix)