import sqlite3

def user_auth(username, password):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Users WHERE email = ? AND password = ?", (username,password))
    user = cursor.fetchone()

    conn.close()
    