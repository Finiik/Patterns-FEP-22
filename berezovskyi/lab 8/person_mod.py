from enum import Enum, auto
from dataclasses import dataclass
from visitor_mod import AssessVisitorMod


class UserRoleMod(Enum):
    STUDENT = auto()
    PROFESSOR = auto()
    MANAGER = auto()


@dataclass
class PersonMod:
    identifier: int
    first_name: str
    last_name: str
    role: Enum

    def get_info(self) -> str:
        return (f"identifier: {self.identifier}\n"
                f"first name: {self.first_name}\n"
                f"last name: {self.last_name}\n"
                f"role: {self.role}")

    def accept(self, assess_visitor: AssessVisitorMod):
        if self.role == UserRoleMod.STUDENT:
            assess_visitor.visit_student(self)
        elif self.role == UserRoleMod.PROFESSOR:
            assess_visitor.visit_professor(self)
