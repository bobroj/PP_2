# CSV - Comma Separated Values
# file format, where each line represents one row (one entity or tuple)
# and each comma separates one column (or attribute for the particular entity)

import psycopg2

# Connect to the database by creating a connection object
conn = psycopg2.connect(
    host='localhost', 
    dbname='students', 
    user='postgres', 
    password='12345'
    )

# Create a cursor to work with the database
cur = conn.cursor()

# Delete table
cur.execute('DROP TABLE students_data;')

conn.commit()

# Create a new table
cur.execute("""CREATE TABLE students_data (
            name VARCHAR(255),
            phone_number VARCHAR(255) PRIMARY KEY
);
""")

conn.commit()

import csv

filename = 'phone_book.csv'

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        name, phone_number = row
        
        # Create new students
        cur.execute(f"""INSERT INTO students_data (name, phone_number) VALUES 
                    ('{name}', '{phone_number}');
        """)

        conn.commit()
