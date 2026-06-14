from db import get_db

conn = get_db()

cursor = conn.cursor()
while True:
    name = input("Enter name to search or 'q' to exit: ")
    if name == 'q':
        break

    query = f"SELECT * FROM std WHERE name = %s"
    cursor.execute(query, (name,))
    std = cursor.fetchone()

    if std:
        print(f"\nName: {std['name']}")
        print(f"Age: {std['age']}")
        print(f"Class: {std['class']}")
        print(f"Email: {std['email']}")
    else:
        print('Student not found')

cursor.close()
conn.close()