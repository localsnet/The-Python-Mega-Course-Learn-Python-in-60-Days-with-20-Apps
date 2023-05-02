filepath = './data'

def get_data(filepath_local):
    with open(filepath_local, 'r') as file:
        data_local = file.readlines()
        return data_local


def get_average():
    data = get_data(filepath)
    values = data[1:]
    new_values = [float(item) for item in values]
    avg = sum(new_values)/len(new_values)
    return avg



average = get_average()
print(average)