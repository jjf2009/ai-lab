"""
Program 3: Determine Whether a Number is Positive, Negative, or Zero
"""


def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


def main():
    print("=" * 45)
    print("  POSITIVE / NEGATIVE / ZERO CHECKER")
    print("=" * 45)

    try:
        number = float(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    result = check_number(number)
    print(f"\nThe number {number} is {result}.")

    # Extra demo with sample values
    print("\n--- Sample checks ---")
    for sample in [15, -7, 0, 3.14, -0.5]:
        print(f"  {sample:>6} -> {check_number(sample)}")


if __name__ == "__main__":
    main()
