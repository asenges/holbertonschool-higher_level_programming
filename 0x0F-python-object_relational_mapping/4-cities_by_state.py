#!/usr/bin/python3
"""
4. Cities by states
"""
if __name__ == "__main__":
    """
    Main Method
    """
    import MySQLdb
    import sys
    conn = MySQLdb.connect(
                           host='localhost',
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8"
                           )
    cur = conn.cursor()
    sql = """SELECT cities.id, cities.name, states.name
             FROM cities INNER JOIN states ON
             cities.state_id=states.id"""
    cur.execute(sql)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
