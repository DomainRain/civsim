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
    #add more resources as required
