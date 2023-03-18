#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from model_city import Base, City
from sys import argv
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
    results = session.query(City).order_by(City.id).all()
    for result in results:
        print("{}: {()} {}".format(result.states.name, result.id, result.name))
    session.close()
