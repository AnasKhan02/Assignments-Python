class Staff:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class Teacher(Staff):
    def __init__(self, name, position, subject):
        super().__init__(name, position)
        self.subject = subject

# Example usage
teacher1 = Teacher("Mr. Anas", "SDE 1", "Data Analytics")
print(teacher1.__dict__)  # Output: {'name': 'Mr. Smith', 'position': 'Math Teacher', 'subject': 'Mathematics'}
