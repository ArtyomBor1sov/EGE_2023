f = open('files/46982.txt')
parts = f.readline().split('A')
counter = 0
for element in parts:
    if len(element) >= 8 and 'B' not in element:
        counter += 1
print(counter)