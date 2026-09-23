"""
Program 1: Variables and Different Data Types in Python
Demonstrates declaration, assignment, type checking, and conversion.
"""

print("=" * 50)
print("PYTHON VARIABLES AND DATA TYPES")
print("=" * 50)

# 1. Integer
age = 20
print(f"\nInteger: age = {age}")
print(f"  Type: {type(age)}")

# 2. Float
height = 5.9
print(f"\nFloat: height = {height}")
print(f"  Type: {type(height)}")

# 3. String
name = "Alice"
print(f"\nString: name = '{name}'")
print(f"  Type: {type(name)}")

# 4. Boolean
is_student = True
print(f"\nBoolean: is_student = {is_student}")
print(f"  Type: {type(is_student)}")

# 5. List (ordered, mutable collection)
subjects = ["Math", "Physics", "Chemistry"]
print(f"\nList: subjects = {subjects}")
print(f"  Type: {type(subjects)}")

# 6. Tuple (ordered, immutable collection)
coordinates = (10, 20)
print(f"\nTuple: coordinates = {coordinates}")
print(f"  Type: {type(coordinates)}")

# 7. Dictionary (key-value pairs)
student = {"name": "Bob", "roll": 101, "marks": 85.5}
print(f"\nDictionary: student = {student}")
print(f"  Type: {type(student)}")

# 8. Set (unordered, unique elements)
unique_ids = {1, 2, 3, 2, 1}
print(f"\nSet: unique_ids = {unique_ids}")
print(f"  Type: {type(unique_ids)}")

# 9. NoneType
result = None
print(f"\nNoneType: result = {result}")
print(f"  Type: {type(result)}")

# Type conversion examples
print("\n" + "=" * 50)
print("TYPE CONVERSION")
print("=" * 50)

num_str = "42"
num_int = int(num_str)
num_float = float(num_str)
print(f"\nString '{num_str}' -> int: {num_int} ({type(num_int).__name__})")
print(f"String '{num_str}' -> float: {num_float} ({type(num_float).__name__})")

pi = 3.14159
print(f"\nFloat {pi} -> int: {int(pi)}")
print(f"Integer {age} -> str: '{str(age)}'")
print(f"Integer {age} -> float: {float(age)}")
print(f"Integer {age} -> bool: {bool(age)}  (0 is False, non-zero is True)")

# Multiple assignment
print("\n" + "=" * 50)
print("MULTIPLE ASSIGNMENT")
print("=" * 50)

x, y, z = 1, 2.5, "hello"
print(f"x = {x}, y = {y}, z = '{z}'")

a = b = c = 0
print(f"a = b = c = {a}")

print("\nProgram completed successfully.")
