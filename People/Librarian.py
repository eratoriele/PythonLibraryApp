import enum

from People.Person import *


class LibrarianPositions(enum.Enum):
    schoolLibrarian = "School Librarian"
    lawLibrarian = "Law Librarian"
    medicalLibrarian = "Medical Librarian"
    artLibrarian = "Art Librarian"


class WorkHours(enum.Enum):
    daytime = "Daytime"
    nighttime = "Nighttime"


class Librarian(Person):
    def __init__(self, name: Name, date_of_birth: datetime, phone_number: str,
                 position: LibrarianPositions, work_hours: WorkHours):
        super().__init__(name, date_of_birth, phone_number)
        self.position = position
        self.work_hours = work_hours

    def to_string(self):
        return super().to_string() + " " + self.position.value + " " + self.work_hours.value
