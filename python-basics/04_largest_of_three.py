"""
Program 4: Find the Largest of Three Numbers
"""


def largest_of_three(a, b, c):
    """Return the largest among a, b, and c."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def main():
    print("=" * 40)
    print("  LARGEST OF THREE NUMBERS")
    print("=" * 40)

    try:
        n1 = float(input("Enter first number:  "))
        n2 = float(input("Enter second number: "))
        n3 = float(input("Enter third number:  "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    largest = largest_of_three(n1, n2, n3)
    print(f"\nAmong {n1}, {n2}, and {n3}")
    print(f"The largest number is: {largest}")

    # Also show using built-in max() for comparison
    print(f"(Verified with max(): {max(n1, n2, n3)})")


if __name__ == "__main__":
    main()
