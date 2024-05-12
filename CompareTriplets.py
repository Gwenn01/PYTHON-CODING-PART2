def compareTriplets(a, b):
    res = []
    a_score = 0
    b_score = 0
    i = 0
    while i < len(a) and i < len(b):
        if a[i] > b[i]:
            a_score += 1
        elif b[i] > a[i]:
            b_score += 1
        i += 1
    res.append(a_score)
    res.append(b_score)
    return res


a = [1, 2, 3]
b = [3, 2, 1]
ans = compareTriplets(a, b)
print(ans)    