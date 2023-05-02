filenames = ['doc', 'report', 'presentation']

for filename in filenames:
    file = open(f'{filename}.txt', 'w')
    file.write("Hello")
    file.close()