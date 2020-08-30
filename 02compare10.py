#Sara Margaret Rizzo
#2020-08-26
#Problem 2 – Write a function that takes two inputs from a user 
#and prints whether the sum is greater than 10, less than 10, or equal to 10.

def compare10(x, y):
    #sum of input
    z = x + y
    #compare sum to 10
    if z > 10:
        print("The sum of", x, "and", y, "is greater than 10.")
    elif z < 10:
        print("The sum of", x, "and", y, "is less than 10.")
    else:
        print("The sum of", x, "and", y, "is equal to 10.")

#get input from user
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

#call function
compare10(x, y)