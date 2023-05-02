while True:
    user_action = input("Type add, show, edit, complete  or exit: ").strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('../todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)
            with open('../todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            with open('../todos.txt', 'r') as file:
                todos = file.readlines()
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
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number -1
            new_todo = input("Enter new todo: ")

            with open('../todos.txt', 'r') as file:
                todos = file.readlines()
                todos[number] = new_todo

            with open('../todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
           number = int(input("Number of the todo to complete: "))

           with open('../todos.txt', 'r') as file:
               todos = file.readlines()

           todos.pop(number-1)

           with open('../todos.txt', 'w') as file:
               file.writelines(todos)



        case 'exit':
            break
        case _:
            print("You entered an uknown command")
print("Bye")
