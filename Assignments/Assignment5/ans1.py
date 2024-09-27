class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# Example usage
student1 = Students("Alice", 20, "A")
print(student1.__dict__)  # Output: {'name': 'Alice', 'age': 20, 'grade': 'A'}
