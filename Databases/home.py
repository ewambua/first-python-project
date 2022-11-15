from config import *
name = input(str("Enter name\n"))
email = input(str("Enter email\n"))
password = input(str("Enter password\n"))

User.create(name=name,email=email,password=password)
