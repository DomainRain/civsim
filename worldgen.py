import names
import random
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import person as per
import tile
import base
from resources import Resources

engine = create_engine('sqlite:///World.db')
base.Base.metadata.create_all(engine, checkfirst=True)
Session = sessionmaker(bind=engine)

#Initialize the database, and create an engine and session for SQLAlchemy


def main():
    session = Session()
    for K in range(10):
        p = per.Person()
        p.resources = Resources() #initialize the resources object for this person
        p.resourceID = p.resources.id
        session.add(p)
    session.commit()
    #A quick test to show that everything was stored correctly
    for instance in session.query(per.Person).order_by(per.Person.pid):
        print(instance.firstName, instance.lastName, instance.resources.id)
main()
