file = open("essay.txt", 'r')
myline = file.read()
#Using readline() inside while-loop will take care of reading all the lines present in the file
# while myline:
#     print(myline)
#     myline = file.readline()
# myfile.close()
#The read() method allows read all strings in a file
print(myline.title())