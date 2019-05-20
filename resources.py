import names
import random
import tile
import person
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
Base = declarative_base()

association_table = Table('resource_association'. Base.metadata,
                            Column('people', Integer, ForeignKey('people.pid')),
                            Column('tile', Integer, ForeignKey('tile.pid')),
                            Column('resources', Integer, ForeignKey('ownerID'))
                            )

class Resources(Base):
    __tablename__ = 'resources'

    id = Column(Integer, primary_key=true)
    ownerID = Column(Integer)
    wood = Column(Integer)
    iron = Column(Integer)
    #add more resources as required
