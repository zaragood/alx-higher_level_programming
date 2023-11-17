#!/usr/bin/python3
""" Defines a State class
    Inherits from SQLAlchemy Base and links to the MySQL table states
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

"""create the base class using declarative_base() function"""
Base = declarative_base()

"""class definition of a State and an instance Base = declarative_base()"""


class State(Base):
    """Represents a state column for a MySQL table
    __table__: the name of the table to store states
    id: the states id
    name: the state's name
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
