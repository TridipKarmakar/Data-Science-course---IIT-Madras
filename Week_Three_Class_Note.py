# Finding the factorial of the given number 
# Test Cases (5,2,0,-7)
# Using for loop

def fact(number) :
    product_factorial = 1
    if (number >= 0) :
        for i in range(1,number + 1) :
            product_factorial *=i
        return product_factorial
    else : 
        return "Not Defined"
     
    

Number = fact(int(input("Enter the Number : ")))
print(Number)