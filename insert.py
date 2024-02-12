import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("insert into Employees values(1,'Faith Karimi',23,345000.00)")
conn.execute("insert into Employees values(2,'Fridah Karimi',43,300000.00)")
conn.execute("insert into Employees values(3,'Jane Muthoni',53,45000.00)")
conn.execute("insert into Employees values(4,'Shantel Omondi',20,445000.00)")
conn.execute("insert into Employees values(5,'Prudence Kirimi',21,645000.00)")

conn.commit()
print("Records inserted successfully")