hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

# converting time into seconds
total_seconds = (hours * 3600) + (minutes * 60) + seconds

# printing the result
print("Total time in seconds is:", total_seconds)
