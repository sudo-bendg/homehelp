import mysql.connector
from flask_bcrypt import Bcrypt
from db_config import db_config  # Import the database configuration

bcrypt = Bcrypt()

# Connect to the database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Add a new user
username = "testuser"
password = "password123"
hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (username, hashed_password))
conn.commit()

cursor.close()
conn.close()