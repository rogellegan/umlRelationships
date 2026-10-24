# 2_composition.py

class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} HP is starting.")

class Car:
    def __init__(self, model: str, horsepower: int):
        self.model = model
        # Engine is created inside Car (strong ownership)
        self.engine = Engine(horsepower)

    def start_car(self):
        print(f"Starting {self.model}...")
        self.engine.start()

if __name__ == "__main__":
    my_car = Car("Mustang", 450)
    my_car.start_car()
