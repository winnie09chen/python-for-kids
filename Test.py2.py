# Test.py
message = input("Enter a message to encode or decode: ")
output = ""
for letter in message:
##    if letter.isupper():
##        d = 32
##    else:
##        d = -32
##    value = ord(letter) + d
    value = ord(letter) + (32 if letter.isupper() else -32)
    letter = chr(value)
    output += letter
print("Output message: ", output)
