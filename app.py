from flask import Flask, render_template
import os

port = int(os.getenv('PORT', 5000))

app = Flask(__name__)

@app.route('/')
def index():
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

@app.errorhandler(404)
def errorhandler(e):
    return render_template('404.html')

app.run(host='0.0.0.0', port=port, debug=True)
