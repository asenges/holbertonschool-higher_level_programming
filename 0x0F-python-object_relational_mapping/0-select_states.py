#!/usr/bin/python3
"""
0. Get all states
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """ 
    Main method
    """
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                           passwd=passwd, db=db, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
