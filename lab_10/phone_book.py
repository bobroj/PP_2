# SQL

# Create - INSERT
# Read - SELECT
# Update - UPDATE
# Delete - DELETE

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

# Create new students
cur.execute("""INSERT INTO students_data (name, phone_number) VALUES 
            ('Ruslan', '+77007007070'),
            ('Nastoyashiy Pelmen', '+77082799385'),
            ('Gudron', '+77772334510'), 
            ('Mariya', '+77077077070');
""")

conn.commit()

# Get students
#cur.execute('SELECT name, phone_number FROM students_data')

#print(cur.fetchall())

cur.execute('SELECT name, phone_number FROM students_data')

print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())


# Update students
cur.execute("""UPDATE students_data
            SET phone_number = '+73221092383'
            WHERE name = 'Ruslan';
""")

conn.commit()

# Delete students
cur.execute("""DELETE FROM students_data
            WHERE name = 'Mariya';
""") 

conn.commit()
