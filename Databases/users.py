from config import *
users = User.select()
for user in users:
    print(user.name, user.email, user.password)
