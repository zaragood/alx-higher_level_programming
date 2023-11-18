#!/usr/bin/python3
from model_state import Base, State
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

"""script that lists all State objects from the database hbtn_0e_6_usa"""
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    states_objs = session.query(State).all()

    for state in states_objs:
        print(f'{state.id}: {state.name}')
