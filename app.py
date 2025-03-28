from flask import Flask
from routes.files import files_bp
from routes.signin import signin_bp
import os
from flask_session import Session

homehelpDirectory = os.getcwd()
if not os.path.isdir(homehelpDirectory + "/homehelpFiles"):
    os.mkdir(homehelpDirectory + "/homehelpFiles")

app = Flask(__name__, template_folder="./templates")

# Configure session
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Register blueprints
app.register_blueprint(files_bp)
app.register_blueprint(signin_bp)

if __name__ == "__main__":
    app.run(debug=True)
