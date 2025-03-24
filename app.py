from flask import Flask, render_template

app = Flask(__name__, template_folder='./templates')

@app.route('/')
def home():
    return render_template('files.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)