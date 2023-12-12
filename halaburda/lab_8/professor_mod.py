from typing import List
from student_mod import StudentMod
from person_mod import PersonMod, UserRoleMod
from visitor_mod import AssessVisitorMod


class ProfessorMod(PersonMod):
    def __init__(self, identifier, first_name, last_name, research_score, academic_score, conduct_lectures):
        super().__init__(identifier, first_name, last_name, UserRoleMod.PROFESSOR)
        self.research_score = research_score
        self.academic_score = academic_score
        self.conduct_lectures = conduct_lectures
        self.published_papers = []

    def accept(self, assess_visitor: AssessVisitorMod):
        assess_visitor.visit_professor(self)

    def perform_research(self, papers):
        for paper in papers:
            self.research_score += 10
            self.published_papers.append(paper)
            print(f"{self.first_name} {self.last_name} has published a paper! Research score: {self.research_score}")

    def conduct_classes(self, class_type, students: List['StudentMod']):
        if class_type == "lecture":
            self.conduct_lectures += 1
            print(f"{self.first_name} {self.last_name} conducted a lecture. Nice!")
        elif class_type == "tutorial":
            for student in students:
                student.perform_studying(self.academic_score)
            print(f"{len(students)} have attended the tutorial. Nice!")
