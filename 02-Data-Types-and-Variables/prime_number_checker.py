import math

n = int(input())
prime = True

if n > 1:
    for i in range(2, math.floor(math.sqrt(n) + 1)):
        if n % i == 0:
            prime = False
            break
else:
    prime = False

if prime:
    print('True')
else:
    print('False')
