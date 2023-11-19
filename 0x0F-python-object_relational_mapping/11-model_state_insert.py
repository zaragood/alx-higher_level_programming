#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
from model_state import Base, State
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

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

    # create an instance to be added
    new_state = State(name='Louisiana')

    session.add(new_state)
    session.commit()

    print(new_state.id)
