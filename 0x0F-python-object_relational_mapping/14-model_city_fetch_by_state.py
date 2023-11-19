#!/usr/bin/python3
"""script 14-model_city_fetch_by_state.py that prints all
City objects from the database hbtn_0e_14_usa:
"""
from model_state import Base, State
from model_city import City
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

"""script that lists all City objects from the database hbtn_0e_6_usa"""
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

    # Query all City objects from the database and order by states.id
    query = session.query(City, State)
    states = query.filter(City.state_id == State.id).order_by(City.id)

    # Print the State objects in the format specified
    for city, state in states:
        print(f'{state.name}: ({city.id}) {city.name}')

    session.close()
