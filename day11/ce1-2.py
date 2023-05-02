def get_max_min():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    minimum = min(grades)
    return maximum, minimum

calc = get_max_min()
message = f"Max: {calc[0]}, Min: {calc[-1]}"
#print('Max: '+ str(calc[0]) + ', ' +' Min: '+ str(calc[-1]))
print(message)

#Method2
# def get_max():
#     grades = [9.6, 9.2, 9.7]
#     maximum = max(grades)
#     minimum = min(grades)
#     message = f"Max: {maximum}, Min: {minimum}"
#     return message
#
#
# print(get_max())