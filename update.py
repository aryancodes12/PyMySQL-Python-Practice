import pymysql
from db import get_db


def update_grade():
    conn = cursor = None

    conn = get_db()
    cursor = conn.cursor()

    grade = input("Enter new grade: ").strip().upper()
    id = int(input("Enter id: "))

    cursor.execute(
        "UPDATE std SET grade = %s WHERE id = %s",
        (grade, id)
        )
    
    if cursor.rowcount == 0:
        print("No student with that ID - nothing was changed")
    else:
        print(f"{cursor.rowcount} student(s) updated")


update_grade()