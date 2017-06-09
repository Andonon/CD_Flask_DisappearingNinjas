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
    pass

@app.route('/blue')
def bluepage():
    '''Blue ninja page'''
    pass

@app.route('/orange')
def orangepage():
    '''Orange ninja page'''
    pass

@app.route('/red')
def redpage():
    '''Red ninja page'''
    pass

@app.route('/purple')
def purplepage():
    '''Purple ninja page'''

@app.route('/<invalidcolor>')
def invalidcolorpage():
    '''Invalid Color Selection page'''
    pass

app.run(debug=True)