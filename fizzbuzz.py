def fizzbuzz():
    num = input("Pick a number: ")

    if(int(num) %3 == 0 and int(num) %5 == 0):
        print("Fizz Buzz")
    elif (int(num) %3 == 0):
        print("Fizz")
    elif (int(num) % 5 == 0):
        print("Buzz")

    else:
        print("no fizzbuzz")

fizzbuzz()