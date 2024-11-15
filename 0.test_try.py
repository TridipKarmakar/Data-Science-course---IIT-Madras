fruits = ["Apple","Orange","Grapes","Banana","Cherry"]
fruit_prices = {"Orange": 4, "Grapes": 3,"Banana": 2, "Cherry": 5,}


   


def dictionary_operation(fruit_prices : dict , fruits :list ):
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
    del  fruit_prices[fruits[3]]
    print(f'4. list of fruits price after after delete the 3rd index fruits {fruit_prices}')
    
    # print the price of fruits[4]
    
    print(f"5. Price of the fruits in 4th index {fruit_prices[fruits[4]]}")

    # print the names of fruits in fruit prices as a list sorted in ascending order
    print(f"6. List of fruits {sorted(fruit_prices.keys())}")

    # print the prices of the fruits as a list sorted in ascending order.
    print(f"7. price of the fruits {sorted(fruit_prices.values())}")

##use of the above functions
print("# list of fruits")
for i in enumerate(fruits) :
   print(i, end = ', ')
print('')
dictionary_operation(fruit_prices,fruits)



def increase_price(fruit_prices) :
    '''
    Increase the prices of every fruit by 20 percent and round to two decimal places

    Arguments:
    fruit_prices: dict - fruit name as key and price as value

    Return:
    None - Do not return any thing - modify inplace

    '''

    for fruits in fruit_prices:
        fruit_prices[fruits] *= 1.2
        fruit_prices[fruits]  = round(fruit_prices[fruits],2)

increase_value = increase_price(fruit_prices)

print(f'8. Fruits value after increase the price of all fruits at 20% {fruit_prices}')

str_input = '''Apple,2
Banana,3
Orange,4
Grapes,3
Papaya,5'''


def dict_from_string(string:str , key_type, value_type) :
    D = {}
    for line in string.split('\n') :
        key, value = line.split(",")
        D[key_type(key)] = value_type(value)
    return(D) 

dict_value = dict_from_string(str_input,str,int)
print(f"9. The new dictionary after converting from string {dict_value}")

def dict_to_string(D : dict) -> str :
    x = ("\n".join(str(key)+","+str(values) for key,values in D.items()))
    return str(x)

print(f"10. The dictionary again converted into a strings \n{(dict_to_string(dict_value))} \n-- The End of GRPA - 1 --")
print()

fruit_prices2 =  {'Apple':2.0,'Banana':2.0,'Orange':4.0,'Grapes':3.0,'Papaya':5.0}
list_purchase = [("Apple",3),("Orange",5),("Grapes",4)]

def total_price(fruit_prices2: dict, list_purchase ) -> float :

    total = 0
    for fruits , qty_purchase in list_purchase :
        total += (fruit_prices2[fruits] * qty_purchase)

    return(total) 

total_price_of_purchase_items = total_price(fruit_prices2,list_purchase)
print(f"11. The total price of purchased items {total_price_of_purchase_items}")

def total_price_no_loops(fruit_prices2: dict, list_purchase ) -> float :
    list_comp = sum((fruit_prices2[fruits] * qty_purchase) for fruits , qty_purchase in list_purchase) 
    return(f"12. The total price of purchased using sum features {list_comp}")

total_price_of_purchase_items = total_price(fruit_prices2,list_purchase)
print(f"12. The total price of purchased using sum features {total_price_of_purchase_items}")


def find_cheapest_fruit(fruit_prices2 : dict ) -> str :

    fruit_prices2_tuples =  list(fruit_prices2.items())
    min_fruits, min_price = fruit_prices2_tuples[0] 

    for fruit,price in fruit_prices2_tuples[1:] :
        if price < min_price :
            min_fruits = fruit 
            min_price = price
        elif price == min_price : 
            min_fruits += ", " + fruit


    if "," in min_fruits :

        return(f"13. The cheapest price fruits are {min_fruits} and the price is Rs.{min_price}")

    else :
        return(f"13. The cheapest price fruit is {min_fruits} and the price is Rs.{min_price}")

cheapest_fruit = find_cheapest_fruit(fruit_prices2)
print(cheapest_fruit)

def find_cheapest_fruit_without_loop(fruit_prices2 : dict ) -> str :
    return(min(fruit_prices2, key = fruit_prices2.get), min(fruit_prices2.values()))

cheapest_fruit_name,cheapest_fruit_price = (find_cheapest_fruit_without_loop(fruit_prices2))
print("The cheapest fruits is",cheapest_fruit_name,"and the price is rs.",cheapest_fruit_price)



# list_of_fruits = ["Avocado","Apple","Banana","Blackberry","Cherry","Cranberry","Grape","Mango"]

# keys_set = set()
# D = {}
# for fruit in list_of_fruits :    
#     keys_set.update(fruit[0]) 

# for key in keys_set :
#     D[key] = []
# print(D)
# for fruit in list_of_fruits :
#     print(fruit)
#     for key in D :
#         if fruit[0] == key : 
#             D[key].append(fruit)

# print(D)


# group

list_of_fruits = ["Avocado","Apple","Banana","Blackberry","Cherry","Cranberry","Grape","Mango"]
def group_fruits (list_of_fruits : list) :

    fruits_with_first_letter = {}
    for fruit in list_of_fruits :
        if fruit[0] not in fruits_with_first_letter :
            fruits_with_first_letter[fruit[0]] = []
        fruits_with_first_letter[fruit[0]].append(fruit)
    return{ letter : sorted( fruits) for letter , fruits in fruits_with_first_letter.items()}

fruits_list_with_first_letter = group_fruits(list_of_fruits)
print(f"14. The dictionary of fruits with the first letter as key {fruits_list_with_first_letter}")


fruits_bin_price = {'Apple':7,'Banana':3,'Orange':4,'Grapes':6,'Papaya':5,'Mango':2,'Amla':1,'Jackfruit':10}

def bin_fruits(fruits_bin_price : dict ):
    binned_fruits = { category : set() for category  in ["cheap","affordable", "costly"]}
    for fruit in fruits_bin_price :
        if fruits_bin_price[fruit] < 3 :
            binned_fruits["cheap"].add(fruit)
        elif  6 >= fruits_bin_price[fruit] >= 3 :
            binned_fruits["affordable"].add(fruit)
        else  :
            binned_fruits["costly"].add(fruit)
        
    return(binned_fruits)

bin_fruits_dict = bin_fruits(fruits_bin_price) 
print(f"15. The list of the bin fruits as per the category is : {bin_fruits_dict}")

# index of the first occurrence

row = [0, 0, 1, 1, 0]
print(f"16. The index number of the first occurrence element in the given list is : {row.index(1)}")

# index of the last occurrence
print(f"17. The index number of the last occurrence element in the given list is : {len(row) - 1 - row[::-1].index(1)}")


matrix = [
[0, 0, 1, 1],
[0, 0, 0, 1],
[1, 1, 1, 1],
[1, 0, 0, 0],
[1, 1, 0, 0]
] 


def is_valid_coordinate(x :int , y : int , matrix) :
    r , c = len(matrix) , len(matrix[0])
    if 0 <= x < r and 0 <= y <c :
        return "a valid coordinate in the given matrix."    
    else :
        return  "not a valid coordinate in the given matrix." 
row = 3
col = 2
is_valid  = is_valid_coordinate (row, col, matrix)

print(f"18. The given {row} X {col} is {is_valid}" )
import re 
passage='''
aaaa bbbb cccc AAAA bbbb
CCCCCC DDDDD CCCCC CdcDC
abab cDcD
'''

set_list ={}
passage = passage.strip()

for first_letter in list(re.split(r'[ \n]+', passage)) :
    print(first_letter)
    print(first_letter[0])
    if first_letter[0].lower() in set_list   :
        set_list[first_letter[0].lower()] = set_list[first_letter[0].lower()] +1  

    elif first_letter[0] not in set_list:
        set_list[first_letter[0].lower()] = 1
    print(set_list)

print(max(set_list, key = set_list.get))