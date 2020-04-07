from math import fabs

with open("./dane/dane4.txt", "r") as file:
    sequence = []
    length = 0
    m = 0
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
        i1 = index
        i2 = index+1
        count = 3
        while i1 < length - 1 and fabs(sequence[i1] - sequence[i2]) == difference:
            i1 += 1
            i2 += 1
            count += 1
        if count > m:
            m = count
        index += 1
    print(m)
#18