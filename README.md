# PyMySQL_Python

A small Python sample project demonstrating how to connect to a MySQL database using `PyMySQL`, insert student records, query students, update grades, and delete records.

## Project files

- `config.py` - MySQL connection settings.
- `db.py` - Database helper that creates a `PyMySQL` connection using settings from `config.py`.
- `connect.py` - Example script to connect to the database and fetch all rows from the `std` table.
- `insert.py` - Interactive script to insert new student records into the `std` table.
- `select.py` - Interactive script to look up a student by name.
- `update.py` - Interactive script to update a student's grade by ID.
- `delete.py` - Script that deletes a student record by ID.

## Requirements

- Python 3.x
- `PyMySQL`
- MySQL server running locally
- A MySQL database named `school` with a table named `std`

### Example `std` table schema

```sql
CREATE DATABASE IF NOT EXISTS school;
USE school;

CREATE TABLE IF NOT EXISTS std (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT,
    class VARCHAR(255),
    email VARCHAR(255),
    grade VARCHAR(5)
);
```

## Setup

1. Activate your Python environment if using a virtual environment.
2. Install dependencies:

```bash
pip install pymysql
```

3. Update `config.py` if your MySQL credentials or database settings differ.

## Usage

- Run `connect.py` to verify the database connection and list all rows from `std`.

```bash
python connect.py
```

- Run `insert.py` to add new student records interactively.

```bash
python insert.py
```

- Run `select.py` to query a student by name interactively.

```bash
python select.py
```

- Run `update.py` to update a student's grade by ID.

```bash
python update.py
```

- Run `delete.py` to delete a student record by ID.

```bash
python delete.py
```

## Notes

- `db.py` uses `DictCursor` so query results are returned as dictionaries.
- `insert.py` commits automatically via `autocommit=True`.
- `insert.py` prompts for name, age, department (`class`), email, and grade.
- `select.py` searches the `std` table by student name.
- If your MySQL password, host, or database name change, update `config.py` accordingly.
