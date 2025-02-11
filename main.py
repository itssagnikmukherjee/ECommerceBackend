from flask import Flask,jsonify,request
from db_operations.createTableOperation import createTables, createProductTable
from db_operations.addOperation import createUser, createNewProduct
from db_operations.readOperation import getAllUsers, getProducts, getSpecificUser, getSpecificUserName
from db_operations.updateOperation import updateUserName, updateUserInfo
from db_operations.auth import user_auth

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

@app.route('/updateUser', methods=['PATCH'])
def updateAnUser():
    try:
        user_id = request.form['user_id']
        name = request.form.get('name', None)
        password = request.form.get('password', None)
        email = request.form.get('email', None)
        phoneNo = request.form.get('phoneNo', None)
        address = request.form.get('address', None)
        pinCode = request.form.get('pinCode', None)
        #previous user information
        prev_user_info = getSpecificUser(user_id)

        if not prev_user_info:
            return jsonify({"message": "User not found"}), 404

        #update user information if provided

        if name:
            updateUserName(user_id, name)
        if email:
            updateUserInfo(user_id, email=email)
        if phoneNo:
            updateUserInfo(user_id, phoneNo=phoneNo)
        if password:
            updateUserInfo(user_id, password=password)
        if address:
            updateUserInfo(user_id, address=address)
        if pinCode:
            updateUserInfo(user_id, pinCode=pinCode)

        #updated information
        updated_user_info = getSpecificUser(user_id)

        return jsonify({"message": "User information updated successfully","previous info": prev_user_info,"new user info":updated_user_info}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500




if __name__ == "__main__":
    createTables()
    createProductTable()
    app.run(debug=True)