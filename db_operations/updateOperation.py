import sqlite3


def updateUserName(userID, name):
    conn = sqlite3.connect("databases/user_info.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE Users SET name = ? WHERE user_id = ?", (name, userID))
    conn.commit()
    conn.close()

def updateUserInfo(userID, **keyword):
    conn = sqlite3.connect("databases/user_info.db")
    cursor = conn.cursor()

    for key, value in keyword.items():
        if key == "name":
            cursor.execute("UPDATE Users SET name = ? WHERE user_id = ?", (value, userID))
        elif key == "password":
            cursor.execute("UPDATE Users SET password =? WHERE user_id =?", (value, userID))
        elif key == "email":
            cursor.execute("UPDATE Users SET email = ? WHERE user_id = ?", (value, userID))
        elif key == "phoneNo":
            cursor.execute("UPDATE Users SET phoneNo = ? WHERE user_id = ?", (value, userID))
        elif key == "address":
            cursor.execute("UPDATE Users SET address = ? WHERE user_id = ?", (value, userID))
        elif key == "pinCode":
            cursor.execute("UPDATE Users SET pinCode = ? WHERE user_id = ?", (value, userID))
        else:
            print(f"Invalid column name: {key}")
    
    conn.commit()
    conn.close()