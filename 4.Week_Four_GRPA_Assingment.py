## GrPA 1 - Basic Collections - GRADED

# Note this prefix code is to verify that you are not using any for loops in this exercise. 
# This won't affect any other functionality of the program.
# The values of the below variables will be changed by the evaluator

int_iterable = range(1,10,3)
string_iterable = ["Apple","Orange", "Banana"]
some_value = 4
some_collection = [1,2,3] # list | set | tuple 

some_iterable = (1,2,3)
another_iterable = {"apple", "banana", "cherry"} # can be any iterable
yet_another_iterable = range(1,10)

# <nofor>
# <eoi>

empty_list = [] 
empty_set = set({}) # be carefull here you might end up creating something called as an empty dict 
empty_tuple = () 

singleton_list = ["tridip"] # list: A list with only one element
singleton_set = {"tridip",} # set: A set with only one element
singleton_tuple = ("tridip",) # tuple: A tuple with only one element

a_falsy_list = [] # list: a list but when passed to bool function should return False.
a_falsy_set = set({}) # set: a list but when passed to bool function should return False.
a_truthy_tuple = (2,3,4) # tuple: a tuple but when passed to bool function should return True

int_iterable_min = min(int_iterable) # int: find the minimum of int_iterable. Hint: use min function
int_iterable_max = max(int_iterable) # int: find the maximum of int_iterable. Hint: use max function
int_iterable_sum = sum(int_iterable) # int: you know what to do
int_iterable_len = len(int_iterable) # int: really... you need hint?
int_iterable_sorted = sorted(int_iterable) # list: the int_iterable sorted in ascending order
int_iterable_sorted_desc = sorted(int_iterable, reverse = True)# list: the int_iterable sorted in desc order

if  isinstance(int_iterable, list): # some iterables are not reversible why?
    int_iterable_reversed = (int_iterable)[::-1] # list: the int_iterable reversed use the reversed function
else: # in that case sort it in ascending order and reverse it
    int_iterable_reversed = sorted(list(int_iterable),reverse = True) #list

if isinstance(some_collection, (list,tuple)): # some collections are not indexable why?
    third_last_element = some_collection[-3] # the third last element of `some_collection`
else: # in that case set third_last_element to None
    third_last_element = None 

if isinstance(some_collection, (list,tuple,range)): # some collections are not slicable
    odd_index_elements = (some_collection)[1::2] # type(some_collection): the elements at odd indices of `some_collection` 
else: # in that case set odd_index_elements to None
    odd_index_elements = None 

is_some_value_in_some_collection = some_value  in some_collection  # bool: True if `some_value` is present in `some_collection`

if isinstance(some_collection, (list,str,tuple)): # some collections are not ordered
    is_some_value_in_even_indices = some_value in some_collection[::2]  # bool: True if `some_value` is present in even indices of `some_collection`
else: # in that case set is_some_value_in_even_indices to None
    is_some_value_in_even_indices = None

all_iterables = list(some_iterable) + list(another_iterable)  + list(yet_another_iterable )  # list: concatenate `some_iterable`, `another_iterable` and `yet_another_iterable` into a list.

if isinstance(string_iterable, list) : # some iterables are not ordered
    all_concat = "-".join(string_iterable) # str: concatenate all the strings in string_iterable with '-' in between
else: # in that case sort them and concatenate
    all_concat = "-".join(sorted(list(string_iterable)))
