from db import get_db
import pymysql


def get_student_by_name():
    conn = cursor = None
    try:
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
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


get_student_by_name()
# conn = get_db()

# cursor = conn.cursor()
# while True:
    # name = input("Enter name to search or 'q' to exit: ")
    # if name == 'q':
    #     break

    # query = f"SELECT * FROM std WHERE name = %s"
    # cursor.execute(query, (name,))
    # std = cursor.fetchone()

    # if std:
    #     print(f"\nName: {std['name']}")
    #     print(f"Age: {std['age']}")
    #     print(f"Class: {std['class']}")
    #     print(f"Email: {std['email']}")
    # else:
    #     print('Student not found')

# cursor.close()
# conn.close()



def get_grade_a_students(grade):
    conn = cursor = None
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name, age, grade FROM std WHERE grade = %s",
            (grade)
        )
        students = cursor.fetchall()
        if not students:
            print(f"No student found with grade {grade}")
        else:
            for s in students:
                print(f"{s['name']} - age {s['age']}")
            return students
    
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
        return []
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# get_grade_a_students("A")