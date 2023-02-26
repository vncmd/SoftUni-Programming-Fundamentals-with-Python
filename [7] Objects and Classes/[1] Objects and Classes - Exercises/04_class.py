class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name

        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if Class.__students_count > len(self.students):
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        if len(self.grades) == 0:
            return 0
        avg_grade = sum(self.grades) / len(self.grades)
        return float(f"{avg_grade:.2f}")

    def __repr__(self):
        students = ', '.join(self.students)
        average_grade = self.get_average_grade()
        return f"The students in {self.name}: {students}. Average grade: {average_grade}"