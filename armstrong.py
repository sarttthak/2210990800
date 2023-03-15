n=int(input())
order=len(str(n))
sum=0
temp=n

while n>6:
    a=n%10
    sum=sum+a**order
    n=n//10

if sum==temp:
    print("its armstrong")
else:
    print("its not")