class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof! Woof!")

    def dog_age(self):
        self.age += 1
        print("Happy birthday!", self.name, "is now", self.age, "years old!" )

    def get_info (self):
        print("Dog Name:", self.name, ", Dog Age:", self.age)


my_dog = dog("Amigo", 5)
my_dog.bark()
my_dog.dog_age()
my_dog.get_info()