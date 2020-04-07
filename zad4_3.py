from math import fabs

with open("./dane/dane4.txt", "r") as file:
    sequence = []
    length = 0
    for line in file.readlines():
        line = line.replace("\n", "")
        sequence.append(int(line))
        length += 1
    index = 1
    cache = {}
    for num1 in sequence:
        if index == length - 1:
            break
        num2 = sequence[index]
        difference = fabs(num1-num2)
        if difference in cache:
            cache[difference] += 1
        else:
            cache[difference] = 1
        index += 1
    most_frequently = -1
    for key in cache.keys():
        if most_frequently == -1 or cache[most_frequently] < cache[key]:
            most_frequently = key
    print(most_frequently)