from flask import Flask, render_template
import os

port = int(os.getenv('PORT', 5000))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
app.run(host='0.0.0.0', port=port)