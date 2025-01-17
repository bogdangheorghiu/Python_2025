


# this initial array
numbers = [101, 202, 303, 202, 404]
# Dictionary of frequencies
frequencies = { }

# Iterate to array
for no in numbers:
    if no % 2  == 0 :
        # get existing value or 0 and add 1 to i
        frequencies[no] = frequencies.get(no, 0) + 1

# check all the frequencies
print(frequencies)

# find the maximum frequency value (int)
max_freq = 0
for i in frequencies:
    if frequencies[i] > max_freq:
        max_freq = frequencies[i]

print("Max freq is", max_freq)

max_freq = 0
max_frequencies = {}
for f in frequencies:
    if frequencies[f] == max_freq:
        max_frequencies.append(f)

print(max_frequencies)
    

max_frequencies.sort
print(min(max_frequencies[0]))