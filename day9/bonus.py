password = input("Enter new password: ")
result = []
#len evaluated to int type
if len(password) >= 8 :
    result.append(True)
else:
    result.append(False)

digit = False
for i in password:
    if i.isdigit():
        digit = True
result.append(digit)

upper = False
for i in password:
    if i.isupper():
        upper = True
result.append(upper)
if all(result):
    print('Strong password')
else:
    print('Weak password')