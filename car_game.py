print('''Welcome to the Car Game
Start
Stop
Quit''')
var = input("what would you like to do? ").upper()
status = False
while len(var) >= 0:
    if var == "START":
        if status == False:
            status = True
            print("Car has started")
            status = True
            var = input("What would you like to do? ").upper()
        else:
            print("The car is already running")
            var = input("What would you like to do? ").upper()
    
    elif var == "STOP":
        if status == True:
            print("Car has stopped")
            var = input("What would you like to do? ").upper()
            status = False
        else:
            print("The car hasn't even started")
            var = input("What would you like to do? ").upper()

    elif var == "QUIT":
        print("You just quit...")
        break

    else:
        print("I dont understand this")
        var = input("what would you like to do? ").upper()