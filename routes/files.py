from flask import Blueprint, render_template, send_from_directory, abort, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

workingDirectory = os.getcwd()
currentRelPath = "/homehelpFiles"

files_bp = Blueprint('files', __name__)

@files_bp.route('/files/', defaults={'path': ''})
@files_bp.route('/files/<path:path>')
def home(path):
    # Construct the full path to the requested directory
    fullPath = os.path.join(workingDirectory + currentRelPath, path)

    # Ensure the path is valid and within the allowed directory
    if not os.path.exists(fullPath) or not os.path.isdir(fullPath):
        abort(404)  # Return a 404 error if the directory doesn't exist

    # List the contents of the directory
    currentDirectoryFiles = os.listdir(fullPath)
    fileInfo = []
    for file in currentDirectoryFiles:
        filePath = os.path.join(fullPath, file)
        fileInfo.append({"name": file, "isDir": os.path.isdir(filePath)})

    # Sort the files: directories first, then files, both alphabetically
    fileInfo = sorted(fileInfo, key=lambda f: (not f['isDir'], f['name'].lower()))

    # Calculate the parent directory
    parentPath = '/'.join(path.strip('/').split('/')[:-1]) if path else None

    return render_template('files.html', files=fileInfo, currentPath=path, parentPath=parentPath)

@files_bp.route('/download/<filename>')
def download_file(filename):
    # Ensure the file exists in the directory
    file_path = os.path.join(workingDirectory + currentRelPath, filename)
    if not os.path.isfile(file_path):
        abort(404)  # Return a 404 error if the file doesn't exist
    return send_from_directory(workingDirectory + currentRelPath, filename, as_attachment=True)

@files_bp.route('/files/upload/<path:path>', methods=['POST'])
def upload_file(path):
    # Construct the full path to the current directory
    fullPath = os.path.join(workingDirectory + currentRelPath, path)

    # Ensure the path is valid and within the allowed directory
    if not os.path.exists(fullPath) or not os.path.isdir(fullPath):
        abort(404)  # Return a 404 error if the directory doesn't exist

    # Check if a file was uploaded
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']

    # Check if the file has a valid name
    if file.filename == '':
        return "No selected file", 400

    # Save the file to the current directory
    filename = secure_filename(file.filename)  # Sanitize the filename
    file.save(os.path.join(fullPath, filename))  # Save the file
    return redirect(url_for('files.home', path=path))  # Redirect back to the current directory