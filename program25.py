a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# calculating semi-perimeter
s = (a + b + c) / 2

# calculating area using Heron's formula
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# printing the result
print("Area of the triangle is:", area)