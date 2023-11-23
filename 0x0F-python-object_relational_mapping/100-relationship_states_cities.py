#!/usr/bin/python3
"""
script that creates the State “California” with the City “San Francisco” 
from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)
"""
from relationship_city import City, Base
from relationship_state import State
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # establish a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(State(name="California", cities=[City(name="San Francisco")]))
    session.commit()
