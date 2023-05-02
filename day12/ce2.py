password = input("Enter new password: ")


def check_password(password_local):
    result = []
    # len evaluated to int type
    if len(password_local) >= 8:
        result.append(True)
    else:
        result.append(False)

    digit = False
    for i in password_local:
        if i.isdigit():
            digit = True
    result.append(digit)

    upper = False
    for i in password_local:
        if i.isupper():
            upper = True
    result.append(upper)
    if all(result):
        print('Strong password')
    else:
        print('Weak password')


check_password(password)