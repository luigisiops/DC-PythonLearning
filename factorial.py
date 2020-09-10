num = int(input("Write a number for factorial: "))
def factorial (num):
    for i in range(num, 1, -1):
        num = num * (i-1)
    return print(num)

factorial(num)
