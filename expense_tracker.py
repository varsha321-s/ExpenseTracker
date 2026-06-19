import csv
import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"

def add_entry():
    date = input("Enter Date (YYYY-MM-DD): ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))
    entry_type = input("Income or Expense: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, entry_type])

    print("Entry Added Successfully!")

def view_entries():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            print("\n===== ALL ENTRIES =====")
            for row in reader:
                print(row)

    except FileNotFoundError:
        print("No entries found!")

def monthly_summary():

    total_income = 0
    total_expense = 0

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:

                amount = float(row[2])

                if row[3].lower() == "income":
                    total_income += amount

                elif row[3].lower() == "expense":
                    total_expense += amount

        balance = total_income - total_expense

        print("\n===== MONTHLY SUMMARY =====")
        print("Total Income:", total_income)
        print("Total Expense:", total_expense)
        print("Balance:", balance)

    except FileNotFoundError:
        print("No entries found!")

def export_to_excel():

    try:

        data = pd.read_csv(
            FILE_NAME,
            header=None,
            names=["Date", "Category", "Amount", "Type"]
        )

        data.to_excel("expenses.xlsx", index=False)

        print("Excel file created successfully!")

    except FileNotFoundError:
        print("No entries found!")

def create_chart():

    try:

        data = pd.read_csv(
            FILE_NAME,
            header=None,
            names=["Date", "Category", "Amount", "Type"]
        )

        expenses = data[data["Type"].str.lower() == "expense"]

        category_total = expenses.groupby("Category")["Amount"].sum()

        category_total.plot(kind="bar")

        plt.title("Expenses by Category")
        plt.ylabel("Amount")

        plt.savefig("expense_chart.png")

        plt.close()

        print("Chart created successfully!")

    except FileNotFoundError:
        print("No entries found!")

while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Entry")
    print("2. View Entries")
    print("3. Monthly Summary")
    print("4. Export to Excel")
    print("5. Create Chart")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_entry()

    elif choice == "2":
        view_entries()

    elif choice == "3":
        monthly_summary()

    elif choice == "4":
        export_to_excel()

    elif choice == "5":
        create_chart()

    elif choice == "6":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")