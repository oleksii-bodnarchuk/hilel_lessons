class Dog:
    def __init__(self, name: str, age: int, gender: str = "male"):
        self.name = name
        self.age = age
        self.gender = gender

    def bark(self):
        print(f"Woof! {self.name}")

    def eat(self):
        print("Woof!")

lucky = Dog("lucky", 5, "male")
lucky1 = Dog("lucky1", 3)

print(lucky.name)
print(lucky.age)
print(lucky.gender)
print(lucky.bark())

print(lucky1.name)
print(lucky1.age)
print(lucky1.gender)
print(lucky1.bark())