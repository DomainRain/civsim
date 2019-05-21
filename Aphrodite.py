import sqlite3
import sqlalchemy
import person



def MatchMaker(session):
    singles = []
    for name in session.query(person.Person).\
        filter(person.Person.married == None):
        singles.append(name)
    for single in singles:
        for suitor in singles:
            if((single == suitor) or (single.married != None) or (suitor.married != None)):
                continue
            if(single.gay):
                if(single.sex == suitor.sex):
                    if(getattr(suitor, single.priorityStat) >= getattr(single, single.priorityStat) - single.desperation):
                        single.married = suitor.pid
                        suitor.married = single.pid
                        print(single.firstName + " got married to " + suitor.firstName)
            else:
                if((single.sex != suitor.sex) and (suitor.gay == 0)):
                    if(getattr(suitor, single.priorityStat) >= getattr(single, single.priorityStat) - single.desperation):
                        single.married = suitor.pid
                        suitor.married = single.pid
                        print(single.firstName + " got married to " + suitor.firstName)
    session.add_all(singles)
    session.commit()
