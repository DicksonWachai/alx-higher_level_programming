#!/usr/bin/python3
'''
importing MySQLdb and sys for
the command line args
'''
import MySQLdb
import sys


def main():
    '''
    The main function that connects to the MySQL database,
    retrieves data, and prints it.
    '''
    try:
        username = sys.argv[1]
        passwd = sys.argv[2]
        database_name = sys.argv[3]
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=passwd,
            db=database_name)
        cur = db.cursor()
        cur.execute("SELECT * from states ORDER BY states.id")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
