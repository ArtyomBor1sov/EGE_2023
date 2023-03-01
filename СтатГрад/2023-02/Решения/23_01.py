data = [[] for i in range(12)]
data[1].append([])
for i in range(2, 12):
    for prog in data[i - 1]:
        new_prog = prog.copy()
        new_prog.append(1)
        data[i].append(new_prog)
    if i - 2 >= 1:
        for prog in data[i - 2]:
                new_prog = prog.copy()
                new_prog.append(2)
                data[i].append(new_prog)
    if i % 2 == 0 and i // 2 >= 1:
        for prog in data[i // 2]:
                new_prog = prog.copy()
                new_prog.append(3)
                data[i].append(new_prog)
    if i % 3 == 0 and i // 3 >= 1:
        for prog in data[i // 3]:
                new_prog = prog.copy()
                new_prog.append(4)
                data[i].append(new_prog)
counter = 0
for prog in data[11]:
    if prog.count(3) + prog.count(4) == 1:
        counter += 1
print(counter)