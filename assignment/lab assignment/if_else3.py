#Practical Example 7: Write a Python program to calculate grades based on percentage using if-else ladder.

per = int(input("enter the percentage : "))

if per>90 and per<99:
    print("GRADE A")
elif per>70 and per<89:
    print("GRADE B")
else:
    print("GRADE C")
    