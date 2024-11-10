#GRPA 1

# heterogeneous - multi line
def get_student_details():
    '''
    Get the student details over multiple lines

    Input format:

    name
    age
    rollno

    Return: name:str, age:int, rollno:int
    '''
    name = input()
    age = int(input())
    rollno = int(input())
    return name, age, rollno

# heterogeneous - single line
def get_student_details_same_line():
    '''
    Get the student details from the same line

    Input format:(separated by space)

    name age rollno

    Return: name:str, age:int, rollno:int
    '''
    name, age, rollno = input().split()
    return name, int(age), int(rollno)

# homogeneous - single line
def get_comma_separated_integers():
    '''
    Get a list of comma separated integers from input

    Return: numbers:list[int]
    '''
    numbers = [int(x) for x in input().split(',')]
    return numbers

# homogeneous - multi-line - definite
def get_n_float_numbers():
    '''
    Get n float numbers with one number in each line
    and the first line has n.

    Input Format:
    n
    num1
    num2
    ...
    numn

    Return: nums:list[float]
    '''
    n = int(input())
    nums = [float(input()) for _ in range(n)]
    return nums

# homogeneous - multi-line - indefinite
def get_nums_until_end():
    '''
    Get float numbers with one number in each line
    until the input is "end"(case insensitive)

    Input Format:
    num1
    num2
    ...
    numx
    End

    Return: nums:list[float]
    '''
    nums = []
    while True:
        num = input()
        if num.lower() == 'end':
            break
        nums.append(float(num))
    return nums

# hybrid - single line
def get_batsman_runs():
    '''
    Get batsman name, number and runs as a list

    Input format: (separated by space)
    name no run1 run2 run3 ...

    Return: name:str, no:int, runs:list[int]
    '''
    inputs = input().split()
    name = inputs[0]
    no = int(inputs[1])
    runs = [int(x) for x in inputs[2:]]
    return name, no, runs

# key value
def get_course_scores():
    '''
    Get course name and scores of the over multiple lines where
    course name and scores are separated by a hypen in each line.
    First line corresponds to the number or entries.

    Input format:
    2
    course1-score1
    course2-score2

    Return: dict[str,int] - with course name as key and score as value
    '''
    n = int(input())
    course_scores = {}
    for _ in range(n):
        course, score = input().split('-')
        course_scores[course] = int(score)
    return course_scores

# dict with list as values
def get_all_batsman_runs():
    '''
    Given the batsman name and the comma separated runs
    where both are seperted by a hypen in multiple lines,
    create a dictionary with batsman name and list of runs as value.
    The number of lines is given in the first line

    Input format:
    3
    batsman1-1,2,1,4,6,2,2,1
    batsman2-2,2,6,4,1
    batsman3-6,1,2,4,4,2

    Return: dict[str,list[int]] - with batsman name as key and list of runs as values
    '''
    n = int(input())
    batsman_runs = {}
    for _ in range(n):
        batsman, runs = input().split('-')
        batsman_runs[batsman] = [int(x) for x in runs.split(',')]
    return batsman_runs

# csv - list of dicts
def get_student_marks():
    '''
    Given the student rollno, city, age,
    course1_marks, course2_marks and course3_marks
    as comma separated values over multiple lines,
    create a list of dict with the above attributes as keys
    and the corresponding value as values.
    The number of lines is given in the first line

    Input Format:
    n
    1,citya,23,86,69,86
    2,cityb,19,78,65,89
    ...
    n,cityx,35,89,57,76

    Return:
    student_data - list[dict]: where each dict would be

    {'rollno':int, 'city':str,'age':int,
    'course1':int, 'course2':int, 'course3':int}
    '''
    n = int(input())
    student_data = []
    for _ in range(n):
        rollno, city, age, c1, c2, c3 = input().split(',')
        student_data.append({
            'rollno': int(rollno),
            'city': city,
            'age': int(age),
            'course1': int(c1),
            'course2': int(c2),
            'course3': int(c3)
        })
    return student_data

# list of dicts
def get_student_data_over_multiple_lines():
    '''
    Given each attribute as described above in given over multiple lines
    and multiple entries are given create a dictionary as described above.

    Input format:
    n
    1
    citya
    23
    86
    69
    86
    2
    cityb
    19
    78
    65
    89
    ...
    n
    cityx
    35
    89
    57
    76
    '''
    n = int(input())
    student_data = []
    for _ in range(n):
        rollno = int(input())
        city = input()
        age = int(input())
        course1 = int(input())
        course2 = int(input())
        course3 = int(input())
        student_data.append({
            'rollno': rollno,
            'city': city,
            'age': age,
            'course1': course1,
            'course2': course2,
            'course3': course3
        })
    return student_data

# this will read the function name from the input.
func = eval(input())

# this will read the actual output that is required which is the second line
expected_output = eval(input())

# The remaining of the input should be read by your function
actual_output = func()

if expected_output != actual_output:
    print("Your output doesn't match the expected output.")
print(actual_output)


# this will read the function name from the input.
func = eval(input()) 

# this will read the actual output that is required which is the second line
expected_output = eval(input())

# The remaining of the input should be read by your function
actual_output = func()

if expected_output != actual_output:
    print("Your output doesn't match the expected output.")
print(actual_output)
#GRPA 2

import random


# heterogenous values in multiple lines
def display_student_details(name:str, age:int, rollno:int):
    '''
    Given name, age, and rollno of student,
    print them over multiple lines

    Output format:
    name
    age
    rollno

    Return: None
    '''
    print(name)
    print(age)
    print(rollno)

# heterogeneous values - single line
def display_student_details_same_line(name:str, age:int, rollno:int):
    '''
    Given name, age, and rollno of student,
    print them in the same line separated by a comma.

    Output format:
    name,age,rollno
    '''
    print(f"{name},{age},{rollno}")

# homogeneous - single line
def display_comma_separated_integers(nums:list):
    '''
    Given a list of nums print them in the same line
    separated by commas.

    For example, if  nums= [1,3,4,5],
    Output format:
    1,3,4,5
    '''
    print(','.join(str(num) for num in nums))

# homogeneous - multi-line - definite
def display_float_nums_over_multiple_lines(nums:list):
    '''
    Given a list of floating point nums print them
    over multiple lines with 3 digits after the decimal point.
    For example, if nums = [1.2, 3.4,5.6,7.8]

    Output format:
    1.200
    3.400
    5.600
    7.800
    '''
    for num in nums:
        print(f"{num:.3f}")

# homogeneous - indefinite
def display_random_ints(seed: int):
    '''
    Given a random seed, set the random seed and
    generate multiple random integers within the range [0,100]
    (using `randint(0,100)`), until 0 is encountered and
    print it with max 10 comma-separated ints per line over multiple lines

    Output format
    34,26,73,82,35,36,7,4,27,46
    6,33,62,78,0
    '''
    random.seed(seed)
    nums = []
    while True:
        num = random.randint(0, 100)
        nums.append(str(num))
        if len(nums) == 10:
            print(','.join(nums))
            nums = []
        if num == 0:
            break
    if nums:
        print(','.join(nums))
       
# hybrid - single line
def display_batsman_runs(name:str, number:int, runs:list):
    '''
    Given name, number and runs scored by a batsman
    display the name, number and runs separated by commas in the same line.

    For example, if name="player1", number=9 and runs=[2,3,4,4,6]

    Output Format;
    player1,9,2,3,4,4,6
    '''
    print(f"{name},{number},{','.join(str(run) for run in runs)}")

# key value
def display_course_scores(course_scores:dict):
    '''
    Given a dictionary of course scores with
    course name as keys and course scores as values.
    Format each course score pair separated by colon(':')
    on each line where each pair is printed over multiple lines
    in the ascending order of keys.

    For example, if course_scores = {"course1":78, "course3":89,"course2":90}

    Output format:
    course1:78
    course2:90
    course3:89
    '''
    for course in sorted(course_scores):
        print(f"{course}:{course_scores[course]}")

def display_all_batsman_runs(batsman_runs:list):
    '''
    Given a list of tuple of batsman runs,
    print the batsman name and comma separated runs
    which are separated by a hyphen and printed over multiple lines.

    Arguments: batsman_runs: list[tuple(str, list[int])]

    For example, if batsman_runs = [
        ("batsman1",[1,2,1,4,6,2,2,1]),
        ("batsman2",[2,2,6,4,1]),
        ("batsman3",[6,1,2,4,4,2])
    ]

    Output format:
    batsman1-1,2,1,4,6,2,2,1
    batsman2-2,2,6,4,1
    batsman3-6,1,2,4,4,2
    '''
    for name, runs in batsman_runs:
        print(f"{name}-{','.join(str(run) for run in runs)}")

def display_student_marks(student_marks:list):
    '''
    Given the student rollno, city, age and marks of
    course1, course2 and course3 as a list of dicts,
    print the attributes of each student in a single
    line as comma separated values (in the previously mentioned order)
    and print the whole list over multiple lines.

    Arguments: student_marks: list[dict] where the keys of the dict are 'rollno':int,'city':str, 'age':int, 'course1':int, 'course2':int,'course2':int

    For example, if student_marks = [
        {'rollno': 1, 'city': 'chennai', 'age': 23, 'course1': 86, 'course2': 69, 'course3': 86},
        {'rollno': 2, 'city': 'mumbai', 'age': 19, 'course1': 78, 'course2': 65, 'course3': 89}
    ]

    Output:
    1,chennai,23,86,69,86
    2,mumbai,19,78,65,89
    '''
    for student in student_marks:
        print(f"{student['rollno']},{student['city']},{student['age']},{student['course1']},{student['course2']},{student['course3']}")

def display_student_marks_over_multiple_lines(student_marks:list):
    '''
    Same input as the above function, but print each attribute
    over mulitple line in the same order of attributes as the previous one.

    For the example given in the above input,

    Output:
    1
    chennai
    23
    86
    69
    86
    2
    mumbai
    19
    78
    65
    89
    '''
    for student in student_marks:
        print(student['rollno'])
        print(student['city'])
        print(student['age'])
        print(student['course1'])
        print(student['course2'])
        print(student['course3'])
     

# this basically reads the input and executes it as code
import sys
exec(sys.stdin.read())
#GRPA 3

# Function to check if a number is sorted
def is_num_sorted(num: int) -> bool:
    digits = list(str(num))
    return digits == sorted(digits)

# Function to count sorted numbers in a list
def sorted_num_count(nums: list) -> int:
    return len([num for num in nums if is_num_sorted(num)])

# Function to find common substring in a list of words
def common_substring(words: list) -> str:
    words_sorted = sorted(words, key=len)
    smallest_word = words_sorted[0]
    for word in words_sorted[1:]:
        if smallest_word not in word:
            return None
    return smallest_word

# Function to check if a phone number is valid
def is_valid_phone_number(phone_no: int) -> bool:
    phone_str = str(phone_no)
    if len(phone_str) != 10 or not phone_str.startswith("98123"):
        return False
    return max(phone_str.count(digit) for digit in phone_str) <= 5

# Function to validate a list of phone numbers
def validate_phone_numbers(phone_nos: list) -> dict:
    return {phone_no: "VALID" if is_valid_phone_number(phone_no) else "INVALID" for phone_no in phone_nos}

# Function to find the election winner
def get_election_winner(votes: dict) -> str:
    return max(votes, key=votes.get)

# Function to find misspelt words
def misspelt_words(vocab: str, sentence: str) -> list:
    vocab_set = set(vocab.split(","))
    return [word for word in sentence.split() if word not in vocab_set]

# Function to count sock pairs
def count_sock_pairs(sock_colors: list) -> int:
    from collections import Counter
    counts = Counter(sock_colors)
    return sum(count // 2 for count in counts.values())

# Function to check if a word is vowely
def is_vowely(word: str) -> bool:
    vowels = "aeiou"
    filtered = ''.join([ch for ch in word if ch in vowels])
    return filtered == vowels

# Function to count vowely words in a list
def vowely_count(words: list) -> int:
    return len([word for word in words if is_vowely(word)])

# Function to format name
def format_name(first: str, middle: str, last: str) -> str:
    return ' '.join([name.capitalize() for name in [first, middle, last] if name])

# Function to find double palindromes
def double_palindromes(n: int) -> list:
    def is_palindrome(num: int) -> bool:
        return str(num) == str(num)[::-1]
   
    return [i for i in range(1, n+1) if is_palindrome(i) and is_palindrome(i*i)]

# Function to calculate scores in a Stone-Paper-Scissor game
def scores_spx(kakashi_moves: list, guy_moves: list):
    beats = {'S': 'X', 'P': 'S', 'X': 'P'}
    k_score, g_score = 0, 0
    for k_move, g_move in zip(kakashi_moves, guy_moves):
        if beats[k_move] == g_move:
            k_score += 1
        elif beats[g_move] == k_move:
            g_score += 1
    return k_score, g_score
