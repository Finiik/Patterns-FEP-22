import unittest
from person import UserRole
from student import Student
from professor import Professor
from manager import Manager
from apply_grant import Processor


class TestProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = Processor()

    def test_process_student(self):
        student = Student(id=1, first_name="Maraaa", second_name="Bodnar", research_score=0, academic_score=70,
                          visited_lectures=[1, 2, 3])
        self.processor.process_student(student)

    def test_process_professor(self):
        professor = Professor(id=10, first_name="Dasha", second_name="Hrychyna", research_score=0,
                              academic_score=100)
        self.processor.process_professor(professor)

    def test_process_manager(self):
        manager = Manager(id=201, first_name="Masha", second_name="Katsuba", role=UserRole.MANAGER)
        self.processor.process_manager(manager)


if __name__ == '__main__':
    unittest.main()
