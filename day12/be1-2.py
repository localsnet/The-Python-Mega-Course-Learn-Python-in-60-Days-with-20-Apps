def speed(distance, time):
    data = [distance, time]
    # Check if user mislead the order of input data and fix it
    if data[0] < data[1]:
        data.reverse()
    return data[0] / data[1]


print(speed(2, 300))