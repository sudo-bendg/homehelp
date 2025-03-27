from flask import Blueprint, render_template

upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/upload')
def upload():
    return render_template('upload.html')