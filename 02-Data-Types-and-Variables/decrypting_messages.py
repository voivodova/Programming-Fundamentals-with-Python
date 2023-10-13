key = int(input())
number = int(input())

message = ""

for _ in range(number):
    line = input()
    decrypted_line = ""
    for char in line:
        if char.isalpha():
            decrypted_char = chr(ord(char) + key)
        else:
            decrypted_char = char
        decrypted_line += decrypted_char
    message += decrypted_line

print(message)