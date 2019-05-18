import names
import random
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import PersonClass as per

engine = create_engine('sqlite:///World.db')
Session = sessionmaker(bind=engine)
per.Base.metadata.create_all(engine)
#Initialize the database, and create an engine and session for SQLAlchemy


def main():
    session = Session()
    for K in range(100):
        p = per.Person()
        session.add(p)
    session.commit()
    #A quick test to show that everything was stored correctly
    for instance in session.query(per.Person).order_by(per.Person.pid):
        print(instance.firstName, instance.lastName)
main()
