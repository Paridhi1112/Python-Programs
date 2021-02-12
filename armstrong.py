n=int(input("enter value of n"))
count=0
temp=n
while(temp!=0):
    count=count+1
    temp=temp//10
def amstr(count,n):
    sum=0
    while(n!=0):
        num=n%10
        sum+=pow(num,count)
        n=n//10
    return sum
if(n==(amstr(count,n))):
    print("is an armstrong")
else:
    print("not an amstrong")
