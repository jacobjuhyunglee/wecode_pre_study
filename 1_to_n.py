# 1부터 n 까지의 합을 구하는 알고리즘 연습

# 첫 번째 방법
def sum_n(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s


print(sum_n(10))
print(sum_n(100))


# 두 번째 방법
def sum_n(n):
    return n * (n + 1) // 2


print(sum_n(10))
print(sum_n(100))


# 1부터 n 까지 연속한 숫자의 제곱의 합을 구하기
# 첫 번째 방법
def sum_sq(n):
    s = 0
    for i in range(1, n + 1):
        s = s + (i * i)
    return s


print(sum_sq(10))
print(sum_sq(100))


# 두 번째 방법
def sum_sq(n):
    return n * (n + 1) * (2 * n + 1) // 6


print(sum_sq(10))
print(sum_sq(100))
