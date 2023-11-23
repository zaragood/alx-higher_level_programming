#!/usr/bin/python3
""" Defines a Cityclass
    Inherits from SQLAlchemy Base and links to the MySQL table states
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

"""create the base class using declarative_base() function"""
Base = declarative_base()

"""class definition of a City and an instance Base = declarative_base()"""


class City(Base):
    """Represents a state column for a MySQL table
    __table__: the name of the table to store cities
    id: the City id
    name: the city's name
    state_id: foreign key to states.id
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
