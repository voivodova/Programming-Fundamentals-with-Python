words = input().lower().split()

output = {}
for word in words:
    output[word] = output.get(word, 0) + 1

for word, quantity in output.items():
    if quantity % 2 != 0:
        print(word, end=' ')
