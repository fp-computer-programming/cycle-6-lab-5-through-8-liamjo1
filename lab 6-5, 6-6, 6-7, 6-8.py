"""""
*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a Python file named lab_6-5
Create a program that will take a list (of numbers) of any length and return the highest and lowest value in the list. If the list does not have at least 2 unique numbers, return the string: “error: list does not meet specifications”)
hint: test the program on lists of 0,1,2 + lengths, as well as lists that do and do not meet specifications! 
"""
# Liam O'Hara

def find_min_max(input_list):
    
# Check if the list has at least 2 unique numbers
    if len(set(input_list)) < 2:
        return "error: list does not meet specifications"

# Find the minimum and maximum values in the list
    min_value = min(input_list)

    max_value = max(input_list)
    
    # Return a tuple containing the highest and lowest values
    return min_value, max_value

test_list_1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

result_1 = find_min_max(test_list_1)

print(result_1)  # Output: (1, 9)

test_list_2 = [1, 1, 1, 1, 1]

result_2 = find_min_max(test_list_2)

print(result_2)
________________________________________________________________________________
"""Create a Python file named lab_6-6

Create a program that asks a user to input 5 unique words.
Construct a list of the 5 input values, in the order that the user gave them.
Have the program display a list where each index corresponds to the length of the word given by the user at the corresponding index.
You may assume accurate input values. NO LOOPS4"""

# list comprehension used to ask the user for five words a list of words is created using the five words.

words = [input("Enter word 1: "), input("Enter word 2: "), input("Enter word 3: "), input("Enter word 4: "), input("Enter word 5: ")]

# generates a list called word_lengths, which holds the word lengths in the words list, using another list comprehension.

word_lengths = [len(word) for word in words]

# prints the original words

print("Original List of Words:", words)

# prints the list
print("Word Lengths:", word_lengths)

_______________________________________________________________________________
""""Create a Python file named lab_6-7
Create a program that asks a user to input 3 numeric values
Construct a list of the 3 input values, in the order that the user gave them.
Have the program display a list with each of the values as integers that have been doubled 
You may assume accurate input values."""

# asks the user tp input three numeric values

value1 = float(input("Enter the first numeric value: ")) 

value2 = float(input("Enter the second numeric value: ")) 

value3 = float(input("Enter the third numeric value: ")) 

# makes a list 

input_values = [value1, value2, value3]

# prints out the list

print("Original list of input values:", input_values)

# doubles all values 

doubled_values = [int(2 * value) for value in input_values]

print("Doubled values as integers:", doubled_values)
_________________________________________________________________________________
"""Create a Python file named lab_6-8
Create a program that asks a user to input 3 numeric values
Construct a list of the 3 input values, in the order that the user gave them.
Have the program display the string “even” if all numbers in the list are even.
Have the program display the string “odd” if all numbers in the list are odd.
Have the program display the string “mixed” if the numbers in the list are both even and odd.
You may assume accurate input values. You may NOT use a loop. """

# collects user inputs

num1 = float(input("Enter the first numeric value: "))

num2 = float(input("Enter the second numeric value: "))

num3 = float(input("Enter the third numeric value: "))

#creates a list

num_list = [num1, num2, num3]

# prints out the list

print("Original list:", num_list)

# numbers are checked to be either even or odd and if they're neither they are mixed

if all(num % 2 == 0 for num in num_list):

    print("even")

elif all(num % 2 != 0 for num in num_list):

    print("odd")

else:
    
    print("mixed")