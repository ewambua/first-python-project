def motto():
    print("Hello this is our motto")

motto()

def addition():
    answer = 10 + 20
    print("Your answer is",answer)
addition()

def sum(x,y,z):
    answer = x + y + z
    print("Hello your answer is", answer)
sum(76,60,40)

def avg(x,y,z):
    average = (x + y + z) / 3
    return average


myValue = avg(23,40,60)
print(myValue)


def BMI(w,h):
    answer = w/pow(h,2)
    if answer < 24:
        print("You are Underweight")
    elif answer < 29:
        print("You are at a Normal weight")
    elif answer < 34:
        print("You are Overwieght")
    else:
        print("You are Obese")

BMI(100,8)



