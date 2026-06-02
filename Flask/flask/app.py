from flask import Flask

# creating an instance of the Flask class which will be my
# WSGI: Web Service Gateway Interface application

app=Flask(__name__) #WSGI application

@app.route("/") # this is a decorator, we re giving a route to the home page
def welcome():
    return "Welcome to this Flask test, this is amazing, so enjoyable"

@app.route("/index") # this is a decorator, we re giving a route to the home page
def enjoy():
    return "So fulfilling and so enjoyable"

if __name__=="__main__":  # __name__ is the entry point of the application
    app.run(debug=True)