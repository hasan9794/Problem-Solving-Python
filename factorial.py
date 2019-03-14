def cube(number):
    print(number * number * number)
cube(2)
 
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)    
number = int(input("Input a number"))
print(factorial(number))



