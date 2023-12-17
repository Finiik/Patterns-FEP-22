from person import Person, UserRole
from assess_visitor import AssessVisitor


class Manager(Person):
    def __init__(self, id, first_name, second_name, role):
        super().__init__(id, first_name, second_name, role)

    def assess_staff(self, person: Person, assess_visitor: AssessVisitor):
        if person.role == UserRole.STUDENT:
            assess_visitor.visit_student(person)
            print(f'Manager {self.first_name} {self.second_name} visited student {person.first_name} '
                  f'{person.second_name}')
        elif person.role == UserRole.PROFESSOR:
            assess_visitor.visit_professor(person)
            print(f'Manager {self.first_name} {self.second_name} visited professor {person.first_name} '
                  f'{person.second_name}')
