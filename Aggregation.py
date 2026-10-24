# 3_aggregation.py

class Teacher:
    def __init__(self, name: str):
        self.name = name

class Department:
    def __init__(self, name: str, teacher: Teacher):
        self.name = name
        # Teacher is passed in from outside (weak ownership)
        self.teacher = teacher

    def display_info(self):
        print(f"Department: {self.name}, Led by: {self.teacher.name}")

if __name__ == "__main__":
    teacher = Teacher("Dr. Smith")
    dept = Department("Computer Science", teacher)
    dept.display_info()
    # If dept is deleted, teacher object still exists independently.
