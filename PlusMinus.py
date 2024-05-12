def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    n = len(arr)
    for ar in arr:
        if ar > 0:
            positive += 1
        elif ar < 0:
            negative += 1
        else:
            zero += 1
    print(f"{positive/n:.6f}")
    print(f"{negative/n:.6f}")
    print(f"{zero/n:.6f}")
    
    
arr = [1, 1, 0, -1, -1]    
plusMinus(arr)