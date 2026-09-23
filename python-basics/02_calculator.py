"""
Program 2: Menu-Driven Calculator
Performs arithmetic operations using Python variables.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None  # signal division by zero
    return a / b


def modulus(a, b):
    if b == 0:
        return None
    return a % b


def power(a, b):
    return a ** b


def display_menu():
    print("\n" + "=" * 40)
    print("        MENU-DRIVEN CALCULATOR")
    print("=" * 40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. Exit")
    print("=" * 40)


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "7":
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ("1", "2", "3", "4", "5", "6"):
            print("Invalid choice. Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == "1":
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == "2":
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == "3":
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == "4":
            result = divide(num1, num2)
            if result is None:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"Result: {num1} / {num2} = {result}")
        elif choice == "5":
            result = modulus(num1, num2)
            if result is None:
                print("Error: Modulus by zero is not allowed.")
            else:
                print(f"Result: {num1} % {num2} = {result}")
        elif choice == "6":
            result = power(num1, num2)
            print(f"Result: {num1} ** {num2} = {result}")


if __name__ == "__main__":
    main()
