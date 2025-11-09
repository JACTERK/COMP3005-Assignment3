# COMP 3005 Assignment 3
# Jacob Terkuc -- 101196620
# November 9th, 2025

import psycopg

config = {
    "host": "IP",
    "port": 5432, # Default postgres port
    "dbname": "DATABASE_NAME",
    "user": "USERNAME",
    "password": "PASSWORD",
}

# getAllStudents takes in no variables and returns a list of students, or an empty list if the connection was
# unsuccessful.
def getAllStudents() -> list:
    # The 'try/except/finally' loop ensures that the app won't crash if the connection was unable to be made, and
    # cleans up the connection.
    try:
        conn = psycopg.connect(
            host=config["host"],
            port=config["port"],
            dbname=config["dbname"],
            user=config["user"],
            password=config["password"],
        )

        with conn.cursor() as cursor:
            # Get all columns from the 'students' table.
            cursor.execute("SELECT * FROM students;")

            # Set to the 'data' variable
            data = cursor.fetchall()

            # Close the cursor.
            cursor.close()

            return data


    except psycopg.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return []

    finally:
        # If the connection was successful, close the connection after the function executes fully.
        if 'conn' in locals() and conn:
            conn.close()


# addStudent takes a first_name, last_name, email and enrollment_date, and uses those to create a new student record
# in the 'students' table. Returns a boolean to indicate success or failure.
def addStudent(first_name, last_name, email, enrollment_date):
    # The 'try/except/finally' loop ensures that the app won't crash if the connection was unable to be made, and
    # cleans up the connection.
    try:
        conn = psycopg.connect(
            host=config["host"],
            port=config["port"],
            dbname=config["dbname"],
            user=config["user"],
            password=config["password"],
        )

        with conn.cursor() as cursor:

            # Insert a new student into the table using the variables provided. psycopg does the value conversion.
            cursor.execute("INSERT INTO students(first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                           (first_name, last_name, email, enrollment_date))

            # Check if any changes were made (if not, we assume that there is likely a duplicate error on the email)
            if cursor.rowcount == 0:
                print(f"Warning: Issue adding student {first_name} {last_name} to database")

            # Commit the changes to the database.
            conn.commit()

            # Close the cursor.
            cursor.close()


    except psycopg.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")

    finally:
        # If the connection was successful, close the connection after the function executes fully.
        if 'conn' in locals() and conn:
            conn.close()


def updateStudentEmail(student_id, email):
    # The 'try/except/finally' loop ensures that the app won't crash if the connection was unable to be made, and
    # cleans up the connection.
    try:
        conn = psycopg.connect(
            host=config["host"],
            port=config["port"],
            dbname=config["dbname"],
            user=config["user"],
            password=config["password"],
        )

        with conn.cursor() as cursor:
            # Update the student with 'student_id''s email address using the provided 'email'.
            cursor.execute("UPDATE students SET email = %s WHERE student_id = %s", (email, student_id))

            # Check if any rows were changed (if not, we assume that there was no student 'student_id'.
            if cursor.rowcount == 0:
                print(f"Warning: student '{student_id}' not found, could not complete update email operation.")

            # Commit the changes
            conn.commit()

            # Close the cursor.
            cursor.close()


    except psycopg.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return []

    finally:
        # If the connection was successful, close the connection after the function executes fully.
        if 'conn' in locals() and conn:
            conn.close()


def deleteStudent(student_id):
    # The 'try/except/finally' loop ensures that the app won't crash if the connection was unable to be made, and
    # cleans up the connection.
    try:
        conn = psycopg.connect(
            host=config["host"],
            port=config["port"],
            dbname=config["dbname"],
            user=config["user"],
            password=config["password"],
        )

        with conn.cursor() as cursor:
            # Delete the user
            s = cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))

            # Check if any rows were changed (if not, we assume that there was no matching 'student_id')
            if cursor.rowcount == 0:
                print(f"Warning: student '{student_id}' not found, could not complete deletion operation.")

            # Commit the changes.
            conn.commit()

            # Close the cursor.
            cursor.close()


    except psycopg.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")

    finally:
        # If the connection was successful, close the connection after the function executes fully.
        if 'conn' in locals() and conn:
            conn.close()


if __name__ == "__main__":
    input("Initial Database Contents (Using getAllStudents() function)")
    students = getAllStudents()
    for student in students:
        print(f"{student}")
    print()

    input("Add a new student: (John Pork, john.pork@example.com, 2023-09-01)")
    addStudent('John', 'Pork', 'john.pork@gmail.com', '2023-09-01')

    print("Database containing the new student (Using getAllStudents() function)")
    students = getAllStudents()
    for student in students:
        print(f"{student}")
    print()

    input("Update student email: (John Pork (Student ID 4), john.pork@hotmail.com)")
    updateStudentEmail('4', 'john.pork@hotmail.com')

    print("Database containing the updated student email (Using getAllStudents() function)")
    students = getAllStudents()
    for student in students:
        print(f"{student}")
    print()

    input("Delete student: (John Pork (Student ID 4))")
    deleteStudent('4')

    print("Database containing the deleted student (Using getAllStudents() function)")
    students = getAllStudents()
    for student in students:
        print(f"{student}")
    print()