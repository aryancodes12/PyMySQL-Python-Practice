import pymysql
from db import get_db

conn = get_db()
cursor = conn.cursor()


try:
    while True:
        query = "INSERT INTO std (name, age, class, email, grade) VALUES (%s, %s, %s, %s, %s)"
        name = input("Enter name: ")
        age = input("Enter age: ")
        dept = input("Enter department: ")
        email = input("Enter email: ")
        grade = input("Enter grade: ")

        values = (name, age, dept, email, grade)

        cursor.execute(query, values)

        print("New Row added succesfully!")
        print(f"Last Row_ID: {cursor.lastrowid}\n")
        confirm = input("Want to add more? ('y'/'n')")
        if confirm == 'n':
            break
except pymysql.err.IntegrityError as e:
    print(f"Duplicate Value: {e}")

finally:
    cursor.close()
    conn.close()