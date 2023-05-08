FILEPATH = 'todos.txt'


def get_todos(filepath_local=FILEPATH):
    # Below triple quotation using for description of function and allows read by help()
    """ The main purpose this function to read a text file and return it as list to
     operate on it the to-do program"""
    with open(filepath_local, 'r') as file:
        todos_local = file.readlines()
        return todos_local


def write_todos(todos_args, filepath_local=FILEPATH):
    with open(filepath_local, 'w') as file_w:
        file_w.writelines(todos_args)


def counts(phrase):
    return phrase.count('.')



#This code will execute while importing this moule
print(__name__)
#Below code will never executes in external program using this module,but only running module itself directly.
if __name__ == "__main__":
    print("Hello")
