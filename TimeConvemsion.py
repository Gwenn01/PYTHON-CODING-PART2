def timeConversion(s):
    if (s[-2] + s[-1]) == "AM":
        if s[0:2] == "12":
            res = "00:"
            res += s[3:8]
            return res
        else:
            return s[:-2]
    else:
        s = s[:-2]
        if s[0:2] == "12":
            return s
        temp = s[0:2]
        add_twelve = 12 + int(temp)
        res = ""
        res += str(add_twelve)
        for i in range(2, len(s)):
            res += s[i]
        return res
        
s = "12:45:54PM"
print(timeConversion(s))