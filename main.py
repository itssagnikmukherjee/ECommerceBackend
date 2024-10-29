from flask import Flask,jsonify,request
from db.createTableOperation import createTables, createProductTable
from db.addOperation import createUser, createNewProduct
from db.readOperation import getAllUsers, getProducts, getSpecificUser, getSpecificUserName
from db.updateOperation import updateUserName
from db.auth import user_auth

app = Flask(__name__)


#sign up a user

@app.route('/signUp',methods = ['POST'])
def signUp():
    name = request.form.get('name',None)
    password = request.form.get('password',None)
    email = request.form.get('email',None)
    address = request.form.get('address',None)
    pinCode = request.form.get('pinCode',None)
    phoneNo = request.form.get('phoneNo',None)

    data = createUser(name=name,password=password,email=email,address=address,pinCode=pinCode,phoneNo=phoneNo)

    return jsonify(data)

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

@app.route('/updateUserName', methods=['PATCH'])
def updateAnUserName():
    try:
        user_id = request.form['user_id']
        name = request.form['name']
        prevUserName = getSpecificUserName(user_id)
        updateUserName(userID=user_id, name=name)
        return jsonify({"status": 200,"message": "user name is updated successfully", "prev user name" : prevUserName,"new user name" : name})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    createTables()
    createProductTable()
    app.run(debug=True)