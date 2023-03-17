#!/usr/bin/python3
"""
a script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa:
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3])
    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM states WHERE states.name LIKE BINARY\
                           'N%' ORDER BY states.id ASC")
    query_rows = mycursor.fetchall()
    for row in query_rows:
        print(row)
    mycursor.close()
    connection.close()

    
