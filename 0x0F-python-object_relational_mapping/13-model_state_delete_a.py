#!/usr/bin/python3
"""
13. Delete states
"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from model_state import Base, State
import sys
if __name__ == "__main__":
    """
    Main Method
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    SessionMaker = sessionmaker(bind=engine)
    session = SessionMaker()
    delete_state = session.query(State).filter(State.name.contains("%a%"))\
        .all()
    for row in delete_state:
        session.delete(row)
    session.commit()
    session.close()
