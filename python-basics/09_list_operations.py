"""
Program 9: List Operations
Demonstrates append, remove, insert, merge, and other common list operations.
"""


def main():
    print("=" * 50)
    print("  LIST OPERATIONS IN PYTHON")
    print("=" * 50)

    # Create a list
    fruits = ["apple", "banana", "cherry"]
    print(f"\n1. Original list: {fruits}")

    # Append - add element at the end
    fruits.append("date")
    print(f"2. After append('date'): {fruits}")

    # Insert - add element at a specific index
    fruits.insert(1, "blueberry")
    print(f"3. After insert(1, 'blueberry'): {fruits}")

    # Extend - add multiple elements
    fruits.extend(["elderberry", "fig"])
    print(f"4. After extend(['elderberry', 'fig']): {fruits}")

    # Remove - remove first occurrence of a value
    fruits.remove("banana")
    print(f"5. After remove('banana'): {fruits}")

    # Pop - remove and return element at index (default last)
    popped = fruits.pop()
    print(f"6. After pop() -> removed '{popped}': {fruits}")
    popped_idx = fruits.pop(0)
    print(f"7. After pop(0) -> removed '{popped_idx}': {fruits}")

    # Index - find position of an element
    if "cherry" in fruits:
        idx = fruits.index("cherry")
        print(f"8. Index of 'cherry': {idx}")

    # Count
    fruits.append("cherry")
    print(f"9. After another append('cherry'): {fruits}")
    print(f"   Count of 'cherry': {fruits.count('cherry')}")

    # Sort and reverse
    numbers = [5, 2, 9, 1, 7, 3]
    print(f"\n10. Numbers list: {numbers}")
    numbers.sort()
    print(f"    After sort(): {numbers}")
    numbers.reverse()
    print(f"    After reverse(): {numbers}")

    # Sorted (returns new list, original unchanged)
    original = [4, 1, 8, 3]
    sorted_copy = sorted(original)
    print(f"\n11. Original: {original}")
    print(f"    sorted(original): {sorted_copy}")

    # Merge two lists
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print(f"\n12. Merging lists:")
    print(f"    list1 = {list1}")
    print(f"    list2 = {list2}")

    # Method A: concatenation with +
    merged_plus = list1 + list2
    print(f"    list1 + list2 = {merged_plus}")

    # Method B: unpacking
    merged_unpack = [*list1, *list2]
    print(f"    [*list1, *list2] = {merged_unpack}")

    # Method C: extend (modifies list1)
    list1_copy = list1.copy()
    list1_copy.extend(list2)
    print(f"    list1.extend(list2) = {list1_copy}")

    # Slicing
    data = [10, 20, 30, 40, 50, 60]
    print(f"\n13. Slicing on {data}:")
    print(f"    data[1:4]  = {data[1:4]}")
    print(f"    data[:3]   = {data[:3]}")
    print(f"    data[3:]   = {data[3:]}")
    print(f"    data[::-1] = {data[::-1]}")

    # Length, min, max, sum
    print(f"\n14. Aggregate operations on {data}:")
    print(f"    len  = {len(data)}")
    print(f"    min  = {min(data)}")
    print(f"    max  = {max(data)}")
    print(f"    sum  = {sum(data)}")

    # Clear
    temp = [1, 2, 3]
    temp.clear()
    print(f"\n15. After clear() on [1,2,3]: {temp}")

    # List comprehension
    squares = [x ** 2 for x in range(1, 6)]
    print(f"\n16. List comprehension (squares of 1..5): {squares}")

    print("\nProgram completed successfully.")


if __name__ == "__main__":
    main()
