from flask import Flask, request, jsonify

app = Flask(__name__)

users =[]
meals =[]

@app.route('/auth/signup', methods = ['POST'])
def signup():
    user_data = request.get_json()
    newuser ={}
    newuser['name'] = user_data['name']
    newuser['email'] = user_data['email']
    newuser['password'] = user_data['password']
    newuser['role'] = user_data['role']
    users.append(newuser)
    return jsonify({"users":users})
    

@app.route('/auth/login', methods = ['POST'])
def login():
    user_login_data = request.get_json() 
    for user in users:
        if user['name'] == user_login_data['name'] and user['password'] == user_login_data['password']:
            return jsonify({"message": "You are logged in"})
        return jsonify({"message": "Invalid login"})    
    return jsonify({"message": "No username found"})    


@app.route('/meals/', methods = ['GET'])
def meals():
    for user in users:
        if newuser['role'] == "admin":
            return jsonify({"meals":meals})
    return jsonify({"message": "Unauthorized please login"})
    
    ''' meal_data = request.get_json()
    newmeal ={"mealname":meal_data['mealname'], "category":meal_data['category'], "price":meal_data['price'] }
    newmeal['mealname'] = meal_data['mealname']

    newmeal['category'] = meal_data['category']

    newmeal['price'] = meal_data['price']'''

    
    
@app.route('/meals/', methods = ['POST'])
def add_meal():
    meal_data = request.get_json()
    newmeal ={"mealname":meal_data['mealname'], "category":meal_data['category'], "price":meal_data['price'] }
    for user in users:
        if newuser['role'] == "admin":
            return jsonify({"meals":meals})
        return jsonify({"message": "Unauthorized please login"})
    



'''meal_data = request.get_json()
newmeal ={}
newmeal['mealname'] = meal_data['mealname']

newmeal['category'] = meal_data['category']

newmeal['price'] = meal_data['price']
meals.append(newmeal)
return jsonify({"meals":meals})
'''


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