from abc import ABC, abstractmethod

class Student(ABC):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def write_exams(self):
        pass

    def attend_class(self):
        print("Attending class.")

class HighSchoolStudent(Student):
    def study(self):
        print("Studying high school subjects.")

    def write_exams(self):
        print("Writing high school exams.")

# Example usage
if __name__ == "__main__":
    student = HighSchoolStudent()
    student.attend_class()
    student.study()
    student.write_exams()
