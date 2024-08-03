num=int(input("Enter the number:"))
factorial=1

if num<0:
    print("Factorial number does not exists for negative numbers.")
elif num==0:
    print("The Factorial of number 0 is : 1")
else:
    for i in range(1, num+1):
        factorial =factorial*i
    print("The factorial of ",num, "is" , factorial)        