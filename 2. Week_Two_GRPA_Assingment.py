## GrPA 1 - Variables and Assignment - GRADED
x1 = input()
x2 = input()
y1 = input()
y2 = input()
y3 = input()
z = input()

# swap the values of `x1` and `x2`

x1,x2 = x2, x1 

# do a circular swap of `y1`, `y2` and `y3`  like y1 = y2, y2 = y3, y3 = y1 

y1, y2, y3 = y2, y3, y1

# create a new variable `a` with the value of `z`
a = z
# delete the variable `z`
del z  

print(x1)
print(x2)
print(y1)
print(y2)
print(y3)
print(a)


## GrPA 2 - String Escaping - GRADED
# A single quote ' and a double quote "
output1  = ("A single quote ' and a double quote \"") 


# A forward slash / and a backward slash \
output2 = ("A forward slash / and a backward slash \\")

# Three single quotes ''' and three double quotes """
output3 = ("Three single quotes ''' and three double quotes \"\"\" ")

# Double forward slash // and Double backward slash \\
output4 = ("Double forward slash // and Double backward slash \\\\")


## GrPA 3 - Basic conditional patterns - GRADED
# part 1 - If pattern
word = "glow" # str
continuous_tense = True # bool

# part 2
age = 5 # int
is_member = True # bool

# part 3

color_code = "R" # str: valid values are R-red, G-green and B-blue

time = "02 PM" # str, format:[2-digit hour][space][AM or PM]
# Morning (6 AM - 12 PM) (including the start and excluding the end)
# Afternoon (12 PM - 6 PM) 
# Evening (6 PM - 12 AM)
# Night (12 AM - 6 AM)

# <eoi>

# part 1 - basic if

new_word = word # donot remove this line

# remove the "ing" suffix from `new_word` if it is there
if new_word.endswith("ing") :
    new_word = (new_word[0:-3])
    



# add the suffix "ing" to `new_word` if `continuous_tense` is True
# write the whole if else block here
if continuous_tense:
    new_word += "ing"

# part 2 - If else pattern

# age_group:str should be "Adult" or "Child" based on the age. assume age greater than or equal to 18 is adult.
if (age >= 18) :
    age_group = "Adult"
    
else:
    age_group = "Child"

# applicant_type:str should be age goup with the member status like "Adult Member" or "Child Non-member"
# write the whole if else block
if is_member :
    applicant_type = f"{age_group} Member"
    
else:
    applicant_type = f"{age_group} Non-member"


# part 3 if ... elif .. else

# based on the value of `color_code` assign the `color` value in lower case and "black" if `color_code` is none of R, B and G

if (color_code == "R") :
    color = "red"
elif (color_code == "B") :
    color = "blue"
     
elif (color_code == "G") :
    color = "green"
    
else:
    color = "black"

# bool: True if time is valid (should be ranging from 1 - 12 both including) else False
try:
    hour = int(time[:2])
    period = time[-2:].upper()
    is_time_valid = 1 <= hour <= 12 and period in ["AM", "PM"]
except (ValueError, IndexError):
    is_time_valid = False  
# time_in_hrs:int should have the time in 24 hrs format . Try to do this in a single expression
time_in_hrs = hour + (12 if "PM" in time and hour != 12 else 0) - (12 if "AM" in time and hour == 12 else 0)


# time_of_day:str should have the time of the day as Morning, etc.. use "Invalid" if not withing the acceptable range

# write your code here
if 6 <= time_in_hrs < 12:
    time_of_day = "Morning"
elif 12 <= time_in_hrs < 18:
    time_of_day = "Afternoon"
elif 18 <= time_in_hrs < 24:
    time_of_day = "Evening"
elif 0 <= time_in_hrs < 6:
    time_of_day = "Night"
else:
    time_of_day = "Invalid"

## GrPA 4 - Conditionals - Applications - GRADED
import math

    
def odd_num_check(number):
    if number % 2 != 0:
        print("yes")
    else:
        print("no")

def perfect_square_check(number):
    sqrt_num = number ** 0.5
    integer_part, decimal_part = str(sqrt_num).split('.')
    if (int(decimal_part) == 0):
        print("yes")
    else:
        print("no")

def vowel_check(text):
    vowels = "aeiouAEIOU"
    if any(v in text for v in vowels):
        print("yes")
    else:
        print("no")

def divisibility_check(number):
    if number % 2 == 0 and number % 3 == 0:
        print("divisible by 2 and 3")
    elif number % 2 == 0:
        print("divisible by 2")
    elif number % 3 == 0:
        print("divisible by 3")
    else:
        print("not divisible by 2 and 3")

def palindrominator(text):
    print(text + text[::-1][1:])

def simple_interest(principal_amount, n_years):
    if n_years < 10:
        interest_rate = 0.05
    else:
        interest_rate = 0.08
    interest = principal_amount * interest_rate * n_years
    print(round(interest))

# Main Program
operation = input()

if operation == "odd_num_check":
    number = int(input())
    odd_num_check(number)
elif operation == "perfect_square_check":
    number = int(input())
    perfect_square_check(number)
elif operation == "vowel_check":
    text = input()
    vowel_check(text)
elif operation == "divisibility_check":
    number = int(input())
    divisibility_check(number)
elif operation == "palindrominator":
    text = input()
    palindrominator(text)
elif operation == "simple_interest":
    principal_amount = int(input())
    n_years = int(input())
    simple_interest(principal_amount, n_years)
else:
    print("Invalid Operation")

## GrPA 5 - Conditionals - Debugging - GRADED
main_dish = input()
time_of_day = int(input())
has_voucher =   input()
is_card_payment = input()
cost = 0
total_cost = 0

if main_dish == "paneer tikka":
    cost = 250
elif main_dish == "butter chicken":
    cost = 240
elif main_dish == "masala dosa":
    cost = 200
else: # if main dish is invalid print invalid dish and exit the code.
    print("Invalid main dish")
    exit()

if ((time_of_day >= 12) and (time_of_day <= 15)):
    total_cost = (1 - 0.15) * cost

else:
    total_cost = cost

if has_voucher == "True":
    total_cost *= 0.9  # Apply voucher discount

if is_card_payment == "True":  # service charge for card payments
    service_charge = 0.05 * total_cost
    total_cost += service_charge

print(f"{total_cost :.2f}")
