import time

dinosaur = ("T-Rex","Spino","Raptor","Carno","Ankylo","Stego","Triceratops","Bronto")
correct = 0

print("Figure out what kind of dinosaur is outside your cave!")
time.sleep(1.4)
print("Please use y/n to respond!")
time.sleep(1.4)
x = input("Does the dinosaur have sharp teeth?? ")
if x == "y":
    x = input("Is the dinosaur over 15 feet tall? ")
    if x == "y":
        x = input("Does the dinosaur have a sail? ")
        if x == "y":
            print("Spino Detected! RUN!")
        elif x == "n":
            print("T-Rex Detected! RUN!")
        else:
            print("Invalid Input!")
    elif x == "n":
        x = input("Does the dinosaur have horns?")
        if x == "y":
            print("Carno Detected! RUN!")
        elif x == "n":
            print("Raptor Detected! RUN!")
        else:
            print("Invalid Input!")
    else:
        print("Invalid Input!")
elif x == "n":
    x = input("Does the dinosaur have bony plates?")
    if x == "y":
        x = input("Does the dinosaur have a club tail?")
        if x == "y":
            print("Anyklo Detected! Safe to approach!")
        elif x == "n":
            print("Stego Detected! Safe to approach!")
        else:
            print("Invalid Input!")
    elif x == "n":
        x = input("Does the dinosaur have a long neck?")
        if x == "y":
            print("Bronto Detected! Safe to approach!")
        elif x == "n":
            print("Triceratops Detected! Safe to approach")
        else:
            print("Invalid Input!")
else:
    print("Invalid Input!")