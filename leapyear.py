# cs362 - hw03
# casey nord
# spring 2021

# get user input from console
year = int(input("Enter year as a positive integer: "))

# test value for leap year condition
valid_condition_01 = (year % 4 == 0) and (year % 100 != 0)
valid_condition_02 = (year % 400 == 0)

if valid_condition_01 or valid_condition_02:
    print("{0} is a leap year".format(year)) 
else:
    print("{0} is not a leap year".format(year))
