
countries = []
while True:
    user_action = input("Where are you from or type exit: ").strip().capitalize()
    match user_action:
        case 'Ukraine':
            countries.append(user_action)
            print("Будьмо")
        case 'Russia':
            countries.append(user_action)
            print("Москаль мені не брат")
        case 'Canada':
            countries.append(user_action)
            print("How are you :), Lovely, Good deal, Pay me more $_$, By-By ")

        case 'Exit':
            if countries:
                print("You have been in :")
                for item in countries:
                    print(item.title())
            else:
                print("Пролетарии  Банановых республик соединяйтесь!")
            break
        case _:
            print("You entered an uknown command")

