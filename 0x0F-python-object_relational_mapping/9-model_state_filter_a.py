#!/usr/bin/python3
"""
9. Contains `a`
"""
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
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
    query = session.query(State).filter(
        State.name.ilike("%a%")).order_by(State.id).all()
    for state in query:
        print("{}: {}".format(state.id, state.name))
    session.close()
