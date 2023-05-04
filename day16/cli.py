import functions
while True:
    user_action = input("Type add, show, edit, done  or exit: ").strip()
    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')
        functions.write_todos(todos)

    elif user_action.startswith('show') :
        todos = functions.get_todos() #missed argument here could work with default value in function's parameter
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

            todos = functions.get_todos()
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue


    elif user_action.startswith('done') :
        try:
           number = int(user_action[5:])

           todos = functions.get_todos()

           todos.pop(number-1)

           functions.write_todos(todos)
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
