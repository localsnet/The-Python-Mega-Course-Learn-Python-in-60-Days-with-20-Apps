content = 'Hello'
filenames = ['file1', 'file2']
for filename in filenames:
    filename = open(f'{filename}.txt', 'w')
    filename.write(content)
    filename.close()