
todos = []
while True:
    user_action = input("Type add, show, edit or exit: ").strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                print(item.title())
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number -1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'exit':
            break
        case _:
            print("You entered an uknown command")
print("Bye")
