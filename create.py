import sqlite3
conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute('''create table Employees(
ID int primary key not null ,
NAME text not null ,
AGE int not null ,
SALARY real not null 
);''')

print("Table created successfully")
conn.close()