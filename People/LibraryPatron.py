from enum import Enum
import random

from People.Person import *


class MembershipTypes(Enum):
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


# These values should have been written and read from a database, but since this is a small project,
# I will be generating them on the fly
def generate_random_library_patrons(count):
    random_first_names = ["Melvin", "Isabel", "May", "Bonnie", "Diana", "Jennifer", "Jenny"]
    random_middle_names = [None, "S.", "D.", "A."]
    random_last_names = ["Kohler", "Thompson", "Silverman", "Swanigan", "Victor", "Faulkner", "White"]

    return_list = []

    for i in range(count):
        # generate random name
        name = Name(title=random.choice(list(Titles)),
                    first_name=random.choice(random_first_names),
                    middle_name=random.choice(random_middle_names),
                    last_name=random.choice(random_last_names))
        # Generate random birth date
        date_of_birth = datetime.date(year=random.randint(1900, 2010),
                                      month=random.randint(1, 12),
                                      day=random.randint(1, 28))
        # Generate random phone number
        random_phone_number = ""
        for j in range(10):
            random_phone_number += str(random.randint(0, 9))

        return_list.append(LibraryPatron(name=name, date_of_birth=date_of_birth, phone_number=random_phone_number,
                                         membership=random.choice(list(MembershipTypes))))

    return return_list
