names = ["Alex","John","Mary","Steve","John", "Steve","Steve"]

## checks against the dicitonary if in the array to know when to add to the result array
## also counts the duplicates

def duplicates(arr):
    hashmap = {}
    result = []
    for name in range(0,len(arr)):
        if(arr[name] not in hashmap):
            hashmap[arr[name]] = 1
            result.append(arr[name])
        else:
            hashmap[arr[name]]+=1
    print(hashmap)
    print(result)

duplicates(names)