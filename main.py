from flask import Flask,jsonify,request
from db.createTableOperation import createTables
from db.addOperation import createUser, createProduct
from db.readOperation import getAllUsers, getProducts
from db.auth import user_auth

app = Flask(__name__)

@app.route('/signUp',methods = ['POST'])
def signUp():
    name = request.form['name']
    password = request.form['password']
    email = request.form['email']
    address = request.form['address']
    pinCode = request.form['pinCode']
    phoneNo = request.form['phoneNo']

    data = createUser(name=name,password=password,email=email,address=address,pinCode=pinCode,phoneNo=phoneNo)

    return data

@app.route('/getAllUsers', methods=['GET'])
def getUsers():
    users = getAllUsers()
    return jsonify(users)

@app.route('/login',methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user = user_auth(email=email, password=password)

    if user:
        return jsonify({"message": "Logged in successfully", "user": user}), 200
    else:
        return jsonify({"message": "Invalid email or password"}), 401
    
    return user

if __name__ == "__main__":
    createTables()
    app.run(debug=True)