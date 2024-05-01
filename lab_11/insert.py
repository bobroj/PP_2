import psycopg2
from psycopg2 import extras

# Параметры подключения к базе данных
conn_params = "dbname='students' user='postgres' host='localhost' password='12345'"

# Данные для вставки
contacts = [
    ('Petrov', '+78743337323'),
    ('Vasiliy', '+77000225100'),
    ('Slava ne svarshik', '+77000093259')
]

# SQL-запрос для вставки данных
sql = "INSERT INTO students_data (name, phone_number) VALUES %s"

# Установка соединения и выполнение запроса
with psycopg2.connect(conn_params) as conn:
    with conn.cursor() as cur:
        # Вставка нескольких записей
        extras.execute_values(cur, sql, contacts, template=None, page_size=100)
        conn.commit()

print("Данные успешно вставлены.")
