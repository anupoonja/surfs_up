from flask import Flask

# __name__ - variable (string)
# Variable with underscore are magic maethods.
# name of the file
    # 1. python app.py - most typical
    # 2. flask run - less obvious, not as common for new comers

# __name__ - variable (string)
    # 1. first type of execution -> __name__ = "__main__" (1)
    # 2. second type of execution -> __name__ = $FLASK_APP

# to run a flask app - Create Flask app
# app. run() -> <app_name>.run()
app = Flask(__name__)

print("Hello anytime")
print(__name__)

# decorator - pass a function into a function
# Starting point or the root
# flask run : from cmd
@app.route('/')
def hello_world():
    #return "Hello World"
    return "<h1>Hello World</h1>"


# extra page eg : http://127.0.0.1:5000/extra or http://localhost:5000/extra
@app.route("/extra")
def extra():
     return "<h1>Hello World 2</h1>"

# python app.py : from cmd line
if __name__ == "__main__":
    print("Hello from cmd line")
    app.run(debug=True)
    # app.run(debug=True)
    # port=50000 host=









