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
    name = sys.argv[3]
    state = sys.argv[4]
    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8"
                           )
    cur = conn.cursor()
    sql = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cur.execute(sql, (state,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
