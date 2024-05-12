def uniqueChar(str):
    str = str.upper()
    unique = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for s in str:
        isEqual = False
        for alpha in alphabet:
            if s == alpha:
                isEqual = True
        if not isEqual:
             unique += s
    return unique
     
                
str = "Gwen#"   
ans = uniqueChar(str)
print(ans)      
                
    