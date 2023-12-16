from person_mod import PersonMod, UserRoleMod


class ManagerMod(PersonMod):
    def __init__(self, identifier, first_name, last_name, role):
        super().__init__(identifier, first_name, last_name, role)

    def assess_staff(self, person, assess_visitor):
        if person.role == UserRoleMod.STUDENT:
            assess_visitor.visit_student(person)
            print(f'Manager {self.first_name} {self.last_name} visited student {person.first_name} {person.last_name}')
        elif person.role == UserRoleMod.PROFESSOR:
            assess_visitor.visit_professor(person)
            print(f'Manager {self.first_name} {self.last_name} visited professor {person.first_name} {person.last_name}')
