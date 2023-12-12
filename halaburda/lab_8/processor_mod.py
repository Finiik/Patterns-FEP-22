from person_mod import UserRoleMod
from professor_mod import ProfessorMod
from student_mod import StudentMod
from visitor_mod import AssessVisitorMod


class ProcessorAssessVisitorMod(AssessVisitorMod):
    def get_all_moves(self):
        pass

    def visit_student(self, student):
        pass

    def visit_professor(self, professor):
        pass


class ProcessorMod:
    def __init__(self):
        self.assess_visitor = ProcessorAssessVisitorMod()

    def process_staff(self, person):
        if person.role == UserRoleMod.STUDENT:
            self.process_student(
                StudentMod(identifier=person.identifier, first_name=person.first_name, last_name=person.last_name,
                           research_score=0, academic_score=0, visited_lectures=[]))
        elif person.role == UserRoleMod.PROFESSOR:
            self.process_professor(
                ProfessorMod(identifier=person.identifier, first_name=person.first_name, last_name=person.last_name,
                             research_score=0, academic_score=0, conduct_lectures=[]))

    def process_student(self, student):
        professor_academic_score = 85
        student.perform_research({"task1": 5, "task2": 8})
        student.perform_studying(professor_academic_score)
        self.assess_visitor.visit_student(student)

    def process_professor(self, professor):
        professor.perform_research(["paper1", "paper2"])
        professor.conduct_classes("lecture", [StudentMod(identifier=1, first_name="John", last_name="Doe",
                                                         research_score=0, academic_score=75,
                                                         visited_lectures=[1, 2, 3])])
        self.assess_visitor.visit_professor(professor)

    def process_manager(self, manager):
        manager.assess_staff(manager, self.assess_visitor)
