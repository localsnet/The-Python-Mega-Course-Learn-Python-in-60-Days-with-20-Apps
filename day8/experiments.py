#with context manager
with open("../todos.txt") as file:
    #is it possible to run another than file
    print("Hello")
    #read file and print to output
    print(file.read())