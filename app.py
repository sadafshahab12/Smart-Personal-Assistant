import datetime
import os
import random
import requests
import sqlite3
from dotenv import load_dotenv

load_dotenv()

ASSISTANT_NAME = "smart personal assistant"
TASK_FILE = "todo_task.txt"


def greet_user():
    current_hour = datetime.datetime.now().hour
    print(current_hour)
    if current_hour < 12:
        print("Good Morning!")
    elif current_hour < 18:
        print("Good Afternoon!")
    else:
        print("Good Evening!")
    print(f"Hello ! I am your {ASSISTANT_NAME}.")


def show_menu():
    print("\n --- Main Menu --- \n")
    print("1. Calculator")
    print("2. Tell me a joke")
    print("3. Show Current Time")
    print("4. To-Do List")
    print("5. Get Weather Info")
    print("6. Login/Signup")
    print("7. Exit")


def calculator():
    print("Welcome to the calculator!")
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b if b != 0 else "Error : Divide by zero")
    print("Thank you for using the calculator!")


def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the bicycle fall over? Because it was two-tired!",
    ]
    print(random.choice(jokes))


def show_time():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print("Current Time is: ", now)


def add_task(task):
    with open(TASK_FILE, "a") as file:
        file.write(task + "\n")
    print(f"{task} Task Added successfully.")


def show_tasks():
    if not os.path.exists(TASK_FILE) or os.stat(TASK_FILE).st_size == 0:
        print("No Task Found")
        return
    with open(TASK_FILE, "r") as file:
        tasks = file.readlines()
        print(tasks)
        for i, task in enumerate(tasks, start=1):
            print(f"{i} . {task.strip()}")


def clear_tasks():
    with open(TASK_FILE, "w") as file:
        pass
    print("All tasks cleared.")


def todo_menu():
    while True:
        print("\n--- To-Do Menu ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Clear Tasks")
        print("4. Back to Main Menu")
        choice = input("Choose an option 1 - 4: ")

        if choice == "1":
            task = input("Enter a new Task: ")
            add_task(task)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            clear_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice, try again.")


def run_assistant():
    greet_user()
    while True:
        show_menu()
        choice = input("Choose an option 1 - 4: ")

        if choice == "1":
            calculator()
        elif choice == "2":
            tell_joke()
        elif choice == "3":
            show_time()
        elif choice == "4":
            todo_menu()
        elif choice == "5":
            city = input("Enter city name: ")
            get_weather(city)

        elif choice == "6":
            print("Goodbye! Have a great day!")
            break

        else:
            print("Invalid choice, try again.")


def get_weather(city):
    BASE_URL = os.getenv("BASE_URL")
    API_KEY = os.getenv("API_KEY")
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        weather = data["weather"][0]["description"]
        temperature = main["temp"]
        print(f"Weather in {city} : {weather} , {temperature}C")

    else:
        print("City Not Found")


def init_db():
    conn = sqlite3.connect("assistant.db")
    cursor = conn.cursor()
    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT NOT NULL)"""
    )
    conn.commit()
    conn.close()


def sign_up(username, password):
    conn = sqlite3.connect("assistant.db")
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?,?)", (username, password)
        )
        conn.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError:
        print("Username already exists. Try a different one.")

    conn.close()


def login(username, password):
    conn = sqlite3.connect("assistant.db")
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


if __name__ == "__main__":
    init_db()
    print("Welcome to the Smart Personal Assistant")
    print("1.Signup")
    print("2.Login")

    choice = input("Choose an option 1 or 2: ")
    if choice == "1":
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        sign_up(username, password)
    elif choice == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if login(username, password):
            run_assistant()
        else:
            print("Exiting the program.")
