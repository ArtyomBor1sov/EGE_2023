# 2^K - 1 нечетный делитель
# 2^K * x^1 - 2 нечетных делителя
# 2^K * x^2 - 3 нечетных делителя
# 2^K * x^3 - 4 нечетных делителя
# 2^K * x^4 - 5 нечетных делителей
# 2^K * x^1 * y^1 - 4 нечетных делителя
# 2^K * x^2 * y^1 - 6 нечетных делителей
# 2^K * x^1 * y^1 * z^1 - 8 нечетных делителей

# 45000000 <= 2^K * x^4 <= 50000000
# x^4 <= 50000000
# x <= 84

def is_prime(num):
    answer = True
    for div in range(2, int(num ** 0.5) + 1):
        if num % div == 0:
            answer = False
            break
    return answer

answer = []
for num in range(2, 85):
    if is_prime(num):
        mult = 1
        while mult * num ** 4 <= 50000000:
            if 45000000 <= mult * num ** 4 <= 50000000:
                answer.append(mult * num ** 4)
            mult *= 2
answer.sort()
print(answer)