import sqlite3

def user_auth(email, password):
    conn = sqlite3.connect("databases/user_info.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Users WHERE email = ? AND password = ?", (email,password))
    user = cursor.fetchone()
    conn.close()
    return user