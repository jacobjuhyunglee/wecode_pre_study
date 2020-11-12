# 동명이인 찾기
def find_same_name(a):
    n = len(a)
    result = set()
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                result.add(a[i])
    return result


name = ['Jacob', 'Courtney', 'Sarah', 'Jacob']
print(find_same_name(name))

name2 = ['Jacob', 'Courtney', 'Sarah', 'Jacob', 'Courtney']
print(find_same_name(name2))


# 두 명을 뽑아 짝으로 만들기
def print_pairs(a):
    n = len(a)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            print(a[i], '-', a[j])


name = ['Jacob', 'Courtney', 'Sarah']
print(print_pairs(name))
