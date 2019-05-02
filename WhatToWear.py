# WhatToWear.py
rainy = input("How's the weather? Is it raining? (y/n)").lower()
cold = input("Is it cold outside? (y/n)").lower()
if (rainy == 'y' and cold == 'y'):      # Rainy and cold, yuck!
    print("You'd better wear a raincoat.")
elif (rainy == 'y' and cold != 'y'):    # Rainy, but warm
    print("Carry an umbrella with you.")
elif (rainy != 'y' and cold == 'y'):    # Dry, but cold
    print("Put on a jacket, it's cold outside!")
elif (rainy != 'y' and cold != 'y'):    # Warm and sunny, yay!
    clothes = input("It's a beautiful day, what do you want?")
    print("Put on your", clothes, "and have a good time!")
