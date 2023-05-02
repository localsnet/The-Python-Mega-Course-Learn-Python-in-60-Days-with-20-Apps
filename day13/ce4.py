def count_names(names):
    names = names.split(',')
    count = len(names)
    return count


names_write = input("Write names separated by commas:")
result = count_names(names_write)
print(result)