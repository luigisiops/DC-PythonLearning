def calculator(num1,operation,num2):
    if (operation == "+"):
        print (num1 + num2)
    elif (operation == "-"):
        print (num1 - num2)
    elif (operation == "*"):
        print (num1 * num2)
    elif (operation == "/"):
        print (num1 / num2)
    else:
        print("not a valid operation")

calculator(11,"*",9)