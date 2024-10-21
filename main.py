from flask import Flask,jsonify,request
from db.createTableOperation import createTables
from db.addOperation import createUser


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return 'Hello, World!'


data = {"name":"Sagnik","role":"Android Dev"}


@app.route('/signUp',methods = ['POST'])
def signUp():
    name = request.form['name']
    password = request.form['password']
    email = request.form['email']
    address = request.form['address']
    pinCode = request.form['pinCode']

    data = createUser(name=name,password=password,email=email,address=address,pinCode=pinCode)

    return data



if __name__ == "__main__":
    createTables()
    app.run(debug=True)