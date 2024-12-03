def add(x , y ) :
    return (x + y)

def sub(x , y ) :
    return (x - y)

def mul(x , y ) :
    return (x * y)

def div(x , y ) :
    return (x / y)


add = lambda x, y : x + y

sub = lambda x, y : x - y

mul = lambda x, y : x * y

div = lambda x, y : x / y

print(add(5,4))
print(sub(5,4))
print(mul(5,4))
print(div(5,4))



fruits = ["mango", "apple", "banana", "orange", "pineapple", "watermelon", "guava", "kiwi"]
size = [5,5,6,6,9,10,5,4]


for fruit in enumerate(fruits):
    print(fruit)

list_enumerate =  list(zip(fruits,size))
zip_enumerate  = dict (zip(fruits,size))

a = [10, 20, 30, 40, 50, 60]
b = [10, 20, 30, 40, 50, 60]

import math

def add(x, y) :
    return x + y

list_map = list(map(add,a,b))

def sqrt_of(x) :
    return math.sqrt(x)

def is_positive(x) :
    if  x > 0 :
        return x

b = [10, -20, 30, 40, -50, 60]

map_filter_object = list(map(sqrt_of,filter(is_positive,b)))
print(map_filter_object)