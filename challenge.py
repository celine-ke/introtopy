nameslist = []
length = 7

for idx in range(length):
    item = input('Enter name')
    nameslist.append(item)

for name in nameslist:
    print(name)

shortnames = []
longnames = []
palindromicnames = []

print("list of short names")
for name in nameslist:
    if len(name) > 4 and len(name) < 7:
        shortnames.append(name)

for name in shortnames:
    print(name)


print("list of long names")

for name in nameslist:
     if len(name) > 7:
         longnames.append(name)
for name in longnames:
    print(name)

print("Palindromes")
for name in nameslist:
     if name == "".join(reversed(name)):
        palindromicnames.append(name)
for name in palindromicnames:
    print(name)


