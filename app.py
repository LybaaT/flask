# Importing all of the dependencies
from flask import Flask, render_template
import os

# This is the port number, defaults to 5000 if no environment variable is found
port = int(os.getenv('PORT', 5000))

# Creating the app, it will be referenced in all of the routes and when starting the server
app = Flask(__name__)

# The homepage
@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/art')
def art():
    paintings = [
        ['birch'] ,
        ['purp'],
        ['shapes'],
        ['field'],
        ['italy'],
        ['kyoto'],
        ['macca'],
        ['eiffel'],
        ['saddar'],
        ['lemons'],
        ['bonfire'],
        ['lake'],
        ['waves'],
    ]
    return render_template('art.html', paintings=paintings)

@app.route('/about')
def about():
    return render_template('about.html')

# The 404 page
@app.errorhandler(404)
def errorhandler(e):
    print(e)
    return render_template('404.html')

# Start hosting the server
app.run(host='0.0.0.0', port=port, debug=True)