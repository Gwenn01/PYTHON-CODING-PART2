def countSubstring(str_x, find):
    count = 0
    for i in range(len(str_x)):
        if str_x[i :].startswith(find):
            count += 1
    return count
    
str_x = "Gwen is good developer, Gwen is a programmer"
find = "Gwen"
ans = countSubstring(str_x, find)
print(ans)
        