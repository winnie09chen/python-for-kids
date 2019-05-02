# WhatsTheTemperature.py
temperature = eval(input("Enter the temperature(0-50): "))
if temperature >= 20:
    print("Today is very hot!")
elif temperature >= 10:
    print("Today isn't hot, isn't cold.")
else:
    print("Today is cold.")
