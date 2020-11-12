num = [17, 92, 18, 33, 58, 7, 33, 42]


def find_max(a):
    max_num = a[0]
    for i in range(1, len(num)):
        if a[i] > max_num:
            max_num = a[i]
    return max_num


print(find_max(num))


def find_max_idx(a):
    max_idx = 0
    for i in range(1, len(num)):
        if a[i] > a[max_idx]:
            max_idx = i
    return max_idx


print(find_max_idx(num))


def find_min(a):
    min_num = a[0]
    for i in range(1, len(num)):
        if a[i] < min_num:
            min_num = a[i]
    return min_num


print(find_min(num))
