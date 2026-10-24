# 1_inheritance.py

class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self):
        print(f"{self.name} makes a generic sound.")

# Dog "is-an" Animal
class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} barks: Woof! Woof!")

if __name__ == "__main__":
    dog = Dog("Buddy")
    dog.make_sound()
