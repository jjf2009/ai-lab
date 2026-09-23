"""
Program 5: Print Numbers from 1 to 10
Demonstrates for-loop, while-loop, and list comprehension approaches.
"""

print("=" * 40)
print("  PRINT NUMBERS FROM 1 TO 10")
print("=" * 40)

# Method 1: for loop with range()
print("\nMethod 1 - for loop with range():")
for i in range(1, 11):
    print(i, end=" ")
print()

# Method 2: while loop
print("\nMethod 2 - while loop:")
n = 1
while n <= 10:
    print(n, end=" ")
    n += 1
print()

# Method 3: list and join
print("\nMethod 3 - list comprehension + join:")
numbers = [str(i) for i in range(1, 11)]
print(" ".join(numbers))

print("\nProgram completed successfully.")
