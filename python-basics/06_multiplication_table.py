"""
Program 6: Print Multiplication Table of a Given Number
"""


def print_table(num, upto=10):
    print(f"\nMultiplication Table of {num}")
    print("-" * 25)
    for i in range(1, upto + 1):
        print(f"  {num} x {i:2} = {num * i}")
    print("-" * 25)


def main():
    print("=" * 40)
    print("  MULTIPLICATION TABLE")
    print("=" * 40)

    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    print_table(number)


if __name__ == "__main__":
    main()
