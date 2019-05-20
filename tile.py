import random
import sqlite3
import resources
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class Tile(Base):
    __tablename__ = 'Tile'

    resources = relationship('Resources')

    tid = Column(Integer, primary_key=True)
    x = Column(Integer)
    y = Column(Integer)
    type = Column(String)
    resourceID = Column(Integer, ForeignKey('resources.id'))


    def __init__(self, x, y, type):
        types = list(("deepwater",
                     "water",
                     "beach",
                     "plains",
                     "forest",
                     "hills",
                     "rocky hills",
                     "snow"))
        self.type = types[random.randint(0,7)]
        #this is a place holder till map gen in unity and python come together

        self.x = x
        self.y = y
        self.type = type
        self.resources = resources.Resources() #initialize the resources table
        self.resourceID = self.resources.id

        #TODO: Put resource generation here
