from snake_game import run_game
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="potkyz2007!"
)
cur = conn.cursor()

username = input("Enter your username: ")

cur.execute("SELECT score, level FROM snake_users WHERE username = %s", (username,))
row = cur.fetchone()
if row:
    print(f"Welcome back, {username}! Your last score: {row[0]}, level: {row[1]}")
else:
    cur.execute("INSERT INTO snake_users (username, score, level) VALUES (%s, %s, %s)", (username, 0, 1))
    conn.commit()

start = input("Do you want to start the game? (yes/no): ")
if start.lower() == "yes":
    print("Starting the game...")
    score, level = run_game(username)
    print(f"Game over! Final score: {score}, level: {level}")
else:
    cur.execute("DELETE FROM snake_users WHERE username = %s AND score = 0 AND level = 1", (username,))
    conn.commit()
    print("Пока-пока!")