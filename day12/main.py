filepath = '../todos.txt'


def get_todos(filepath_local=filepath):
    with open(filepath_local, 'r') as file:
        todos_local = file.readlines()
        return todos_local


def write_todos(filepath_local, todos_args):
    with open(filepath_local, 'w') as file_w:
        file_w.writelines(todos_args)


while True:
    user_action = input("Type add, show, edit, done  or exit: ").strip()
    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos(filepath)

        todos.append(todo + '\n')
        write_todos(filepath, todos)

    elif user_action.startswith('show') :
        todos = get_todos() #missed argument here could work with default value in function's parameter
# 1 way - Using loop
        # new_todos = []

        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)
#2 way - List comprehension
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
#3 way - simple, use variable, we are avoid extra loop/list-comprehension
            item = item.strip('\n')
            row = f"{index +1 }-{item}"
            print(row)
            # print(todos)
    elif user_action.startswith('edit') :
        try:
            number = int(user_action[5:])
            number = number -1
            new_todo = input("Enter new todo: ")

            todos = get_todos(filepath)
            todos[number] = new_todo + '\n'

            write_todos(filepath, todos)
        except ValueError:
            print("Your command is not valid.")
            continue


    elif user_action.startswith('done') :
        try:
           number = int(user_action[5:])

           todos = get_todos(filepath)

           todos.pop(number-1)

           write_todos(filepath, todos)
        except IndexError:
            print("You exceed number of range")
            continue
        except ValueError:
            print("You probably missed number of task")
            continue
    elif user_action.startswith('exit') :
        break
    else:
        print("You entered an unknown command")
print("Bye")
