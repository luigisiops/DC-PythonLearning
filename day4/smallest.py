arr = [1,0,500000,32,240,5,23,4545,90,-20]


#naive approach
def largest(arr):
    current = arr[0]
    for x in arr:
        if (x <= current):
            current = x
    return print(current)

largest(arr)