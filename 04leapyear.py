#Sara Margaret Rizzo
#2020-08-30
#Problem 4 – Write a function that takes a year as a parameter 
#and returns True if the year is a leap year, False if it is otherwise.

def leapyear(year):
    if year %4 == 0:
        if year %100 == 0:
            if year %400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input("Enter a year:"))
leapyear(year)
if leapyear(year) == True:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")