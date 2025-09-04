import datetime
import os
import random

ASSISTANT_NAME = "smart personal assistant"


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
    print("3. Show Currenrt Time")
    print("4. Exit")


def calculator():
    print("Welcome to the calculator!")
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print("Addition:" , a + b)
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
        "Why did the bicycle fall over? Because it was two-tired!"
    ]
    print(random.choice(jokes))

def show_time():
    now  = datetime.datetime.now().strftime("%H:%M:%S")
    print("Current Time is: ", now)


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
            print("Goodbye! Have a great day!")
            break
        
        else:
            print("Invalid choice, try again.")
            
run_assistant()
