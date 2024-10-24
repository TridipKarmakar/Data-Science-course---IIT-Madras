some_iterable = [1,2,3,45,6,7,8,9]
another_iterable = ("tridip", "karmakar") 
yet_another_iterable = ("misti","das")

all_concat = some_iterable + list(another_iterable) + list(yet_another_iterable)
str_instamces = ["tridip", "karmakar","misti","das"]
join_iterable = "_".join(sorted(str_instamces)) 
print(join_iterable)