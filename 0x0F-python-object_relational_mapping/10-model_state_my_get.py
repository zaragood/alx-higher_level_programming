#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

"""script that prints the State object with the name passed as
    argument from the database hbtn_0e_6_usa
"""
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
    states_obj = session.query(State).filter_by(name=sys.argv[4]).first()

    # Print the State objects in the format specified
    if states_obj is None:
        print('Not found')
    else:
        print(f'{states_obj.id}')

    session.close()
