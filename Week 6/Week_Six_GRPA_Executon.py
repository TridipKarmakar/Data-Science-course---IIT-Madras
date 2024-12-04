# import Week_Six_GRPA_Assingments as week_six


# name, age, rollno = (week_six.get_student_details())
# print(f"The student name is {name}, age is {age} and the roll no is {rollno}.")

# number = ("1,2,3,4,5")

# list_comma_separated_value = week_six.get_comma_separated_integers()
# print(list_comma_separated_value)

# n = 2
# batsman_runs_dict = {}
# batsman_runs = ["Math-90","Science-85"]
# for i in batsman_runs :
#     key, value = i.split("-")
#     batsman_runs_dict[key] = value
# print(batsman_runs_dict)

# n = 2
# batsman_run = []

# for i in range(n):
#     batsman_run.append(input().split("-"))

# # for subject , score  in batsman_run :
# #     Score_dict[subject] = int(score)
# # print(Score_dict)

# Score_dict = {subject : int(score) for subject, score in batsman_run}
# print(Score_dict)


# get_student_marks
# [{'rollno': 1, 'city': 'chennai', 'age': 23, 'course1': 86, 'course2': 69, 'course3': 86},{'rollno': 2, 'city': 'mumbai', 'age': 19, 'course1': 78, 'course2': 65, 'course3': 89}]
# 2
# 1,chennai,23,86,69,86
# 2,mumbai,19,78,65,89


# n = int(input())
# student_data = []
 
# # for i in range(n) :
# #     student_data_dict = {}
# #     rollno,city,age,course1,course2,course3 = input().split(",") 
# #     student_data_dict["rollno"] = int(rollno)
# #     student_data_dict["city"] = city
# #     student_data_dict["age"] = int(age)
# #     student_data_dict["course1"] = int(course1)
# #     student_data_dict["course2"] = int(course2)
# #     student_data_dict["course3"] = int(course3)
# #     student_data.append(student_data_dict)    
# # print(student_data)
    
 
# for i in range(n) :
#     student_data_dict = {}
#     rollno,city,age,course1,course2,course3 = input().split(",") 
#     student_data.append    
#     print(student_data)


# student_data = [ 
#     {   
#         "Roll No" : int(input(f"Enter the {i+1} student Roll No : ")),
#         "City" : input("Enter the City : "),
#         "Age" : int(input("Enter the Age : ")),
#         "Course1" : int(input("Enter the 1st Course number : ")),
#         "Course2" : int(input("Enter the 2nd Course number : ")),
#         "Course3" : int(input("Enter the 3rd Course number : "))
#     }
      
#       for i in range(int(input()))  ]

# print(student_data)


nums= [1,3,4,5]
print(*nums, sep= ",")