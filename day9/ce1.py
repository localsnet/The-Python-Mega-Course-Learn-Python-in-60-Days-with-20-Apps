password = input("Enter a new password :")
result = {}

if len(password) == 7:
    print("Password is OK, but not too strong")
elif len(password) > 7:
    print("Great password there!")
else:
    print("Your password is weak.")