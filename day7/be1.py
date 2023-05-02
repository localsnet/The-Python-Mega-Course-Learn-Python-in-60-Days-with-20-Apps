temperatures = [10, 12, 14]

file = open("file.txt", 'w')
file.writelines([str(i)+'\n' for i in temperatures])
file.close()