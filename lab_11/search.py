import psycopg2

def search_contacts(name_part=None, phone_part=None):
    conn_params = "dbname='students' user='postgres' host='localhost' password='12345'"
    query = "SELECT * FROM students_data WHERE "
    params = []

    if name_part:
        query += "name LIKE %s "
        params.append(f"%{name_part}%")
    if phone_part:
        if name_part:
            query += "AND "
        query += "phone_number LIKE %s "
        params.append(f"%{phone_part}%")

    with psycopg2.connect(conn_params) as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
            results = cur.fetchall()
            print("Найденные контакты:")
            for result in results:
                print(result)

# вызов функции
search_contacts(name_part="Sn", phone_part="")
