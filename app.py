from flask import Flask, render_template
import os

port = int(os.getenv('PORT', 5000))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/art')
def art():
    return render_template('art.html')

@app.route('/about')
def about():
    return render_template('about.html')

app.run(host='0.0.0.0', port=port, debug=True)
