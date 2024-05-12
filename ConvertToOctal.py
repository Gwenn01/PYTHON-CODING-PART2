#division algorithm a=b(q)+r
def convertToOctal(decimal):
    answer = []
    result= ""
    while decimal != 0:
        rem = decimal % 8
        answer.append(rem)
        decimal //= 8
    for i in range(len(answer)-1, -1, -1):
        result += str(answer[i]) + " "
    return result

num = int(input('Enter Number: '))  
print(f"Octal: {convertToOctal(num)}")