import datetime
import enum
import random
from People.Person import Name, Titles


class BookGenre(enum.Enum):
    Biography = "Biography"
    AutoBiography = "AutoBiography"
    Action = "Action And Adventure"
    Dictionary = "Dictionary"
    Mystery = "Mystery"
    Satire = "Satire"
    Fantasy = "Fantasy"
    Science = "Science"
    History = "History"
    Comic = "Comic"


class BookPosition:
    def __init__(self, floor: int, section: int):
        self.floor = floor
        self.section = section


class Book:
    def __init__(self, name: str, author: Name, genre: BookGenre, publish_date: datetime,
                 position: BookPosition, is_borrowed: bool):
        self.name = name
        self.author = author
        self.genre = genre
        self.publish_date = publish_date
        self.position = position
        self.is_borrowed = is_borrowed

    def to_string(self):
        return_string = self.name + " by " + self.author.to_string() + " in the " + self.genre.value + " genre published in " + \
                        self.publish_date.strftime("%Y")

        if self.is_borrowed:
            return_string += " is currently borrowed and not available"
        else:
            return_string += " is currently in floor " + str(self.position.floor) + " section " + str(
                self.position.section)

        return return_string


# These values should have been written and read from a database, but since this is a small project,
# I will be generating them on the fly
def generate_random_books(count):
    # These names were taken from https://www.ryanmwilliams.com/python-titles/
    random_first_names = ["Crazy ", "Curvy ", "Fleshy ", "Flirty ", "Kinky ", "Lusty ", "Steamy ", "Sultry "]
    random_second_names = ["", "Innocent ", "Bold ", "Live ", "Cute ", "Brunette ", "Wild ", "Ancient ", "Blonde "]
    random_third_names = ["Reapers", "Gargoyles", "Sirens", "Zombies", "Ghosts", "Demons", "Angels", "Mummies"]

    random_author_first_names = ["Roy", "Lisa", "Damian", "Dwight", "Sonya", "David", "Judith"]
    random_author_middle_names = [None, "E.", "G."]
    random_author_last_names = ["Garcia", "Calvert", "Beall", "Howard", "Seitz", "Hardaway", "Goolsby"]

    return_list = []

    for i in range(count):
        # generate random name
        name = random.choice(random_first_names) + random.choice(random_second_names) + random.choice(
            random_third_names)
        # generate random author name
        author_name = Name(title=random.choice(list(Titles)),
                           first_name=random.choice(random_author_first_names),
                           middle_name=random.choice(random_author_middle_names),
                           last_name=random.choice(random_author_last_names))
        # Generate random publish_date
        publish_date = datetime.date(year=random.randint(1900, 2010),
                                     month=random.randint(1, 12),
                                     day=random.randint(1, 28))

        return_list.append(Book(name=name, author=author_name, genre=random.choice(list(BookGenre)),
                                publish_date=publish_date,
                                position=BookPosition(floor=random.randint(0, 4), section=random.randint(1, 12)),
                                is_borrowed=bool(random.getrandbits(1))))

    return return_list
