def abs_diff_between_sum_and_sum_of_squares(a:int, b:int) -> int:
    '''
    Given two integers, find the absolute difference between 
    their sum and the sum of their squares.
    Eg. 
    a, b = 2,3 
    sum is 5
    sum of squares is 13 
    absolute difference is 8

    Args:
        a - int : The first integer.
        b - int : The second integer.

    Returns:
        int: absolute difference between the sum and the sum of squares
    '''

    # sum of 2 numbers
    sum_ab = a+b

    # sum of squares
    sum_sq = a**2+b**2

    # absolute value
    abs_diff = abs(sum_ab-sum_sq)

    # return
    return abs_diff

# practice done 

def swap_except_middle_three(s: str) -> str:
    '''
    Given an odd-length string, 
    swap the parts before and after the middle three characters,
    while keeping the middle three characters in place.

    Assume the string has at least 5 characters.

    Examples:
        "firstabclast1" -> "last1abcfirst"
        "abcdefghi" -> "ghidefabc"

    Args:
        s (str): The input string of odd length.

    Returns:
        str: The modified string with the parts swapped.
    '''

    # middle substring calc
    mid = len(s)//2 

    # get start and end index of the middle part of the string
    mid_start , mid_end = mid - 1 , mid+2

    # get new string
    new_string = s[mid_end:] + s[mid_start:mid_end] + s[: mid_start]

    # return
    return new_string

#practice done
def interleave_lists(list1, list2, list3):
    '''
    Given three lists of same length, 
    interleave them together and return the interleaved list.

    Example:
        list1 = [1, 2, 3]
        list2 = ['a', 'b', 'c']
        list3 = [(1,1),(2,2),(3,3)]
        output = [1, 'a', (1,1), 2, 'b', (2,2), 3, 'c', (3,3)]

    Args:
        list1 (list): The first list.
        list2 (list): The second list.
        list3 (list): The third list.

    Returns:
        list: A list containing interleaved elements from all three lists.
    '''
    
    # empty list
    interleaved_list = []

    # iterate over each of the list
    for i in range(len(list1)):
        # add one element form each list at the current index to interleaved list
        interleaved_list.extend([list1[i], list2[i], list3[i]])

    # return
    return interleaved_list

#practice done
def has_more_than_5_unique_digits(num: int) -> bool:
    '''
    Determine if a given integer has more than 5 unique digits.

    Args:
        num (int): The input integer.

    Returns:
        bool: True if the integer has more than 5 unique digits, otherwise False.
    '''
    
    # convert num to string
    num_to_str = str(abs(num))

    # set co0onversion
    unique_val = set(num_to_str) 

    # check for 5 or more uniques values / boolean check
    ans = len(unique_val)>5

    # return ans
    return ans

#practice done
def final_position(pos: tuple, vel: tuple, time:int) -> tuple:
    '''
    Given an initial position of a point moving in a cartesian plane with a constant velocity, 
    find the the final position of the point after a given time. 

    Hint: final position = initial position + velocity * time

    Args:
        pos - tuple[int]: A tuple representing the position vector (x1, y1).
        vel - tuple[int]: A tuple representing the velocity vector (vx, vy).
        time - int: time of movement.

    Returns:
        tuple[int]: A tuple representing the displacement (dx, dy).
    '''
    
    # get final x position
    final_x = pos[0] + vel[0] * time

    # get final_y
    final_y = pos[1] + vel[1] * time

    # return tuple
    return (final_x, final_y)

# practice Done 

def remove_keys_not_in_list(d: dict, l: list) -> None:
    '''
    Remove keys from a dictionary that are not present in a given list.
    The function modifies the dictionary in place and does not return anything.

    Note: 
        Modifying a dict while iterating over it will give an error in python. 
        So, make a copy of the dict keys and then iterate over it.d

    Args:
        d (dict): The dictionary to modify.
        l (list): The list of keys to keep in the dictionary.

    Returns:
        None
    '''
    key_list = list(d.keys())

    for k in key_list:
        if k not in l:
            del d[k]



# Problems 2 
# practice done
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

def most_occurring_first_letter(passage: str) -> str:
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
def most_occurring_first_letter(passage: str) -> str:
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
# Practice Done 
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
# practice done
def swap_even_and_odd_indices(l: List[int]) -> None:
    '''
    Given a list of integers, swap the values at the even indices and the odd indices by modifying the same list.
    '''
    for i in range(1, len(l), 2):
        # Swap the current odd index with the previous even index
        l[i - 1], l[i] = l[i], l[i - 1]
# Practice Done
def unique_chars_present_in_first_not_in_second(s1: str, s2: str) -> Set[str]:
    '''
    Given two words as strings, find the unique chars that are present in the first word but not in the second word.
    '''
    return set(s1) - set(s2)
# Practice Done
def repeat(t: Tuple[int, int]) -> Tuple[int, ...]:
    '''
    Given a tuple of length two, create a tuple with a repeated b number of times and b repeated a number of times.
    '''
    a, b = t
    return (a,) * b + (b,) * a

# practice Done
def num_squares(n: int) -> Dict[int, int]:
    '''
    Given an integer n, create a dictionary with the numbers from 1 to n (inclusive) as keys and their squares as values.
    '''
    return {i: i ** 2 for i in range(1, n + 1)}

# practice Done
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

#Practice done
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
