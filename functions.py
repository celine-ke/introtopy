import math


def motto():
    print("Ora et Labora")

motto()
motto()

def vision():
    print("This is our vision")
vision()

def add():
    x = 10
    y = 20
    z = x + y
    print(z)
add()
add()

def avg(x, y, z):
    average = (x +y +z)/3
    print("Your average is "+str(average))

avg(12, 23, 45)
avg(43, 54, 67)

def bmicalc(weight, height):
    bmi = weight / pow(height, 2)
    if bmi <=18:
        print("Underweight")
    elif bmi <= 29:
        print("Normal weight")
    elif bmi <= 34:
        print("Overweight")
    else:
        print("Obese")


bmicalc(90, 1.8)

def gradecalc(totmarks, subnum):
    marks = totmarks / subnum
    if marks < 40:
        print("E")
    elif marks < 50:
        print("D")
    elif marks < 60:
        print("C")
    elif marks < 70:
        print("B")
    else:
        print("A")

gradecalc(420, 6)

def login(email, password):
    if email == "user@example.com" and password == "user123":
        gradecalc(460, 6)
    else:
        print("Login Fail")

login("user@example.com", "user123")
login("thea2@gmail.com", "1234")

def areaofacircle(radius):
    area = math.pi * pow(radius, 2)
    return area
# If you use the return function you have to use print to display the answer
print(areaofacircle(14))





