#!/usr/bin/python3
"""import sys and MySQLdb"""
import sys
import MySQLdb

def list_all_states(mysql_username, mysql_password, mysql_database):
    """make a connection to mysql server to make a connection to the database"""
    try:
        mysql_connection = MySQLdb.connect(host='localhost', user=mysql_username, port=3306, db=mysql_database, passwd= mysql_password)
        
        """creat a cursor object"""
        cur = mysql_connection.cursor()

        """execute the SELECT"""
        cur.execute("SELECT * FROM states ORDER BY states.id ASC")
        states = cur.fetchall()

        for state in states:
            print("(%s, '%s')" % state)

        """cleanup"""
        mysql_connection.close()
        cur.close()
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")      

if __name__ == "__main__":
    """check if the correct command-line argument is passed"""
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <mysql_database>")
        sys.exit(1)

    """extract command-line arguments"""
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_database = sys.argv[3]

    list_all_states(mysql_username, mysql_password, mysql_database)
