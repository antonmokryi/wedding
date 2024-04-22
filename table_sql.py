import sqlite3

con = sqlite3.connect(
    "guests.db"
)

cursor = con.cursor()

# cursor.execute("""
#     CREATE TABLE guests(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         number INTEGER,
#         name TEXT,
#         compliment TEXT
#     )
# """)

# con.commit()


# cursor.execute("INSERT INTO guests(number, name, compliment) VALUES(380681941410, 'Андрій та Інна', 'Дорогі наші')")
# con.commit()

cursor.execute("SELECT * FROM guests")
ss = cursor.fetchall()
print(ss)
for user in cursor.fetchall():
    print(user)


