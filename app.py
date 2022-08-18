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
        ['birch', """if you hear a sound, just know the birch aches for you in ashes."""] ,
        ['bonfire', """to hold you near and tender, has always been a dream."""],
        ['eiffel', """Paris is for lovers, not people with broken skins."""],
        ['field', 'Picture me when I learn civility, and always when I run to better lands.'],
        ['italy', 'I would write you a song that will feel like walking home.'],
        ['kyoto', 'gather around and watch the sunset. Maybe you can make a story out of it.'],
        ['lake', 'Take me to the lakes where all the poets went to die.'],
        ['lemons', 'I want to take you out, for lemonade picnics and all things pretty.'],
        ['macca', 'You pray because at heart, you are a child yearning for things out of reach.'],
        ['purp', 'You can forget who I wanted to be, but things always come back.'],
        ['saddar', 'the birch sings a song, it calls for something.'],
        ['shapes', 'She wears a pleated skirt, folded like my sins on a platter.'],
        ['waves', 'I go there when I need peace, and a screaming contest is just where it is.'],
    ]
    return render_template('art.html', paintings=paintings)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile/<username>')
def profile(username):
    if username == 'Warze':
        coins = 500
    else:
        coins = 0
    return render_template('profile.html', username = username, coins = coins)

# The 404 page
@app.errorhandler(404)
def errorhandler(e):
    print(e)
    return render_template('404.html')

# Start hosting the server
app.run(host='0.0.0.0', port=port, debug=True)