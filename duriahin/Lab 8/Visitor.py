import unittest
from enum import Enum

class Role(Enum):
    STUDENT = 1
    TEACHING_STAFF = 2
    RESEARCH_STAFF = 3
    ADMINISTRATION_STAFF = 4

class Person:
    def __init__(self, id, first_name, second_name, role):
        self.id = id
        self.first_name = first_name
        self.second_name = second_name
        self.role = role

    def get_info(self):
        return f"ID: {self.id}, Name: {self.first_name} {self.second_name}, Role: {self.role}"

    def accept(self, assess_visitor):
        pass

class Student(Person):
    def __init__(self, id, first_name, second_name, role):
        super(Student, self).__init__(id, first_name, second_name, role)
        self.research_score = {}
        self.academic_score = 0
        self.visited_lectures = 0

    def accept(self, assess_visitor):
        assess_visitor.visit_student(self)

    def perform_research(self, tasks):
        for task, score in tasks.items():
            self.research_score[task] = score

    def perform_studying(self, *args):
        self.academic_score = sum(args) / len(args) if args else 0

class Professor(Person):
    def __init__(self, id, first_name, second_name, role):
        super(Professor, self).__init__(id, first_name, second_name, role)
        self.research_score = {}
        self.academic_score = 0

    def accept(self, assess_visitor):
        assess_visitor.visit_professor(self)

    def perform_research(self, *args):
        self.research_score = {f"Task_{i + 1}": score for i, score in enumerate(args)}

    def conduct_classes(self, students):
        for student in students:
            student.perform_studying()

class Manager(Person):
    def assess_staff(self, person, assess_visitor):
        person.accept(assess_visitor)

class AssessVisitor:
    def visit_student(self, student):
        pass

    def visit_professor(self, professor):
        pass

class ApplyGrant(AssessVisitor):
    def visit_student(self, student):
        student.academic_score += 10

    def visit_professor(self, professor):
        professor.academic_score += 20

class MakeCompliant(AssessVisitor):
    def visit_student(self, student):
        student.visited_lectures += 1

    def visit_professor(self, professor):
        professor.academic_score += 20

class TestProcessor(unittest.TestCase):
    def test_student_class(self):
        student = Student(1, "John", "Doe", Role.STUDENT)
        self.assertEqual(student.get_info(), "ID: 1, Name: John Doe, Role: Role.STUDENT")

        student.perform_research({'Task1': 90, 'Task2': 85})
        self.assertEqual(student.research_score, {'Task1': 90, 'Task2': 85})

    def test_professor_class(self):
        professor = Professor(2, "Alice", "Smith", Role.TEACHING_STAFF)
        self.assertEqual(professor.get_info(), "ID: 2, Name: Alice Smith, Role: Role.TEACHING_STAFF")

        professor.perform_research(90, 85)
        self.assertEqual(professor.research_score, {'Task_1': 90, 'Task_2': 85})

    def test_manager_class(self):
        manager = Manager(3, "Bob", "Johnson", Role.ADMINISTRATION_STAFF)
        student = Student(4, "Emily", "Johnson", Role.STUDENT)
        professor = Professor(5, "David", "Brown", Role.TEACHING_STAFF)

        manager.assess_staff(student, ApplyGrant())
        self.assertEqual(student.academic_score, 10)

        manager.assess_staff(professor, MakeCompliant())
        self.assertEqual(professor.academic_score, 20)

if __name__ == '__main__':
    unittest.main()
