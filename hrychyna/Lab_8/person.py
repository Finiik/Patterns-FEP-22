from enum import Enum, auto
from dataclasses import dataclass
from assess_visitor import AssessVisitor


class UserRole(Enum):
    STUDENT = auto()
    PROFESSOR = auto()
    MANAGER = auto()


@dataclass
class Person:
    id: int
    first_name: str
    second_name: str
    role: Enum

    def get_info(self) -> str:
        return (f"id: {self.id}\n"
                f"first name: {self.first_name}\n"
                f"second_name: {self.second_name}\n"
                f"role: {self.role}")

    def accept(self, assess_visitor: AssessVisitor):
        if self.role == UserRole.STUDENT:
            assess_visitor.visit_student(self)
        elif self.role == UserRole.PROFESSOR:
            assess_visitor.visit_professor(self)
