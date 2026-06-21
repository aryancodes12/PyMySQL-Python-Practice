from db import get_db

conn = get_db()
cursor = conn.cursor()

cursor.execute(
    "UPDATE std SET age = %s WHERE id = %s",
    (20, 5)
)

if cursor.rowcount == 0:
    print("No student with that ID - nothing was changed")
else:
    print(f"{cursor.rowcount} student(s) updated")