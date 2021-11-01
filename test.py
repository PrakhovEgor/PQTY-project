import sqlite3
import sys





con = sqlite3.connect('engdata.db')
cur = con.cursor()
for i in con:

con.close()

#\"%s\"