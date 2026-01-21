import sqlite3

conn=sqlite3.connect('site.db')  #sqlite will connect with the database and database create automatically

curser=conn.cursor()  #now we can write a command

curser.execute('''
create table user(
    id int primary key,
    name char not null,
    email char unique not null
)                        
''')

conn.commit()
conn.close()