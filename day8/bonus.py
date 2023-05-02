date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10?\n ")
thoughts = input("Let your thoughts flow:\n")
with open(f"journal/{date}.txt", "w") as file:
    #it will be appended
    file.write(mood + 2*"\n")
    # and it will be appended (how many you want)
    file.write(thoughts)