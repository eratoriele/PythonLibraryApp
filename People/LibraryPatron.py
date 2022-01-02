import enum

from People.Person import *


class MembershipTypes(enum.Enum):
    Guest = "Guest"
    FullIndividual = "Full Individual Membership"
    FullLife = "Full Life Membership"
    Overseas = "Overseas Membership"


class LibraryPatron(Person):
    def __init__(self, name: Name, date_of_birth: datetime, phone_number: str, membership: MembershipTypes):
        super().__init__(name, date_of_birth, phone_number)
        self.membership = membership

    def to_string(self):
        return super().to_string() + " " + self.membership.value
