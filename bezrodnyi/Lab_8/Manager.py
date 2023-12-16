from AssessVisitor import AssessVisitor
from Person import PersonRole, Person


class Manager(Person):

    def __init__(self, id, first_name, second_name):
        super().__init__(id, first_name, second_name, PersonRole.MANAGER)

    def assess_staff(self, person: Person, assess_visitor: AssessVisitor):
        if person.role == PersonRole.STUDENT:
            assess_visitor.visit_student(person)
            print(
                f"Manager {self.first_name} {self.second_name} visited student {person.first_name} "
                f"{person.second_name}")
        elif person.role == PersonRole.PROFESSOR:
            assess_visitor.visit_professor(person)
            print(
                f"Manager {self.first_name} {self.second_name} visited Professor {person.first_name} "
                f"{person.second_name}")
