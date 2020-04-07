from math import fabs

with open("./dane/dane4.txt", "r") as file:
    sequence = []
    length = 0
    max_difference = 0
    min_difference = 99999999999
    for line in file.readlines():
        line = line.replace("\n", "")
        sequence.append(int(line))
        length += 1
    index = 1
    for num1 in sequence:
        if index == length - 1:
            break
        num2 = sequence[index]
        difference = fabs(num1-num2)
        max_difference = max(max_difference, difference)
        min_difference = min(min_difference, difference)
        index += 1
    print(max_difference, min_difference)