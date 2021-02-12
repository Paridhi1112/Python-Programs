n=int(input("enter value of n"))

def fact(n):
    facto=1
    if(n<0):
        return 0
    if(n==0 | n==1):
        return 1
    for i in range(1,n+1):
        facto*=i
    return facto

print(fact(n))