command = ""
running = False
false = False

while false == False:
    print("\nHello, your car is ready, ")
    false == True
    while True:
        command = input(str("\nPlease select your option: "))
        if command.lower() in "help":
            print(
                """
Your Car Instructions:
    - help: for help
    - start: to star the car
    - stop: to stop the car
    - quit: exit aplication
            """
            )

        elif command in "start":
            if not running:  # == false:
                running = True
                print("\nCar started. Your car is running now.")
            else:
                print("\nCar already running. Choose a different option.")
        elif command in "stop":
            if running:  # == false:
                running = False
                print("\nCar stopped.")
            else:
                print("\nCar already stopped. Choose a different option.")
        elif command in "quit":
            break
        else:
            print("\nSorry. Type a valid input. Use Help.")
    break

