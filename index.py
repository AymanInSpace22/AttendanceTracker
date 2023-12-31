import bcrypt
from globals import connection, month_mapping



# Function to retrieve hashed password from the database
def get_hashed_password(username):
    cursor = connection.cursor()
    query = "SELECT password_hash FROM employees WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else None

# Function to verify user credentials
def verify_password(entered_password, hashed_password):
    return bcrypt.checkpw(entered_password.encode('utf-8'), hashed_password.encode('utf-8'))

# Function to hash the password
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Function to add an employee to the database
def add_employee(username, password, first_name, last_name, email, department=None):
    hashed_password = hash_password(password)
    cursor = connection.cursor()
    insert_query = """
    INSERT INTO employees (username, password_hash, first_name, last_name, email, department)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (username, hashed_password, first_name, last_name, email, department))
    connection.commit()
    cursor.close()

# Function to add attendance for the user
def add_attendance(user_id, date):
    points = 10  # Points awarded for attending
    cursor = connection.cursor()

    # Insert attendance record into the database
    insert_query = """
    INSERT INTO employee_attendance (user_id, date_in_office, points_earned)
    VALUES (%s, %s, %s)
    """
    cursor.execute(insert_query, (user_id, date, points))

    connection.commit()
    cursor.close()

def getDaysForUser(user_id):
    cursor = connection.cursor()
    query = "SELECT date_in_office FROM employee_attendance WHERE user_id = %s order by date_in_office desc"
    cursor.execute(query, (user_id,))
    result = cursor.fetchall()
    cursor.close()
    return result


def countDaysPerMonth(user_id, selected_month):
    cursor = connection.cursor()
    #it shouls be pulling the count based on the user_id

    # query = "SELECT COUNT(date_in_office) FROM employee_attendance WHERE MONTH(date_in_office) = MONTH('2023-10-01') AND user_id = %s"
    query = "SELECT COUNT(date_in_office) FROM employee_attendance WHERE MONTH(date_in_office) = MONTH(" "'"+ month_mapping[selected_month] + "'" ") AND user_id = %s"
    print(query)
    # query = "SELECT COUNT(date_in_office) FROM employee_attendance WHERE MONTH(date_in_office) = MONTH(CURRENT_DATE())"
    cursor.execute(query, (user_id,))
    # result = cursor.fetchall()
    result = cursor.fetchone()
    cursor.close()
    print(result)
    return result[0]
    