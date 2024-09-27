class Teacher:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary  # Private attribute

    def get_salary(self):
        return self.__salary

# Example usage
teacher = Teacher("Mr. Smith", 30, 50000)
print(teacher.get_salary())  # Output: 50000
# print(teacher.__salary)  # This will raise an AttributeError
