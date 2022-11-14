# Tuples
cars = ("Limo","Range","Mercedes","Porsche","Nissan","Toyota")
print(cars[3])
for car in cars:
    print(car)

slicedcars = cars[0:3][::-1]
for sc in slicedcars:
    print(sc)

# Lists
students = ["Samson","Chris","Emmanuel","Owen"]
students.append("Ted")
# students.remove("Chris")
# students.pop(0)
# students[1] = "Mwangi"
# students[0],students[3] = students[3],students[0]
for student in students:
    print(student)
# Dictionaries
users = {"c@test.com":"Chris","e@test.com":"Emmanuel",
         "s@test.com":"Samson","o@test.com":"Owen"}
print(users["c@test.com"])

for user in users.values():
    print(user)

for user in users.keys():
    print(user)

