from typing import List
from student import Student
from person import Person, UserRole
from visitor import AssessVisitor


class Professor(Person):
    def __init__(self, id, first_name, surname, research_score, academic_score, conduct_lectures):
        super().__init__(id, first_name, surname, UserRole.PROFESSOR)
        self.research_score = research_score
        self.academic_score = academic_score
        self.conduct_lectures = conduct_lectures
        self.published_papers = []

    def accept(self, assess_visitor: AssessVisitor):
        assess_visitor.visit_professor(self)

    def perform_research(self, papers: list):
        for paper in papers:
            self.research_score += 10
            self.published_papers.append(paper)
            print(f"{self.first_name} {self.surname} has published a paper! Research score: {self.research_score}")

    def conduct_classes(self, class_type, students: List['Student']):
        if class_type == "lecture":
            self.conduct_lectures += 1
            print(f"{self.first_name} {self.surname} conducted a lecture. Nice!")
        elif class_type == "tutorial":
            for student in students:
                student.perform_studying(self.academic_score)
            print(f"{len(students)} have attended the tutorial. Nice!")