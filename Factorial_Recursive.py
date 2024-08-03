def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

num =7
print("The Factorial of", num , "is",factorial(num))

#ternary operator
#return 1 if(n==0 or n==1) else  n*factorial (n-1)