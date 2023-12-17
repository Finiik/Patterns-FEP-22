from typing import List
from student import Student
from person import Person, UserRole
from assess_visitor import AssessVisitor


class Professor(Person):
    def __init__(self, id, first_name, second_name, research_score, academic_score):
        super().__init__(id, first_name, second_name, UserRole.PROFESSOR)
        self.research_score = research_score
        self.academic_score = academic_score
        self.conduct_lectures = 0
        self.books_published = 0

    def accept(self, assess_visitor: AssessVisitor) -> None:
        assess_visitor.visit_professor(self)

    def perform_research(self):
        self.research_score += 1
        print(f"{self.first_name} {self.second_name} performed research!")

    def publish_book(self):
        self.books_published += 1
        print(f"{self.first_name} {self.second_name} published a book!")

    def conduct_classes(self, class_type, students: List['Student']):
        if class_type == "lecture":
            self.conduct_lectures += 1
            print(f"{self.first_name} {self.second_name} conducted a lecture.")
        elif class_type == "tutorial":
            for student in students:
                student.perform_studying(self.academic_score)
            print(f"{len(students)} have attended the tutorial.")
