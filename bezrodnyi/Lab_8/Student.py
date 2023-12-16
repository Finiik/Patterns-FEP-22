from AssessVisitor import AssessVisitor
from Person import PersonRole, Person


class Student(Person):

    def __init__(self, id, first_name, second_name, research_score, academic_score, visited_lectures,
                 articles) -> None:
        super().__init__(id, first_name, second_name, PersonRole.STUDENT)
        self.research_score = research_score
        self.academic_score = academic_score
        self.visited_lectures = visited_lectures
        self.articles = articles
        self.read_articles = []

    def accept(self, assess_visitor: AssessVisitor) -> None:
        assess_visitor.visit_student(self)

    def perform_search(self, tasks: dict) -> None:
        for key, value in tasks.items():
            tasks[key] = self.research_score + 5

    def perform_studying(self) -> None:
        performed_studying_score = 0
        for article in self.articles:
            if article not in self.read_articles:
                self.read_articles.append(article)
                performed_studying_score += 20

        self.academic_score += performed_studying_score

        print(f"Student {self.first_name} {self.second_name} studied articles and increased the academic score up to "
              f"{performed_studying_score}. Current academic score: {self.academic_score}")
