from flask import Flask, request, jsonify

app = Flask(__name__)

users =[]

@app.route('/auth/signup', methods = ['POST'])
def signup():

    user_data = request.get_json()
    name = user_data['name']
    email = user_data['email']
    username = user_data['username']
    password = user_data['password']
    #return '{} is a customer and her email is {}, username is {} and password is {}'.format(name, email, username, password))
    return 'User register'

@app.route('/auth/login', methods = ['POST'])
def login():
    return 'User login'    


@app.route('/meals/', methods = ['GET'])
def meals():
    return 'Get all meal options'

@app.route('/meals/', methods = ['POST'])
def add_meal():
    return 'Add a meal'

@app.route('/meals/<meal_id>', methods = ['PUT'])
def edit_meal():
    return 'Update the information of a meal option'  

@app.route('/meals/<meal_id>', methods = ['DELETE'])
def delete_meal():
    return 'Remove a meal option' 

@app.route('/menu/', methods = ['POST'])
def set_menu():
    return 'Set up menu for the day'  

@app.route('/menu/', methods = ['GET'])
def get_menu():
    return 'Get menu for the day'  

@app.route('/orders', methods = ['POST'])
def orders():
    return 'Select the meal option from the menu'   

@app.route('/orders/order_id', methods = ['PUT'])
def edit_order():
    return 'Modify an order'         

@app.route('/orders', methods = ['GET'])
def get_orders():
    return 'Get all orders'          
    


        

if __name__== '__main__':
    app.run(Debug=True)