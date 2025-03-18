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
        print(final_grade)

scores = [20, 40, 60, 80]
my_student = Student("Danny")
for score in scores:
    my_student.add(score)
my_student.calculate()