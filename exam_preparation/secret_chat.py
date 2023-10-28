string_messages = input()
while True:
    command = input().split(":|:")
    if command[0] == "Reveal":
        print(f"You have a new text message: {string_messages}")
        break
    if command[0] == "InsertSpace":
        index_command = int(command[1])
        string_messages = string_messages[:index_command] + ' ' + string_messages[index_command:]
        print(string_messages)
    elif command[0] == "Reverse":
        substring = command[1]
        if substring in string_messages:
            string_messages = string_messages.replace(substring, '', 1)
            string_messages += substring[::-1]
            print(string_messages)
        else:
            print("error")
    elif command[0] == "ChangeAll":
        substring, replacement = command[1], command[2]
        if substring in string_messages:
            string_messages = string_messages.replace(substring, replacement)
            print(string_messages)
