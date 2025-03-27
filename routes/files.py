from flask import Blueprint, render_template
import os

workingDirectory = os.getcwd()
currentRelPath = ("/homehelpFiles")

files_bp = Blueprint('files', __name__)

@files_bp.route('/')
def home():
    currentDirectoryFiles = os.listdir(workingDirectory + currentRelPath)
    fileInfo = []
    for file in currentDirectoryFiles:
        filePath = os.path.join(workingDirectory + currentRelPath + "/" + file)
        fileInfo.append({"name": file, "isDir": os.path.isdir(filePath)})
    return render_template('files.html', files = fileInfo)