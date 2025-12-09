# getting student details
roll_no = input("Enter your Roll No.: ")
marks_pf = int(input("Enter marks in Programming Fundamentals: "))
marks_ic = int(input("Enter marks in Introduction to Computing: "))
marks_cg = int(input("Enter marks in Computer Graphics: "))

# calculating total and average
total = marks_pf + marks_ic + marks_cg
average = total / 3

# printing the results
print("Roll No.:", roll_no)
print("Total marks:", total)
print("Average marks:", average)