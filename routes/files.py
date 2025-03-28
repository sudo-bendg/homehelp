from flask import Blueprint, render_template, send_from_directory, abort
import os

workingDirectory = os.getcwd()
currentRelPath = "/homehelpFiles"

files_bp = Blueprint('files', __name__)

@files_bp.route('/')
def home():
    currentDirectoryFiles = os.listdir(workingDirectory + currentRelPath)
    fileInfo = []
    for file in currentDirectoryFiles:
        filePath = os.path.join(workingDirectory + currentRelPath + "/" + file)
        fileInfo.append({"name": file, "isDir": os.path.isdir(filePath)})
    return render_template('files.html', files=sorted(fileInfo, key=lambda f: str(not f['isDir']) + f['name']))

@files_bp.route('/download/<filename>')
def download_file(filename):
    # Ensure the file exists in the directory
    file_path = os.path.join(workingDirectory + currentRelPath, filename)
    if not os.path.isfile(file_path):
        abort(404)  # Return a 404 error if the file doesn't exist
    return send_from_directory(workingDirectory + currentRelPath, filename, as_attachment=True)