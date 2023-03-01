f = open('files/33528.txt')
N, M = [int(x) for x in f.readline().split()]
data = []
for line in f:
    price, amount, kind = line.split()
    price, amount = int(price), int(amount)
    if kind == 'A':
        M -= price * amount
    else:
        data.append([price, amount])
data.sort()
counter = 0
for price, amount in data:
    if price * amount <= M:
        counter += amount
        M -= price * amount
    else:
        counter += M // price
        M -= M // price * price
        break
print(counter, M)