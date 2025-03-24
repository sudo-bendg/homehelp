# homehelp  

homehelp is a self-hosted file storage solution designed for home servers, providing a google drive-like experience for personal and family use. The goal is to create a secure, efficient, and user-friendly platform for storing, accessing, and managing files on a private network.  

## features (planned & in development)  

### **phase 1: basic functionality (google drive clone)**  
- ✅ file upload, download, and organization  
- ✅ user authentication and access control  
- ✅ web-based interface for managing files  
- ✅ local storage with support for basic metadata  

### **phase 2: ai integration for enhanced file management**  
- 🔄 **ai-powered search & tagging** – automatically categorize files using image recognition, text extraction (ocr), and content analysis.  
- 🔄 **document & image processing** – extract metadata and keywords for efficient searching.  
- 🔄 **automated file sorting** – suggest folder structures based on file types and usage patterns.  

## technologies used  
- **backend:** python (flask or fastapi)  
- **frontend:** html, css, javascript (react or vue.js)  
- **database:** sqlite / postgresql / mariadb  
- **ai tools:** tesseract ocr, spacy, openai clip (for tagging and search)  
- **storage:** local filesystem (with potential cloud backup options)  

## usage  
homehelp is designed for personal and family use within a home lab environment. future plans include improving search functionality, optimizing performance, and adding smart file management features.  

## roadmap  
- 🚀 **phase 1:** build a functional self-hosted file manager.  
- 🧠 **phase 2:** implement ai-driven tagging and search capabilities.  
- 🛠 **future improvements:** mobile access, encrypted backups, and multi-user collaboration.

## a crazy notion

### Flask-Go Hybrid Approach

For this project, I am considering a **Flask-Go hybrid approach** to achieve improved speed and scalability for handling file operations.

- **Flask**: The Flask application will handle the **web interface**, including user interactions such as uploading, downloading, and organizing files. It will also manage the front-end logic and communicate with the Go backend for file handling.
  
- **Go**: Go will be used to handle **file operations** such as uploads, downloads, and managing the file system. Go is chosen for its superior speed in handling file I/O and its concurrency model, which will allow for efficient file transfers, especially when dealing with frequent backups and large files.

#### Why This Approach?
- **Performance**: Go is designed for high-performance applications and will be more efficient at handling large file operations than Python.
- **Scalability**: With Go's concurrency model, the application will handle multiple simultaneous file operations more effectively than a Python-based solution.
- **Learning Opportunity**: This hybrid approach provides an opportunity to test my learning ability by combining different technologies and optimizing them for performance in a home server environment.

In the future, the goal is to integrate **AI-powered features**, such as tagging and categorizing files, which will be handled primarily by Python and can be integrated with the Go-based file handling.

---  

this project is under active development and is not yet public. stay tuned for updates!  

