from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html', file=False)

@app.route('/image_upload')
def image_upload():
    return render_template('index.html', file=True)

if __name__ == '__main__':
    app.run(debug=True)