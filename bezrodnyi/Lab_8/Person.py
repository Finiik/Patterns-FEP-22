from enum import Enum, auto

from AssessVisitor import AssessVisitor
from dataclasses import dataclass


class PersonRole(Enum):
    STUDENT = auto()
    PROFESSOR = auto()
    MANAGER = auto()


@dataclass
class Person:
    id: int
    first_name: str
    second_name: str
    role: Enum

    def get_info(self):
        return f"id={self.id}, first_name={self.first_name}, second_name={self.second_name}, role={self.role}"

    def accept(self, assess_visitor: AssessVisitor):
        if self.role == PersonRole.STUDENT:
            assess_visitor.visit_student(self)
        elif self.role == PersonRole.PROFESSOR:
            assess_visitor.visit_professor(self)
