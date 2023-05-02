
todos = []
while True:
    user_action = input("Type add or show: ").strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                print(item.title())
        case 'exit':
            break
        case _:
            print("You entered an uknown command")
print("Bye")
