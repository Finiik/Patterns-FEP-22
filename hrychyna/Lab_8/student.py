from person import Person, UserRole
from assess_visitor import AssessVisitor


class Student(Person):
    def __init__(self, id, first_name, second_name, research_score, academic_score, visited_lectures):
        super().__init__(id, first_name, second_name, UserRole.STUDENT)
        self.research_score = research_score
        self.academic_score = academic_score
        self.visited_lectures = visited_lectures

    def accept(self, assess_visitor: AssessVisitor) -> None:
        assess_visitor.visit_student(self)

    def perform_research(self, tasks):
        for key, value in tasks.items():
            tasks[key] = self.research_score + 50

    def perform_studying(self, academic_score):
        laboratory_scores = 0.5
        modules_scores = 0.4 * academic_score
        lectures_scores = 0.1 * len(self.visited_lectures)

        studying_rate = laboratory_scores + modules_scores, lectures_scores

        print(f"Studying rate for {self.first_name} {self.second_name}: {studying_rate}")
