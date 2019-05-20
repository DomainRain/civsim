import names
import random
import sqlite3
import resources
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Person(Base):
    __tablename__ = 'people'

    children = relationship("Children")
    resources = relationship("Resources")

    pid = Column(Integer, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)
    sex = Column(Integer) #0 for female, 1 for male
    age = Column(Integer)
    desperation = Column(Integer)
    gay = Column(Integer)
    strength = Column(Integer)
    dexterity = Column(Integer)
    constitution = Column(Integer)
    intelligence = Column(Integer)
    wisdom = Column(Integer)
    charisma = Column(Integer)
    priorityStat = Column(String)
    fatherID = Column(Integer)
    motherID = Column(Integer)
    resourceID = Column(Integer, ForeignKey('resources.id'))


    def __init__(self, lastName=None):
        """The standard constructor will create an average person that has
        no parents. This is used soley during world creation.

        If the lastName argument is supplied, then this new person is assumed
        to have been born though parents, and will inherit the last name
        supplied.

        @args
        lastName(optional): Will give the new person the last name supplied.
        """
        random.seed()
        stats = list(("strength",
                    "dexterity",
                    "constitution",
                    "intelligence",
                    "wisdom",
                    "charisma"))
        self.priorityStat = stats[random.randint(0,5)]
        #Select the stat to prioritize from the list of possible stats
        self.sex = random.randint(0,1)
        #The person will be either a male or female
        if (self.sex == 0):
            self.firstName = names.get_first_name(gender='female')
        elif (self.sex == 1):
            self.firstName = names.get_first_name(gender='male')
        #Select a first name based on thier sex
        if(random.randint(1,100) == 1):
            self.gay = 1
        else:
            self.gay = 0
        if(lastName == None):
            self.age = random.randint(18,30)
            self.lastName = names.get_last_name()

            if self.age >= 18 and self.age <= 21:
                self.desperation = 0
            elif self.age >= 22 and self.age <= 25:
                self.desperation = 1
            elif self.age >=26:
                self.desperation = 2
        else:
            self.age = 0
            self.lastName = lastName
            p3.desperation = 0

        self.strength = random.randint(9,12)
        self.dexterity = random.randint(9,12)
        self.constitution = random.randint(9,12)
        self.intelligence = random.randint(9,12)
        self.wisdom = random.randint(9,12)
        self.charisma = random.randint(9,12)
        #Let the stats get generated randomly evertime, the fuck method will modify them afterwards.
        self.resources = resources.Resources() #initialize the resources table
        self.resourceID = self.resources.id
    def fuck(self, p2):
        """Two people engage in the art of babymaking to create a new person.
        @args
        p2: The lucky person who's getting thier night rocked.
        """
        p3 = Person(self.lastName)
        if(self.sex == 1):
            p3.fatherID = self.pid
            p3.motherID = p2.pid
        else:
            p3.fatherID = p2.pid
            p3.motherID = self.pid
        self.children = Children(pid=self.pid, childID=p3.pid)
        p2.children = Children(pid=self.pid, childID=p3.pid)
        #create entries in the children database for both parents and add the child to the ChildID field
        p3.strength = random.randint(min(self.strength, p2.strength), max(self.strength, p2.strength))
        p3.dexterity = random.randint(min(self.dexterity, p2.dexterity), max(self.dexterity, p2.dexterity))
        p3.constitution = random.randint(min(self.constitution, p2.constitution), max(self.constitution, p2.constitution))
        p3.intelligence = random.randint(min(self.intelligence, p2.intelligence), max(self.intelligence, p2.intelligence))
        p3.wisdom = random.randint(min(self.wisdom, p2.wisdom), max(self.wisdom, p2.wisdom))
        p3.charisma = random.randint(min(self.charisma, p2.charisma), max(self.charisma, p2.charisma))
        return p3
        #Modify the stats of the new person such that it is between the parents' stats
class Children(Base):
    """Keeps track of a parent's child. Is called automatically when a child
    is born, and should not be called manually.
    """
    __tablename__ = 'children'

    tid = Column(Integer, primary_key=True) #unique id for this table. Is not needed for anything else
    pid = Column(Integer, ForeignKey('people.pid')) #the ID of the parent
    childID = Column(Integer) #the ID of the child
