import sqlite3

def init_user_db():
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY, password TEXT NOT NULL)"""
    )
    conn.commit()
    conn.close()
    
def signup (username, password):
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES(? , ?)" , (username , password)
            
        )
        conn.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError:
        print("Username already exists. Try a different one.")
    conn.close()
    
    
def login(username, password):
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?", (username, password)
    )
    user = cursor.fetchone()
    conn.close()
    
    if user:
        print(f"Welcome back, {username}")
        return True
    else:
        print("Invalid credentials, try again.")
        return False
    
init_user_db()
print("1. Signup")
print("2. Login")

choice = input("Choose an option 1 or 2: ")

if choice == "1":
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    signup(username, password)
    
elif choice == "2":
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    login(username, password)