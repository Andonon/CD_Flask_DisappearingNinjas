'''Coding Dojo Assignment, Flask Fundamentals, "Disappearing Ninjas"
    by Troy Center June 2017, troycenter1@gmail.com
'''
#pylint: disable=C0103

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def homepage():
    '''Home page'''
    return render_template("index.html")

@app.route('/ninja')
def ninjapage():
    '''Ninja page'''
    return render_template("ninja.html")

@app.route('/blue')
def bluepage():
    '''Blue ninja page'''
    return render_template("blue.html")

@app.route('/orange')
def orangepage():
    '''Orange ninja page'''
    return render_template("orange.html")

@app.route('/red')
def redpage():
    '''Red ninja page'''
    return render_template("red.html")

@app.route('/purple')
def purplepage():
    '''Purple ninja page'''
    return render_template("purple.html")

@app.route('/<invalidcolor>')
def invalidcolorpage():
    '''Invalid Color Selection page'''
    return render_template("invalid.html")

app.run(debug=True)
