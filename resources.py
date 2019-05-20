import names
import random
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship
from base import Base

class Resources(Base):
    __tablename__ = 'resources'

    id = Column(Integer, primary_key=True)
    wood = Column(Integer)
    iron = Column(Integer)
    flint = Column(Integer)
    berries = Column(Integer)
    meat = Column(Integer)
    axe = Column(Integer)
    pickaxe = Column(Integer)
    hoe = Column(Integer)
    bow = Column(Integer)
    arrows = Column(Integer)
    #add more resources as required
