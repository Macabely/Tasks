try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    sum = a + b
    difference = a - b
    product = a * b
    quotient = a / b
    print("sum:", sum)
    print("difference:", difference)
    print("product:", product)
    print("quotien:", quotient) 
except:
    print("Plese inter an integer")

# OR

# def operations(a, b):
#     sum = a + b
#     difference = a - b
#     product = a * b
#     quotient = a / b if b != 0 else "Undefined ==> division by zero"
#     return(f"sum: {sum} \ndifference: {difference} \nproduct: {product} \nquotient: {quotient}") 

# print(operations(a, b))