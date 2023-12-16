import unittest

from manager_mod import ManagerMod
from person_mod import UserRoleMod
from processor_mod import ProcessorMod
from professor_mod import ProfessorMod
from student_mod import StudentMod


class TestProcessorMod(unittest.TestCase):
    def setUp(self):
        self.processor = ProcessorMod()

    def test_process_student(self):
        student = StudentMod(identifier=1, first_name="John", last_name="Doe", research_score=0, academic_score=75,
                             visited_lectures=[1, 2, 3])
        self.processor.process_student(student)

    def test_process_professor(self):
        professor = ProfessorMod(identifier=101, first_name="Dr. Johnson", last_name="Smith", research_score=0,
                                 academic_score=90,
                                 conduct_lectures=1)
        self.processor.process_professor(professor)

    def test_process_manager(self):
        manager = ManagerMod(identifier=201, first_name="Manager", last_name="Smith", role=UserRoleMod.MANAGER)
        self.processor.process_manager(manager)


if __name__ == '__main__':
    unittest.main()
