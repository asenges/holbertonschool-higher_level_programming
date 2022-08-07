#!/usr/bin/python3
"""
3. SQL Injection...
"""
if __name__ == "__main__":
    """
    Main Method
    """
    import MySQLdb
    import sys
    state = str(sys.argv[4])
    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8"
                           )
    cur = conn.cursor()
    sql = """SELECT * FROM states WHERE name LIKE BINARY '{}'
          ORDER BY id""".format(state)
    cur.execute(sql)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
