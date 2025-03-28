from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import mysql.connector
from flask_bcrypt import Bcrypt
from db_config import db_config 

signin_bp = Blueprint("signin", __name__)
bcrypt = Bcrypt()

@signin_bp.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Check if the user exists
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user and bcrypt.check_password_hash(user["password_hash"], password):
            # Successful login
            session["user"] = username
            return redirect(url_for("files.home"))
        else:
            flash("Invalid username or password", "error")

        cursor.close()
        conn.close()

    return render_template("signin.html")


@signin_bp.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("signin.signin"))
