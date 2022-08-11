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
        ['birch', 'the birch sings a song, it calls for something.'] ,
        ['bonfire', 'the birch sings a song, it calls for something.'],
        ['eiffel', 'the birch sings a song, it calls for something.'],
        ['field', 'the birch sings a song, it calls for something.'],
        ['italy', 'the birch sings a song, it calls for something.'],
        ['kyoto', 'the birch sings a song, it calls for something.'],
        ['lake', 'the birch sings a song, it calls for something.'],
        ['lemons', 'the birch sings a song, it calls for something.'],
        ['macca', 'the birch sings a song, it calls for something.'],
        ['purp', 'the birch sings a song, it calls for something.'],
        ['saddar', 'the birch sings a song, it calls for something.'],
        ['shapes', 'the birch sings a song, it calls for something.'],
        ['waves', 'the birch sings a song, it calls for something.'],
    ]
    return render_template('art.html', paintings=paintings)

@app.route('/about')
def about():
    return render_template('about.html')

app.run(host='0.0.0.0', port=port, debug=True)
