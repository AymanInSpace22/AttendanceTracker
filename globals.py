import mysql.connector

# Establish MySQL connection
connection = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='root', 
    database='attendancedb'   
)

month_mapping = {
    "JANUARY": "1999-01-01",
    "FEBRUARY": "1999-02-01",
    "MARCH": "1999-03-01",
    "APRIL": "1999-04-01",
    "MAY": "1999-05-01",
    "JUNE": "1999-06-01",
    "JULY": "1999-07-01",
    "AUGUST": "1999-08-01",
    "SEPTEMBER": "1999-09-01",
    "OCTOBER": "1999-10-01",
    "NOVEMBER": "1999-11-01",
    "DECEMBER": "1999-12-01"
}

print(month_mapping)
