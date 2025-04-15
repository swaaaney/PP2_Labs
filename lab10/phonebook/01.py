import psycopg2
import csv

# Подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    password="potkyz2007!"
)
cur = conn.cursor()

# Создание таблицы, если её нет
def create_table():
    cur.execute("DROP TABLE IF EXISTS PhoneBook")
    cur.execute("""
        CREATE TABLE PhoneBook (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL
        )
    """)
    conn.commit()

# Вставка из консоли
def insert_from_console():
    name = input("Введите имя: ")
    phone = input("Введите номер: ")
    cur.execute("INSERT INTO PhoneBook (username, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Данные успешно добавлены!")

# Вставка из CSV
def insert_from_csv():
    path = input("Введите путь к CSV-файлу: ")
    try:
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                cur.execute("INSERT INTO PhoneBook (username, phone) VALUES (%s, %s)", (row[0], row[1]))
        conn.commit()
        print("Данные из CSV загружены!")
    except Exception as e:
        print("Ошибка при чтении файла:", e)

# Обновление данных
def update_data():
    old_name = input("Введите имя, которое хотите изменить: ")
    new_name = input("Новое имя (нажмите Enter, если не менять): ")
    new_phone = input("Новый номер (нажмите Enter, если не менять): ")
    if new_name:
        cur.execute("UPDATE PhoneBook SET username = %s WHERE username = %s", (new_name, old_name))
    if new_phone:
        cur.execute("UPDATE PhoneBook SET phone = %s WHERE username = %s", (new_phone, new_name or old_name))
    conn.commit()
    print("Данные обновлены!")

# Поиск по имени или номеру
def query_data():
    option = input("Фильтр по (1 - имя, 2 - номер, Enter - показать всё): ")
    if option == '1':
        name = input("Введите имя: ")
        cur.execute("SELECT * FROM PhoneBook WHERE username = %s", (name,))
    elif option == '2':
        phone = input("Введите номер: ")
        cur.execute("SELECT * FROM PhoneBook WHERE phone = %s", (phone,))
    else:
        cur.execute("SELECT * FROM PhoneBook")
    
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Удаление
def delete_data():
    value = input("Введите имя или номер, который хотите удалить: ")
    cur.execute("DELETE FROM PhoneBook WHERE username = %s OR phone = %s", (value, value))
    conn.commit()
    print("Удалено!")

# Главное меню
def menu():
    create_table()
    while True:
        print("\n--- Меню ---")
        print("1. Добавить запись вручную")
        print("2. Загрузить из CSV")
        print("3. Обновить запись")
        print("4. Найти запись")
        print("5. Удалить запись")
        print("6. Выйти")

        choice = input("Выберите действие (1-6): ")

        if choice == '1':
            insert_from_console()
        elif choice == '2':
            insert_from_csv()
        elif choice == '3':
            update_data()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_data()
        elif choice == '6':
            print("Пока-пока!")
            break
        else:
            print("Неверный выбор. Попробуй снова.")

if __name__ == "__main__":
    menu()