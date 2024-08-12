def calculate(r,unit,arr,n):
    if arr is None or n==0:   
        return -1              #return 1 if the array is null
    
    totalfoodrequired= r*unit
    foodtillnow=0
 
    for house in range(n):
        foodtillnow += arr[house]
        if foodtillnow >= totalfoodrequired:
            return house+1
        
    return 0
#input handling
r=int(input("Enter the number of rats:"))
unit=int(input("enter the value of units:"))
n= int(input("Number of elements in an array:"))   
arr=list(map(int,input("list the elements with the space separated:").split()))

#calculate the result            #time complexity is O(n) it serach each and every index val one by one
print(calculate(r,unit,arr,n))