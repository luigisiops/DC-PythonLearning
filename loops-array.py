"""friends = ["deez", "nuts", "yeah"]

for index in range((len(friends)-1),-1,-1):
    print(friends[index])"""

#array indexing and appending
"""
animals = []

animals.append("dog")
animals.append("fox")
animals.append("wolf")

print(animals)

animals.remove('wolf')

print(animals)

animals.insert(0,"yuh")

print(animals)"""

#Write app to ask input for name to add to array and prints

names = []
for i in range(0,5):
    name = input("Write your name: ")
    names.append(name)

print(names)
