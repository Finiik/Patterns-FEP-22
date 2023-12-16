from AssessVisitor import AssessVisitor
from Manager import Manager
from Person import PersonRole, Person
from Student import Student
from Professor import Professor


class ProcessorAssessVisitor(AssessVisitor):
    def get_all_moves(self):
        pass

    def visit_student(self, student: Student):
        pass

    def visit_professor(self, professor: Professor):
        pass


class Processor:
    def __init__(self):
        self.assess_visitor = ProcessorAssessVisitor()

    def process_staff(self, person: Person):
        if person.role == PersonRole.STUDENT:
            self.process_student()
        elif person.role == PersonRole.PROFESSOR:
            self.process_professor()

    def process_student(self, student: Student):
        student.perform_search({"task1": 10, "task2": 150})
        student.perform_studying()
        self.assess_visitor.visit_student(student)

    def process_professor(self, professor: Professor):
        professor.perform_research(["paper1", "paper2", "paper3", "paper4"])
        professor.conduct_classes([Student(
            id=1,
            first_name="Someone",
            second_name="Else",
            research_score=7,
            academic_score=18,
            visited_lectures=[1,2,3],
            articles=["article1", "article2"]
        ), Student(
            id=2,
            first_name="Mathematical",
            second_name="Guy",
            research_score=99,
            academic_score=99,
            visited_lectures=[1, 2, 3, 4, 5, 6, 7],
            articles=["article1", "article2", "article4", "article5", "article7", ]
        )])
        self.assess_visitor.visit_professor(professor)

    def process_manager(self, manager: Manager):
        manager.assess_staff(manager, self.assess_visitor)
