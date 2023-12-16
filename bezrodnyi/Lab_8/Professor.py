from Person import Person, PersonRole
from AssessVisitor import AssessVisitor
from Student import Student


class Professor(Person):

    def __init__(self, id, first_name, second_name, research_score: int, academic_score: int) -> None:
        super().__init__(id, first_name, second_name, PersonRole.PROFESSOR)
        self.research_score = research_score
        self.academic_score = academic_score
        self.stolen_papers = []

    def accept(self, assess_visitor: AssessVisitor) -> None:
        assess_visitor.visit_professor(self)

    def perform_research(self, papers) -> None:
        for i, paper in enumerate(papers):
            self.research_score += 15
            if i % 3 == 0:
                self.stolen_papers.append(paper)
                self.research_score -= 15
            else:
                continue
        print(f"Professor {self.first_name} {self.second_name} has stolen this papers:\n"
              f"{self.stolen_papers}")

    def conduct_classes(self, students: list[Student]) -> None:
        for student in students:
            student.perform_studying()
        print(f"Professor {self.first_name} {self.second_name} has conducted classes successfully")
