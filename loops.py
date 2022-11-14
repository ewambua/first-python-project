# LOOPS
# While loop
counter = 0
while counter <=5:
    print(counter)
    counter+=1

countertwo = 90
while countertwo >= 85:
    print(countertwo)
    countertwo-=1

counterthree = 20
while counterthree  <= 50:
    if counterthree%2==1:
        print(counterthree)
    counterthree+=1





# For in loop
numbers = range(6)
for nambari in numbers:
    print(nambari)

marks = range(40,101,10)
for mark in marks:
    if mark <= 40:
        print("E")
    elif mark <= 50:
        print("D")
    elif mark <= 60:
        print("C")
    elif mark <= 70:
        print("B")
    else:
        print("A")