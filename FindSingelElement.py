def findSingle(arr):
    answer = []
    temp = []
    for a in arr:
        if a not in temp:
            temp.append(a)
    for t in temp:
        count = 0
        for a in arr:
            if a == t:
                count += 1
        if count == 1:
            answer.append(t)
    return answer
            
    
    
arr = [1, 1, 1, 2, 2, 2, 3, 4]
ans = findSingle(arr)
print(ans)
