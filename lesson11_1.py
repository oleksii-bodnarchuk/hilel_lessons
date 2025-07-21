class Animal:

    def speak(self):
        x = []
        for i in range(10):
            x.append(i)
        return x

    def eat(self):
        return "food"

class Dog(Animal):

    def speak(self):
        base_sound = super().speak() # Виклик методу базового класу
        return f"{base_sound} Woof!"

class Pet(Animal):

    def speak(self):
        return "Woof friendly!"

class Pitbull(Dog, Pet):

    def hunt(self):
        return "lion hunted cats"

lucky_dog = Pitbull()

print(lucky_dog.speak())