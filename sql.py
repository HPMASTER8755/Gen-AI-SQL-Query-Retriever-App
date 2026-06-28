import sqlite3

connection=sqlite3.connect("student.db")

cursor=connection.cursor()

table_info="""
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);

"""

cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Suresh','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Drew','Data Science','A',102)''')
cursor.execute('''Insert Into STUDENT values('Vikash','DeveOps','A',50)''')
cursor.execute('''Insert Into STUDENT values('Deep','DeveOps','A',35)''')


print("The Inserted records are : ")

data=cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)


connection.commit()
connection.close()  