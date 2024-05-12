def powerSubset(arr):
    container = []
    container.append([])
    for i in range(len(arr)):
       temp_list = []
       for j in range(len(container)):
           temp_list = container[j].copy()
           temp_list.append(arr[i])
           container.append(temp_list)
    return container
    
arr = [1, 2, 3]
ans = powerSubset(arr)
for an in ans:
    print(an)
           
           