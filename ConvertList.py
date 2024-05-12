def convertList():
    res_list = []
    sequence = input('Enter a Sequence: ')
    for i in range(len(sequence)):
        if sequence[i] == ',':
            res_list.append(int(sequence[i-1]))
    res_list.append(int(sequence[len(sequence)-1]))
    return res_list
           
print(convertList())