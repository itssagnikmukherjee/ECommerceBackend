from flask import Flask,jsonify,request
from db.createTableOperation import createTables, createProductTable
from db.addOperation import createUser, createNewProduct
from db.readOperation import getAllUsers, getProducts, getSpecificUser
from db.auth import user_auth

app = Flask(__name__)


#sign up a user

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


#products 

@app.route('/createProduct', methods=['POST'])
def createProduct():
    product_name = request.form['product_name']
    stock = request.form['stock']
    price = request.form['price']
    category = request.form['category']
    expiry_date = request.form['expiry_date']

    data = createNewProduct(product_name,stock,price,category,expiry_date)
    return data


@app.route('/getAllProducts', methods=['GET'])
def getAllProducts():
    products = getProducts()
    return jsonify(products)


#get specific user information

@app.route('/getSpecificUser', methods=['POST'])
def getAnySpecificUser():
    user_id = request.form['user_id']
    getUserInfo = getSpecificUser(user_id)
    return jsonify(getUserInfo)


if __name__ == "__main__":
    createTables()
    createProductTable()
    app.run(debug=True)