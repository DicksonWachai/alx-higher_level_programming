#!/usr/bin/python3
"""
A script that connects to a MySQL database
and retrieves states matching a given name.

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
            db=sys.argv[3])
    except MySQLdb.Error as e:
        print(f"Connection failed: {e}")

    cur = conn.cursor()
    search_name = sys.argv[4]
    try:
        cur.execute("""SELECT * from states WHERE name=%s ORDER BY\
                states.id""", (search_name,))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print(f"Execution failed: {e}")
    finally:
        cur.close()
        conn.close
