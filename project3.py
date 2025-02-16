import csv  # To handle saving expenses in a CSV file
import os  

FILE_NAME = "expenses.csv"

# 1️ Make sure the file exists before using it
def setup_file():
    if not os.path.exists(FILE_NAME):  
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", " Amount", " Category", " Description"])  # Column headers

# 2️ Function to add a new expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")  
    amount = input("Enter amount spent: ")  
    category = input("Enter category (Food, Transport, etc.): ")  
    description = input("Enter description: ")  
    
    # Open the file in append mode (to add new data)
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])  # Save the new expense
    
    print("✅ Expense added successfully!\n")

# 3️ Function to show all expenses
def view_expenses():
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            print("\n📜 Your Expenses:")
            print("Date        | Amount  | Category      | Description")
            print("-" * 50)

            for row in reader:
                print(f"{row[0]} | ₹{row[1]:<7} | {row[2]:<12} | {row[3]}")  # Nicely formatted output
            print()

    except FileNotFoundError:
        print(" No expenses recorded yet. Start adding some!\n")

# 4️ Function to show total spent in a category
def category_summary():
    category = input("Enter category to check total expenses: ")
    total = 0  # Start total from zero

    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            for row in reader:
                if row[2].lower() == category.lower():  # Check if category matches
                    total += float(row[1])  # Add to total
            
        print(f"Total spent on '{category}': ₹{total}\n")

    except FileNotFoundError:
        print(" No expenses recorded yet!\n")

# 5️ Function to display the menu
def menu():
    while True:
        print("\n Expense Tracker Menu")
        print("1️ Add Expense")
        print("2️ View All Expenses")
        print("3️ View Category Summary")
        print("4️ Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            category_summary()
        elif choice == '4':
            print("👋 Exiting... Have a great day!")
            break  # End the loop
        else:
            print("Invalid choice! Try again.\n")

# 6️ Start the program!
if __name__ == "__main__":
    setup_file()  
    menu()  
