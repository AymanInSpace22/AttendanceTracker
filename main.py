import streamlit as st
import mysql.connector
import bcrypt
import pandas as pd

from index import getDaysForUser, countDaysPerMonth, add_attendance, add_employee, get_hashed_password, verify_password
from globals import connection, month_mapping
from styles import remove_black_overlay, page_bg_color

# Establish MySQL connection
# connection = mysql.connector.connect(
#     host='localhost',
#     port='3306',
#     user='root',
#     password='root',  # Replace with your password
#     database='attendancedb'   # Replace with your database name
# )

# month_mapping = {
#     "JANUARY": "1999-01-01",
#     "FEBRUARY": "1999-02-01",
#     "MARCH": "1999-03-01",
#     "APRIL": "1999-04-01",
#     "MAY": "1999-05-01",
#     "JUNE": "1999-06-01",
#     "JULY": "1999-07-01",
#     "AUGUST": "1999-08-01",
#     "SEPTEMBER": "1999-09-01",
#     "OCTOBER": "1999-10-01",
#     "NOVEMBER": "1999-11-01",
#     "DECEMBER": "1999-12-01"
# }
# print(month_mapping)

# # Function to retrieve hashed password from the database
# def get_hashed_password(username):
#     cursor = connection.cursor()
#     query = "SELECT password_hash FROM employees WHERE username = %s"
#     cursor.execute(query, (username,))
#     result = cursor.fetchone()
#     cursor.close()
#     return result[0] if result else None

# # Function to verify user credentials
# def verify_password(entered_password, hashed_password):
#     return bcrypt.checkpw(entered_password.encode('utf-8'), hashed_password.encode('utf-8'))

# # Function to hash the password
# def hash_password(password):
#     return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# # Function to add an employee to the database
# def add_employee(username, password, first_name, last_name, email, department=None):
#     hashed_password = hash_password(password)
#     cursor = connection.cursor()
#     insert_query = """
#     INSERT INTO employees (username, password_hash, first_name, last_name, email, department)
#     VALUES (%s, %s, %s, %s, %s, %s)
#     """
#     cursor.execute(insert_query, (username, hashed_password, first_name, last_name, email, department))
#     connection.commit()
#     cursor.close()

# # Function to add attendance for the user
# def add_attendance(user_id, date):
#     points = 10  # Points awarded for attending
#     cursor = connection.cursor()

#     # Insert attendance record into the database
#     insert_query = """
#     INSERT INTO employee_attendance (user_id, date_in_office, points_earned)
#     VALUES (%s, %s, %s)
#     """
#     cursor.execute(insert_query, (user_id, date, points))

#     connection.commit()
#     cursor.close()

# testing this one
# def getDaysForUser(user_id):
#     cursor = connection.cursor()
#     query = "SELECT date_in_office FROM employee_attendance WHERE user_id = %s order by date_in_office desc"
#     cursor.execute(query, (user_id,))
#     result = cursor.fetchall()
#     cursor.close()
#     return result

# def countDaysPerMonth(user_id, selected_month):
#     cursor = connection.cursor()
#     #it shouls be pulling the count based on the user_id

#     # query = "SELECT COUNT(date_in_office) FROM employee_attendance WHERE MONTH(date_in_office) = MONTH('2023-10-01') AND user_id = %s"
#     query = "SELECT COUNT(date_in_office) FROM employee_attendance WHERE MONTH(date_in_office) = MONTH(" "'"+ month_mapping[selected_month] + "'" ") AND user_id = %s"
#     print(query)
#     # query = "SELECT COUNT(date_in_office) FROM employee_attendance WHERE MONTH(date_in_office) = MONTH(CURRENT_DATE())"
#     cursor.execute(query, (user_id,))
#     # result = cursor.fetchall()
#     result = cursor.fetchone()
#     cursor.close()
#     print(result)
#     return result[0]
    



# Apply the custom CSS
st.markdown(remove_black_overlay, unsafe_allow_html=True)
st.markdown(page_bg_color, unsafe_allow_html=True)

# Streamlit app
st.title("Login and Attendance Tracking")

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    username = st.session_state.username
    user_id = st.session_state.user_id

    st.write(f"Welcome, {username}")

    # Section for adding attendance
    st.header("Add Attendance")
    date = st.date_input("Select date of attendance")
    if st.button("Add Attendance"):
        add_attendance(user_id, date)
        st.balloons()
        st.success("Attendance added successfully!")

    #testing here too
    # if st.button("Get Days"):
    #     result = getDaysForUser(user_id)
    #     st.text(result)

    # if st.button("Get Days"):
    #     result = getDaysForUser(user_id)
    #     for n in result:
    #         st.text(n)
    #         st.divider()

    if st.button("Get Days"):
        result = getDaysForUser(user_id)
        dates = [date[0] for date in result]  # Extract the actual date from the result
        df = pd.DataFrame(dates, columns=['Date'])  # Create a DataFrame with only the 'Date' column
        st.dataframe(df)


    selected_month = st.selectbox("Select a month", list(month_mapping.keys()))
    print(month_mapping[selected_month])
    if st.button("Get Days Count"):
        result = countDaysPerMonth(user_id, selected_month)
        st.text(result)


    # if selected_month:
    #     st.write(f"The value for {selected_month} is: {month_mapping[selected_month]}")
        

    # Link back to login page
    if st.button("Back to Login"):
        st.session_state.logged_in = False

    

else:
    option = st.radio("Choose an option:", ("Login", "Register"))

    if option == "Login":
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            stored_hashed_password = get_hashed_password(username)

            if stored_hashed_password and verify_password(password, stored_hashed_password):
                cursor = connection.cursor()
                query = "SELECT user_id FROM employees WHERE username = %s"
                cursor.execute(query, (username,))
                user_data = cursor.fetchone()
                cursor.close()
                
                if user_data:
                    user_id = user_data[0]
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.session_state.user_id = user_id
                    st.success("Logged in successfully!")
                else:
                    st.error("Invalid username or password")
            else:
                st.error("Invalid username or password")

    elif option == "Register":
        st.title("Employee Registration")
        reg_username = st.text_input("Username")
        reg_password = st.text_input("Password", type="password")
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email")
        department = st.text_input("Department (Optional)")

        if st.button("Register"):
            add_employee(reg_username, reg_password, first_name, last_name, email, department)
            st.success("Employee registered successfully!")