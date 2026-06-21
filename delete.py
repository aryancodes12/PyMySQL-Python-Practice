from db import get_db

def delete_std(std_id: int)-> bool:
    conn = cursor  = None

    try:
        conn = get_db()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM std WHERE id = %s",
            (std_id,)
        )

        student = cursor.fetchone()

        if not student:
            print(f"No student with id {std_id}")
            return False
        
        cursor.execute(
            "DELETE FROM std WHERE id = %s",
            (std_id,)
        )

        print(f"DELETED: {student['name']}")
        return True
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

delete_std(5)
delete_std(9)