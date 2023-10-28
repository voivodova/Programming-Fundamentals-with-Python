import re

pattern = r"(=|/)([A-Z][A-Za-z]{2,})\1"
places = input()
valid_destinations = []
len_of_destinations = 0
destinations = ''
for destination in re.finditer(pattern, places):
    valid_destinations.append(destination.group(2))

for valid in valid_destinations:
    len_of_destinations += len(valid)
to_print = ', '.join(valid_destinations)
print(f"Destinations: {to_print}")
print(f"Travel Points: {len_of_destinations}")
