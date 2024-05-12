def sumOfThreeEqualZero(arr, sum):
   answer = []
   sumOfThree = 0
   for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                sumOfThree = arr[i] + arr[j] + arr[k]
                if sumOfThree == sum:
                    temp = []
                    temp.append(arr[i])
                    temp.append(arr[j])
                    temp.append(arr[k])
                    answer.append(temp)
                    sumOfThree = 0                   
   return answer
    
arr = [1,0,1,2,-1,-4]
sum = 0
print(sumOfThreeEqualZero(arr, sum));