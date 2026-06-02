## Building a URL dynamically
## Variable Rule
## Jinja 2 template Engine

### Jinja 2 template Engine
"""
{{}} expression to print output in html file
{%...%} conditions, for loops...
{#...#} comment
"""

from flask import Flask, render_template, request, redirect, url_for

# creating an instance of the Flask class which will be my
# WSGI: Web Service Gateway Interface application

app=Flask(__name__) #WSGI application

@app.route("/") # this is a decorator, we re giving a route to the home page
def welcome():
    return "<html><H1>Welcome to my first Flask App</H1></html>"

@app.route("/index", methods=['GET']) # this is a decorator, we re giving a route to the home page
def index():
    return render_template("index1.html")

@app.route("/AbruvaTech") # this is a decorator, we re giving a route to the home page
def abruva():
    return render_template("AbruvaTech.html")

@app.route("/AboutUs")
def aboutus():
    return render_template('aboutus.html')

#Variable Rule
@app.route("/success/<int:score>")
def success(score):
    res=""
    if score >= 50:
        res="PASS"
    else:
        res="FAIL"

    return render_template("result.html", results=res)

#Variable Rule
@app.route("/successres/<int:score>")
def success_results(score):
    res=""
    if score >= 50:
        res="PASS"
    else:
        res="FAIL"
    
    exp={'score':score, 'res':res}

    return render_template("result1.html", results=exp)


# if condition
@app.route("/successif/<int:score>")
def success_if(score):
    return render_template("result.html", results=score)

@app.route("/submit", methods=["GET", "POST"])
def submit():
    #total_score = 0
    if request.method=='POST':
        science=float(request.form["science"])
        math=float(request.form["maths"])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+math+c+data_science)/4
    
        return redirect(url_for('success_results',score=total_score))
    return render_template("get_results.html")

if __name__=="__main__":  # __name__ is the entry point of the application
    #app.run(debug=True)
    app.run(debug=True, host="0.0.0.0", port=5000)


#adding below the comments