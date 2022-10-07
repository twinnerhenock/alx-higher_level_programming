#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=MY_USER, passwd=MY_PASS, db=MY_DB)
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id")
    print (id, '%s') % c.fetchone()