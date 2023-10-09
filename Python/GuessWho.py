characters = ("Mario","Luigi","Peach","Koopa","Latiku","Bowser","Donkey Kong","Toad","Buzzy Beetle")

print("Choose a character from:")
for counter in range(9):
    print(characters[counter])
print("Use 'yes' and 'no' to respond")

correct = 0

while correct == 0:
    x= input("Is your character human?")
    if x == "yes":
        x = input("Is your character italian?")
        if x == "no":
            print("Your character is Princess Peach!")
            correct = 1
        elif x == "yes":
            x = input("Is your character primarily red?")
            if x == "yes":
                print("Your character is Mario!")
                correct = 1
            elif x == "no":
                print("Your character is Luigi!")
                correct = 1
    elif x == "no":
        x = input("Is your character a turtle?")
        if x == "yes":
            x = input("Does your character have a smooth shell?")
            if x == "yes":
                x = input("Can your character fly?")
                if x == "yes":
                    print("Your character is Latiku!")
                    correct = 1
                elif x == "no":
                    print("Your character is Koopa!")
                    correct = 1
            elif x == "no":
                print("Your character is Bowser!")
                correct = 1
        elif x == "no":
            x = input("Is your character a monkey?")
            if x == "yes":
                print("Your character is Donkey Kong!")
                correct = 1
            elif x == "no":
                x = input("Is your character friendly?")
                if x == "yes":
                    print("Your character is Toad!")
                    correct = 1
                elif x == "no":
                    print("Your character is Buzzy Beetle!")
                    correct = 1
    else:
        print("Don't break me :(")
        correct = 1