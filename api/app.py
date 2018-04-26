from flask import Flask

app = Flask(__name__)



@app.route('/signup', methods = ['POST'])
def signup():
    return 'User register'

if __name__== '__main__':
    app.run(Debug=True)