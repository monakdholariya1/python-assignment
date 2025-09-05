#Practical Example 3: Write a Python program to find a specific string in the list using a simple 
# for loop and if condition.


list = ["monank","ronak","utsav"]
search=input("enter the name : ")

for i in list:
    if i == search:
        print("this is available")
    else:
        print("this is not available")
