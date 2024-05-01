import psycopg2
from psycopg2 import sql

def create_or_update_contact(name, phone_number):
    # Параметры подключения к базе данных
    conn = psycopg2.connect(
        "dbname='students' user='postgres' host='localhost' password='12345'"
    )
    
    try:
        # Создаем курсор для выполнения операций с базой данных
        with conn.cursor() as cur:
            # Проверяем, есть ли контакт с таким именем
            cur.execute(
                sql.SQL("SELECT phone_number FROM students_data WHERE name = %s"),
                (name,)
            )
            result = cur.fetchone()
            
            if result:
                # Если контакт найден, обновляем номер телефона
                cur.execute(
                    sql.SQL("UPDATE students_data SET phone_number = %s WHERE name = %s"),
                    (phone_number, name)
                )
                print(f"Контакт '{name}' обновлен с новым номером телефона: {phone_number}")
            else:
                # Если контакта нет, создаем новый
                cur.execute(
                    sql.SQL("INSERT INTO students_data (name, phone_number) VALUES (%s, %s)"),
                    (name, phone_number)
                )
                print(f"Новый контакт '{name}' добавлен с номером телефона: {phone_number}")
            
            # Сохраняем изменения в базе данных
            conn.commit()

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        # Закрываем соединение с базой данных
        conn.close()

# Пример использования функции
create_or_update_contact('SOSA', '+71211111111')
