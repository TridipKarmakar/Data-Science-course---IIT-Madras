# GrPA 1 - Dictionary Basics - GRADED
# Practice Done
def dictionary_operations(fruit_prices:dict, fruits:list):
    # add the fruit fruits[0] to fruit_prices with cost 3
    fruit_prices[fruits[0]] = 3
    print(f'1. list of fruits price after adding 3 in 0th index {fruit_prices}') 

    # modify the cost of fruits[1] as 2 in fruit_prices
    fruit_prices[fruits[1]] = 2
    print(f'2. list of fruits price after update 2 in 1th index {fruit_prices}')

    # increase the cost of fruits[2] by 2 in fruit_prices
    fruit_prices[fruits[2]] += 2
    print(f'3. list of fruits price after increase by 2 in 2nd index {fruit_prices}')
    
    # delete both key and value for fruits[3] from fruit_prices
    del fruit_prices[fruits[3]]
    print(f'4. list of fruits price after after delete the 3rd index fruits {fruit_prices}')
    

    # print the price of fruits[4]
    print(f"5. Price of the fruits in 4th index {fruit_prices[fruits[4]]}")

    # print the names of fruits in fruit prices as a list sorted in ascending order
    print(f"6. List of fruits {sorted(fruit_prices.keys())}")

    # print the prices of the fruits as a list sorted in ascending order.
    print(f"7. price of the fruits {sorted(fruit_prices.values())}")

def increase_prices(fruit_prices:dict) -> None:

    '''
    Increase the prices of every fruit by 20 percent and round to two decimal places

    Arguments:
    fruit_prices: dict - fruit name as key and price as value

    Return:
    None - Do not return any thing - modify inplace

    '''

    for fruit in fruit_prices:
        fruit_prices[fruit]*= 1.2
        fruit_prices[fruit] = round(fruit_prices[fruit],2)

# Practice done
def dict_from_string(string:str,key_type,value_type):
    
    '''
    Given a string where each line has a comma separated key-value pair, create a dictionary out of it. Also convert the types of key and values to the given types.

    Arguments:
    string - str: string to be parsed
    key_type - class: the data type of the keys
    value_type - class: the data type of the values

    Return:
    D - dict: the output dictionary

    '''

    D = {}
    for line in string.split("\n"):
        key, value = line.split(",")
        D[key_type(key)]=value_type(value)
    return D

def dict_to_string(D:dict) -> str:
    '''
    Convert the given dictionary back to the string format produced by `dict_from_string`. Again, do not use loops or conditionals, use comprehensions.

    '''

    return "\n".join(str(key)+","+str(value) for key, value in D.items())

# GrPA 2 - Dictionary Applications - GRADED

def total_price(fruit_prices: dict, purchases) -> float:
    
    '''
    Compute the fruit prices give the quantity of each fruit. Do not use the sum function.

    Arguments:
    fruit_prices: dict - fruit name as key and price as value
    purchases: list[tuple] - as list of tuples of (fruit, quantity)

    Return:
    total_price: float

    '''

    total = 0
    for fruit, quantity in purchases:
        total+= fruit_prices[fruit]*quantity
    return total

def total_price_no_loops(fruit_prices: dict, purchases) -> float:
    '''
    Compute the total price without loops.

    '''

    return sum(
        fruit_prices[fruit]*quantity
        for fruit, quantity in purchases
    )

def find_cheapest_fruit(fruit_prices:dict) -> str:
    '''
    Find the cheapest fruit from the fruit_prices dict, do not use min function

    Arguments:
    fruit_prices: dict - fruit name as key and price as value

    Return:
    cheapest_fruit: str - the fruit with the lowest price

    '''

    fruit_price_tuples = list(fruit_prices.items())
    min_fruit, min_price = fruit_price_tuples[0]
    for fruit, price in fruit_price_tuples[1:]:
        if price<min_price:
            min_fruit,min_price = fruit, price
    return min_fruit

def find_cheapest_fruit_no_loops(fruit_prices:dict) -> str:
    '''
    Find the cheapest fruit using min function. Do not use loops

    '''

    return min(fruit_prices, key=fruit_prices.get)

# grouping
def group_fruits(fruits:list):
    '''
    Group the fruits based on the first letter of the names. Assume first letters will be upper case.

    Arguments:
    fruits - list: list of fruit names

    Return:
    dict: dict with the first letters as keys and list of fruits sorted in ascending order as values.
    '''

    fruits_with_first_letter = {}
    for fruit in fruits:
        if fruit[0] not in fruits_with_first_letter:
            fruits_with_first_letter[fruit[0]] = []
        fruits_with_first_letter[fruit[0]].append(fruit)
    return {
      letter: sorted(fruits)
      for letter, fruits in fruits_with_first_letter.items()
    }

# binning
def bin_fruits(fruit_prices):
    '''
    Classify the fruits as cheap, affordable and costly based on the fruit prices. Create a dictionary with the classification as keys and a set of fruits in that category.

    cheap - less than 3 (not inclusive)
    affordable - between 3 and 6 (both inclusive)
    costly - greater than 6 (not inclusive)

    Arguments:
    fruit_prices: dict - dictionary with fruits as keys and prices as values

    Return:
    binned_fruits: dict - dictionary with category as key and a set of fruits in that category as values.
    '''

    binned_fruits = {category:set() for category in ["cheap","affordable","costly"]}
    for fruit, price in fruit_prices.items():
        if price<3:
            binned_fruits["cheap"].add(fruit)
        elif 3<=price<=6:
            binned_fruits["affordable"].add(fruit)
        else:
            binned_fruits["costly"].add(fruit)
    return binned_fruits

# GrPA 3 - Composing functions - GRADED
def index_of_first_occurrence(row:list,elem):
    '''
    Given a list find the index of first occurrence of 1 in it
    '''
    return row.index(elem)

def index_of_last_occurrence(row:list,elem):
    '''
    Given a list find the index of last occurrence of 1 in it.
    Hint: use index_of_first_one with reversal.
    '''
    return len(row) - 1 - row[::-1].index(elem)

def is_valid_coordinate(x:int,y:int, M):
    '''
    Checks if the x,y is a valid coordinate(indices) in the matrix M(list of list). Assume coordinates are non-negative
    '''

    r,c = len(M), len(M[0])
    return 0<=x<r and 0<=y<c
# practice done
def valid_adjacent_coordinates(x:int,y:int, M):
    '''
    Create a set of valid adjacent coordinates(indices) given x,y and a matrix M
    '''
    return {
      (x1,y1)
      for x1,y1 in {(x-1,y), (x+1,y), (x,y-1),(x,y+1)} # all the possible adjacent coordinates
      if is_valid_coordinate(x1,y1, M)
    }


# practice done
def next_coordinate_with_value(curr_coords, value, M, prev_coords=None):
    '''
    Find the coordinate(indices) of the next coordinate that has the `value` in it. For the starting coordinate the prev_coords would be None
    '''

    x,y = curr_coords
    for x1,y1 in valid_adjacent_coordinates(x,y, M)-{prev_coords}:
        if M[x1][y1] == value:
            return x1,y1


# practice done 
def get_path_coordinates(M):
    '''
    Given the matrix m, find the path formed by 1 from the last row to the first row.
    '''
    x_start, x_end = len(M)-1,0
    y_start, y_end = index_of_last_occurance(M[-1],1), index_of_first_occurance(M[0],1)

    path = []
    prev_coords= None
    curr_coords = x_start, y_start
    while curr_coords != (x_end,y_end):
        path.append(curr_coords)
        curr_coords, prev_coords = next_coordinate_with_value(curr_coords, 1, M,prev_coords), (curr_coords)
    path.append(curr_coords)
    return path


# practice done 
def print_path(M):
    path = get_path_coordinates(M)

    for coordinate in path:
        print(coordinate)

# practice done 
def alternate_path(M):
    path = get_path_coordinates(M)

    for i,(x,y) in enumerate(path,1):
        if i%2==0:
            M[x][y] = 2


def count_path(M):
    path = get_path_coordinates(M)

    for i,(x,y) in enumerate(path,1):
        M[x][y] = i

def mirror_horizontally(M):
    path = get_path_coordinates(M)

    for x,y in path:
        M[x][-y-1] = 1

def mirror_vertically(M):
    path = get_path_coordinates(M)

    for x,y in path:
        M[-x-1][y] = 1


# GrPA 4 - lambda, zip, enumerate, map, filter - GRADED

def groupby(data:list, key:callable):
    '''
    Given a list of items, and a key, create a dictionary with the key as key function called 
    on item and the list of items with the same key as the corresponding value. 
    The order of items in the group should be the same order in the original list
    '''

    groups = {}
    for item in data:
        group = key(item)
        if group not in groups:
            groups[group] = []
        groups[group].append(item)
    return groups

def apply_to_groups(groups:dict, func:callable):
    '''
    Apply a function to the list of items for each group.
    '''

    return {
      group: func(members)
      for group, members in groups.items()
    }

def min_course_marks(student_data, course):
    '''Return the min marks on a given course'''

    return min(map(lambda x:x[course], student_data))

def max_course_marks(student_data, course):
    '''Return the max marks on a given course'''

    return max(map(lambda x:x[course], student_data))

def rollno_of_max_marks(student_data, course):
    '''Return the rollno of student with max marks in a course'''

    return max(student_data,key= lambda x: x[course])['rollno']

def sort_rollno_by_marks(student_data, course1, course2, course3):
    '''
    Return a sorted list of rollno sorted based on their marks on the three course marks. 
    course1 is compared first, then course2, then course3 to break ties.
    Hint: use tuples comparision
    '''

    sorted_student_data = sorted(student_data,key= lambda stud: (stud[course1],stud[course2],stud[course3]))
    return list(map(lambda stud: stud["rollno"], sorted_student_data))

def count_students_by_cities(student_data):
    '''
    Create a dictionary with city as key and number of students from each city as value.
    '''

    students_by_city = groupby(student_data, lambda stud: stud["city"])
    return apply_to_groups(students_by_city, len)

def city_with_max_no_of_students(student_data):
    '''
    Find the city with the maximum number of students.
    '''

    city_student_count = count_students_by_cities(student_data)
    return max(city_student_count, key=city_student_count.get)

def group_rollnos_by_cities(student_data):
    '''
    Create a dictionary with city as key and 
    a sorted list of rollno of students that belong to 
    that city as the value.
    '''

    # this lambda is named so that it is easy to remember what it is doing.
    get_sorted_rollnos = lambda items: sorted(map(lambda item: item['rollno'],items))
    students_by_city = groupby(student_data, lambda x: x["city"])
    return apply_to_groups(students_by_city, get_sorted_rollnos)

def city_with_max_avg_course_mark(student_data, course):
    '''
    Find the city with the maximum avg course marks.
    '''

    students_by_city = groupby(student_data, lambda x: x['city'])
    avg = lambda x: sum(x)/len(x)
    get_course_avg = lambda items: avg(list(map(lambda x: x[course], items)))
    course_avg_by_city = apply_to_groups(students_by_city,get_course_avg)
    return max(course_avg_by_city, key=course_avg_by_city.get)

# GrPA 5 - min, max, sorted, groupby - GRADED
import random
def generate_student_data(n_students, courses, cities, random_seed=42):
    '''
    Create a list of dict with dictionaries representing each attributes of each student.
    '''
    random.seed(random_seed)
    return [
      {
        "rollno": i, "city": random.choice(cities), 
        **{course: random.randint(1,100) for course in courses} 
      }
      for i in range(1,n_students+1)
    ]

def groupby(data:list, key:callable):
    '''
    Given a list of items, and a key, create a dictionary with the key as key function called 
    on item and the list of items with the same key as the corresponding value. 
    The order of items in the group should be the same order in the original list
    '''

    groups = {}
    for item in data:
        group = key(item)
        if group not in groups:
            groups[group] = []
        groups[group].append(item)
    return groups

def apply_to_groups(groups:dict, func:callable):
    '''
    Apply a function to the list of items for each group.
    '''

    return {
      group: func(members)
      for group, members in groups.items()
    }

def min_course_marks(student_data, course):
    '''Return the min marks on a given course'''

    return min(map(lambda x:x[course], student_data))

def max_course_marks(student_data, course):
    '''Return the max marks on a given course'''

    return max(map(lambda x:x[course], student_data))

def rollno_of_max_marks(student_data, course):
    '''Return the rollno of student with max marks in a course'''

    return max(student_data,key= lambda x: x[course])['rollno']

def sort_rollno_by_marks(student_data, course1, course2, course3):
    '''
    Return a sorted list of rollno sorted based on their marks on the three course marks. 
    course1 is compared first, then course2, then course3 to break ties.
    Hint: use tuples comparision
    '''

    sorted_student_data = sorted(student_data,key= lambda stud: (stud[course1],stud[course2],stud[course3]))
    return list(map(lambda stud: stud["rollno"], sorted_student_data))

def count_students_by_cities(student_data):
    '''
    Create a dictionary with city as key and number of students from each city as value.
    '''

    students_by_city = groupby(student_data, lambda stud: stud["city"])
    return apply_to_groups(students_by_city, len)

def city_with_max_no_of_students(student_data):
    '''
    Find the city with the maximum number of students.
    '''

    city_student_count = count_students_by_cities(student_data)
    return max(city_student_count, key=city_student_count.get)

def group_rollnos_by_cities(student_data):
    '''
    Create a dictionary with city as key and 
    a sorted list of rollno of students that belong to 
    that city as the value.
    '''

    # this lambda is named so that it is easy to remember what it is doing.
    get_sorted_rollnos = lambda items: sorted(map(lambda item: item['rollno'],items))
    students_by_city = groupby(student_data, lambda x: x["city"])
    return apply_to_groups(students_by_city, get_sorted_rollnos)

def city_with_max_avg_course_mark(student_data, course):
    '''
    Find the city with the maximum avg course marks.
    '''

    students_by_city = groupby(student_data, lambda x: x['city'])
    avg = lambda x: sum(x)/len(x)
    get_course_avg = lambda items: avg(list(map(lambda x: x[course], items)))
    course_avg_by_city = apply_to_groups(students_by_city,get_course_avg)
    return max(course_avg_by_city, key=course_avg_by_city.get)


