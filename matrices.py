n=int(input())
m=int(input())
matrix=[]
print("enter the value in matrix")

for i in range(n):
    data=[]
    for j in range(m):
        b=int(input())
        data.append(b)
    matrix.append(data)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=" ")
    print()

for i in range(n):
    sum=0
    for j in range(m):
        sum=sum+matrix[i][j]
    print("sum of row",i+1,",",sum)


