from person import Person, UserRole
from visitor import AssessVisitor


class Student(Person):
    def __init__(self, id, first_name, surname, research_score, academic_score, visited_lectures):
        super().__init__(id, first_name, surname, UserRole.STUDENT)
        self.research_score = research_score
        self.academic_score = academic_score
        self.visited_lectures = visited_lectures

    def accept(self, assess_visitor: AssessVisitor):
        assess_visitor.visit_student(self)

    def perform_research(self, tasks):
        for key, value in tasks.items():
            tasks[key] = self.research_score + 10

    def perform_studying(self, prof_academic_score):
        base_studying_rate = 0.5
        academic_influence = 0.2 * self.academic_score
        professor_influence = 0.2 * prof_academic_score
        lectures_influence = 0.1 * len(self.visited_lectures)

        studying_rate = base_studying_rate + academic_influence + lectures_influence + professor_influence

        print(f"Studying rate for {self.first_name} {self.surname}: {studying_rate}")

