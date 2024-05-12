def birthdayCakeCandles(candles):
    count = 0
    max = 0
    for can in candles:
        if can > max:
            max = can
    for can in candles:
         if can == max:
             count += 1
    return count
    
candles = [3, 2, 1, 3]
ans = birthdayCakeCandles(candles)
print(ans)