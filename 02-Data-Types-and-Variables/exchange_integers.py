a = int(input())
b = int(input())

print("Before:")
print("a =", a)
print("b =", b)

temporary_variable = a
a = b
b = temporary_variable

print("After:")
print("a =", a)
print("b =", b)