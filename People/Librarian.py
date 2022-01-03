from enum import Enum
import random
from People.Person import *


class LibrarianPositions(Enum):
    schoolLibrarian = "School Librarian"
    lawLibrarian = "Law Librarian"
    medicalLibrarian = "Medical Librarian"
    artLibrarian = "Art Librarian"


class WorkHours(Enum):
    daytime = "Daytime"
    nighttime = "Nighttime"


class Librarian(Person):
    def __init__(self, pid: int, name: Name, date_of_birth: datetime, phone_number: str,
                 position: LibrarianPositions, work_hours: WorkHours):
        super().__init__(pid, name, date_of_birth, phone_number)
        self.position = position
        self.work_hours = work_hours

    def to_string(self):
        return super().to_string() + " " + self.position.value + " " + self.work_hours.value


# These values should have been written and read from a database, but since this is a small project,
# I will be generating them on the fly
def generate_random_librarians(count):
    random_first_names = ["Jerry", "Ruth", "Charlene", "Nancy", "Martin", "Freda", "Thomas"]
    random_middle_names = [None, "C.", "A."]
    random_last_names = ["Gold", "Steed", "Rolfe", "Smith", "Rose", "Anderson", "Carpenter"]

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
        for j in range(count):
            random_phone_number += str(random.randint(0, 9))

        return_list.append(Librarian(pid=i + 1, name=name, date_of_birth=date_of_birth, phone_number=random_phone_number,
                                     position=random.choice(list(LibrarianPositions)),
                                     work_hours=random.choice(list(WorkHours))))

    return return_list
