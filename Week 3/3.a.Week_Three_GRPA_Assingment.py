## GrPA 1 - While Loop - GRADED

# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "for " in content:
    print("You should not use for loop or the word for anywhere in this exercise")

# This is the first line of the exercise
task = input()
# <eoi>

if task == "sum_until_0":
    total = 0
    n = int(input())
    while (n!=0): # the terminal condition
        total += n # add n to the total
        n = int(input()) # take the next n form the input
    print(total)

elif task == "total_price":
    total_price = 0
    while True: # repeat forever since we are breaking inside
        line = input()
        if line == "END": # The terminal condition
            break
        quantity, price = line.split(" ") # split uses space by default
        quantity, price = int(quantity),int(price) # convert to ints
        total_price += quantity*price # accumulate the total price
    print(total_price)
elif task == "only_ed_or_ing":
    while True: # repeat forever since we are breaking inside
        string_input = input()
        if string_input == "STOP": # The terminal condition
            break
        elif string_input.endswith(("ing", "ed")):
            print(string_input)

elif task == "reverse_sum_palindrome":
    while True: # repeat forever since we are breaking inside
        number = int(input())
        if number == -1 : # The terminal condition
            break
        else:
            new_number  = number
            sum = 0
            while (new_number > 0) :
                remainder = new_number % 10 
                sum += remainder
                new_number  = new_number // 10
            if sum == int(str(sum)[::-1]) :
                print(number)


elif task == "double_string":
    while True: # repeat forever since we are breaking inside
        string_input = input()
        if string_input == "" : # The terminal condition
            break
        else :
            print(string_input+string_input)

elif task == "odd_char":
    while True: # repeat forever since we are breaking inside
        string_input = input()
        print(string_input[::2], end = " ")
        if string_input.endswith((".")): # The terminal condition
            break
elif task == "only_even_squares":
    while True: # repeat forever since we are breaking inside
            number_input = input()
            if number_input == "NAN" : # The terminal condition
                break
            elif (int(number_input) % 2 == 0 ) :
                squares_of_even = int(number_input) * int(number_input)
                print(squares_of_even)
            

elif task == "only_odd_lines":
    result = ""
    line_no = 1
    while True :
        line = input()
        if line == "END" :
            break
        if line_no % 2 :
            result = line + "\n" + result
        line_no +=1
    print(result)
    
## GrPA 2 - While Loop - GRADED    
    
# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.

with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "while " in content:
    print("You should not use while loop or the word while anywhere in this exercise")

# your code should not use more than 7 for loops 
# assuming one for loop per problem
if content.count("for ")>7:
    print("You should not use more than 7 for loops")

# This is the first line of the exercise
task = input()
# <eoi>

if task == 'factorial':
    n = int(input())
    result = 1
    for i in range(1,(n+1)):
        result *= i
    print(result)
elif task == 'even_numbers':
    n = int(input())
    for i in range(n+1) :
        if i % 2 == 0:
            print(i)

elif task == 'power_sequence':
    n = int(input())
    for i in range(n) :
        power_of_two = 2 ** i
        print(power_of_two)

elif task == 'sum_not_divisible':
    n = int(input())
    sum = 0
    for i in range(n) :
        if ((i % 4 != 0) and (i % 5 != 0))  :
            sum += i
    print(sum)

elif task == 'from_k':
    n = int(input()) 
    k = int(input())
    print_number = 1
    for i in range(k,0,-1) :
        if ( i % 2 != 0) and ( '9' not in str(i)) and ( '5' not in str(i)) : 
            if print_number <= n :
                print(str(i)[::-1])
                print_number +=1
            else :
                break

elif task == 'string_iter':
    n = input()
    prev = 1
    for i in n :
        num = int(i)
        print(num * prev)
        prev = num
        

elif task == 'list_iter':
    lst = eval(input()) # this will load the list from input
    for i in lst:
        print(f'{i} - type: {type(i)}')
else:
    print("Invalid")

## GrPA 3 - Nested loops - GRADED


task = input()


if task == 'permutation':
    value = input()
    for i in value :
        for j in value :
            if i == j :
                continue    
            else :
                print(i+j)
        
    
elif task == 'sorted_permutation':
    value = input()
    result_list = []
    for i in range(len(value)):
        for j in range(i + 1, len(value)):
            if value[i] < value[j]:
                print(value[i] + value[j])
            elif value[j] < value[i]:
                print(value[j] + value[i])

elif task == 'repeat_the_repeat':
    value = int(input())
    n = 1 
    while (n <= value) :
        for i in range (1,int(value)+1) :
            print(i, end = '')
        print() 
        n +=1
        
elif task == 'repeat_incrementally':
    value = int(input())
    n = 1 
    while (n <= value) :
        for i in range (1,n+1) :
            print(i, end ='')
        print()
        n +=1
        
elif task == 'increment_and_decrement':
    value = int(input())
    n = 1 
    
    while (n <= value) :
        k = 0
        for i in range (1,n+1) :
            print(i, end ='')
        for j in range (n,0,-1) :
            if k == 0 :
                pass
            else :
                print(j, end ='')
            k += 1    
        print()
        n +=1
        
## GrPA 4 - Loops Application - GRADED
# this is to ensure that you cannot use the built in any, all and min function for this exercise but you can use it in the OPPEs.
any = None 
all = None
min = None 

task = input()

if task == 'factors':
    value = int(input())
    for i in range(1,value+1) :
        if value % i == 0 :
            print(i)
            
elif task == 'find_min':
    
    number = int(input())
    min = int(input())
    for i in range(number-1) :
        current = int(input())
        if  current < min :
            min = current
    print(min)
    
elif task == 'prime_check':
    value = int(input())
    prime = "Flase"
    for i in range(2,value) :
        if value % i != 0 :
            prime = "True"
    print(prime)
    
elif task == 'is_sorted':
    value = input()
    is_sorted = "False"
    if ''.join(sorted(value)) == value:
        is_sorted = "True"
    print(is_sorted)

elif task == 'any_true':
    number = int(input())
    dev_sts = "False"
    for i in range(number) : 
        value = int(input())
        if  value % 3 == 0 :
            dev_sts = "True"
            break
    print(dev_sts)
    
elif task == 'manhattan':
    x,y = 0,0
    
    Value = True
    
    while True :
        
        Value = input()
        
        if Value == "STOP" :
            break
        elif Value == "UP" :
            y += 1
        elif Value == "DOWN" :
            y -= 1
        elif Value == "RIGHT" :
            x += 1
        elif Value == "LEFT" :
            x -= 1
            
    print(x+y)
        
        
        
else :
    print("Invalid task")
    
    
    
    
    
    
    
