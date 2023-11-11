def sum_ascii_values(start_char, end_char, random_string):
    ascii_sum = 0
    for char in random_string:
        if ord(start_char) < ord(char) < ord(end_char):
            ascii_sum += ord(char)
    return ascii_sum

start_char = input()
end_char = input()
random_string = input()

result = sum_ascii_values(start_char, end_char, random_string)
print(result)
