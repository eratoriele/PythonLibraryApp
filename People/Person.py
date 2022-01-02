import datetime

class Person:
    def __init__(self, firstName: str, lastName: str, dateOfBirth: datetime.date):

        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth