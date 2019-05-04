# HighCard.py
import random
suits = ["clubs", "diamonds", "hearts", "spades"]
faces = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
my_point = 0
your_point = 0
tie_point = 0
keep_going = True
while keep_going:
    my_point = 0
    your_point = 0
    tie_point = 0
    for x in range(26):
        my_face= random.choice(faces)
        my_suit = random.choice(suits)
        your_face = random.choice(faces)
        your_suit = random.choice(suits)
        print("I have the", my_face, "of", my_suit)
        print("You have the", your_face, "of", your_suit)
        if faces.index(my_face) > faces.index(your_face):
            print("I win!")
            my_point += 1
        elif faces.index(my_face) < faces.index(your_face):
            print("You win!")
            your_point += 1
        else:
            print("It's a tie!")
            tie_point += 1
        print(your_point, my_point, tie_point)
    if my_point > your_point:
        print("Computer wins!")
    elif my_point == your_point:
        print("It's a tie!")
    else:
        print("You win!")
    answer = input("Hit [ENTER] to keep going, any key to exit: ")
    keep_going = (answer == "")


