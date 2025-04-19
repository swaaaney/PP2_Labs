import psycopg2
from psycopg2.extensions import register_adapter, AsIs

# Адаптация списка Python в SQL-массив
def adapt_list(lst):
    return AsIs("ARRAY[%s]" % ",".join(["'%s'" % x for x in lst]))
register_adapter(list, adapt_list)

# Подключение
conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    password="potkyz2007!"
)
cur = conn.cursor()

def drop_all_insert_many_versions(cur):
    cur.execute("""
        SELECT proname, oidvectortypes(proargtypes)
        FROM pg_proc
        WHERE proname = 'insert_many_users';
    """)
    procedures = cur.fetchall()
    for proc in procedures:
        name, args = proc
        cur.execute(f'DROP PROCEDURE IF EXISTS {name}({args});')

def init_db():
    cur.execute("DROP TABLE IF EXISTS PhoneBook CASCADE;")
    cur.execute("DROP FUNCTION IF EXISTS search_by_pattern(TEXT);")
    cur.execute("DROP FUNCTION IF EXISTS get_paginated(INT, INT);")
    cur.execute("DROP PROCEDURE IF EXISTS insert_user(TEXT, TEXT);")
    cur.execute("DROP PROCEDURE IF EXISTS delete_user(TEXT);")
    drop_all_insert_many_versions(cur)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS PhoneBook (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            phone TEXT NOT NULL
        );
    """)

    cur.execute("""
        CREATE OR REPLACE FUNCTION search_by_pattern(pattern TEXT)
        RETURNS TABLE (id INT, username TEXT, phone TEXT) AS $$
        BEGIN
            RETURN QUERY
            SELECT pb.id, pb.username, pb.phone FROM PhoneBook pb
            WHERE pb.username ILIKE '%' || pattern || '%'
               OR pb.phone ILIKE '%' || pattern || '%';
        END;
        $$ LANGUAGE plpgsql;
    """)

    cur.execute("""
        CREATE OR REPLACE PROCEDURE insert_user(name TEXT, phone TEXT)
        LANGUAGE plpgsql AS $$
        BEGIN
            IF EXISTS (SELECT 1 FROM PhoneBook WHERE username = name) THEN
                UPDATE PhoneBook SET phone = phone WHERE username = name;
            ELSE
                INSERT INTO PhoneBook(username, phone) VALUES (name, phone);
            END IF;
        END;
        $$;
    """)

    cur.execute("""
        CREATE OR REPLACE PROCEDURE insert_many_users(names TEXT[], phones TEXT[])
        LANGUAGE plpgsql AS $$
        DECLARE
            i INT;
            bad_entries TEXT := '';
        BEGIN
            FOR i IN 1 .. array_length(names, 1) LOOP
                IF phones[i] ~ '^[0-9]+$' THEN
                    BEGIN
                        CALL insert_user(names[i], phones[i]);
                    EXCEPTION WHEN OTHERS THEN
                        bad_entries := bad_entries || names[i] || ',';
                    END;
                ELSE
                    bad_entries := bad_entries || names[i] || ',';
                END IF;
            END LOOP;
            IF bad_entries != '' THEN
                RAISE NOTICE 'Invalid entries: %', bad_entries;
            END IF;
        END;
        $$;
    """)

    cur.execute("""
        CREATE OR REPLACE FUNCTION get_paginated(limit_num INT, offset_num INT)
        RETURNS TABLE (id INT, username TEXT, phone TEXT) AS $$
        BEGIN
            RETURN QUERY
            SELECT * FROM PhoneBook
            ORDER BY id
            LIMIT limit_num OFFSET offset_num;
        END;
        $$ LANGUAGE plpgsql;
    """)

    cur.execute("""
        CREATE OR REPLACE PROCEDURE delete_user(info TEXT)
        LANGUAGE plpgsql AS $$
        BEGIN
            DELETE FROM PhoneBook WHERE username = info OR phone = info;
        END;
        $$;
    """)

    conn.commit()
    print("Database initialized successfully.")

# Текстовое меню
def menu():
    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Search by pattern")
        print("2. Insert or update user")
        print("3. Insert many users")
        print("4. Get paginated results")
        print("5. Delete user by name or phone")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            pattern = input("Enter pattern to search: ")
            cur.execute("SELECT * FROM search_by_pattern(%s);", (pattern,))
            results = cur.fetchall()
            for row in results:
                print(row)

        elif choice == '2':
            name = input("Enter username: ")
            phone = input("Enter phone: ")
            cur.execute("CALL insert_user(%s, %s);", (name, phone))
            conn.commit()
            print("User inserted or updated.")

        elif choice == '3':
            count = int(input("How many users to add? "))
            names = []
            phones = []
            for _ in range(count):
                names.append(input("Enter username: "))
                phones.append(input("Enter phone: "))
            cur.execute("CALL insert_many_users(%s, %s);", (names, phones))
            conn.commit()
            print("Users inserted (some may have been skipped if invalid).")

        elif choice == '4':
            limit = int(input("Enter limit: "))
            offset = int(input("Enter offset: "))
            cur.execute("SELECT * FROM get_paginated(%s, %s);", (limit, offset))
            results = cur.fetchall()
            for row in results:
                print(row)

        elif choice == '5':
            info = input("Enter username or phone to delete: ")
            cur.execute("CALL delete_user(%s);", (info,))
            conn.commit()
            print("User deleted (if existed).")

        elif choice == '6':
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Try again.")

# Запуск
init_db()
menu()

cur.close()
conn.close()