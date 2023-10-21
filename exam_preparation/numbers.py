def top_5(data):
    avg = sum(data) / len(data)

    temp_sum = [x for x in sorted(data, reverse=True) if x > avg]

    if len(temp_sum) != 0:
        return ' '.join(map(str, temp_sum[:5]))
    else:
        return 'No'


numbers = list(map(int, input().split()))
print(top_5(numbers))
