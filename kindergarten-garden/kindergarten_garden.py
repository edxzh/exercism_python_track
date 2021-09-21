DEFAULT_STUDENTS = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
PLANT_TYPES = {'C': 'Clover', 'G': 'Grass', 'R': 'Radishes', 'V': 'Violets'}

class Garden:
    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        self.pots = diagram.split('\n')
        self.students = sorted(students)

    def plants(self, student):
        student_index = self.students.index(student)
        plants_aconym = [pot[student_index * 2:student_index * 2 + 2] for pot in self.pots]

        return [PLANT_TYPES[acronym] for row in plants_aconym for acronym in row]

