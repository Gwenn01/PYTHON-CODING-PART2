def printPrevSum(n):
    print(f"Print Current and Previous number sum in a range {n}")
    for i in range(n):
        cur = i
        if i == 0:
             prev = 0 
        else: 
            prev = i - 1
        sum = cur + prev
        print(f"Current {cur} Prev {prev} Sum {sum}")
        
    
    
n = 10
printPrevSum(n)