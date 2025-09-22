lst = [10,40,70,30]
print(lst)

#addition

lst.append(10)
print(lst)

lst.extend([10,20,30])
print(lst)

#update

lst[1] = 25
print(lst)
lst[2:3] = 35,45
print(lst)


#slicing

print(lst[1:])
print(lst[::-1])


#deletion


lst.remove(10)
print(lst)

lst.pop(1)
print(lst)

del lst[0]
print(lst)
