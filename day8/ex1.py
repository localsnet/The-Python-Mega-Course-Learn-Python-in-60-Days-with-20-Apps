flips = []
head = 0
while True:
    flip = input("Throw the coin and enter head or tail here?: ").strip()
    match flip:
        case 'head':
            with open('flip.txt', 'w') as file:
                flips.append(flip + "\n")
                file.writelines(flips)
                head += 1
                print(head)


        case 'tail':
            with open('flip.txt', 'w') as file:
                flips.append(flip + "\n")
                file.writelines(flips)

