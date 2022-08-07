#!/usr/bin/python3
"""
10. Get a state
"""
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys
if __name__ == "__main__":
    """
    Main Method
    """
    param = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    SessionMaker = sessionmaker(bind=engine)
    session = SessionMaker()
    state = session.query(State).filter(
        State.name.like(param)).first()
    if state is None:
        print("Not found")
    print(state.id)
    session.close()
