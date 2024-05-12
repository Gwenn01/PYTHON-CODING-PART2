def camel_casting(s):
    s = list(s)
    camel = ""
    for i in range(len(s)):
        if s[i] != ' ':
            camel += s[i]
        else:
            s[i+1] = s[i+1].upper()
            i += 1
    return camel
            
s = "hello world"
print(camel_casting(s))         
   