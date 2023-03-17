#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connect_db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3])
    mycursor = connect_db.cursor()
    sql_query = """
SELECT * FROM cities
JOIN states ON cities.id = states.id
ORDER BY cities.id ASC
"""
    mycursor.execute(sql_query)
    query_rows = mycursor.fetchall()
    for result in query_rows:
        print(result)
    mycursor.close()
    connect_db.close()
