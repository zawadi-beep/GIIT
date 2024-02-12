import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("DELETE FROM Employees WHERE ID = 3")
conn.commit()

cursor = conn.execute("select * from Employees")

for row in cursor:
    print("ID     :", row[0])
    print("NAME   :", row[1])
    print("AGE    :", row[2])
    print("SALARY :", row[3])

print("Deleted successfully")
conn.close()