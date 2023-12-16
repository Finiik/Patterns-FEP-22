from abc import ABC


class AssessVisitor(ABC):

    def __init__(self):
        pass

    def visit_student(self, student):
        pass

    def visit_professor(self, professor):
        pass


class ApplyGrant(AssessVisitor):
    def __init__(self, grant_amount):
        self.grant_amount = grant_amount

    def get_all_moves(self):
        print("Applying grant to all individuals.")

    def visit_student(self, student):
        print(f"Grant of {self.grant_amount} applied to student {student.first_name} with ID {student.id}.")

    def visit_professor(self, professor):
        print(f"Grant of {self.grant_amount} applied to professor {professor.first_name} with ID {professor.id}.")


class MakeCompliant(AssessVisitor):
    def get_all_moves(self):
        print("Making all individuals compliant.")

    def visit_student(self, student):
        print(f"Making student {student.first_name} with ID {student.id} compliant.")

    def visit_professor(self, professor):
        print(f"Making professor {professor.first_name} with ID {professor.id} compliant.")
