#Sara Margaret Rizzo
#2020-08-30
#Problem 3 – Write a function that takes a list and prints if the value 5 is in that list.

#fuction that checks if 5 is in list
def list5(list):
    if 5 in list:
        print("5 is in this list")
    else:
        print("5 is not in this list")

#list has five
list = [1, 2, 3, 4, 5]
list5(list)
#list that does not
list = [6, 7, 8, 9, 10, -5, 0]
list5(list)