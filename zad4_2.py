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
        nums = [num1, num2]
        while i1 < length - 1 and fabs(sequence[i1] - sequence[i2]) == difference:
            nums.append(sequence[i2])
            i1+=1
            i2+=1
        total_nums = len(nums)
        if total_nums > m:
            print(total_nums, index-1, i2)
            m = total_nums
        index += 1
    print(m)
#17