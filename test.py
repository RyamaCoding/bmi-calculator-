year = int(input("Which year do you want to check?"))

# Check if the year is a leap year

if (year % 4 == 0) and (year % 100 != 0):
    print("Leap year")
elif (year % 100 == 0) and (year % 400 == 0):
    print("Leap year")
else: print("Not a leap year")