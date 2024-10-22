import sqlite3
import uuid
from datetime import date

def createUser(name,password,email,pinCode,address,phoneNo):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    user_id = str(uuid.uuid4)

    date_of_account_creation = date.today()

    cursor.execute(
    """
    INSERT INTO Users(user_id,password,level,date_of_account_creation,isApproved,block,name,email,pin,address,phoneNo)
    VALUES(?,?,?,?,?,?,?,?,?,?,?)
    """,(user_id,password,1,date_of_account_creation,0,0,name,email,pinCode,address,phoneNo)
    )

    conn.commit()
    conn.close()

    return user_id
