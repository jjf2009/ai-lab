"""
Program 7: Print Multiplication Tables from 1 to 10
"""


def print_all_tables(start=1, end=10, upto=10):
    for num in range(start, end + 1):
        print(f"\n{'=' * 28}")
        print(f"  Multiplication Table of {num}")
        print(f"{'=' * 28}")
        for i in range(1, upto + 1):
            print(f"  {num} x {i:2} = {num * i:3}")


def print_tables_grid(start=1, end=10, upto=10):
    """Compact side-by-side style summary."""
    print("\n" + "=" * 50)
    print("  COMPACT VIEW (n x 1 .. n x 10)")
    print("=" * 50)
    for num in range(start, end + 1):
        row = "  ".join(f"{num * i:3}" for i in range(1, upto + 1))
        print(f"{num:2} | {row}")


def main():
    print("=" * 40)
    print("  MULTIPLICATION TABLES (1 TO 10)")
    print("=" * 40)

    print_all_tables(1, 10, 10)
    print_tables_grid(1, 10, 10)
    print("\nProgram completed successfully.")


if __name__ == "__main__":
    main()
