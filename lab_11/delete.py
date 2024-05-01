import psycopg2
from psycopg2 import sql

def delete_user_by_name_or_phone(name=None, phone_number=None):
    # Параметры подключения к базе данных
    conn = psycopg2.connect(
        "dbname='students' user='postgres' host='localhost' password='12345'"
    )

    try:
        with conn.cursor() as cur:
            if name:
                # Удаляем пользователя по логину
                cur.execute(
                    sql.SQL("DELETE FROM students_data WHERE name = %s"),
                    (name,)
                )
                print(f"Пользователь с логином '{name}' удален.")
            elif phone_number:
                # Удаляем пользователя по телефону
                cur.execute(
                    sql.SQL("DELETE FROM students_data WHERE phone_number = %s"),
                    (phone_number,)
                )
                print(f"Пользователь с телефоном '{phone_number}' удален.")

            # Сохраняем изменения в базе данных
            conn.commit()

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        # Закрываем соединение с базой данных
        conn.close()

# Примеры использования функции
delete_user_by_name_or_phone(name='')
delete_user_by_name_or_phone(phone_number='+77000093259')
