def fac(n):
   multiply = 1
   while n != 0:
     multiply *= n
     n -= 1
   return multiply

def f(n):
    if n == 1:
        return n
    return n * f(n-1)

print(fac(4))
print(f(4))