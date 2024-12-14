def factorial(n):
    """This is a fctorial recursion function"""
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Please enter the number"))
print(factorial(n))
print("using__doc__")
print(factorial.__doc__)