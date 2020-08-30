#Sara Margaret Rizzo
#2020-08-26
#Problem 1 – Write a function that takes two inputs from a user 
#and prints whether they are equal or not.

def equal10(x, y):
    #compare x and y
    if x == y:
        print(x, "is equal to", y)
    else:
        print(x, "is not equal to", y)

#get input from user
x = (input("Enter a number: "))
y = (input("Enter a number: "))

#call function
equal10(x, y)