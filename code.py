class Student:
    def __init__(self, name, age, student_id):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def average(self):
        total = sum(self.grades.values())
        return total / len(self.grades)


class Subject:
    def __init__(self, name):
        self.name = name


class Diary:
    def __init__(self):
        self.students = []
        self.subjects = []

    def add_student(self, student):
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)


math = Subject("Math")
physics = Subject("Physics")

alice = Student("Alice", 16, "A123")
bob = Student("Bob", 15, "B456")

diary = Diary()
diary.add_student(maks)
diary.add_student(bob)
diary.add_subject(math)
diary.add_subject(physics)


alice.add_grade(math, 90)
alice.add_grade(physics, 85)

bob.add_grade(math, 78)
bob.add_grade(physics, 92)


print(f"{maks.name} has an average grade of {maks.average()}")
print(f"{bob.name} has an average grade of {bob.average()}")
