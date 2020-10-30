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

    def FishingIssue(self):
        
        print("Name of river: " + RiverName)
        print("Location of River" + Location)

        if self.Fishing is True:
          return f"{self.RiverName} has fishing so be wary of fishermen"
        else:
          return f"{self.RiverName} has no fishing so have fun!"

    def PermitApplicationRiver(self, RiverName, Fishing):
        pass


class RiverDetails(River):

    def __init__(self, RiverLength, Grade):
        self.RiverLength = RiverLength
        self.Grade = Grade
        super().__init__(RiverName, Location, Fishing)  # noqa: F821

    print("Name of river: " + RiverName)
    print("Location of River" + Location)

    def Rating(self):
        if self.Grade > 3:
            return f"{self.RiverName} is rated Extreme"
        elif self.Grade == 3:
            return f"{self.RiverName} is rated HARD!"
        elif self.Grade < 3:
            return f"{self.RiverName} is rated Easy!"

    def __str__(self):
        return f"River Name: {self.RiverName}. Location: {self.Location}"

    def __repr__(self):
        return "RiverDetails()"


Spey = River("River Spey", "Scotland", True)
Wye = River("River Wye", "Wales", False)
Tees = River("River Tees", "NE England", False)
Thames = River ("River Thames", "SE England", True)

print(repr(Spey))
print(str(Spey))

