# cs362 - hw03
# casey nord
# spring 2021

# get user input from console
while True:
    try:
        year = int(input("Enter year as a positive integer: "))
        if year < 0:
            raise ValueError

        break  # exit loop on valid input
    except ValueError:
        print("Invalid input, please try again...")

# test value for leap year condition
valid_condition_01 = (year % 4 == 0) and (year % 100 != 0)
valid_condition_02 = (year % 400 == 0)

if valid_condition_01 or valid_condition_02:
    print("{0} is a leap year".format(year)) 
else:
    print("{0} is not a leap year".format(year))
