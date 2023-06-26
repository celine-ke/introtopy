def challenge(names):
    print("QN1. Names > 4 and < 7 characters")
    for name in names:
        if len(name) > 4 and len(name) < 7:
            print(name)

    print("QN2 . Sorted names > 7 characters")
    names.sort()
    for name in names:
        if len(name) > 7:
            print(name)

    print("QN3 . Palindromic names")
    for name in names:
        if name == name[::-1]:
            print(name)