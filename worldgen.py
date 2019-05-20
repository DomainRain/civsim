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
        session.add(p)
    for J in range(10):
        t = tile.Tile(x=J, y=0, type="beach")
        session.add(t)
    session.commit()
    #A quick test to show that everything was stored correctly
    for instance in session.query(per.Person).order_by(per.Person.pid):
        print(instance.firstName, instance.lastName, instance.resources.id)
    for instance in session.query(tile.Tile).order_by(tile.Tile.tid):
        print(instance.x, instance.y, instance.resources.id)
main()
