
# WEEK06_GRPA01
# heterogeneous - multi line

# practice Done
def get_student_details():
    '''
    Get the student details over multiple lines

    Input format:

    name
    age
    rollno

    Return: name:str, age:int, rollno:int
    '''
    name, age, rollno = input(), int(input()), int(input())
    return name, age, rollno

# practice Done
# heterogeneous - single line 
def get_student_details_same_line():
    '''
    Get the student details from the same line

    Input format:(separated by space)

    name age rollno

    Return: name:str, age:int, rollno:int
    '''

    name, age, rollno = input().split()
    age, rollno = int(age), int(rollno)

    return name, age, rollno

# homogeneous - single line

# practice done
def get_comma_separated_integers():
    '''
    Get a list of comma separated integers from input

    Return: numbers:list[int]
    '''

    numbers = list(map(int, input().split(",")))
    # another approach using comprehensions
    # numbers = [int(num) for num in input().split(",")]

    return numbers

# homogeneous - multi-line - definite

# practice done
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
    nums = [float(input()) for i in range(n)]

    return nums

# homogeneous - multi-line - indefinite
# practice done
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
        if num.lower() == "end":
            break
        nums.append(float(num))

    return nums

# hybrid - single line
# practice done
def get_batsman_runs():
    '''
    Get batsman name, number and runs as a list

    Input format: (separated by space)
    name no run1 run2 run3 ...

    Return: name:str, no:int, runs:list[int]
    '''

    name, no, *runs = input().split()
    no = int(no)
    runs = list(map(int, runs))

    return name, no, runs

# key value
#  practice done
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
    course_scores = [input().split('-') for i in range(n)] # split each line using '-'
    # create the dictionary using comprehensions
    course_scores = {course:int(score) for course, score in course_scores}

    return course_scores

# dict with list as values
# practice done
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
    batsman_runs = [input().split('-') for i in range(n)] # split name and runs using '-'
    batsman_runs = {
        name:list(map(int, runs.split(',')))  # split runs by ',' and map to int
        for name, runs in batsman_runs
    }

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
    for i in range(n):
        rollno, city, age, course1, course2, course3 = input().split(',')
        rollno,age, course1, course2, course3 = map(int, [rollno,age, course1, course2, course3])
        student_data.append({
            "rollno":rollno,
            "city":city,
            "age":age,
            "course1":course1,
            "course2":course2,
            "course3":course3,
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

    student_data = [
        {
            "rollno":int(input()), "city":input(), "age":int(input()),
            "course1":int(input()),"course2":int(input()),"course3":int(input()),
        }
        for i in range(int(input()))
    ]

    return student_data

# WEEK06_GRPA02
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

    print(name,age,rollno,sep=",")

# homogeneous - single line
def display_comma_separated_integers(nums:list):
    '''
    Given a list of nums print them in the same line 
    separated by commas.

    For example, if  nums= [1,3,4,5],
    Output format:
    1,3,4,5
    '''

    print(*nums, sep=",")

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

    print(*[f"{num:.3f}" for num in nums], sep="\n")

# homogeneous - indefinite
def display_random_ints(seed:int):
    '''
    Given a random seed, set the random seed and 
    generate multiple random integers within the range [0,100] 
    (using `randint(0,100)`), until 0 is encountered and 
    print it with max 10 comma seperated ints per line over multiple lines

    Output format
    34,26,73,82,35,36,7,4,27,46
    6,33,62,78,0
    '''

    random.seed(seed)

    i = 0
    while True:
        i+=1
        num = random.randint(0,100)
        if num ==0:
            print(num)
            break
        if i%10==0:
            print(num)
            continue
        print(num,end=',')

# hybrid - single line
def display_batsman_runs(name:str, number:int, runs:list):
    '''
    Given name, number and runs scored by a batsman
    display the name, number and runs separated by commas in the same line.

    For example, if name="player1", number=9 and runs=[2,3,4,4,6]

    Output Format;
    player1,9,2,3,4,4,6
    '''

    print(name, number, *runs, sep=",")

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

    for course, score in sorted(course_scores.items()):
        print(f"{course}:{score}")
    # alternate solution
    # print(*(f"{course}:{score}" for course, score in sorted(course_scores.items())),sep="\n")

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

    for batsman, runs in batsman_runs:
        print(batsman, end="-")
        print(*runs,sep=",")
    # alternate way
    '''
    for batsman, runs in batsman_runs:
        print(f"{batsman}-{','.join(map(str,runs))}")
    '''

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

    attrs = ['rollno','city','age','course1','course2','course3']
    for student in student_marks:
        print(*(student[attr] for attr in attrs), sep=",")

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

    attrs = ['rollno','city','age','course1','course2','course3']
    for student in student_marks:
        print(*(student[attr] for attr in attrs), sep="\n")

#WEEK06_GRPA03
def is_num_sorted(num)->bool:
    '''
    Check if a number is sorted.
    sorted means the digits of a number are sorted in ascending order.
    Eg. 1468 - sorted , 4948 - not sorted.

    Argument: num: int
    Return: bool
    '''

    num_str = str(num)
    num_str_sorted = "".join(sorted(list(num_str)))
    return num_str == num_str_sorted

def sorted_num_count(nums:list) -> int:
    '''
    Given a list of nums(int) find the count of sorted numbers in the list.

    Arguments: nums - list[int]
    Return: count - int
    '''

    return len(list(filter(is_num_sorted, nums)))
    # another approach - can also use comprehensions
    # return sum(map(well_behaved, nums)) # sum of boolean will be the count

def common_substring(words:list)->str:
    '''
    Given a list of words check whether there is a word in words 
    that is a substring of all other words.
    If there is a word return that word else return None

    Hint: only the smallest word can be a substring of all other words.

    Arguments: words - list[str]
    Return: common_substr_word - str
    '''

    min_word = min(words, key = len)
    # check if min_word in word for all word in words
    if all(map(lambda word : min_word in word, words)):
        return min_word
    # another approach using comprehensions
    # if all(min_word in word for word in words):
    #     return min_word

def is_valid_phone_number(phone_no:int)->bool:
    '''
    Check if a number is valid for a specific operator.

    A phone number is valid if 
        - it has 10 digits
        - should begin with 98123
        - same digit should not occur more that 5 times.
    '''

    phone_no_str = str(phone_no)
    # note that the below return statement is a single experssion
    return (
        len(phone_no_str) == 10 # has 10 digits
        and phone_no_str[:5] == "98123" # begins with 98123
        and all(phone_no_str.count(str(digit))<=5 for digit in range(0,10)) # check if all the numbers are present less than 5 times
    )

def validate_phone_numbers(phone_nos:list)->dict:
    '''
    Given a list of phone numbers, create a dict with 
    phone numbers as keys and the string "VALID" or "INVALID"
    depending on the validity of the phone number as described by the above funtion.

    Arguments: phone_nos - list
    Return: validity_dict - dict[int,str]
    '''

    return {
        number: "VALID" if is_valid_phone_number(number) else "INVALID"
        for number in phone_nos
    }

def get_election_winner(votes:dict)->str:
    '''
    Given a dictionary with candidate name as key and number of votes as values,
    Find the winner of the election who has the maximum votes

    Arguments: votes - dict[str, int]
    Return: winner - str
    '''

    return max(votes, key = votes.get)

def misspelt_words(vocab:str, sentence:str)->list:
    '''
    Given a comma separated string of vocabulary, 
    and a space separated string sentence,
    return a list of misspelt words in the order they occur in the sentence.

    The words which are not in the vocabulary are considered misspelt.

    Arguments: 
        vocab - str: comma separated string with vocabulary
        sentence - str: space separated string of sentence
    Return:
        misspelt_words - list
    '''

    vocab, words = set(vocab.split(",")), sentence.split()
    return [word for word in words if word not in vocab]

    # another approach
    # return list(filter(lambda x: word not in vocab, words))

def count_sock_pairs(sock_colors:list)->int:
    '''
    Given a list of sock colors representing the color of each sock, 
    find the number of sock pair (both having same color) is there.
    Eg. ["red","blue","green","green","red","green","red","red","blue","black"] 
    2 red+ 1 green+ 1 blue = 5 pairs

    Arguments: sock_colors - list: of sock colors
    Return: number of pairs of sock - int
    '''

    sock_counts = {}
    # count socks of each color
    for color in sock_colors:
        if color not in sock_counts:
            sock_counts[color] = 0
        sock_counts[color] += 1
    # use floor division to find the number of sock pairs
    return sum(count//2 for count in sock_counts.values())

def is_vowely(word:str)->bool:
    '''
    Check if a given word is vowely. A word is vowely if 
    - it has all the vowels in it.
    - the vowels occur in ascending order.

    Assume no letter repeats in the given word.

    Eg. abecidofu - vowely, tripe - not vowely, eviaoqu - not vowely

    Argument: word - a string with no letter repeated
    Return: bool 

    Hint: if the non-vowels are removed from the word, it would be just aeiou
    '''

    return "".join(char for char in word if char in "aeiou" ) == "aeiou"
    # alternate approach using filter
    # return "".join(filter(lambda char: char in "aeiou", word)) == "aeiou"

def vowely_count(words:list)->int:
    '''
    Given a list of words find the number of vowely words from the list.    

    Arguments: words :list[str]

    Return: int - number of vowely words
    '''

    return len(list(filter(is_vowely, words)))

def format_name(first:str, middle:str, last:str)->str:
    '''
    Given three lower case parts of name, 
    return the full name with first letter capitalized in each part.

    Note that middle name can be empty.
    '''

    first, middle, last = map(str.title, (first, middle, last))
    return f"{first} {middle} {last}" if middle else f"{first} {last}"

def double_palindromes(n:int)->list:
    '''
    Given a number n, find all the positive integers till n (including)
    that are double_palindrome. A number is double palindrome if 
    it is a palindrome and its square is a palindrome.

    Eg. 
    8 - palindrome, not double palindrome
    11 - palindrome and double palindrome
    12 - not palindrome and not double palindrome

    Arguments: n - int: range of numbers to search
    Return: list of integers which are double palindrome in the ascending order
    '''

    def is_palindrome(n):
        n_str = str(n)
        return n_str==n_str[::-1]
    return list(filter(lambda x: is_palindrome(x) and is_palindrome(x**2), range(1,n+1)))
    # alternate approach using comprehensions
    '''
    return [
        num for num in range(1,n+1)
        if is_palindrome(x) and is_palindrome(x**2)
    ]
    '''

def scores_spx(kakashi_moves:list, guy_moves:list):
    '''
    Given the series of moves played by Kakashi and Guy in a Stone-Paper-Scissor game,
    find the scores of Kakashi and guy respectively.
    Rules - Stone beats Scissor, Scissor beats Paper and Paper beats Stone
    Score - Number of times won
    Symbols - Stone - S, Paper - P, Scissor - X

    Arguments: 
    kakashi_moves and guy_moves - list of moves where each move 
        is a string corresponding to the symbol

    Return: kakashi_score:int , guy_score:int
    '''

    wins = [('S','X'), ('X','P'),('P','S')]

    k_score, g_score = 0,0
    for k, g in zip(kakashi_moves, guy_moves):
        if (k,g) in wins:
            k_score+=1
        elif (g,k) in wins:
            g_score+=1

    return k_score, g_score
