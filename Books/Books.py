import datetime
import enum


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
    def __init__(self, name: str, author: str, genre: BookGenre, publish_date: datetime,
                 position: BookPosition, is_borrowed: bool):
        self.name = name
        self.author = author
        self.genre = genre
        self.publish_date = publish_date
        self.position = position
        self.is_borrowed = is_borrowed

    def to_string(self):
        return_string = self.name + " by " + self.author + " in the " + self.genre.value + " genre published in " + \
            self.publish_date.strftime("%Y")

        if self.is_borrowed:
            return_string += " is currently borrowed and not available"
        else:
            return_string += " is currently in floor " + str(self.position.floor) + " section " + str(self.position.section)

        return return_string

