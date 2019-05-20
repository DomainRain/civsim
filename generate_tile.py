import random
import sqlite3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class grid(Base):
    __tablename__ = 'Tile'

    tid = Column(Integer, primary_key=True)
    x = Column(Integer)
    y = Column(Integer)
    type = Column(String)

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
