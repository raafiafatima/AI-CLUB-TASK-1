# TITLE: Even Odd Number 

# PARAMETERS: 
#  - num (int): Number that is even or odd

# RETURNS: 
# - str: Whether the number is even or odd

# TEST CASE 1
# Input: 123456 (large even number)
# Expected Output: Even

# TEST CASE 2
# Input: 2 (small even number)
# Expected Output: Even


# TEST CASE 3
# Input: 5 (small even number)
# Expected Output: Odd

def even_odd():
    num = int(input("Enter number "))
    if num%2 == 0:
        return("The given number is even ")
    else:
        return("The given number is odd ")

# print(even_odd())

# TITLE: Finding Min & Max numbers in a sequence(List) 

# PARAMETERS: 
#  - list l: List to find max and min number 
#  - int n: size of input 
#  - int num: number for list
#  - int x: max number  
#  - int y: min number  

# RETURNS: 
# - str and int: Whether the number is max or min 

# TEST CASE 1
# [5, 2, 7, 5, 9, 2, 7]
# Expected Output (Max): 9
# Expected Output (Min): 2

# TEST CASE 2
# [3, 6, 2, 8, 1]
# Expected Output (Max): 8
# Expected Output (Min): 1

def max_min():
    n = int(input("Enter size of input "))
    l = []
    for i in range (0,n):
        num  = int(input("Enter number "))
        l.append(num)
    x = max(l)
    y = min(l)
    print(f"The maximum number is {x}")
    print(f"The minimum number is {y}")
    
print(max_min())
    
# TITLE: Table of any number

# PARAMETERS: 
#  - int tn: table number 
#  - int tr: table range


# RETURNS: 
# - str and int: table of given number

# TEST CASE 1
# Number = 5, Range = 10
# Expected Output:

# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 10 = 50

# TEST CASE 2
# Number = 7, Range = 4
# Expected Output:

# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
    
def table():
    tn = int(input("Enter number "))
    tr = int(input("Enter range "))
    for i in range(1,tr+1):
        print(tn,"*",i,"=",tn*i)
    
# table()

# TITLE: Factorial of any number

# PARAMETERS: 
#  - int num: number for factorial 
#  - int fact: factorial of the number 


# RETURNS: 
# - int: factorial of given number

# TEST CASE 1
# Input: 5
# Expected Output: the factorial of num is 120

# TEST CASE 2
# Input: 4
# Expected Output: 24
     
def factorial():
    fact = 1
    num = int(input("Enter number "))
    if num == 1 or num == 0:
        return (f"The factorial of {num} is 1")
    else:
        for i in range(1,num+1):
            fact = fact*i
        return(f"The factorial of {num} is {fact}")
    
# print(factorial())


# TITLE: Sum of given sequence (list)

# PARAMETERS: 
#  - int n: number of elements inside the list  
#  - list l: list of number 
#  - int s: sum of list


# RETURNS: 
# - int: sum of given list 


# TEST CASES 
# Input: [1, 2, 3, 4, 5]
# Expected Output: 15

# TEST CASES 
# Input: [-1, 2, -3, 4, -5]
# Expected Output: -3
def sum_of_list():
    n = int(input("Enter size of input "))
    l = []
    for i in range (0,n):
        num  = int(input("Enter number "))
        l.append(num)
    s = sum(l)
    return (f"The sum of list is {s}")

# print(sum_of_list())    

# TITLE: Generating acsending and decending numbers sequence using loop

# PARAMETERS: 
#  - int n: number of elements inside the list  
#  - list l: list of number 
#  - int num: numbers for list
#  - int temp: variable to temporary store element


# RETURNS: 
# - list: ascending and descending order of list 


# TEST CASES 
# Input: [5,7,6,2,9,8,10,1,3,4]
# Expected Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# TEST CASES 
# Input: [0,1,-1,4,-4,3,-3,5,2,-5,-2]
# Expected Output: [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]
# Expected Output: [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]

def asc_dec():
    n = int(input("Enter size of input "))
    l = []
    for i in range (0,n):
        num  = int(input("Enter number "))
        l.append(num)

    for j in range(len(l)):
        for i in range(0,len(l)-1):
            if l[i]<l[i+1]:
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp
    print (f"Descending {l}")

    for j in range(len(l)):
        for i in range(0,len(l)-1):
            if l[i]>l[i+1]:
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp
    print (f"Ascending {l}")

# print(asc_dec())
    
# TITLE: Calculating area of a circle

# PARAMETERS: 
#  - int r: radius of circle 
#  - int a : area of circle

# RETURNS: 
# - int: area of circle

# TEST CASES 
# Input: Radius = 5
# Expected Output: Area = π * radius^2 = 3.14159 * 5^2 = 78.53975

# TEST CASES 
# Input: Radius = 3.5
# Expected Output: Area = 38.4848875
import math 
def area():
    r = int(input("Enter radius "))
    a = math.pi*(r**2)
    return(f'Area of circle is {round(a,3)}')

# print(area())

# TITLE: Convert Celsius to Fahrenheit and vice versa

# PARAMETERS: 
#  - int yrmp : tempersture in fahrenhite or celsius 
#  - int a : area of circle

# RETURNS: 
# - int f: temperature in fahrenhite
# - int c: temperature in celsius

# TEST CASES 
# Input: Fahrenheit = 32
# Expected Output: Celsius ≈ 0

# TEST CASES 
# Input: Fahrenheit = 212
# Expected Output: Celsius ≈ 100

def fahrenhite():
    temp = float(input("Enter temperature in Celsius "))
    f = (9/5)*temp +32 
    return (f'Temperature in Fahrenhite is {round(f,3)}')

# print(fahrenhite())

def celsius():
    temp = float(input("Enter temperature in Fahrenhite "))
    c = (temp - 32)*(5/9)
    return (f'Temperature in Celsius is {round(c,3)}')

# print(celsius())

# TITLE: Sum of the first n positive integers

# PARAMETERS: 
#  - int num: nth number 
#  - int sum : sum till nth number 

# RETURNS: 
# - int: sum till nth number 

# TEST CASES 
# Input:n=5
# Expected Output: sum = 15

# TEST CASES 
# Input:n=100
# Expected Output: sum = 5050

def sum_of_int():
    num = int(input("Enter number "))
    sum = 0
    for i in range (0,num+1):
        sum = sum+i
    return (f'Sum of first {num} positive integers is {sum}')

# print(sum_of_int())

# TITLE: Linear search

# PARAMETERS: 
#  - int r: size of input
#  - list l : empty list
#  - int x : number to be searched

# RETURNS: 
# - int: position (index) of number in array

# TEST CASES 
# Input: List = [1, 2, 3, 4, 5], Target = 3
# Expected Output: Index = 2 (since 3 is at index 2 in the list)

# TEST CASES 
# Input: List = [1, 2, 3, 4, 5], Target = 6
# Expected Output: 6 not present in list 


def search():
    n = int(input("Enter size of input "))
    l = []
    for i in range (0,n):
        num  = int(input("Enter number "))
        l.append(num)
    x = int(input("enter number to be searched "))
    for i in range(len(l)):
        if l[i] == x:
            return(f"The index of {x} is {i}")
            break
        else:
            return(f"{x} is not present in given list ")
            continue

# print(search())



    


























