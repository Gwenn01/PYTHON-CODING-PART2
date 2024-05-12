def minMaxSum(arr):
   min = 10000000000
   max = 0
   summation = []
   for i in range(len(arr)):
       sum = 0
       for j in range(len(arr)):
           if i != j:
               sum += arr[j]
       summation.append(sum)
   for s in summation:
         if s > max:
             max = s
         if s < min:
             min = s
   print(f"{min} {max}")
         

arr = [1, 3, 5, 7, 9]    
minMaxSum(arr)