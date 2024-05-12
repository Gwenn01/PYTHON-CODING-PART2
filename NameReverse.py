def nameReverse():
    firstName = input('Enter First Name: ')
    lastName = input('Enter Last Name: ')
    result = ""
    fLength = len(firstName)
    lLength = len(lastName)
    for i in range(lLength-1, -1, -1):
        result += lastName[i]
    result += " "
    for i in range(fLength-1, -1, -1):
        result += firstName[i]
    return result
        
    
    
print(nameReverse())