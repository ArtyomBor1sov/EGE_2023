f = open('files/46982.txt')
parts = f.readline().split('E')
counter = 0
for element in parts:
    if len(element) >= 10 and 'F' not in element:
        counter += 1
print(counter)