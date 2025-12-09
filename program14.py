# getting millimeters from the user
mm = float(input("Enter length in millimeters: "))

# conversion factor
INCH = 25.4  # 1 inch = 25.4 mm

# converting mm to inches
inches = mm / INCH

# printing the result
print(mm, "millimeters is equal to", inches, "inches")