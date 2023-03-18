
#!/usr/bin/python3
"""
a python file that contains the class definition of a State
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class State(Base):
    """
    a blueprint for the states table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    
    cities = relationship(
        "City",
        cascade="all, delete-orphan",
        backref=backref("state", cascade="all"),
        single_parent=True
