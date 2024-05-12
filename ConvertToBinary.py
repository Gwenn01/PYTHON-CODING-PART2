#division algorithm a=b(q)+r
def convertToBinary(decimal):
    answer = []
    result= ""
    while decimal != 0:
        rem = decimal % 2
        answer.append(rem)
        decimal //= 2
    for i in range(len(answer)-1, -1, -1):
        result += str(answer[i])
    return result

num = int(input('Enter Number: '))  
print(f"Binary: {convertToBinary(num)}")