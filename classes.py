class Student:

    def __init__(self, name:str):
        self.name = name
        self.grades = []

    def add(self, grade:int):
        self.grades.append(grade)

    def calculate(self):
        total_score = 0
        for grade in self.grades:
            total_score = total_score+grade
        final_grade = total_score/len(self.grades)
        return final_grade

class Classroom:
    def __init__(self):
        self.students = []

    def add(self, student: Student):
        self.students.append(student)

    def calculate(self):
        total_score = 0
        for student in self.students:
            total_score = total_score + student.calculate()
        final_grade = total_score/len(self.students)
        print(final_grade)


classroom = Classroom()
scores = [20, 40, 60, 80]
danny = Student("Danny")
for score in scores:
    danny.add(score)
classroom.add(danny)

scores = [50, 70, 30, 40]
christina = Student("Christina")
for score in scores:
    christina.add(score)
classroom.add(christina)

classroom.calculate()
