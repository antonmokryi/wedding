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
#         text TEXT
#     )
# """)

# con.commit()


cursor.execute("INSERT INTO guests(number, name, text) VALUES(068777, 'Дорогі наші <br /> Іван та Сергій', 'skhdf,sdfksdfkshdfkskdjfhskdh')")
con.commit()

cursor.execute("SELECT * FROM guests")
ss = cursor.fetchall()
print(ss)
# for user in cursor.fetchall():
#     print(user)


