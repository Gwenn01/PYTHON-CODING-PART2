#division algorithm a=b(q)+r
def convertToHexa(decimal):
    answer = []
    result= ""
    while decimal != 0:
        rem = decimal % 16
        answer.append(rem)
        decimal //= 16
    for i in range(len(answer)-1, -1, -1):
        if answer[i] < 10:
            result += str(answer[i])
        else:
            if answer[i] == 10:
                result += 'A'
            elif answer[i] == 11:
                result += 'B'
            elif answer[i] == 12:
                result += 'C'
            elif answer[i] == 13:
                result += 'D'
            elif answer[i] == 14:
                result += 'E'
            elif answer[i] == 15:
                result += 'F'    
    return result

num = int(input('Enter Number: '))  
print(f"Hexa: {convertToHexa(num)}")