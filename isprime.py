num = int(input("pick a number to check if prime: "))
def isprime (num):
    ##case if 1
    if num <= 1:
        return False
    for i in range (2, num-1):
        if (num%i) == 0:
            print('False')
            return False
    return print("True")
            
isprime(num)