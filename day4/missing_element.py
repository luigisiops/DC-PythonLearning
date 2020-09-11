complete = [0,1,2,3,4,5,6,7,8,9]

def missing_element(arr):
    for num in complete:
        if num not in arr:
            return num
    return

print(missing_element([0,1,2,3,5,6,7,8,9]))


