from flask import Flask, render_template

# creating an instance of the Flask class which will be my
# WSGI: Web Service Gateway Interface application

app=Flask(__name__) #WSGI application

@app.route("/") # this is a decorator, we re giving a route to the home page
def welcome():
    return "<html><H1>Welcome to my first Flask App</H1></html>"

@app.route("/index") # this is a decorator, we re giving a route to the home page
def index():
    return render_template("index1.html")

@app.route("/AbruvaTech") # this is a decorator, we re giving a route to the home page
def abruva():
    return render_template("AbruvaTech.html")

@app.route("/AboutUs")
def aboutus():
    return render_template('aboutus.html')

if __name__=="__main__":  # __name__ is the entry point of the application
    app.run(debug=True)