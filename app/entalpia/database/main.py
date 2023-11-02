import sqlite3

try:
    conn = sqlite3.connect('./database.sqlite3')
    print("Database connection established")
except Exception as e:
    print("Database connection failed: ")
    print(e)
