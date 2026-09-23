"""
Program 8: Function to Calculate Area of a Circle
Define a function and invoke it to display the result.
"""

import math


def area_of_circle(radius):
    """
    Calculate the area of a circle.
    Formula: A = π * r²
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius * radius


def main():
    print("=" * 40)
    print("  AREA OF A CIRCLE")
    print("=" * 40)

    try:
        r = float(input("Enter the radius of the circle: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    if r < 0:
        print("Radius cannot be negative.")
        return

    area = area_of_circle(r)

    print(f"\nRadius (r)  = {r}")
    print(f"Formula     = π × r²")
    print(f"Area        = {area:.4f} square units")
    print(f"(using π ≈ {math.pi:.6f})")

    # Demo with sample values
    print("\n--- Sample calculations ---")
    for sample_r in [1, 2.5, 7, 10]:
        print(f"  r = {sample_r:>5}  ->  Area = {area_of_circle(sample_r):.4f}")


if __name__ == "__main__":
    main()
