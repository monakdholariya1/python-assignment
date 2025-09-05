'''Practical Example 4: Print this pattern using nested for loop:
markdown
Copy code
*
**
***
****
*****'''


num=int(input("enter the number : "))

for i in range(1,num+1):

    for j in range(i):
        print("*",end="")
    print()
