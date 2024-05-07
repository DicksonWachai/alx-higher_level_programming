#!/usr/bin/python3
"""
A script that connects to a MySQL database
and retrieves cities in a state.

"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connects to a MySQL database and retrieves states matching a given name.

    Args:
         <username> <password> <database> <state_name>
    """
    try:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
    except MySQLdb.Error as e:
        print(f"Connection error {e}")

    cur = conn.cursor()
    state_name = sys.argv[4]
    try:
        cur.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON\
                cities.state_id=states.id\
                WHERE states.name=%s\
                ORDER BY cities.id", (state_name,))
        rows = cur.fetchall()
        cities_name = ', '.join(row[0] for row in rows)
        print(cities_name)
    except MySQLdb.Error as e:
        print(f"Execution failed {e}")
    finally:
        cur.close()
        conn.close()
