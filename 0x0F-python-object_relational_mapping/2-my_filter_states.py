#!/usr/bin/python3
"""Filter states by user input"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connect_db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3])
    mycursor = connect_db.cursor()
    sql_query = """
    SELECT * FROM states WHERE name LIKE '{}' ORDER BY states.id ASC"""
    format_query = sql_query.format(argv[4])
    mycursor.execute(format_query)
    query_rows = mycursor.fetchall()
    for results in query_rows:
        print(results)
    mycursor.close()
    connect_db.close()
