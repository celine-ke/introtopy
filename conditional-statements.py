age = 18
if age < 18:
    print("TRUE")
else:
    print("FALSE")

x = 10
y = 20
if x < y and y > 30:
    print("TRUE")
else:
    print("FALSE")

if x < y or y > 30:
    print("TRUE")
else:
    print("FALSE")

marks = 90
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

bettingNumber = 0
if bettingNumber == 1:
    print("You won a goat!!!")
elif bettingNumber == 2:
    print("You won a cow!!")
elif bettingNumber == 3:
    print("You won 3 cow!!")
elif bettingNumber == 4:
    print("You won 5 cow!!")
else:
    print("Please enter a number from 1 - 4 to bet!!")


loan = 100000
rate = 5
time = 1
interest = (loan * rate * time)/100
print(interest)

if interest < 7000:
    print("Good loan")
elif interest < 10000:
    print("Bad loan")
else:
    print("Scam")


height = 1.702
weight = 67
BMI = weight/(height * height)

if BMI <= 18:
    print("Underweight")
elif BMI <= 29:
    print("Normal Weight")
elif BMI <= 34:
    print("Over Weight")
else:
    print("Obese")