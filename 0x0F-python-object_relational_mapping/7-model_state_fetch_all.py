#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

"""script that lists all State objects from the database hbtn_0e_6_usa"""
if __name__ == "__main__":
    # establish a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
    )

    # creates a all tables associsted with the Base metadata
    Base.metadata.create_all(engine)

    # create a new session instance bound to the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects from the database and order by states.id
    states_objs = session.query(State).all()

    # Print the State objects in the format specified
    for state in states_objs:
        print(f'{state.id}: {state.name}')

    session.close()
