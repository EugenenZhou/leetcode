a,b = list(map(str,input().split()))

def compare(a,b):
    j = 0
    length_b = len(b)
    length_a = len(a)
    for i in a:
        if i != b[j]:
            if i == '.':
                return -1
            elif b[j] == '.':
                return 1
            else:
                res_a = a[j]
                res_b = b[j]
                while a[j+1] != '.' and j != length_a-1 and j != length_b - 1:
                    j = j + 1
                    if b[j] == '.':
                        return 1
                    else:
                        res_a = res_a + a[j]
                        res_b = res_b + b[j]
                if j != length_b - 1 and b[j+1] != '.':
                    return -1
                elif j == length_b - 1 and j != length_a - 1:
                    return 1
                else:
                    return 1 if res_a > res_b else -1
        if j+1 == length_b and j != length_a-1:
            return 1
        j = j + 1
    if j == length_b:
        return 0
    else:
        return -1
res = compare(a,b)
print(res)