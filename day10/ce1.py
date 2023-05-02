#Percentage calculation
total = ""
value = ""
while type(total) and type(value) is not int or total == 0:
#way2:
#while type(total) is not int or type(value) is not int:
#yet another way:
#while type(total) != type(int()) or type(value) != type(int()):
    try:
        total = int(input("Enter total value: "))
        value = int(input("Enter value: "))
        percentage = 100 * value / total
        # yet another way to calc
        #        percentage_n = value / total * 100
        print(f"That is {percentage}%")
#this code below will not run if ValueError arrised above
    except ValueError:
        print("You need to enter a number.")
        continue
    except ZeroDivisionError:
        print("Your total value cannot be zero.")
        continue