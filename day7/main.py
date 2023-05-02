while True:
    user_action = input("Type add, show, edit, complete  or exit: ").strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('../todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)
            file = open('../todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show' | 'display':
            file = open('../todos.txt', 'r')
            todos = file.readlines()
            file.close()
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
            todos[number] = new_todo
        case 'complete':
           number = int(input("Number of the todo to complete: "))
           todos.pop(number-1)



        case 'exit':
            break
        case _:
            print("You entered an uknown command")
print("Bye")
