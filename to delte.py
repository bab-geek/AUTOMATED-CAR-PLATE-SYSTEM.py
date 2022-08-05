from time import gmtime, strftime

import sqlite3

connection = sqlite3.connect("parking.db")
y = ("Hello")
x = strftime("%Y-%m-%d %H:%M:%S")
connection.execute("INSERT INTO LOGS (`numberPlate`,`time`) VALUES(?,?)", (y, x))
connection.commit()
print('Log Added')
connection.close()