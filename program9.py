# getting four numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))

# finding the maximum
maximum = num1  # assume first number is maximum

if num2 > maximum:
    maximum = num2
if num3 > maximum:
    maximum = num3
if num4 > maximum:
    maximum = num4

# printing the maximum number
print("The maximum number is:", maximum)