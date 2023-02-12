# 2^m <= 600000000 => m = [0, 28]
# 3^n <= 600000000 => n = [1, 17]

answer = []
for m in range(0, 29, 2):
    for n in range(1, 18, 2):
        if 400000000 <= 2 ** m * 3 ** n <= 600000000:
            answer.append(2 ** m * 3 ** n)
answer.sort()
print(answer)