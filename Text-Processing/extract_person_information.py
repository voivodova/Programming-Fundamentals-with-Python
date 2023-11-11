import re

def extract_name_and_age(line):
    name = re.search(r'@(.+?)\|', line).group(1)
    age = re.search(r'#(.+?)\*', line).group(1)
    return name, age

def main():
    n = int(input())
    lines = []
    for _ in range(n):
        line = input()
        lines.append(line)

    for line in lines:
        name, age = extract_name_and_age(line)
        print(f"{name} is {age} years old.")

if __name__ == "__main__":
    main()
