from flask import Flask
from routes.files import files_bp
from routes.signin import signin_bp
from routes.upload import upload_bp
import os

homehelpDirectory = os.getcwd()
if not os.path.isdir(homehelpDirectory + "/homehelpFiles"):
    os.mkdir(homehelpDirectory + "/homehelpFiles")

app = Flask(__name__, template_folder="./templates")

app.register_blueprint(files_bp)
app.register_blueprint(signin_bp)
app.register_blueprint(upload_bp)

if __name__ == "__main__":
    app.run(debug=True)
