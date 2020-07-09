action = ""
false = False
running = False


while false == False:
    print("\nHello, your car is ready, ")
    false == True
    while True:
        action = input("What would you like to do now?\n> ").lower()
        if action == "start":
            if running == False:
                running = True
                print("Car started . . . ")
            else:
                print("Car is already starded, try again.")
        elif action == "stop":
            if not running:
                print("Car already stopped, try again.")
            else:
                running = False
                print("Car stopped . . . ")
        elif action == "help":
            print(
                """
    Your Car Instructions:
    - help: for help
    - start: to star the car
    - stop: to stop the car
    - quit: exit aplication
            """
            )
        elif action == "quit":
            break
        else:
            print("Sorry, command not understood. Please try again")
    break
