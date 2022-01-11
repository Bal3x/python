# write a program that works out wheter if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. 


# 1. On every year that is evenly divisible by 4 
# 2. Except every year that is evenly divisible by 100 
# 3. Unless the year is also evenly divisible by 400

year = int(input("Which year do you want to check?\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

