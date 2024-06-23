#!/usr/bin/python3
"""deletes all State objects with a name containing the
letter a from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    args = sys.argv
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(args[1], args[2], args[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    sts = session.query(State).filter(State.name.like('%a%')).all()
    for st in sts:
        session.delete(st)
    session.commit()
    session.close()
