import unittest
from person import UserRole, Person
from student import Student
from professor import Professor
from manager import Manager
from processor import Processor


class TestProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = Processor()

    def test_process_student(self):
        student = Student(id=1, first_name="John", surname="Doe", research_score=0, academic_score=75,
                          visited_lectures=[1, 2, 3])
        self.processor.process_student(student)

    def test_process_professor(self):
        professor = Professor(id=101, first_name="Dr. Johnson", surname="Smith", research_score=0, academic_score=90,
                              conduct_lectures=1)
        self.processor.process_professor(professor)

    def test_process_manager(self):
        manager = Manager(id=201, first_name="Manager", surname="Smith", role=UserRole.MANAGER)
        person = Person(id=2, first_name="Jane", surname="Doe", role=UserRole.STUDENT)
        self.processor.process_manager(person, manager)


if __name__ == '__main__':
    unittest.main()
