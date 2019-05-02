# SayOurNames.py
# Ask the user for their name
name = input("What is your name? ")

# Keep printing names until we want to quit
while name != "":
    # Print their name 100 times
    time = 0
    while time < 100 :
        # Print their name followed by a space, not a new line
        print(name, end = " ")
        time = time + 1
    print()   # After the for loop, skip down to the next line
    # Ask for another name, or quit
    
    name = input("Type another name, or just hit [ENTER] to quit: ")
print("Thanks for playing!")
             
