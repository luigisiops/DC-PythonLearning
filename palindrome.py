def palindrome(data):
    name = data
    reverse=""
    #check reverse
    for i in range(len(data) -1 , -1, -1):
        reverse = reverse + data[i]
    
    if reverse == name:
        print("true")
        return True
    else: 
        print("false")
        return False

palindrome("racecar")
    
