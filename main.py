import calendar
import streamlit as st
import pandas as pd
from index import getDaysForUser, countDaysPerMonth, add_attendance, add_employee, get_hashed_password, verify_password, countCurrentMonthDays, displayDaysForCurentMonth
from globals import connection, month_mapping
from styles import remove_black_overlay, page_bg_color, login, attendance, rainbow_divider

import plotly.express as px
from datetime import datetime



# Apply the custom CSS
st.markdown(remove_black_overlay, unsafe_allow_html=True)
st.markdown(page_bg_color, unsafe_allow_html=True)


# Streamlit app
# st.title("Login and Attendance Tracking")
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    username = st.session_state.username
    user_id = st.session_state.user_id

    # st.header("Attendance Tracking",divider='rainbow')
    # st.write(f"Welcome, {username}")

    st.markdown(attendance, unsafe_allow_html=True)
    st.markdown(rainbow_divider, unsafe_allow_html=True)

    st.sidebar.header("Welcome,")
    st.sidebar.subheader(username)
    st.sidebar.divider()

    # st.markdown(title, unsafe_allow_html=True)

    count = countCurrentMonthDays(user_id)
    st.sidebar.subheader('Current Month Count:')
    if count < 5 or count == 5:
        st.sidebar.subheader(f":red[Little Behind - {count}]")
        st.sidebar.subheader(':disappointed:')
    elif count > 5 and count <= 10:
        st.sidebar.subheader(f":orange[On Track - {count}]")
        st.sidebar.subheader(':stuck_out_tongue_closed_eyes:')
    elif count > 10 and count <= 15:
        st.sidebar.subheader(f":green[Great Job! - {count}]")
        st.sidebar.subheader(':sunglasses:')
    else:
        st.sidebar.subheader(f":blue[All Star! - {count}]")
        st.sidebar.subheader(':100:')

    # Link back to login page
    if st.sidebar.button("Back to Login"):
        st.session_state.logged_in = False



    # # Section for adding attendance
    # st.header("Add Attendance")
    # date = st.date_input("Select date of attendance")
    # if st.button("Add Attendance"):
    #     add_attendance(user_id, date)
    #     st.balloons()
    #     st.success("Attendance added successfully!")


    # Section for adding attendance
    st.header("Add Attendance")
    date = st.date_input("Select date of attendance")
    if st.button("Add Attendance"):
        add_attendance(user_id, date)

    
    # if st.button("Get Days"):
    #     result = getDaysForUser(user_id)
    #     for n in result:
    #         st.text(n)
    #         st.divider()


    tab1, tab2 = st.tabs(["Month Data", "All Time"])
    with tab1:
        # testing
        st.write("Select a month to display days")
        selected_month = st.selectbox("Select a month", list(month_mapping.keys()))
        print(month_mapping[selected_month])

        if st.button("Get Days"):
            result = displayDaysForCurentMonth(user_id, selected_month)
            dates = [date[0] for date in result]  # Extract the actual date from the result
            df = pd.DataFrame(dates, columns=['Date'])  # Create a DataFrame with only the 'Date' column
            st.dataframe(df, hide_index=True)

        # Section for counting attendance
        if st.button("Get Month Count"):
            result = countDaysPerMonth(user_id, selected_month)
            st.text(result)

    with tab2:
            # get all time days
        st.write("All Time Days")
        if st.button("Get All Days"):
            result = getDaysForUser(user_id)
            dates = [date[0] for date in result]  # Extract the actual date from the result
            df = pd.DataFrame(dates, columns=['Date'])  # Create a DataFrame with only the 'Date' column
            st.dataframe(df, hide_index=True)




else:
    # st.header("Login", divider='rainbow')
    # st.header(heading, divider='rainbow')
    # st.header("", divider='rainbow')

    st.markdown(login, unsafe_allow_html=True)
    st.markdown(rainbow_divider, unsafe_allow_html=True)

    option = st.radio("Choose an option:", ("Login", "Register"))

    # remove this
    # num = 10
    # st.subheader("This is some text. :red[" "'"+ str(num) + "'" "]")
    # st.subheader(f"This is some text: :red[{num}]")

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