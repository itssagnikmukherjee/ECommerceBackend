import sqlite3,requests

def getAllUsers():
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    conn.close()
    userJson = []
    for user in users:
        tempUser = {
            "id": user[0],
            "user_id": user[1],
            "password": user[2],
            "level": user[3],
            "date_of_account_creation": str(user[4]),
            "isApproved": user[5],
            "block": user[6],
            "name": user[7],
            "email": user[8],
            "pin": user[9],
            "address": user[10],
            "phoneNo": user[11]
        }
        userJson.append(tempUser)
        
    print(userJson)
    return userJson

def getProducts():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    conn.close()
    productJson = []
    for product in products:
        tempProduct = {
            "product_name": product[0],
            "stock": product[1],
            "price": product[2],
            "category": product[3],
            "expiry_date": str(product[4])
        }
        productJson.append(tempProduct)
        
    print(productJson)
    return productJson

def getSpecificUser(user_id):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    userJson = []
    tempUser = {
            "id": user[0],
            "user_id": user[1],
            "password": user[2],
            "level": user[3],
            "date_of_account_creation": str(user[4]),
            "isApproved": user[5],
            "block": user[6],
            "name": user[7],
            "email": user[8],
            "pin": user[9],
            "address": user[10],
            "phoneNo": user[11]
        }
    userJson.append(tempUser)
    print(userJson)
    return userJson

def getSpecificUserName(user_id):
    users = getAllUsers()
    for user in users:
        if user['user_id'] == user_id:
            return user['name']
    return "User not found"