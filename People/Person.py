import datetime
import enum
from abc import ABC, abstractmethod


class Titles(enum.Enum):
    Mr = "Mr."
    Mrs = "Mrs."
    Ms = "Ms."
    Miss = "Miss."
    Dr = "Dr."
    Professor = "Professor"


class Name:
    def __init__(self, title: Titles, first_name: str, last_name: str, middle_name: str = None):
        self.title = title
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name

    @abstractmethod
    def to_string(self):
        if self.middle_name is not None:
            return self.title.value + " " + self.first_name + " " + self.middle_name + " " + self.last_name
        else:
            return self.title.value + " " + self.first_name + " " + self.last_name


class Person(ABC):
    @abstractmethod
    def __init__(self, name: Name, date_of_birth: datetime, phone_number: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number

    @abstractmethod
    def to_string(self):
        return self.name.to_string() + " " + self.date_of_birth.strftime("%Y/%m/%d")
