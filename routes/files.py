from flask import (
    Blueprint,
    render_template,
    send_from_directory,
    abort,
    request,
    redirect,
    url_for,
)
import os
from werkzeug.utils import secure_filename

workingDirectory = os.getcwd()
currentRelPath = "/homehelpFiles"

files_bp = Blueprint("files", __name__)


@files_bp.route("/files/", defaults={"path": ""})
@files_bp.route("/files/<path:path>")
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
    fileInfo = sorted(fileInfo, key=lambda f: (not f["isDir"], f["name"].lower()))

    # Calculate the parent directory
    parentPath = "/".join(path.strip("/").split("/")[:-1]) if path else None

    return render_template(
        "files.html", files=fileInfo, currentPath=path, parentPath=parentPath
    )


@files_bp.route("/download/<filename>")
def download_file(filename):
    # Ensure the file exists in the directory
    file_path = os.path.join(workingDirectory + currentRelPath, filename)
    if not os.path.isfile(file_path):
        abort(404)  # Return a 404 error if the file doesn't exist
    return send_from_directory(
        workingDirectory + currentRelPath, filename, as_attachment=True
    )


@files_bp.route("/files/upload/<path:path>", methods=["POST"])
def upload_file(path):
    # Construct the full path to the current directory
    fullPath = os.path.join(workingDirectory + currentRelPath, path)

    # Ensure the path is valid and within the allowed directory
    if not os.path.exists(fullPath) or not os.path.isdir(fullPath):
        abort(404)  # Return a 404 error if the directory doesn't exist

    # Check if a file was uploaded
    if "file" not in request.files:
        return "No file part", 400

    file = request.files["file"]

    # Check if the file has a valid name
    if file.filename == "":
        return "No selected file", 400

    # Save the file to the current directory
    filename = secure_filename(file.filename)  # Sanitize the filename
    file.save(os.path.join(fullPath, filename))  # Save the file
    return redirect(
        url_for("files.home", path=path)
    )  # Redirect back to the current directory


@files_bp.route("/files/upload-directory/<path:path>", methods=["POST"])
def upload_directory(path):
    # Construct the full path to the current directory
    fullPath = os.path.join(workingDirectory + currentRelPath, path)

    # Ensure the path is valid and within the allowed directory
    if not os.path.exists(fullPath) or not os.path.isdir(fullPath):
        abort(404)  # Return a 404 error if the directory doesn't exist

    # Check if files were uploaded
    if "files" not in request.files:
        return "No files part", 400

    files = request.files.getlist("files")  # Get the list of uploaded files

    for file in files:
        # Extract the relative path of the file from the client's directory structure
        relative_path = file.filename
        save_path = os.path.join(fullPath, relative_path)

        # Ensure the directory structure exists
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Save the file
        file.save(save_path)

    # Create the directory itself if it doesn't exist
    for file in files:
        relative_path = file.filename
        directory_path = os.path.join(fullPath, os.path.dirname(relative_path))
        os.makedirs(directory_path, exist_ok=True)

    return redirect(
        url_for("files.home", path=path)
    )  # Redirect back to the current directory


@files_bp.route('/files/create-directory', methods=['POST'])
def create_directory():
    # Get the path and directory name from the form
    path = request.form.get('path', '').strip()
    directory_name = request.form.get('directory_name', '').strip()

    # Ensure the path and directory name are valid
    if not directory_name:
        return "Invalid path or directory name", 400

    # Construct the full path to the current directory
    fullPath = os.path.join(workingDirectory + currentRelPath, path)

    # Ensure the path is valid and within the allowed directory
    if not os.path.exists(fullPath) or not os.path.isdir(fullPath):
        abort(404)  # Return a 404 error if the directory doesn't exist

    # Construct the full path for the new directory
    new_directory_path = os.path.join(fullPath, directory_name)

    # Create the new directory
    try:
        os.makedirs(new_directory_path, exist_ok=False)  # Raise an error if the directory already exists
    except FileExistsError:
        return "Directory already exists", 400

    return redirect(url_for('files.home', path=path))  # Redirect back to the current directory
