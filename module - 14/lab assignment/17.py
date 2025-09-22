def cal(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a//b

    print(f"adition of {a} and {b} is :{sum}")
    print(f"substraction of {a} and {b} is :{sub}")
    print(f"multiplication of {a} and {b} is :{mul}")
    print(f"divition of {a} and {b} is :{div}")

a,b = int(input("enter the number : "))

cal(a,b)
