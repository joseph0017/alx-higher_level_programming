#!/usr/bin/python3
"""python script which is free from SQL injections"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connect_db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3])
    mycursor = connect_db.cursor()
    sql_query = """
SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"""
    mycursor.execute(sql_query, (argv[4], ))
    query_rows = mycursor.fetchall()
    for result in query_rows:
        print(result)
    mycursor.close()
    connect_db.close
