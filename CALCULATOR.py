# ==========================================
#        ADVANCED PYTHON CALCULATOR
# ==========================================

import math
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def calculator():

    while True:

        clear()

        print("=" * 50)
        print("             🧮 PYTHON CALCULATOR")
        print("=" * 50)

        print("""
        1. Addition          (+)
        2. Subtraction       (-)
        3. Multiplication    (*)
        4. Division          (/)
        5. Power             (**)
        6. Percentage        (%)
        7. Square Root       (√)
        8. Exit
        """)

        print("=" * 50)

        choice = input("Enter your choice: ")

        # Addition
        if choice == "1":
            a = float(input("\nEnter first number: "))
            b = float(input("Enter second number: "))

            print(f"\n✅ Result = {a + b}")

        # Subtraction
        elif choice == "2":
            a = float(input("\nEnter first number: "))
            b = float(input("Enter second number: "))

            print(f"\n✅ Result = {a - b}")

        # Multiplication
        elif choice == "3":
            a = float(input("\nEnter first number: "))
            b = float(input("Enter second number: "))

            print(f"\n✅ Result = {a * b}")

        # Division
        elif choice == "4":
            a = float(input("\nEnter first number: "))
            b = float(input("Enter second number: "))

            if b == 0:
                print("\n❌ Cannot divide by zero!")
            else:
                print(f"\n✅ Result = {a / b}")

        # Power
        elif choice == "5":
            a = float(input("\nEnter base: "))
            b = float(input("Enter power: "))

            print(f"\n✅ Result = {a ** b}")

        # Percentage
        elif choice == "6":
            number = float(input("\nEnter number: "))
            percent = float(input("Enter percentage: "))

            result = (number * percent) / 100

            print(f"\n✅ Result = {result}")

        # Square Root
        elif choice == "7":
            number = float(input("\nEnter number: "))

            if number < 0:
                print("\n❌ Cannot find square root of a negative number.")
            else:
                print(f"\n✅ √{number} = {math.sqrt(number)}")

        # Exit
        elif choice == "8":
            print("\n👋 Calculator closed!")
            break

        else:
            print("\n❌ Invalid choice!")

        input("\nPress ENTER to continue...")


calculator()