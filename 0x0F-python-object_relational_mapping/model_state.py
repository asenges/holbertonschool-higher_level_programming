#!/usr/bin/python3
"""
6. First state model
"""
from model_state import Base, State
from sqlalchemy import (create_engine)
import sys
if __name__ == "__main__":
    """
    Main Method
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
