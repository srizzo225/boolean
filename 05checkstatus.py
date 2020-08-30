#Sara Margaret Rizzo
#2020-08-30
#Problem 5 - Write a function that checks whether your game character 
#has picked up all the items needed to perform certain tasks 
#and checks against any status debuffs. 
#Confirm checks with print statements.
#Game Character has the following item list: [pan, paper, idea, rope, groceries]
#Game Character has the following status debuffs: [slow]

#Task 1: Climb a mountain – needs rope, coat, and first aid kit, cannot have slow
def task1(items, debuffs):
    if "rope" and "coat" and "first aid kit" in items:
        if "slow" in debuffs:
            print("Character has correct items, but not correct status for Task 1: Climb a mountain")
        else:
            print("Character has correct items and status for Task 1: Climb a mountain")
    else:
        print("Character does not have correct items and status for Task 1: Climb a mountain")

#Task 2: Cook a meal – needs pan, groceries, cannot have small
def task2(items, debuffs):
    if "pan" and "groceries" in items:
        if "small" in debuffs:
            print("Character has correct items, but not correct status for Task 2: Cook a meal")
        else:
            print("Character has correct items and status for Task 2: Cook a meal")
    else:
        print("Character does not have correct items and status for Task 2: Cook a meal")

#Task 3: Write a book – needs pen, paper, idea, cannot have confusion
def task3(items, debuffs):
    if "pen" and "paper" and "idea" in items:
        if "confusion" in debuffs:
            print("Character has correct items, but not correct status for Task 3: Write a book")
        else:
            print("Character has correct items and status for Task 3: Write a book")
    else:
        print("Character does not have correct items and status for Task 3: Write a book")

#call function
items = ["pan", "paper", "idea", "rope", "groceries"]
debuffs = ["slow"]
task1(items, debuffs)
task2(items, debuffs)
task3(items, debuffs)