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
    name = input("Enter a name:")
    phone = input("Enter a phone number:")
    cur.execute("INSERT INTO PhoneBook (username, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("The data has been added successfully!")

# Вставка из CSV
def insert_from_csv():
    path = input("Enter the path to the CSV file:")
    try:
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                cur.execute("INSERT INTO PhoneBook (username, phone) VALUES (%s, %s)", (row[0], row[1]))
        conn.commit()
        print("The CSV data has been uploaded!")
    except Exception as e:
        print("Error reading the file:", e)

# Обновление данных
def update_data():
    old_name = input("Enter the name you want to change:")
    new_name = input("New name (press Enter if not changed):")
    new_phone = input("New number (press Enter if not changed):")
    if new_name:
        cur.execute("UPDATE PhoneBook SET username = %s WHERE username = %s", (new_name, old_name))
    if new_phone:
        cur.execute("UPDATE PhoneBook SET phone = %s WHERE username = %s", (new_phone, new_name or old_name))
    conn.commit()
    print("The data has been updated!")

# Поиск по имени или номеру
def query_data():
    option = input("Фильтр по (1 - name, 2 - number, Enter - show all): ")
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
    value = input("Enter the name or number you want to delete.:")
    cur.execute("DELETE FROM PhoneBook WHERE username = %s OR phone = %s", (value, value))
    conn.commit()
    print("Deleted!")

# Главное меню
def menu():
    create_table()
    while True:
        print("\n--- Меню ---")
        print("1. Add an entry manually")
        print("2. Download from CSV")
        print("3. Update the entry")
        print("4. Find the entry")
        print("5. Delete entry")
        print("6. Exit")

        choice = input("Select an action (1-6): ")

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
            print("Bye bye")
            break
        else:
            print("Wrong choice. Try again.")

if __name__ == "__main__":
    menu()