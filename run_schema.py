import sqlite3

with open("schema.sql") as f:
    sql = f.read()

conn = sqlite3.connect("sales.db")
conn.executescript(sql)
conn.close()

print("✅ sales.db created with products & sales tables")
