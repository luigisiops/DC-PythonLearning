"""def calculator(num1,operation,num2):
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

calculator(11,"*",9)"""

def add(num1, num2): 
    print (int(num1) + int(num2))

def subtract(num1, num2): 
    print (int(num1)-int(num2))

def multiply(num1, num2): 
    print(int(num1)*int(num2))
    
def divide(num1, num2): 
    print(int(num1)/int(num2))

def calculator():
    check = False
    while(check == False):
        try:
            num1 = int(input("first num: "))
            num2 = int(input("second num: "))
            op = input("put operation: ")
            check = True
        except:
            check = False
            print('needs to be a number')

    if (op == "+"):
        add(num1, num2)
    elif (op == "-"):
        subtract(num1, num2)
    elif (op == "*"):
        multiply(num1, num2)
    elif (op == "/"):
        divide(num1,num2)
    else:
        print("not a valid operation")
    return
    
calculator()