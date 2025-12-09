a = input("Enter first value: ")
b = input("Enter second value: ")

# printing before swapping
print("Before swapping: a =", a, "b =", b)

# swapping using a temporary variable
temp = a
a = b
b = temp

# printing after swapping
print("After swapping: a =", a, "b =", b)