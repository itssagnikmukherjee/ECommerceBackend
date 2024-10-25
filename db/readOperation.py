import sqlite3

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
    conn = sqlite3.connect("my_medicalshop.db")
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
