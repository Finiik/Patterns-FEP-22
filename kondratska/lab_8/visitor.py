from abc import ABC, abstractmethod


class AssessVisitor(ABC):
    @abstractmethod
    def get_all_moves(self):
        pass

    @abstractmethod
    def visit_student(self, student):
        pass

    @abstractmethod
    def visit_professor(self, professor):
        pass


class ApplyGrant(AssessVisitor):
    def __init__(self, grant_amount):
        self.grant_amount = grant_amount

    def get_all_moves(self):
        print("Applying grant to all individuals.")

    def visit_student(self, student):
        print(f"Grant of {self.grant_amount} applied to student {student.name} with ID {student.student_id}.")

    def visit_professor(self, professor):
        print(f"Grant of {self.grant_amount} applied to professor {professor.name} with ID {professor.professor_id}.")


class MakeCompliant(AssessVisitor):
    def get_all_moves(self):
        print("Making all individuals compliant.")

    def visit_student(self, student):
        print(f"Making student {student.name} with ID {student.student_id} compliant.")

    def visit_professor(self, professor):
        print(f"Making professor {professor.name} with ID {professor.professor_id} compliant.")