import pymysql
from db import get_db

print("step 1: importing done")

try:
    conn = get_db()
    print("connected!")
    print("Server version: ", conn.get_server_info())

    cursor= conn.cursor()
    cursor.execute("SELECT * FROM std")
    rows = cursor.fetchall()
    print("Rows Fetched: ", len(rows))

    for r in rows:
        print(" -", r)

    cursor.close()
    conn.close()
    print("Connection closed")

except pymysql.MySQLError as e:
    print(f"MySQL error: {e}")
