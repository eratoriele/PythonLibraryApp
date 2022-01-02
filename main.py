import datetime
import random

from People.Librarian import *
from People.LibraryPatron import *
from Books.Books import *


if __name__ == "__main__":
    p = Librarian(name=Name(title= Titles.Mr, first_name="Bora", last_name="Gulerman"),
                  date_of_birth=datetime.datetime(year=1998, month=6, day=22),
                  phone_number="626-860-5839",
                  position=LibrarianPositions.schoolLibrarian,
                  work_hours=WorkHours.daytime)

    p2 = LibraryPatron(name=Name(title=Titles.Mr, first_name="Mike", last_name="Barrett", middle_name="C."),
                       date_of_birth=datetime.date(year=1936, month=11, day=23),
                       phone_number="503-993-7347",
                       membership=MembershipTypes.FullLife)

    b = Book(name="Homegoing", author="Yaa Gyasi", genre=random.choice(list(BookGenre)),
             publish_date=datetime.datetime(year=2016, month=1, day=1), position=BookPosition(floor=1, section=1),
             is_borrowed=False)

    print(p.to_string())
    print(p2.to_string())
    print(b.to_string())
