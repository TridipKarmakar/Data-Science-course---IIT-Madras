import json

def create_station_dict(n):
    """
    Create a nested dictionary of train details.

    Arguments:
    - n: integer, number of trains
    
    Returns:
    - A nested dictionary with train names as keys and another dictionary 
      containing compartment names and passenger counts.
    """
    station_dict = {}  # Initialize the station dictionary
    
    # Read the input for each train
    for _ in range(n):
        train_name = input().strip()  # Read train name
        m = int(input().strip())  # Read number of compartments
        
        # Create an inner dictionary for the compartments
        train_dict = {}
        
        # For each compartment, store the compartment name and passengers
        for _ in range(m):
            comp_data = input().strip().split(',')
            comp_name = comp_data[0].strip()
            passengers = int(comp_data[1].strip())
            train_dict[comp_name] = passengers
        
        # Add the train's inner dictionary to the station_dict
        station_dict[train_name] = train_dict
    
    return station_dict

# Reading the number of trains from the user
n = int(input().strip())

# Calling the function to create the station_dict
station_dict = create_station_dict(n)

# Print the resulting dictionary in JSON format with sorted keys and indentation
#print(json.dumps(station_dict, sort_keys=True, indent=2))


#Problems 2 

def is_all_same_word_twice(strings: list) -> bool:
    '''
    Checks if all strings follow the format where 
    the same word is repeated exactly twice with a hyphen in-between them.

    Args:
        strings (list): A list of strings to be checked.

    Returns:
        bool: True if all strings are of the given format, otherwise False.
    '''
    ...
    
    
    for string in strings:
        # Check if the string contains exactly one hyphen
        if string.count("-") != 1:
            return False
        
        # Split the string into two parts
        before_string, after_string = string.split("-")
        
        # Check if the word is repeated and not empty
        if before_string != after_string or not before_string:
            return False
    
    return True
#problem 3
import re
def most_occuring_first_letter(passage: str) -> str:
    '''
    Returns the letter which occurs most frequently 
    as the first letter of any word.(case insensitive)

    Args:
        passage (str): A multi-line string representing the passage.

    Returns:
        str: The most frequently occurring first letter in lowercase.
    '''
    ...
    
    set_list ={}
    passage = passage.strip()
    for first_letter in list(re.split(r'[ \n]+', passage)) :
        if first_letter[0].lower() in set_list :
            set_list[first_letter[0].lower()] = set_list[first_letter[0].lower()] +1  
        elif first_letter[0].lower() not in set_list:
            set_list[first_letter[0].lower()] = 1
    
    return(max(set_list, key = set_list.get))


#problems3
import re
def most_occuring_first_letter(passage: str) -> str:
    '''
    Returns the letter which occurs most frequently 
    as the first letter of any word.(case insensitive)

    Args:
        passage (str): A multi-line string representing the passage.

    Returns:
        str: The most frequently occurring first letter in lowercase.
    '''
    ...
    
    set_list ={}
    passage = passage.strip()
    for first_letter in list(re.split(r'[ \n]+', passage)) :
        if first_letter[0].lower() in set_list :
            set_list[first_letter[0].lower()] = set_list[first_letter[0].lower()] +1  
        elif first_letter[0].lower() not in set_list:
            set_list[first_letter[0].lower()] = 1
    
    return(max(set_list, key = set_list.get))

#problems4 
# Take the input from standard input using input()
# and print the output according to the problem .

# Write your code here

def run_length_encode(n: int, numbers: list):
    results = []
    
    for number in numbers:
        encoded = []
        current_digit = number[0]
        count = 1
        
        # Traverse each digit in the number
        for i in range(1, len(number)):
            if number[i] == current_digit:
                count += 1
            else:
                # Append the count and digit to the encoded list
                encoded.append(f"{count} {current_digit}")
                current_digit = number[i]
                count = 1
        
        # Append the final count and digit
        encoded.append(f"{count} {current_digit}")
        
        # Join the encoded pairs with spaces and add to results
        results.append(" ".join(encoded))
    
    return "\n".join(results)


# Parse the input data
number  = int(input())
input_data = ''
for i in range(number) :
    input_1 = input()
    input_data = input_data +input_1
    input_data += '\n'
lines = input_data.strip().split('\n')
n = int(lines[0].strip())
numbers = [line.strip() for line in lines[0:]]

# Output the run-length encoding
print(run_length_encode(n, numbers))


# OPPE 1 MAY 24 - Set 2

#problem 1 

from typing import List, Tuple, Set, Dict

def is_right_triangle_with_even_sides(a: int, b: int, c: int) -> bool:
    '''
    Given three side lengths in the increasing order of length as a, b, and c, where a<=b<=c,
    check if the given sides are the sides of a right triangle whose perpendicular sides are of even length.
    '''
    # Check if it's a right triangle
    if a**2 + b**2 == c**2:
        # Check if both perpendicular sides are even
        return a % 2 == 0 and b % 2 == 0
    return False

def is_odd_indices_alpha_and_even_indices_digits(string: str) -> bool:
    '''
    Given a string, check if all the odd indices are alphabets and the even indices are digits.
    '''
    for i, char in enumerate(string):
        if i % 2 == 0:  # Even index
            if not char.isdigit():
                return False
        else:  # Odd index
            if not char.isalpha():
                return False
    return True

def swap_even_and_odd_indices(l: List[int]) -> None:
    '''
    Given a list of integers, swap the values at the even indices and the odd indices by modifying the same list.
    '''
    for i in range(1, len(l), 2):
        # Swap the current odd index with the previous even index
        l[i - 1], l[i] = l[i], l[i - 1]

def unique_chars_present_in_first_not_in_second(s1: str, s2: str) -> Set[str]:
    '''
    Given two words as strings, find the unique chars that are present in the first word but not in the second word.
    '''
    return set(s1) - set(s2)

def repeat(t: Tuple[int, int]) -> Tuple[int, ...]:
    '''
    Given a tuple of length two, create a tuple with a repeated b number of times and b repeated a number of times.
    '''
    a, b = t
    return (a,) * b + (b,) * a

def num_squares(n: int) -> Dict[int, int]:
    '''
    Given an integer n, create a dictionary with the numbers from 1 to n (inclusive) as keys and their squares as values.
    '''
    return {i: i ** 2 for i in range(1, n + 1)}
#problems 2
def row_index_with_most_number_of_zeros(matrix: list) -> int:
    max_zeros = -1
    row_index = -1
    
    for i, row in enumerate(matrix):
        zero_count = row.count(0)  # Count the zeros in the current row
        if zero_count > max_zeros:  # Update if this row has more zeros
            max_zeros = zero_count
            row_index = i
            
    return row_index

#problems 3
from collections import defaultdict

def top_k_teams(batsmen: list, k: int) -> list:
    # Dictionary to store total runs for each team
    team_runs = defaultdict(int)
    
    # Aggregate runs for each team
    for batsman in batsmen:
        team = batsman['team']
        runs = batsman['runs']
        team_runs[team] += runs
    
    # Sort teams by total runs in descending order and get top k teams
    sorted_teams = sorted(team_runs, key=team_runs.get, reverse=True)
    
    # Return the top k teams
    return sorted_teams[:k]
#problems 4

def longest_antakshari_subsequence(words: list) -> int:
    max_length = 0
    current_length = 1
    
    # Traverse through the list of words to find the longest antakshari subsequence
    for i in range(1, len(words)):
        if words[i - 1][-1] == words[i][0]:  # Check if last letter matches the first letter of the next word
            current_length += 1
        else:
            # Update max_length if current sub-sequence is longer
            max_length = max(max_length, current_length)
            current_length = 1  # Reset length for a new sequence

    # Final check to update max_length in case the longest sequence ends at the last word
    max_length = max(max_length, current_length)
    
    return max_length

def process_input(n: int, sequences: list) -> list:
    results = []
    for line in sequences:
        words = line.split(',')
        results.append(longest_antakshari_subsequence(words))
    return results

# Input handling and execution
n = int(input())
sequences = []

for _ in range(n):
    sequence = input()
    sequences.append(sequence)

# Process each sequence and print results
results = process_input(n, sequences)
for result in results:
    print(result)
