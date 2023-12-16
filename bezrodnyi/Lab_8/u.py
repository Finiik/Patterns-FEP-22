import unittest
from processor import Processor
from Professor import Professor
from Student import Student
from Manager import Manager


class TestProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = Processor()

    def test_process_student(self):
        student = Student(id=1, first_name="Someone", second_name="Else", research_score=7,
                          academic_score=18, visited_lectures=[1,2,3], articles=["article1", "article2"])
        self.processor.process_student(student)

    def test_process_professor(self):
        professor = Professor(id=2, first_name="Zelisko", second_name="Not Zelenski",
                              research_score=10, academic_score=10)
        self.processor.process_professor(professor)

    def test_process_manager(self):
        manager = Manager(id=201, first_name="Manager", second_name="Smith")
        self.processor.process_manager(manager)


if __name__ == '__main__':
    unittest.main()
