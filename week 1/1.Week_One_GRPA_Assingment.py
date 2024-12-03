## WEEK01_GRPA01 - GRADED
# Sample inputs (# note: The values given in the prefix code(grey) will be changed by the autograder according to the testcase while running them.
a = 5
b = 6
price, discount_percent = 80, 5.75
total_mins = 470
# <eoi>

output1 = (a+b) # int: sum of a and b
output2 = (output1 * 2) # int: twice the sum of a and b
output3 = abs(a-b) # int: absolute difference between a and b
output4 =  abs(output1 - (a*b)) # int: absolute difference between sum and product of a and b

# Find discounted price given price and discount_percent
# input variables : price: int, discount_percent: float
discounted_price = (price - (price * (discount_percent/100))) # float

# Round the discounted_price
rounded_discounted_price = int(discounted_price) # int

# Find hrs and mins given the total_mins
# input variables : total_mins
hrs = total_mins // 60 # int: hint: think about floor division operator
mins = int(((total_mins / 60) - hrs)* 60)  # int


## WEEK01_GRPA02 - GRADED
# Sample inputs (# note: The values given in the prefix code(grey) will be changed by the autograder according to the testcase while running them.
a = 5

price1, discount1 = 50, 4 # for offer1
price2, discount2 = 60, 8 # for offer2

# Assume discount is given in percentages

# <eoi>

output1 = a >= 5 # bool: True if a greater than or equal to 5

output2 = a % 5 == 0  # bool: True if a is divisible by 5

output3 = ((a % 2 !=0) and a < 10) # bool: True if a is odd number less than 10

output4 = ((a % 2 !=0) and (-10 <= a <= 10)) # bool: True if a is an odd number within the range -10 and 10

output5 = (a % 2 == 0) and ((len(str(a)) <= 10)) # bool: True if a has even number of digits but not more than 10 digits

is_offer1_cheaper = (price1 * (1- discount1/100)) < (price2 * (1- discount2/100))  # bool: True if the offer1 is strictly cheaper

## WEEK01_GRPA03 - GRADED
# Sample inputs (# note: The values given in the prefix code(grey) will be changed by the autograder according to the testcase while running them.

s = "hello pyhton"
course_code = "24t2cs1002" # 24 - year, t2 - term 2, cs1002 - course id
# <eoi>

output1 = s[2] # str: get the third character of s

output2 = s[-4] # str: get the fourth last character of s

output3 = s[:3] # str: get the first 3 characters of s

output4 = s[::2] # str: get every second character of s

output5 = s[-3:] # str: get the last 3 characters of s

output6 = s[::-1] # str: get the reverse of s

course_term = int(course_code[3]) # int: get the term of the year as number from course_code
course_year = int(course_code[:2]) # int: get the year as two digit number from course_code


## WEEK01_GRPA04 - GRADED

# Sample inputs (# note: The values given in the prefix code(grey) will be changed by the autograder according to the testcase while running them.
word1 = "Wingardium" # str
word2 = "Leviyosa" # str
word3 = "Silver" # str
sentence = "Learning python is fun"
n1 = 6 # int
n2 = 4 # int
# <eoi>

output1 = word1 + " "+word2 # str: join word1 and word2 with space in between

output2 = word1[:4] + "-"+word2[-4:] # str: join first four letters of word1 and last four letters of word 2 with a hyphen "-" in between

output3 = word3+" "+str(n1) # str: join the word3 and n1 with a space in between

output4 = "-"*50 # str: just the hypen "-" repeated 50 times

output5 = "-"*n2 # str: just the hypen "-" repeated n2 times

output6 = str(n1)*n2 # str: repeat the number n1, n2 times

are_all_words_equal = word1 == word2 == word3 # bool: True if all three words are equal

is_word1_comes_before_other_two = (word2>word1)and(word3>word1) # bool: True if word1 comes before word2 and word3 assume all words are different

has_h = "h" in word1 # bool: True if word1 has the letter h

ends_with_a = ("a" == word1[-1]) or ("A" == word1[-1]) # bool: True if word1 ends with letter a or A

has_the_word_python = "python" in sentence # bool: True if the sentence has the word python


## WEEK01_GRPA05 - GRADED
age = int(input()) # int: Read a number as integer from standard input
dob = str(input()) # str: Read a string of format dd/mm/yy from standard input
day, month, year = int(dob[:2]),int(dob[3:5]),int(dob[6:]) # int, int, int: Get the correct parts from dob as int

fifth_birthday = str(day)+"/"+str(month)+"/"+str(year+5) # str: fifth birthday formatted as day/month/year 

last_birthday = str(day)+"/"+str(month)+"/"+str(year+age) # str: last birthday formatted as day/month/year

if ((month+10)>12) :
    year += 1
    ten_month = 10 - (12 - month)
else :
    ten_month = month + 10

tenth_month = str(day)+"/"+str(ten_month)+"/"+str(year) # str: dob same day after 10 months formatted as day/month/year

# print tenth_month, fifth_birthday and last_birthday in same line separated by comma and a space
print(", ".join([tenth_month,fifth_birthday,last_birthday]))

weight = float(input()) # float: Read a number as float from stdin(Standard input)

weight_readable = str(int(weight))+" kg "+ str(int((weight - int(weight))*1000))+ " grams " # str: reformat weight of format 55 kg 250 grams

# print weight_readable 
print(weight_readable)

