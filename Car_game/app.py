command = ""
started = False

while True:
    command = input('>').lower()
    if command == "start":
        if started:
            print("Already Started")
        else:
            started = True
            print("Car is started!")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car is stopped")
    elif command == "help":
        print("""
Type start to start
Type stop to stop
Type quit to quit
""")
    elif command == "quit":
        break
    else:
        print("That is not a command")

