from person import Person, UserRole
from visitor import AssessVisitor


class Manager(Person):
    def __init__(self, id, first_name, surname, role):
        super().__init__(id, first_name, surname, role)

    def assess_staff(self, person: Person, assess_visitor: AssessVisitor):
        if person.role == UserRole.STUDENT:
            assess_visitor.visit_student(person)
            print(f'Manager {self.first_name} {self.surname} visited student {person.first_name} {person.surname}')
        elif person.role == UserRole.PROFESSOR:
            assess_visitor.visit_professor(person)
            print(f'Manager {self.first_name} {self.surname} visited professor {person.first_name} {person.surname}')
            