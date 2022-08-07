#!/usr/bin/python3
"""
5. All cities by state
"""
if __name__ == "__main__":
    """
    Main Method
    """
    import MySQLdb
    import sys
    state = sys.argv[4]
    conn = MySQLdb.connect(
                           host='localhost',
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset='utf8'
                           )
    cur = conn.cursor()
    sql = """SELECT cities.name FROM cities
             INNER JOIN states
             ON cities.state_id=states.id
             WHERE states.name = %s ORDER BY
             cities.id"""
    cur.execute(sql, (state,))
    query_rows = cur.fetchall()
    print(", ".join(i[0] for i in query_rows))
    cur.close()
    conn.close()
