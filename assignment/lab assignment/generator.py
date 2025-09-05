#Write a generator function that generates the first 10 even numbers.    

def even_numbers():
    num = 2
    count = 0
    while count < 10:
        yield num
        num += 2
        count += 1

# using the generator
for n in even_numbers():
    print(n)
