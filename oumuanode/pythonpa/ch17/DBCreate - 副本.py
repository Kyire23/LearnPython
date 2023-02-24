import sqlite3
#创建SQLite数据库：c:\Pythonpa\sales.db
con = sqlite3.connect(r"c:\Pythonpa\sales.db")
#创建表：regions，包含两个列，id（主码）和name
con.execute("create table region(id primary key, name)")
