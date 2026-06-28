# Mutable and Immutable in Python

# Immutable examples
name = "Alice"
print(name)  # Alice
print(id(name))

# Reassigning creates a new object
name = "Bob"
print(name)  # Bob
print(id(name))

# Mutable example
numbers = [1, 2, 3]
print(numbers)  # [1, 2, 3]

# Changing the list modifies the same object
numbers.append(4)
print(numbers)  # [1, 2, 3, 4]

# Explanation
print("\nImmutable objects cannot be changed in place.")
print("Mutable objects can be changed in place.")
