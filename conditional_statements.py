# # This is an if statement
# age = int(input("Enter your age\n"))
# if age < 20:
#     print("Sorry, you can't attend this party")
# else:
#     print("Welcome to the party")

# Simple interest calculator
# principle = float(input("Enter your principle\n"))
# rate = float(input("Enter your rate\n"))
# time = float(input("Enter your time\n"))
# simpleInterest = (principle * rate * time) / 100
# if simpleInterest <=1000:
#     print("The loan is affordable")
# elif simpleInterest <=2000:
#     print("The loan is expensive")
# else:
#     print("This is a scam")

grade = int(input("Enter your grade"))

if grade >= 90 and grade<= 100:
        print("A")

elif grade >= 80 and grade <= 89:
        print("B")
elif grade >= 70 and grade <= 79:
        print("C")

elif grade >= 60 and grade <= 69:
        print("D")

elif grade >= 50 and grade <= 59:
        print("E")
else:
        print("F")
