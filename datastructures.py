# 1. TUPLES
cars = ("Mercedes", "R34", "Pagani", "Supra", "GTR")

print(cars)
print(cars[2])

# cars [0] = "Mercedes Benz" This is impossible.

print(cars[1:4])
print(cars[1:])

for gari in cars:
    print(gari)

# 2. LISTS
colours = ["Red", "Green", "Purple", "Blue", "Grey", "Black"]
print(colours)
print(colours[2])

colours[0] = "Light Red"

print(colours[1:4])
print(colours[1:])

for rangi in colours:
    print(rangi)

colours.reverse()
print(colours)

colours.pop(2)
print(colours)
colours.sort(reverse=True)
print(colours)

# 3 DICTIONARIES
students = {"ADM1": "Lauret", "ADM2": "Leo", "ADM3": "Trevor", "ADM4": "Samara", "ADM5": "Celine", "ADM6":"Maxwell"    }
print(students ["ADM5"])
for ufunguo in students.keys():
    print(ufunguo)

for jina in students.values():
    print(jina)

# 4 SETS

ranks = {1, 2, 4, 7, 8, 9, 10, 13, 3, 5, 6,}
print(ranks)





