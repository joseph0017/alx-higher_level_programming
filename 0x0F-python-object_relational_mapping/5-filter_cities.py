#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state
using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connect_db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3])
    mycursor = connect_db.cursor()
    sql_query = """
SELECT cities.name FROM cities
JOIN states ON cities.state_id = states.id
WHERE states.name = %s
ORDER BY cities.id ASC
"""
    mycursor.execute(sql_query,  (argv[4], ))
    query_row = mycursor.fetchall()
    print(", ".join(map(lambda x: x[0], query_row)))
    mycursor.close()
    connect_db.close()
