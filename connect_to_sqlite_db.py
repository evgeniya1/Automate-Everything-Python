import sqlite3
import pandas as pd
#establish connection
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# #run SQL query
# print("***\n***")
# cursor.execute("SELECT * FROM 'ips' ORDER BY asn")
# print(cursor.fetchall())

# #practice querying
# print("***\n***")
# cursor.execute("SELECT address, asn FROM 'ips' ORDER BY asn")
# print(cursor.fetchall())

# #practice querying
# print("***\n***")
# cursor.execute("SELECT address, asn FROM 'ips' WHERE asn<300")
# print(cursor.fetchall())

# #run SQL query
# print("***\n***")
# df = pd.read_sql_query("SELECT * FROM 'ips' ORDER BY asn", conn)
# print(df)

# df.to_csv("save_table_from_sqlite_database.csv", index=None)

#insert data to sqlite database
new_rows = [("100.100.100.100", 'a.b.c', 10010), 
           ("200.200.200.200", 'a.b.c', 10020), 
           ("300.30.30.30", 'a.b.c', 10030)]

cursor.executemany(
    "INSERT INTO 'ips' VALUES (?, ?, ?)", new_rows)
conn.commit()

cursor.execute("SELECT * FROM 'ips'")
print(cursor.fetchall())
