import sqlite3


def updateUserName(userID, name):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE Users SET name = ? WHERE user_id = ?", (name, userID))
    conn.commit()
    conn.close()