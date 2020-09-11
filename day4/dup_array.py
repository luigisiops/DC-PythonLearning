arr = [1,2,3,4,5]
copy = arr

def dup_array(arr):
    for x in range(0,len(arr)):
        copy.append(arr[x])
    return copy

print(dup_array(arr))