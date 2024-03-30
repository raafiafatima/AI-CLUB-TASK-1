# TITLE: calculator

# PARAMETERS: 
#  - int x : first input
#  - int y : second input
#  - int z : output
#  - int c : choice of operation


# RETURNS: 
# - int : answer of the operation 


# TEST CASES 
# Input: 2 + 3
# Expected Output: 5

# TEST CASES 
# Input: 5 - 3
# Expected Output: 2

import math

def add(): #function for addition
    z = x + y
    return(f"RESULT: {x} + {y} = {z}")

def sub():  #function for subtraction
    z = x - y
    return(f"RESULT: {x} - {y} = {z}")

def mul():  #function for multiplication
    z = x * y
    return(f"RESULT: {x} * {y} = {z}")

def div():  #function for division
    try: 
        z = x / y
        return(f" RESULT: {x} / {y} = {round(z,3)}")
    except ZeroDivisionError:
        print("You cannot divide by zero ")



print(f'            Welcome to Calculator                 ')   
q = True 
while q:
    print()                                                #Giving choice of operation 
    print ("1 . ADDITION ")
    print ("2 . SUBTRACTION ")
    print ("3 . MULTIPLICATION ")
    print ("4 . DIVISION ")
    print ("5 . EXIT ")
    
    c = int(input("Choose your operation "))

    if c == 5:   #code for exiting the programe 
        print("Exiting..... Goodbyee")
        break 

    x = int(input("Enter 1st number  "))
    y = int(input("Enter 2nd number "))

    if x==" " or y == " ":   #input validation
        print("Enter valid text ")


    if c == 1:
        print(add())

    if c == 2:
        print(sub())

    if c == 3:
        print(mul())

    if c == 4:
        print(div())

    






























































































