'''
MSc Computer Systems and Management
CSTM65 Software Engineering Principles
Author: Paul Jones
Date: 30/10/2020
'''


class River():
    '''
    Defines a class in python, in this case the class is called 'River'
    '''

    Canoeing = "Yes"  # this is a class variable.

    def __init__(self, RiverName, Location, Fishing):
        self.RiverName = RiverName  # sets attributes for each class instance
        self.Location = Location  # sets attributes for each class instance
        self.Fishing = Fishing  # sets attributes for each class instance

    def fishing_on_river(self):

        if self.Fishing is True:
            return f"{self.RiverName} has fishing so be wary of fishermen"
        else:
            return f"{self.RiverName} has no fishing so have fun!"
    
    print_river_details(Spey)


class RiverDetails(River):

    def __init__(self, RiverLength, Grade):
        self.RiverLength = RiverLength
        self.Grade = Grade
        super().__init__(RiverName, Location, Fishing)  # noqa: F821

    print_river_details(Spey)

    def river_rating(self):
        if self.Grade > 3:
            RiverRating = "Extreme"
            return RiverRating
        elif self.Grade == 3:
            RiverRating = "Hard"
            return RiverRating
        elif self.Grade < 3:
            RiverRating = "Medium"
            return RiverRating

    def __str__(self):
        return f"River Name: {self.RiverName}. Location: {self.Location}"

    def __repr__(self):
        return "RiverDetails()"


class Permits():
    '''
    Defines a class in python, in this case the class is called 'Permits'
    '''

    def permit_application_river(self, RiverName, Fishing):
        pass


def print_river_details(self, Name, Location):
    print("Name of river: " + RiverName)
    print("Location of River" + Location)


Spey = River("River Spey", "Scotland", True)
Wye = River("River Wye", "Wales", False)
Tees = River("River Tees", "NE England", False)
Thames = River ("River Thames", "SE England", True)

print(repr(Spey))
print(str(Spey))

