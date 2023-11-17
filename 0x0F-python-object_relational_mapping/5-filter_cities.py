#!/usr/bin/python3
"""import sys and MySQLdb"""
import sys
import MySQLdb

if __name__ == "__main__":
    """make a connection to the database hbtn_0e_0_usa"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    """creat a cursor object"""
    cur = db.cursor()

    """execute the SELECT query"""
    cur.execute("SELECT c.name FROM cities as c \
                INNER JOIN states as s ON c.state_id = s.id \
                WHERE s.name = %s", (sys.argv[4],))
    states = cur.fetchall()

    """list all states from the  table"""
    print(", ".join([city[0] for city in states]))

    cur.close()
    db.close()
