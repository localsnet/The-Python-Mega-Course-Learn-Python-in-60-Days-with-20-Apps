def convert_liters_cubic(liters_local):
    m3 = float(liters_local) / 1000
    return m3


liters = input("Enter liters value: ")
cubes = convert_liters_cubic(liters)
message = f"{cubes} cubic meters in {liters} liters"
print(message)
