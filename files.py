# TITLE: takes the name of a file as input and returns occurances of word inside file

# PARAMETERS: 
#  - str name : name of file
#  - str word : word 
#  - str count : occurances of word

# RETURNS: 
# - int and str: count of word
# 

# TEST CASES 
# Input: File = "sample.txt", Word = "apple" (assuming "apple" appears multiple times in the file)
# Expected Output: Count of occurrences of "apple" in the file

# TEST CASES 
# Input: File = "sample.txt", Word = "banana" (assuming "banana" does not appear in the file)
# Expected Output: 0 (since "banana" does not appear in the file)

def search_word(name,word):
    file = open(f"{name}.txt","r")
    data = file.read()
    count = 0
    x = data.split()
    for i in x:
        if i == word:
            count += 1
    return (f'{word} occurs {count} times in the file ')

# print(search_word("hello" , "i"))

# TITLE: takes the name of a file as input and returns number of lines, words and character

# PARAMETERS: 
#  - str name : name of file
#  - str word : word inside the file
#  - str char : characters inside the file
#  - str line : lines inside the file

# RETURNS: 
# - int and str: number of words, char and lines

# TEST CASES 
# Input: File = "sample.txt" (containing multiple lines, words, and characters)
# Expected Output: Number of lines, words, and characters in the file

# TEST CASES 
# Input: File = "single_line.txt" (containing one line of text)
# Expected Output: Number of lines = 1, Number of words, Number of characters

def analyze_file(name):
    file = open(f"{name}.txt","r")
    data = file.read()
    char = 0
    word = 0
    # lines = 0
    y = file.readlines()
    # for line in file:
    #     lines += 1
    x = data.split()
    for i in x:
        word += 1
        for j in i:
            char += 1
    print(f'The number of characters in the file are {char}')
    print(f'The number of words in the file are {word}')
    print(f'The number of lines in the file are {y}')
    file.close()

# analyze_file("hello")

# TITLE: encrypt a given string using the Caesar cipher with a specified shift value.

# PARAMETERS: 
#  - str word : plain text
#  - str ans : encrypted text
#  - str shift : ceasar shift 


# RETURNS: 
# - str: encrypted text

# TEST CASES 
# Input: ("hello", 3) 
# Expected Output: "khoor"

# TEST CASES 
# Input: ("world", 5) 
# Expected Output: "btwqi"
    
def ceasar_cipher():
    # 97 to 122
    word = input("Enter phrase ").lower()
    shift = int(input("Enter number for shift "))
    ans  = ""
    for i in range (len(word)):
        char  = word[i]
        if char == " ":
            ans += " "
        else :
            ans += chr((ord(char) + shift-97) % 26 + 97)
    return (f"The encrypted text is {ans}")

# print(ceasar_cipher())

# TITLE: the second minimum and maximum elements from an integer array

# PARAMETERS: 
#  - int x : first max number
#  - int y : first min number
#  - int maximum : second max number
#  - int minimum : second max number

# RETURNS: 
# - str and int: second maximum and minimum number 

# TEST CASES 
# Input Array: [3, 1, 7, 4, 9, 2] 
# Expected Output: Second Min: 2, Second Max:7

# TEST CASES 
# Input Array: [5, 5, 3, 8, 2, 9, 1] 
# Expected Output: Second Min: 2, Second Max: 8


def find_second_min_max():
    n = int(input("Enter size of input "))
    l = []
    for i in range (0,n):
        num  = int(input("Enter number "))
        l.append(num)
    x = max(l)
    l.remove(x)
    maximum = max(l)
    y = min(l)
    l.remove(y)


    minimum = min(l)
    print(f'The second maximum number of given array is {maximum}')
    print(f'The second minimum number of given array is {minimum}')

find_second_min_max()




    



