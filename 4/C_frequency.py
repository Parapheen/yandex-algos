
with open("input.txt") as f:
    lines = f.readlines()
    frequency = {}
    for line in lines:
        for word in line.split():
            if word not in frequency:
                frequency[word] = 0
            else:
                frequency[word] += 1

    freq_list = sorted([(frequency[el], el) for el in frequency], key=lambda x: (-x[0], x[1]))
    for el in freq_list:
        print(el[1])
