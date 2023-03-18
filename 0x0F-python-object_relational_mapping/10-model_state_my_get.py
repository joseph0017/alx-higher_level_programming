#!/usr/bin/python3
"""
displays the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
      'mysql+mysqldb://{}:{}@localhost/{}'
      .format(argv[1], argv[2], argv[3]),
      pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    search_state = argv[4]
    for state in session.query(State)\
            .filter(State.name.contains(search_state)).order_by(State.id).all():
        if state:
            print(state.id)
        elif(state != search_state):
            print("Not found")
    session.close()
    
