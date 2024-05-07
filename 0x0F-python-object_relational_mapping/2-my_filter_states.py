#!/usr/bin/python3
'''
import MySQLdb and the sys
module that will help in
getting the args
Arg : username
      password
      database name
'''
import MySQLdb
import sys


if __name__ == "__main__":
    '''
    The main function that connects to the MySQL database,
    retrieves data, and prints it.
    '''
    try:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
    except MySQLdb.Error:
        print("Connection Error")
    cur = conn.cursor()
    try:
        search_name = sys.argv[4]
        cur.execute(
            """SELECT * FROM states
            WHERE BINARY name = '{}'
            ORDER BY states.id""".format(search_name))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error:
        print("Unable to execute!")
    finally:
        cur.close()
        conn.close()
