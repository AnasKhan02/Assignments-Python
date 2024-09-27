class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

student = Students("Alice", 20, "A")

# Get writable attributes
writable_attrs = [attr for attr in dir(student) if not attr.startswith('__') and not callable(getattr(student, attr))]
print(writable_attrs)  # Output: ['age', 'grade', 'name']
