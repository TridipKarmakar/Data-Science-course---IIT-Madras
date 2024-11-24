import week_Five_5_b__GRP_Assingment as week5 
##use of the above functions
fruits = ["Apple","Orange","Grapes","Banana","Cherry"]
fruit_prices = {"Orange": 4, "Grapes": 3,"Banana": 2, "Cherry": 5,}
print("# list of fruits")
for i in enumerate(fruits) :
   print(i, end = ', ')
print('')

# Execution Part  GrPA 1 - Dictionary Basics - GRADED
# 1st Basic dictionary functions | 
# def dictionary_operations(fruit_prices:dict, fruits:list):
week5.dictionary_operations(fruit_prices,fruits)


# def increase_prices(fruit_prices:dict) -> None:
increase_value = week5.increase_prices(fruit_prices)
print(f'8. Fruits value after increase the price of all fruits at 20% {fruit_prices}')

# def dict_from_string(string:str,key_type,value_type):
str_input = '''Apple,2
Banana,3
Orange,4
Grapes,3
Papaya,5'''
dict_value = week5.dict_from_string(str_input,str,int)
print(f"9. The new dictionary after converting from string {dict_value}")



print(f"10. The dictionary again converted into a strings \n{(dict_to_string(dict_value))} \n-- The End of GRPA - 1 --")
print()




