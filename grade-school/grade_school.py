class School:
    def __init__(self):
        self.students = []

    def add_student(self, name, grade):
        self.students.append({'name': name, 'grade': grade})

    def roster(self):
        students_sort_by_grade = sorted(self.students, key=lambda stu: (stu.get('grade'), stu.get('name')))

        return [stu.get('name') for stu in students_sort_by_grade]

    def grade(self, grade_number):
        return sorted(student.get('name') for student in self.students if student.get('grade') == grade_number)
