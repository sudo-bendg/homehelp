from flask import Blueprint, render_template

files_bp = Blueprint('files', __name__)

@files_bp.route('/')
def home():
    return render_template('files.html')